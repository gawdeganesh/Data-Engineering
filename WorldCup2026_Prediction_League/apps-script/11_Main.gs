/**
 * ============================================================================
 *  11_Main.gs  ·  Entry points, custom menu, triggers, diagnostics
 * ============================================================================
 */

/** Adds the "World Cup" menu when the sheet opens. */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('⚽ World Cup')
    .addItem('Update now (latest scores + standings)', 'menuUpdateNow')
    .addItem('Update — finished matches only', 'menuUpdateFinishedOnly')
    .addSeparator()
    .addItem('Lock tabs (Bonus + Leaderboard)', 'menuProtectTabs')
    .addItem('Apply kickoff locks now', 'menuApplyLocks')
    .addItem('Unlock all auto-locks', 'menuUnlockAll')
    .addSeparator()
    .addItem('Fill knockout bracket preview', 'menuKnockoutPreview')
    .addItem('Settle Bonus Calls (end of tournament)', 'menuSettleBonus')
    .addItem('Convert kickoff times ET → CT (one-time)', 'convertKickoffTimesToCT')
    .addSeparator()
    .addItem('Set API key…', 'menuSetApiKey')
    .addItem('Run diagnostics', 'menuDiagnostics')
    .addItem('Install hourly auto-update', 'menuInstallTrigger')
    .addItem('Remove auto-update', 'menuRemoveTrigger')
    .addToUi();
}

/* ----------------------------- Menu handlers ----------------------------- */

// Default update: always pulls FRESH data (no cache), shows live scores, and
// finalizes points/standings for finished matches. This is the everyday button.
function menuUpdateNow() {
  var s = updateAll_({ includeLive: true });
  toast_('Update done · ' + s.actualsWritten + ' scores, ' + s.pointsWritten +
         ' points, ' + s.standingsWritten + ' standings, ' + s.knockoutWritten +
         ' knockout, ' + s.bonusWritten + ' bonus, ' + s.locksApplied + ' locks' +
         (s.unmatched.length ? ' · ⚠ ' + s.unmatched.length + ' unmatched teams (check Executions log)' : ''));
}

// Conservative variant: ignore in-play matches; only write scores that are FINAL.
function menuUpdateFinishedOnly() {
  var s = updateAll_({ includeLive: false });
  toast_('Finished-only update · ' + s.actualsWritten + ' scores, ' + s.pointsWritten +
         ' points, ' + s.standingsWritten + ' standings.');
}

function menuProtectTabs() {
  var n = protectLockedTabs_();
  toast_('Locked ' + n + ' tab(s): ' + CONFIG.PROTECT_TABS.join(', '));
}

function menuApplyLocks() {
  var n = applyKickoffLocks_();
  toast_('Kickoff-locked ' + n + ' match row(s).');
}

function menuUnlockAll() {
  var ui = SpreadsheetApp.getUi();
  var resp = ui.alert('Unlock everything?',
    'This removes ALL kickoff locks and tab protections this script created. Continue?',
    ui.ButtonSet.YES_NO);
  if (resp === ui.Button.YES) toast_('Removed ' + unlockAllAuto_() + ' protection(s).');
}

function menuKnockoutPreview() {
  var fixtures = fetchAllFixtures_(false);
  var resolve = makeTeamResolver_(allSheetTeams_());
  var n = updateKnockout_(fixtures, resolve, { knockoutPreview: true });
  toast_('Knockout: wrote/updated ' + n + ' cell(s).');
}

function menuSettleBonus() {
  var fixtures = fetchAllFixtures_(false);
  var resolve = makeTeamResolver_(allSheetTeams_());
  var n = updateBonusActuals_(fixtures, resolve);
  toast_('Bonus Calls: ' + n + ' derivable result(s) written. (Golden Boot/Ball + Surprise team stay manual.)');
}

function menuSetApiKey() {
  var ui = SpreadsheetApp.getUi();
  var resp = ui.prompt('Set football-data.org token',
    'Paste your football-data.org API token (stored privately in Script Properties):',
    ui.ButtonSet.OK_CANCEL);
  if (resp.getSelectedButton() === ui.Button.OK) {
    var key = resp.getResponseText().trim();
    if (key) {
      PropertiesService.getScriptProperties().setProperty(CONFIG.API_KEY_PROP, key);
      toast_('API key saved.');
    }
  }
}

function menuDiagnostics() {
  var report = runDiagnostics_();
  SpreadsheetApp.getUi().alert('Diagnostics', report, SpreadsheetApp.getUi().ButtonSet.OK);
}

function menuInstallTrigger() { installHourlyTrigger_(); toast_('Hourly auto-update installed.'); }
function menuRemoveTrigger() { removeTriggers_(); toast_('Auto-update removed.'); }

/* ------------------------ Trigger target + management -------------------- */

/** The function the time-trigger calls. Lighter than the menu update. */
function scheduledUpdate() {
  // Prevent overlapping runs (a slow protect() pass + the next hourly tick).
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(1000)) {
    diagLog_('scheduledUpdate skipped — previous run still holds the lock.');
    return;
  }
  try {
    if (tournamentComplete_()) {
      diagLog_('Tournament complete and all results filled — auto-removing trigger.');
      removeTriggers_();
      return;
    }
    updateAll_({ includeLive: true });
  } catch (e) {
    diagLog_('scheduledUpdate ERROR: ' + e.message);
    throw e;
  } finally {
    lock.releaseLock();
  }
}

/** True once the Final (match 104) has both actual scores written. */
function tournamentComplete_() {
  var sh;
  try { sh = sheetByName_(CONFIG.TAB_KNOCKOUT); } catch (e) { return false; }
  var loc = locateMatchTab_(sh);
  var matches = readMatches_(sh, loc);
  var fin = matches[104];
  return !!(fin && numOrNull_(fin.actH) !== null && numOrNull_(fin.actA) !== null);
}

function installHourlyTrigger_() {
  removeTriggers_();
  ScriptApp.newTrigger('scheduledUpdate').timeBased().everyHours(1).create();
}

function removeTriggers_() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'scheduledUpdate') ScriptApp.deleteTrigger(t);
  });
}

/* ------------------------------- Helpers --------------------------------- */

function allSheetTeams_() {
  var gSh = sheetByName_(CONFIG.TAB_GROUP);
  var loc = locateMatchTab_(gSh);
  var matches = readMatches_(gSh, loc);
  var set = {};
  Object.keys(matches).forEach(function (n) {
    if (matches[n].home) set[matches[n].home] = true;
    if (matches[n].away) set[matches[n].away] = true;
  });
  return Object.keys(set);
}

function toast_(msg) {
  try { ss_().toast(msg, '⚽ World Cup', 8); } catch (e) { Logger.log(msg); }
}

/* ----------------------------- Diagnostics ------------------------------- */

/**
 * Logger. By default writes ONLY to the Apps Script execution log (no new tab).
 * If CONFIG.CREATE_DIAG_TAB is true, also appends to a hidden "_diag" tab inside
 * this same spreadsheet (never a separate file).
 */
function diagLog_(msg) {
  Logger.log(msg);
  if (!CONFIG.CREATE_DIAG_TAB) return;
  try {
    var sh = ss_().getSheetByName(CONFIG.TAB_DIAG);
    if (!sh) { sh = ss_().insertSheet(CONFIG.TAB_DIAG); sh.hideSheet(); sh.appendRow(['When', 'Message']); }
    sh.insertRowAfter(1);
    sh.getRange(2, 1, 1, 2).setValues([[new Date(), msg]]);
  } catch (e) { Logger.log(msg); }
}

/** End-to-end health check used by the menu. */
function runDiagnostics_() {
  var lines = [];
  lines.push('API key set: ' + (apiKeyIsSet_() ? 'yes' : 'NO — run "Set API key…"'));

  // Tabs present?
  [CONFIG.TAB_GROUP, CONFIG.TAB_STANDINGS, CONFIG.TAB_KNOCKOUT, CONFIG.TAB_BONUS, CONFIG.TAB_LEADERBOARD].forEach(function (t) {
    lines.push('Tab "' + t + '": ' + (ss_().getSheetByName(t) ? 'found' : 'MISSING'));
  });

  // Header location on Group Stage.
  try {
    var loc = locateMatchTab_(sheetByName_(CONFIG.TAB_GROUP));
    lines.push('Group Stage header row: ' + loc.headerRow + '; players located: ' +
               Object.keys(loc.players).join(', '));
    lines.push('Columns — Home:' + loc.col.home + ' Away:' + loc.col.away +
               ' ActH:' + loc.col.actH + ' ActA:' + loc.col.actA + ' Lock:' + loc.col.lock);
  } catch (e) { lines.push('Group Stage parse ERROR: ' + e.message); }

  // API reachability (only if key set).
  if (apiKeyIsSet_()) {
    try {
      var fx = fetchAllFixtures_(true);
      lines.push('API returned ' + fx.length + ' fixtures.');
      var finished = fx.filter(function (f) { return f.finished; }).length;
      lines.push('Finished fixtures: ' + finished);
      // Team-name match check.
      var resolve = makeTeamResolver_(allSheetTeams_());
      var unmatched = {};
      fx.forEach(function (f) {
        if (!resolve(f.homeName, f.homeTla)) unmatched[f.homeName] = true;
        if (!resolve(f.awayName, f.awayTla)) unmatched[f.awayName] = true;
      });
      var u = Object.keys(unmatched);
      lines.push('Unmatched team names: ' + (u.length ? u.join(', ') : 'none ✓'));
    } catch (e) { lines.push('API check ERROR: ' + e.message); }
  }
  var report = lines.join('\n');
  diagLog_('Diagnostics:\n' + report);
  return report;
}
