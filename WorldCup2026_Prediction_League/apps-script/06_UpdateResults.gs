/**
 * ============================================================================
 *  06_UpdateResults.gs  ·  The main engine: API → Group Stage / Standings /
 *                          Knockout. Formula-aware throughout.
 * ============================================================================
 */

/**
 * Master update. Safe to run repeatedly (idempotent).
 *  1. fetch fixtures (1 API call)
 *  2. match API fixtures to Group Stage rows by team names
 *  3. write Act H / Act A for finished matches (and live, if you want)
 *  4. (optional) write per-player points into empty, non-formula cells
 *  5. recompute Standings (into empty, non-formula cells)
 *  6. fill Knockout team names + scores from the API
 *  7. apply kickoff locks
 * Returns a summary object for the toast/log.
 */
function updateAll_(opts) {
  opts = opts || {};
  // Defaults that make "refresh → latest score" actually work:
  //  • force      → bypass the 5-min cache, always pull fresh from the API.
  //  • overwrite* → actuals/points reflect the LATEST API value, not just the
  //    first one written (a 0–0 must be able to become 2–2). The formula guard
  //    in setCellSafe_ still protects any formula cells, and the no-op guard
  //    skips writes when the value is unchanged.
  if (opts.force === undefined) opts.force = true;
  if (opts.overwriteActuals === undefined) opts.overwriteActuals = true;
  if (opts.overwritePoints === undefined) opts.overwritePoints = true;

  var fixtures = fetchAllFixtures_(opts.force);
  var summary = { actualsWritten: 0, pointsWritten: 0, standingsWritten: 0, knockoutWritten: 0, bonusWritten: 0, locksApplied: 0, unmatched: [] };

  // ---- Group Stage ---------------------------------------------------------
  var gSh = sheetByName_(CONFIG.TAB_GROUP);
  var gLoc = locateMatchTab_(gSh);
  var gMatches = readMatches_(gSh, gLoc);

  var sheetTeams = [];
  Object.keys(gMatches).forEach(function (n) {
    if (gMatches[n].home) sheetTeams.push(gMatches[n].home);
    if (gMatches[n].away) sheetTeams.push(gMatches[n].away);
  });
  var resolve = makeTeamResolver_(sheetTeams);

  // Index API fixtures by an unordered team-pair key, resolved to sheet names.
  var apiByPair = {};
  var unmatchedNames = {};
  fixtures.forEach(function (fx) {
    var h = resolve(fx.homeName, fx.homeTla), a = resolve(fx.awayName, fx.awayTla);
    if (!h) unmatchedNames[fx.homeName] = true;
    if (!a) unmatchedNames[fx.awayName] = true;
    if (h && a) {
      apiByPair[pairKey_(h, a)] = fx;     // store both orientations
    }
  });
  summary.unmatched = Object.keys(unmatchedNames);

  // Write actuals + points for each group match we can match.
  Object.keys(gMatches).forEach(function (n) {
    var m = gMatches[n];
    if (!m.home || !m.away) return;
    var fx = apiByPair[pairKey_(m.home, m.away)];
    if (!fx) return;

    // Orient API goals to the sheet's home/away.
    var oriented = orientGoals_(fx, m.home, m.away, resolve);
    // Write the SCORE for finished OR (when live mode on) in-play matches, so
    // the Act columns mirror reality. Compute POINTS only for FINISHED matches
    // — the rules award points "once the real result is in", and free-tier live
    // data is delayed/volatile, so provisional points would mislead.
    var showScore = fx.finished || (opts.includeLive && fx.inPlay);
    var scorePoints = fx.finished;

    if (showScore && oriented.h !== null && oriented.a !== null) {
      if (setCellSafe_(gSh, m.rowIndex, gLoc.col.actH, oriented.h, opts.overwriteActuals)) summary.actualsWritten++;
      if (setCellSafe_(gSh, m.rowIndex, gLoc.col.actA, oriented.a, opts.overwriteActuals)) summary.actualsWritten++;
      m.actH = oriented.h; m.actA = oriented.a; // reflect for points/standings below
    }
    // Tell standings whether this result is FINAL (don't count a live score in
    // the group tables until the match is over).
    m.finished = !!fx.finished;

    // Per-player points — only if enabled and the target cell is empty/non-formula.
    if (CONFIG.WRITE_POINTS && scorePoints) {
      CONFIG.PLAYERS.forEach(function (p) {
        var pc = gLoc.players[p];
        if (!pc) return;
        var pred = m.preds[p] || {};
        var res = scorePrediction_(pred.h, pred.a, m.actH, m.actA, isJoker_(pred.jk), true);
        if (setCellSafe_(gSh, m.rowIndex, pc.pts, res.points, opts.overwritePoints)) {
          summary.pointsWritten++;
          // Cosmetic: gild an active, positive Joker points cell.
          if (isJoker_(pred.jk) && res.points > 0) {
            gSh.getRange(m.rowIndex, pc.pts).setBackground(CONFIG.JOKER_GOLD);
          }
        }
      });
    }
  });

  // ---- Standings -----------------------------------------------------------
  if (CONFIG.WRITE_STANDINGS) {
    summary.standingsWritten = recomputeStandings_(gMatches);
  }

  // ---- Knockout ------------------------------------------------------------
  summary.knockoutWritten = updateKnockout_(fixtures, resolve, opts);

  // ---- Bonus Calls (derivable actuals) -------------------------------------
  // Self-gating: writes nothing until the Final/3rd-place/knockout data exists,
  // so it's safe to call every run. Subjective picks stay manual.
  try {
    summary.bonusWritten = updateBonusActuals_(fixtures, resolve);
  } catch (e) {
    summary.bonusWritten = 0;
    diagLog_('Bonus auto-fill skipped: ' + e.message);
  }

  // ---- Kickoff locks -------------------------------------------------------
  if (CONFIG.ENABLE_KICKOFF_LOCK) {
    summary.locksApplied = applyKickoffLocks_();
  }

  // ---- Diagnostics ---------------------------------------------------------
  if (summary.unmatched.length) {
    diagLog_('UNMATCHED API team names (add to TEAM_ALIASES): ' + summary.unmatched.join(', '));
  }
  diagLog_('updateAll summary: ' + JSON.stringify(summary));
  return summary;
}

/** Unordered pair key so home/away orientation doesn't matter for lookup. */
function pairKey_(a, b) {
  return [normName_(a), normName_(b)].sort().join('|');
}

/**
 * Return API goals oriented to the sheet's home/away teams.
 * @return {{h:(number|null), a:(number|null)}}
 */
function orientGoals_(fx, sheetHome, sheetAway, resolve) {
  var apiHome = resolve(fx.homeName, fx.homeTla);
  if (apiHome && normName_(apiHome) === normName_(sheetHome)) {
    return { h: numOrNull_(fx.homeGoals), a: numOrNull_(fx.awayGoals) };
  }
  // API home is the sheet's away → swap.
  return { h: numOrNull_(fx.awayGoals), a: numOrNull_(fx.homeGoals) };
}

function numOrNull_(v) {
  return (v === null || v === undefined || v === '') ? null : Number(v);
}
