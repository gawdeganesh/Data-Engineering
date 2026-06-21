/**
 * ============================================================================
 *  10_BonusCalls.gs  ·  Auto-fill the derivable "ACTUAL RESULTS" on Bonus Calls
 * ============================================================================
 *  The Bonus Calls tab says only 3 inputs are manual (Golden Boot, Golden Ball,
 *  Surprise team). The rest can be derived once the tournament resolves:
 *    • World Cup Winner   = winner of the Final (match 104)
 *    • Runner-up          = loser of the Final
 *    • Third place        = winner of the 3rd-place playoff (match 103)
 *    • USA escaped group? = was "United States" 1st/2nd in Group D after groups
 *
 *  IMPORTANT: this tab is PROTECTED (locked). To write into it the script must
 *  briefly run as the protection's editor — which it is (the trigger owner).
 *  We write derivable values into the labelled cells of the ACTUAL RESULTS
 *  block, formula-aware and only when empty.
 * ============================================================================
 */

/**
 * @param {Array<Object>} fixtures normalized API fixtures
 * @param {function} resolve team resolver
 * @return {number} cells written
 */
function updateBonusActuals_(fixtures, resolve) {
  var sh;
  try { sh = sheetByName_(CONFIG.TAB_BONUS); } catch (e) { return 0; }
  var values = sh.getDataRange().getValues();
  var written = 0;

  // Find the "ACTUAL RESULTS" anchor, then the labelled rows beneath it.
  var anchor = findRowContaining_(values, 'ACTUAL RESULTS');
  if (anchor < 0) return 0;

  // Resolve outcomes from the API knockout fixtures.
  var finalFx = pickStageFixture_(fixtures, 'F');
  var thirdFx = pickStageFixture_(fixtures, '3P');

  var winner = null, runnerUp = null, third = null;
  if (finalFx && finalFx.finished) {
    var w = winnerOf_(finalFx, resolve);
    winner = w.winner; runnerUp = w.loser;
  }
  if (thirdFx && thirdFx.finished) {
    third = winnerOf_(thirdFx, resolve).winner;
  }
  var usaEscaped = computeUsaEscaped_(fixtures, resolve, sh);

  // Write each derivable value next to its label (value goes one col right of label).
  written += writeBesideLabel_(sh, values, anchor, 'World Cup Winner', winner);
  written += writeBesideLabel_(sh, values, anchor, 'Runner-up', runnerUp);
  written += writeBesideLabel_(sh, values, anchor, 'Third place', third);
  written += writeBesideLabel_(sh, values, anchor, 'USA escaped group', usaEscaped);

  if (written) diagLog_('Bonus actuals written: ' + written);
  return written;
}

/** Winner/loser of a finished fixture, resolved to sheet names. */
function winnerOf_(fx, resolve) {
  var h = resolve(fx.homeName) || fx.homeName;
  var a = resolve(fx.awayName) || fx.awayName;
  var gh = numOrNull_(fx.homeGoals), ga = numOrNull_(fx.awayGoals);
  // If level after 120', decide by shootout.
  if (gh === ga && fx.decidedOnPens) {
    return numOrNull_(fx.penHome) > numOrNull_(fx.penAway)
      ? { winner: h, loser: a } : { winner: a, loser: h };
  }
  return gh > ga ? { winner: h, loser: a } : { winner: a, loser: h };
}

/**
 * Did the USA escape the group, i.e. reach the knockout stage? Yes/No/null.
 * In the 2026 format the 8 best 3rd-placed teams ALSO advance, so finishing
 * 3rd is not automatically "out". PRIMARY signal: does the USA appear in any
 * API knockout fixture (the API resolves the 3rd-place permutation for us)?
 * Only once the group stage is fully played do we fall back to a top-2 read.
 */
function computeUsaEscaped_(fixtures, resolve, bonusSh) {
  // PRIMARY: USA present in any knockout fixture → definitively escaped.
  var koFixtures = (fixtures || []).filter(function (fx) {
    return /(round of|final|quarter|semi|16|32|play)/i.test(fx.round || '');
  });
  for (var i = 0; i < koFixtures.length; i++) {
    var fx = koFixtures[i];
    if (resolve(fx.homeName) === 'United States' || resolve(fx.awayName) === 'United States') {
      return 'Yes';
    }
  }
  // If there ARE knockout fixtures and USA isn't in any of them, it's out.
  if (koFixtures.length > 0) return 'No';

  // FALLBACK (no knockout data yet): only answer once Group D is fully played,
  // and only "Yes" for a clear top-2; a 3rd-place finish stays unresolved (null)
  // because 3rd-place qualification can't be known without the knockout draw.
  var gSh;
  try { gSh = sheetByName_(CONFIG.TAB_GROUP); } catch (e) { return null; }
  var loc = locateMatchTab_(gSh);
  var gMatches = readMatches_(gSh, loc);

  // Find the USA's group letter and whether all its group games are done.
  var usaGroup = null, totalGroupGames = 0, playedGroupGames = 0;
  Object.keys(gMatches).forEach(function (n) {
    var m = gMatches[n];
    if (m.home === 'United States' || m.away === 'United States') usaGroup = String(m.grp).trim();
  });
  if (!usaGroup) return null;

  var table = {};
  function team(t) { if (!table[t]) table[t] = { gf: 0, ga: 0, pts: 0 }; return table[t]; }
  Object.keys(gMatches).forEach(function (n) {
    var m = gMatches[n];
    if (String(m.grp).trim() !== usaGroup) return;
    totalGroupGames++;
    var ah = numOrNull_(m.actH), aa = numOrNull_(m.actA);
    if (ah === null || aa === null) return;
    playedGroupGames++;
    var H = team(m.home), A = team(m.away);
    H.gf += ah; H.ga += aa; A.gf += aa; A.ga += ah;
    if (ah > aa) H.pts += 3; else if (ah < aa) A.pts += 3; else { H.pts++; A.pts++; }
  });
  if (playedGroupGames < totalGroupGames || totalGroupGames === 0) return null; // group not finished

  var ranked = Object.keys(table).map(function (t) {
    return { team: t, pts: table[t].pts, gd: table[t].gf - table[t].ga, gf: table[t].gf };
  }).sort(function (a, b) { return (b.pts - a.pts) || (b.gd - a.gd) || (b.gf - a.gf); });

  var pos = ranked.findIndex(function (x) { return x.team === 'United States'; });
  if (pos === 0 || pos === 1) return 'Yes';     // clear top-2 → escaped
  if (pos === 2) return null;                    // 3rd → depends on best-3rd draw; unknown
  return 'No';                                   // 4th → out
}

/** Pick the single fixture for a knockout stage code (F / 3P). */
function pickStageFixture_(fixtures, stageCode) {
  var list = fixtures.filter(function (fx) { return stageOf_(fx.round) === stageCode; });
  list.sort(function (a, b) { return (b.timestamp || 0) - (a.timestamp || 0); });
  return list[0] || null;
}

/** Find first row index whose any cell contains `substr`. */
function findRowContaining_(values, substr) {
  for (var r = 0; r < values.length; r++) {
    for (var c = 0; c < values[r].length; c++) {
      if (String(values[r][c]).indexOf(substr) >= 0) return r;
    }
  }
  return -1;
}

/**
 * Write `value` into the ACTUAL RESULTS row whose label cell STARTS WITH `label`
 * (anchored match — avoids "Runner-up" matching inside another cell). The value
 * is placed into the row's ">>> TYPE … <<<" placeholder cell if present, else
 * the first empty cell to the right of the label. Formula-aware; empty-only.
 * @return {number} 1 if written, 0 otherwise
 */
function writeBesideLabel_(sh, values, fromRow, label, value) {
  if (value === null || value === undefined) return 0;
  var want = label.trim().toLowerCase();
  for (var r = fromRow; r < values.length; r++) {
    var row = values[r];
    for (var c = 0; c < row.length; c++) {
      var cell = String(row[c]).trim().toLowerCase();
      if (cell.indexOf(want) === 0) {                 // anchored: label at start of cell
        // Prefer the ">>>" placeholder cell in this row.
        var targetCol = -1;
        for (var cc = c + 1; cc < row.length; cc++) {
          if (String(row[cc]).indexOf('>>>') >= 0) { targetCol = cc + 1; break; }
        }
        // Else first empty cell to the right of the label.
        if (targetCol < 0) {
          for (var ce = c + 1; ce < Math.max(row.length, c + 4); ce++) {
            if (String(row[ce] || '').trim() === '') { targetCol = ce + 1; break; }
          }
        }
        if (targetCol < 0) targetCol = c + 2;          // last-resort
        return setCellSafe_(sh, r + 1, targetCol, value, false) ? 1 : 0;
      }
    }
  }
  return 0;
}
