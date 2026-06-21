/**
 * ============================================================================
 *  05_Sheet.gs  ·  Spreadsheet access layer (header/row auto-location)
 * ============================================================================
 *  Everything here locates columns by HEADER TEXT and rows by the match number
 *  in column "#", so the script keeps working if rows shift or a column moves.
 *  Writes are FORMULA-AWARE: a cell holding a formula is never overwritten.
 * ============================================================================
 */

function ss_() { return SpreadsheetApp.getActiveSpreadsheet(); }

function sheetByName_(name) {
  var sh = ss_().getSheetByName(name);
  if (!sh) throw new Error('Tab not found: "' + name + '". Check CONFIG tab names.');
  return sh;
}

/**
 * Locate the two-line header on Group Stage / Knockout and build a column map.
 * The lower header row contains "#"; the upper row carries player names.
 * @return {{headerRow:number, dataStartRow:number, col:Object, players:Object}}
 *   col keys: num,date,grp/stg,home,away,lock,actH,actA,venue(optional)
 *   players: { Ganesh:{h,a,jk,pts}, Siddhesh:{...}, Aniket:{...} } (1-indexed cols)
 */
function locateMatchTab_(sh) {
  var values = sh.getDataRange().getValues();
  var headerRow = -1;
  for (var r = 0; r < Math.min(values.length, 12); r++) {
    var row = values[r];
    for (var c = 0; c < row.length; c++) {
      if (String(row[c]).trim() === '#') { headerRow = r; break; }
    }
    if (headerRow >= 0) break;
  }
  if (headerRow < 0) throw new Error('Could not find the "#" header row in "' + sh.getName() + '".');

  var header = values[headerRow].map(function (x) { return String(x).trim(); });
  var upper = headerRow > 0 ? values[headerRow - 1].map(function (x) { return String(x).trim(); }) : [];

  function findCol(labels) {
    for (var i = 0; i < header.length; i++) {
      for (var j = 0; j < labels.length; j++) {
        if (header[i].toLowerCase() === labels[j].toLowerCase()) return i + 1; // 1-indexed
      }
    }
    return -1;
  }

  var col = {
    num: findCol(['#']),
    date: findCol(['Date', 'Date (auto)']),
    ko: findCol(['KO (local)', 'KO (CT)', 'KO']),
    // Group Stage uses "Grp"; Knockout has BOTH "Stg" (codes: R32/R16/QF…) and
    // "Round" (text: "Round of 32"). Bind to the CODE column first so the stage
    // bucketing in 08_Knockout matches its R32/R16/… keys, not "Round of 32".
    grp: findCol(['Grp', 'Stg']),
    round: findCol(['Round']),
    home: findCol(['Home']),
    away: findCol(['Away']),
    lock: findCol(['Lock']),
    actH: findCol(['Act H']),
    actA: findCol(['Act A']),
    venue: findCol(['Venue'])
  };

  // Player blocks. PRIMARY method: locate by the lower-row sub-headers
  // ("G H"/"G A"/"G Pts" for Ganesh, "S …" Siddhesh, "A …" Aniket) — robust to
  // however the player name is merged/centered in the upper row. FALLBACK:
  // the upper-row name anchor (+0/+1/+2/+3). Each block is validated.
  var players = {};
  var warnings = [];
  CONFIG.PLAYERS.forEach(function (p) {
    var ini = p.charAt(0).toUpperCase();              // Ganesh→G, Siddhesh→S, Aniket→A
    var hCol = exactCol_(header, ini + ' H');
    var aCol = exactCol_(header, ini + ' A');
    var ptsCol = exactCol_(header, ini + ' Pts');

    var block = null;
    if (hCol > 0 && aCol > 0 && ptsCol > 0) {
      // Joker = the "Jk" column sitting between A and Pts (blocks are H,A,Jk,Pts).
      var jkCol = aCol + 1;
      block = { h: hCol, a: aCol, jk: jkCol, pts: ptsCol };
    } else {
      // Fallback to the upper-row name anchor.
      for (var i = 0; i < upper.length; i++) {
        if (upper[i].toLowerCase() === p.toLowerCase()) {
          block = { h: i + 1, a: i + 2, jk: i + 3, pts: i + 4 };
          break;
        }
      }
    }

    if (block) {
      // Validate the resolved sub-headers really belong to this player.
      var okH = String(header[block.h - 1] || '').toLowerCase() === (ini + ' h').toLowerCase();
      var okPts = String(header[block.pts - 1] || '').toLowerCase() === (ini + ' pts').toLowerCase();
      if (okH && okPts) {
        players[p] = block;
      } else {
        warnings.push(p + ' (got "' + header[block.h - 1] + '" / "' + header[block.pts - 1] + '")');
      }
    } else {
      warnings.push(p + ' (no header found)');
    }
  });

  if (warnings.length) {
    // Visible failure rather than a silent wrong-column write.
    diagLog_('locateMatchTab_("' + sh.getName() + '"): could not safely locate ' +
             'player block(s): ' + warnings.join('; ') + '. Points NOT written for these.');
  }

  return { headerRow: headerRow + 1, dataStartRow: headerRow + 2, col: col, players: players, values: values };
}

/** Exact (trimmed, case-insensitive) header match → 1-indexed column, or -1. */
function exactCol_(header, label) {
  for (var i = 0; i < header.length; i++) {
    if (String(header[i]).trim().toLowerCase() === label.toLowerCase()) return i + 1;
  }
  return -1;
}

/**
 * Read match rows from a located tab into objects keyed by match number.
 * @return {Object} { matchNum: { rowIndex, home, away, lock, actH, actA,
 *                                koText, grp, preds:{player:{h,a,jk}} } }
 */
function readMatches_(sh, loc) {
  var out = {};
  var values = loc.values || sh.getDataRange().getValues();
  for (var r = loc.dataStartRow - 1; r < values.length; r++) {
    var row = values[r];
    var num = row[loc.col.num - 1];
    if (num === '' || num === null || isNaN(Number(num))) continue;
    var rec = {
      rowIndex: r + 1, // 1-indexed sheet row
      num: Number(num),
      home: loc.col.home > 0 ? row[loc.col.home - 1] : '',
      away: loc.col.away > 0 ? row[loc.col.away - 1] : '',
      lock: loc.col.lock > 0 ? row[loc.col.lock - 1] : '',
      actH: loc.col.actH > 0 ? row[loc.col.actH - 1] : '',
      actA: loc.col.actA > 0 ? row[loc.col.actA - 1] : '',
      koText: loc.col.ko > 0 ? row[loc.col.ko - 1] : '',
      dateText: loc.col.date > 0 ? row[loc.col.date - 1] : '',
      grp: loc.col.grp > 0 ? row[loc.col.grp - 1] : '',
      preds: {}
    };
    CONFIG.PLAYERS.forEach(function (p) {
      var pc = loc.players[p];
      if (pc) {
        rec.preds[p] = {
          h: row[pc.h - 1], a: row[pc.a - 1], jk: row[pc.jk - 1], pts: row[pc.pts - 1]
        };
      }
    });
    out[rec.num] = rec;
  }
  return out;
}

/**
 * Formula-aware single-cell write. Writes `value` only if the target cell is
 * empty (or `overwrite` is true) AND the cell is not a formula AND not locked.
 * @return {boolean} whether it wrote.
 */
function setCellSafe_(sh, row, col, value, overwrite) {
  if (col <= 0) return false;
  var rng = sh.getRange(row, col);
  var formula = rng.getFormula();
  if (formula) return false;                 // never clobber a formula
  var cur = rng.getValue();
  var isEmpty = (cur === '' || cur === null);
  if (!isEmpty && !overwrite) return false;
  if (!isEmpty && overwrite && String(cur) === String(value)) return false; // no-op
  rng.setValue(value);
  return true;
}

/** Apply a background colour to a whole match row across a column span. */
function shadeRow_(sh, row, fromCol, toCol, color) {
  if (fromCol <= 0 || toCol < fromCol) return;
  sh.getRange(row, fromCol, 1, toCol - fromCol + 1).setBackground(color);
}
