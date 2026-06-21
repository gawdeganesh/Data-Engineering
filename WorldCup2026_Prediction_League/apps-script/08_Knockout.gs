/**
 * ============================================================================
 *  08_Knockout.gs  ·  Fill the Knockout tab (matches 73–104) from the API
 * ============================================================================
 *  Once groups end, football-data.org returns the knockout fixtures with the real
 *  qualified team names + scores. We match them to Knockout rows by match
 *  number where possible, else by round + chronological order.
 *
 *  Before the API has knockout data, we optionally write a bracket PREVIEW
 *  (e.g. "Runner-up A" vs "Runner-up B") so the tab isn't empty. Preview text
 *  is only written into empty, non-formula Home/Away cells and is replaced by
 *  real team names as soon as the API provides them.
 * ============================================================================
 */

/**
 * @param {Array<Object>} fixtures  normalized API fixtures
 * @param {function} resolve        team-name resolver
 * @return {number} cells written
 */
function updateKnockout_(fixtures, resolve, opts) {
  opts = opts || {};
  var sh;
  try { sh = sheetByName_(CONFIG.TAB_KNOCKOUT); } catch (e) { return 0; }
  var loc = locateMatchTab_(sh);
  var kMatches = readMatches_(sh, loc);
  var written = 0;

  // Knockout fixtures from the API (anything whose round is not a group round).
  var koFixtures = fixtures.filter(function (fx) {
    return /(round of|final|quarter|semi|16|32|play)/i.test(fx.round || '');
  });

  // -- PASS 1: SCORES, matched by team pair (UNAMBIGUOUS) --------------------
  // For any knockout row that already has both teams, find the API fixture for
  // that exact pair and write its score to THAT row. Row order is irrelevant,
  // so teams/scores can never be swapped between rows.
  var apiByPair = {};
  koFixtures.forEach(function (fx) {
    var h = resolve(fx.homeName, fx.homeTla), a = resolve(fx.awayName, fx.awayTla);
    if (h && a) {
      var k = pairKey_(h, a);
      // Prefer a finished fixture if duplicates exist for the same pair.
      if (!apiByPair[k] || (fx.finished && !apiByPair[k].finished)) apiByPair[k] = fx;
    }
  });
  Object.keys(kMatches).forEach(function (n) {
    var m = kMatches[n];
    if (!m.home || !m.away) return;                 // teams not set yet → pass 2
    var fx = apiByPair[pairKey_(m.home, m.away)];
    if (fx && fx.finished) {
      written += writeKnockoutScore_(sh, loc, m, fx, resolve, opts);
    }
  });

  // -- PASS 2: TEAM NAMES into BLANK rows (best-effort, never overwrites) -----
  // Genuinely ambiguous (FIFA match # ↔ API fixture mapping isn't in the API),
  // so we bucket by stage + date and fill ONLY empty Home/Away cells. A human
  // correction (a non-empty cell) is never clobbered, and Pass 1 will still put
  // the right score on it next run because scores match by pair, not position.
  var byStage = groupByStage_(koFixtures);
  var rowsByStage = knockoutRowsByStage_(kMatches);
  Object.keys(rowsByStage).forEach(function (stg) {
    var rows = rowsByStage[stg];                    // ascending match #
    var fx = (byStage[stg] || []).slice().sort(function (a, b) {
      return (a.timestamp || 0) - (b.timestamp || 0);
    });
    var ambiguous = hasTimestampTie_(fx);           // same-stage same-KO collisions
    for (var i = 0; i < rows.length && i < fx.length; i++) {
      var m = rows[i];
      if (m.home || m.away) continue;               // already has teams; leave it
      written += fillKnockoutTeams_(sh, loc, m, fx[i], resolve, ambiguous);
    }
    if (ambiguous && fx.length) {
      diagLog_('Knockout stage ' + stg + ' has same-time fixtures; team rows ' +
               'filled by best-effort order — please eyeball them. Scores are ' +
               'always matched by team pair regardless.');
    }
  });

  // PREVIEW for rows still missing team names (no API knockout data yet).
  if (opts.knockoutPreview) {
    var preview = buildKnockoutPreview_();
    Object.keys(kMatches).forEach(function (n) {
      var m = kMatches[n];
      if (preview[n] && !m.home && !m.away) {
        if (setCellSafe_(sh, m.rowIndex, loc.col.home, preview[n].home, false)) written++;
        if (setCellSafe_(sh, m.rowIndex, loc.col.away, preview[n].away, false)) written++;
      }
    });
  }
  return written;
}

/** True if two fixtures in the list share a kickoff timestamp (ambiguous order). */
function hasTimestampTie_(fixtures) {
  var seen = {};
  for (var i = 0; i < fixtures.length; i++) {
    var t = fixtures[i].timestamp || 0;
    if (seen[t]) return true;
    seen[t] = true;
  }
  return false;
}

/** Map a knockout fixture's round string to a stage code matching the sheet. */
function stageOf_(round) {
  var r = String(round || '').toLowerCase();
  if (/round of 32|1\/16/.test(r)) return 'R32';
  if (/round of 16|1\/8/.test(r)) return 'R16';
  if (/quarter|1\/4/.test(r)) return 'QF';
  if (/semi|1\/2/.test(r)) return 'SF';
  if (/3rd place|third place|play-?off for third/.test(r)) return '3P';
  if (/final/.test(r)) return 'F';
  return '?';
}

function groupByStage_(fixtures) {
  var out = {};
  fixtures.forEach(function (fx) {
    var s = stageOf_(fx.round);
    (out[s] = out[s] || []).push(fx);
  });
  return out;
}

/** Group Knockout rows by their Stg column value, each list sorted by match #. */
function knockoutRowsByStage_(kMatches) {
  var out = {};
  Object.keys(kMatches).forEach(function (n) {
    var m = kMatches[n];
    var stg = String(m.grp || '').trim().toUpperCase() || stageFromNum_(m.num);
    (out[stg] = out[stg] || []).push(m);
  });
  Object.keys(out).forEach(function (s) {
    out[s].sort(function (a, b) { return a.num - b.num; });
  });
  return out;
}

/** Derive stage from match number when the Stg cell is blank. */
function stageFromNum_(num) {
  if (num >= 73 && num <= 88) return 'R32';
  if (num >= 89 && num <= 96) return 'R16';
  if (num >= 97 && num <= 100) return 'QF';
  if (num >= 101 && num <= 102) return 'SF';
  if (num === 103) return '3P';
  if (num === 104) return 'F';
  return '?';
}

/**
 * PASS 1 writer: the row's teams already match this fixture's pair, so just
 * write the oriented score. Formula-aware. Used only for finished fixtures.
 */
function writeKnockoutScore_(sh, loc, m, fx, resolve, opts) {
  var written = 0;
  var oriented = orientGoals_(fx, m.home, m.away, resolve);
  if (oriented.h !== null && setCellSafe_(sh, m.rowIndex, loc.col.actH, oriented.h, opts && opts.overwriteActuals)) written++;
  if (oriented.a !== null && setCellSafe_(sh, m.rowIndex, loc.col.actA, oriented.a, opts && opts.overwriteActuals)) written++;

  // Shootout note — set ONCE (don't re-stamp every run; don't clobber a human note).
  if (fx.decidedOnPens && loc.col.actA > 0) {
    var cell = sh.getRange(m.rowIndex, loc.col.actA);
    var note = 'Pens ' + fx.penHome + '–' + fx.penAway;
    if (!cell.getNote()) cell.setNote(note);
  }
  return written;
}

/**
 * PASS 2 writer: fill team names into an EMPTY knockout row (best-effort
 * positional alignment). Never overwrites; if ambiguous, flag a review note.
 */
function fillKnockoutTeams_(sh, loc, m, fx, resolve, ambiguous) {
  var written = 0;
  var h = resolve(fx.homeName, fx.homeTla) || fx.homeName;
  var a = resolve(fx.awayName, fx.awayTla) || fx.awayName;
  var wroteH = setCellSafe_(sh, m.rowIndex, loc.col.home, h, false);  // empty-only
  var wroteA = setCellSafe_(sh, m.rowIndex, loc.col.away, a, false);
  if (wroteH) written++;
  if (wroteA) written++;
  if (ambiguous && (wroteH || wroteA) && loc.col.home > 0) {
    sh.getRange(m.rowIndex, loc.col.home)
      .setNote('Auto-filled by kickoff order among same-time games — verify the pairing.');
  }
  return written;
}
