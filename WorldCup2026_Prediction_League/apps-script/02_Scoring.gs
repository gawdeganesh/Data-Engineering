/**
 * ============================================================================
 *  02_Scoring.gs  ·  Pure scoring logic (no Sheet/API dependencies)
 * ============================================================================
 *  Mirrors the "How to Play" tab exactly:
 *    5  exact scoreline
 *    4  right result + right goal difference
 *    3  right result only
 *    0  wrong
 *   -1  no prediction on a played match
 *  Joker ('J') doubles ONLY a positive score.
 *
 *  Kept side-effect-free so it is unit-testable (see 09_Tests.gs).
 * ============================================================================
 */

/**
 * Score a single prediction against an actual result.
 * @param {number|null} predH  predicted home goals
 * @param {number|null} predA  predicted away goals
 * @param {number|null} actH   actual home goals
 * @param {number|null} actA   actual away goals
 * @param {boolean} joker       Joker active on this match
 * @param {boolean} played      whether the match has a final result
 * @return {{points:number, tier:string}}
 */
function scorePrediction_(predH, predA, actH, actA, joker, played) {
  // No actual result yet → nothing to score.
  if (!played || actH === null || actA === null || actH === '' || actA === '') {
    return { points: 0, tier: 'PENDING' };
  }

  var hasPred = predH !== null && predA !== null && predH !== '' && predA !== '';
  if (!hasPred) {
    // Played match with no prediction → penalty. Joker cannot rescue a negative.
    return { points: SCORING.NO_PREDICTION, tier: 'NO_PREDICTION' };
  }

  predH = Number(predH); predA = Number(predA);
  actH = Number(actH); actA = Number(actA);
  if (isNaN(predH) || isNaN(predA) || isNaN(actH) || isNaN(actA)) {
    return { points: 0, tier: 'INVALID' };
  }

  var base, tier;
  if (predH === actH && predA === actA) {
    base = SCORING.EXACT; tier = 'EXACT';
  } else if (sign_(predH - predA) === sign_(actH - actA) && (predH - predA) === (actH - actA)) {
    // same winner AND same goal difference (margin), but not the exact line
    base = SCORING.RESULT_AND_GD; tier = 'RESULT_AND_GD';
  } else if (sign_(predH - predA) === sign_(actH - actA)) {
    // same winner / draw, wrong margin
    base = SCORING.RESULT_ONLY; tier = 'RESULT_ONLY';
  } else {
    base = SCORING.WRONG; tier = 'WRONG';
  }

  if (joker && base > 0) base *= 2;   // Joker doubles positive scores only
  return { points: base, tier: tier };
}

/** Returns -1, 0, or 1 for negative/zero/positive — the match outcome class. */
function sign_(n) {
  return n > 0 ? 1 : (n < 0 ? -1 : 0);
}

/** True if a Joker cell holds the joker flag (case-insensitive 'J'). */
function isJoker_(cell) {
  return String(cell || '').trim().toUpperCase() === SCORING.JOKER_FLAG;
}

/** True if a Lock cell holds the lock flag (case-insensitive 'L'). */
function isLocked_(cell) {
  return String(cell || '').trim().toUpperCase() === SCORING.LOCK_FLAG;
}
