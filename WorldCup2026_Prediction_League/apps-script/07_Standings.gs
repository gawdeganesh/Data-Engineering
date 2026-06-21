/**
 * ============================================================================
 *  07_Standings.gs  ·  Compute the 12 group tables from Group Stage actuals
 * ============================================================================
 *  Ranking per the Standings tab note: Points → Goal Difference → Goals For.
 *  (FIFA's full tie-break adds head-to-head etc.; the sheet itself says rare
 *  exact ties "may need a manual head-to-head check", so we stop at Pts→GD→GF
 *  and leave true ties in sheet order — matching the sheet's own caveat.)
 *
 *  Formula-aware: if the Standings cells already contain live formulas, every
 *  write is skipped (setCellSafe_ returns false on a formula cell). This block
 *  only "comes alive" if those formulas were lost with the old script.
 * ============================================================================
 */

/**
 * Build standings from matched group fixtures and write them.
 * @param {Object} gMatches  output of readMatches_ on the Group Stage tab
 * @return {number} cells written
 */
function recomputeStandings_(gMatches) {
  // 1. Tally each team from played group matches.
  var table = {}; // teamName → {pld,w,d,l,gf,ga}
  function team(t) {
    if (!table[t]) table[t] = { team: t, pld: 0, w: 0, d: 0, l: 0, gf: 0, ga: 0 };
    return table[t];
  }
  Object.keys(gMatches).forEach(function (n) {
    var m = gMatches[n];
    if (!m.home || !m.away) return;
    // Only count FINISHED matches. m.finished is set by updateAll_; if absent
    // (e.g. standings run standalone), fall back to "has both actuals".
    if (m.finished === false) return;           // live/in-play score → don't count yet
    var ah = numOrNull_(m.actH), aa = numOrNull_(m.actA);
    if (ah === null || aa === null) return;     // not played yet
    var H = team(m.home), A = team(m.away);
    H.pld++; A.pld++; H.gf += ah; H.ga += aa; A.gf += aa; A.ga += ah;
    if (ah > aa) { H.w++; A.l++; }
    else if (ah < aa) { A.w++; H.l++; }
    else { H.d++; A.d++; }
  });
  Object.keys(table).forEach(function (t) {
    var x = table[t];
    x.gd = x.gf - x.ga;
    x.pts = x.w * 3 + x.d;
  });

  // 2. Write into the Standings tab, locating each GROUP block and its team rows.
  var sh = sheetByName_(CONFIG.TAB_STANDINGS);
  var values = sh.getDataRange().getValues();
  var written = 0;

  // Find every "Pos / Team / Pld..." header row; the 4 rows beneath are teams.
  for (var r = 0; r < values.length; r++) {
    var row = values[r].map(function (x) { return String(x).trim(); });
    var posCol = row.indexOf('Pos');
    if (posCol < 0) continue;
    var teamCol = row.indexOf('Team', posCol);
    if (teamCol < 0) continue;
    var colIdx = mapStandingsCols_(row);
    if (colIdx.pts < 0) continue;

    // Collect the up-to-4 team rows beneath this header.
    var block = [];
    for (var k = 1; k <= 6 && r + k < values.length; k++) {
      var trow = values[r + k];
      var tname = String(trow[teamCol]).trim();
      if (!tname) break;
      if (String(trow[posCol]).trim() === 'Pos') break; // next header
      block.push({ sheetRow: r + k + 1, name: tname });
      if (block.length === 4) break;
    }
    if (!block.length) continue;

    // Stats for each team in this block (zero-stat if it hasn't played yet),
    // tagged with sheet order so tie-breaks are deterministic across runs.
    var stats = block.map(function (b, i) {
      var s = table[b.name] || { team: b.name, pld: 0, w: 0, d: 0, l: 0, gf: 0, ga: 0, gd: 0, pts: 0 };
      return { s: s, order: i };
    });

    // If NOT ONE team in this group has played, leave the block untouched —
    // don't replace the sheet's "-" placeholders with arbitrary 1–4 positions.
    var anyPlayed = stats.some(function (x) { return x.s.pld > 0; });
    if (!anyPlayed) continue;

    // Rank: Pts → GD → GF → original sheet order (stable, no churn on ties).
    var ranked = stats.slice().sort(function (a, b) {
      return (b.s.pts - a.s.pts) || (b.s.gd - a.s.gd) || (b.s.gf - a.s.gf) || (a.order - b.order);
    });
    var posByTeam = {};
    ranked.forEach(function (x, i) { posByTeam[x.s.team] = i + 1; });

    // Write each team's row (formula-aware; skips formula cells automatically).
    block.forEach(function (b) {
      var s = table[b.name];
      if (!s) return; // team hasn't played; leave its zero/placeholder cells alone
      written += writeStat_(sh, b.sheetRow, colIdx, s, posByTeam[b.name]);
    });
  }
  return written;
}

/** Map a Standings header row to 1-indexed columns. */
function mapStandingsCols_(row) {
  function f(label) { var i = row.indexOf(label); return i < 0 ? -1 : i + 1; }
  return {
    pos: f('Pos'), team: f('Team'), pld: f('Pld'), w: f('W'), d: f('D'),
    l: f('L'), gf: f('GF'), ga: f('GA'), gd: f('GD'), pts: f('Pts')
  };
}

/** Write one team's computed stats; returns number of cells written. */
function writeStat_(sh, sheetRow, c, s, pos) {
  var n = 0;
  if (setCellSafe_(sh, sheetRow, c.pos, pos, true)) n++;
  if (setCellSafe_(sh, sheetRow, c.pld, s.pld, true)) n++;
  if (setCellSafe_(sh, sheetRow, c.w, s.w, true)) n++;
  if (setCellSafe_(sh, sheetRow, c.d, s.d, true)) n++;
  if (setCellSafe_(sh, sheetRow, c.l, s.l, true)) n++;
  if (setCellSafe_(sh, sheetRow, c.gf, s.gf, true)) n++;
  if (setCellSafe_(sh, sheetRow, c.ga, s.ga, true)) n++;
  if (setCellSafe_(sh, sheetRow, c.gd, s.gd, true)) n++;
  if (setCellSafe_(sh, sheetRow, c.pts, s.pts, true)) n++;
  return n;
}
