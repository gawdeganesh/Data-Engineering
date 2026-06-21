/**
 * ============================================================================
 *  09_Locks.gs  ·  Lock-cell features (Strict Mode) + tab protection
 * ============================================================================
 *  TWO distinct "lock" features, both requested:
 *
 *  (A) KICKOFF LOCK (per match, on Group Stage / Knockout):
 *      When a match's kickoff has passed, put 'L' in its Lock column, grey the
 *      row, and protect the three players' prediction cells (H/A/Jk) so no one
 *      can change a prediction after kickoff. Actual-score + points cells stay
 *      editable so the scorekeeper/formulas can still fill them.
 *
 *  (B) TAB LOCK (whole sheet): protect "Bonus Calls" and "Leaderboard" so they
 *      can't be edited. (You asked for these two tabs to be locked.)
 *
 *  Protection uses the Apps Script Protection API. With PROTECT_WARNING_ONLY
 *  = false, only the script's authorizing user can edit protected ranges;
 *  others are blocked. Set true for a softer "are you sure?" warning instead.
 * ============================================================================
 */

/** Unique id we tag our protections with, so re-runs update instead of duplicate. */
var PROT_TAG = '[wc2026-auto]';

/**
 * (A) Apply kickoff locks across Group Stage (and Knockout) matches.
 * @return {number} rows newly locked this run
 */
function applyKickoffLocks_() {
  var now = new Date();
  var locked = 0;
  [CONFIG.TAB_GROUP, CONFIG.TAB_KNOCKOUT].forEach(function (tabName) {
    var sh;
    try { sh = sheetByName_(tabName); } catch (e) { return; }
    var loc = locateMatchTab_(sh);
    if (loc.col.lock <= 0) return;
    var matches = readMatches_(sh, loc);

    Object.keys(matches).forEach(function (n) {
      var m = matches[n];
      if (isLocked_(m.lock)) return;               // already locked
      var ko = parseKickoff_(m.dateText, m.koText);
      if (!ko) return;                             // no parseable time (e.g. TBD knockout)
      if (ko.getTime() > now.getTime()) return;    // not started yet

      // Stamp 'L', grey the row, protect the prediction cells.
      setCellSafe_(sh, m.rowIndex, loc.col.lock, SCORING.LOCK_FLAG, true);
      var firstCol = 1;
      var lastCol = loc.col.venue > 0 ? loc.col.venue : sh.getLastColumn();
      shadeRow_(sh, m.rowIndex, firstCol, lastCol, CONFIG.LOCK_GREY);
      protectPredictionCells_(sh, loc, m.rowIndex);
      locked++;
    });
  });
  if (locked) diagLog_('Kickoff-locked ' + locked + ' match row(s).');
  return locked;
}

/** Protect the three players' H/A/Jk cells on one match row. */
function protectPredictionCells_(sh, loc, row) {
  CONFIG.PLAYERS.forEach(function (p) {
    var pc = loc.players[p];
    if (!pc) return;
    var rng = sh.getRange(row, pc.h, 1, 3); // H, A, Jk contiguous
    var prot = rng.protect().setDescription(PROT_TAG + ' lock M-row ' + row + ' ' + p);
    applyProtectionMode_(prot);
  });
}

/**
 * Apply the configured protection strength to a Protection object, degrading
 * safely. Hard-lock needs identity + sharing scopes; if either is unavailable
 * we fall back to warning-only protection rather than abort the whole update.
 */
function applyProtectionMode_(prot) {
  if (CONFIG.PROTECT_WARNING_ONLY) {
    prot.setWarningOnly(true);
    return;
  }
  try {
    var me = Session.getEffectiveUser();          // needs userinfo.email scope
    prot.removeEditors(prot.getEditors());         // needs full spreadsheets scope
    try { prot.addEditor(me); } catch (e) {}
    if (prot.canDomainEdit()) prot.setDomainEdit(false);
  } catch (e) {
    // Scope/permission shortfall → keep the protection but as a soft warning.
    diagLog_('Hard-lock unavailable (' + e.message + '); using warning-only.');
    try { prot.setWarningOnly(true); } catch (e2) {}
  }
}

/**
 * Parse a kickoff Date from the sheet's "Date" + "KO (CT)" text.
 * Date looks like "Thu, Jun 11"; KO like "15:00" (CT). Year from CONFIG.
 * Returns a Date in the spreadsheet timezone, or null if unparseable.
 */
function parseKickoff_(dateText, koText, tz) {
  if (!dateText || !koText) return null;
  var d = String(dateText).replace(/^[A-Za-z]{3},\s*/, '').trim(); // "Jun 11"
  var mdMatch = d.match(/([A-Za-z]{3,})\s+(\d{1,2})/);
  var ko = String(koText).match(/(\d{1,2}):(\d{2})/);
  if (!mdMatch || !ko) return null;
  var months = { jan: 0, feb: 1, mar: 2, apr: 3, may: 4, jun: 5, jul: 6, aug: 7, sep: 8, oct: 9, nov: 10, dec: 11 };
  var mon = months[mdMatch[1].slice(0, 3).toLowerCase()];
  if (mon === undefined) return null;
  var day = Number(mdMatch[2]);
  var hh = Number(ko[1]), mm = Number(ko[2]);
  // Parse the wall-clock time IN the sheet's timezone (CT). Utilities.parseDate
  // honours the named zone and resolves CST/CDT (DST) correctly — unlike
  // `new Date(string)`, which would parse in the VM's own zone and be hours off.
  var str = Utilities.formatString('%04d/%02d/%02d %02d:%02d:00',
    CONFIG.EDITION_YEAR, mon + 1, day, hh, mm);
  var dt;
  try {
    dt = Utilities.parseDate(str, tz || CONFIG.TIMEZONE, 'yyyy/MM/dd HH:mm:ss');
  } catch (e) {
    return null;
  }
  return (dt && !isNaN(dt.getTime())) ? dt : null;
}

/**
 * (B) Protect whole tabs listed in CONFIG.PROTECT_TABS (Bonus Calls, Leaderboard).
 * Idempotent: updates the existing auto-protection instead of stacking new ones.
 * @return {number} tabs protected
 */
function protectLockedTabs_() {
  var count = 0;
  CONFIG.PROTECT_TABS.forEach(function (tabName) {
    var sh;
    try { sh = sheetByName_(tabName); } catch (e) { return; }
    // Remove our previous auto sheet-protection on this tab, then re-add.
    sh.getProtections(SpreadsheetApp.ProtectionType.SHEET).forEach(function (pr) {
      if ((pr.getDescription() || '').indexOf(PROT_TAG) === 0) pr.remove();
    });
    var prot = sh.protect().setDescription(PROT_TAG + ' tab lock ' + tabName);
    applyProtectionMode_(prot);
    count++;
  });
  diagLog_('Protected ' + count + ' tab(s): ' + CONFIG.PROTECT_TABS.join(', '));
  return count;
}

/** Remove ALL auto-protections this script created (escape hatch). */
function unlockAllAuto_() {
  var removed = 0;
  var sheets = ss_().getSheets();
  sheets.forEach(function (sh) {
    [SpreadsheetApp.ProtectionType.SHEET, SpreadsheetApp.ProtectionType.RANGE].forEach(function (type) {
      sh.getProtections(type).forEach(function (pr) {
        if ((pr.getDescription() || '').indexOf(PROT_TAG) === 0) { pr.remove(); removed++; }
      });
    });
  });
  diagLog_('Removed ' + removed + ' auto-protection(s).');
  return removed;
}
