/**
 * ============================================================================
 *  01_Bracket.gs  ·  Verified FIFA World Cup 2026 knockout bracket structure
 * ============================================================================
 *
 *  Source of truth at RUNTIME is API-Football: once the group stage ends, the
 *  /fixtures response returns matches 73–104 already populated with the real
 *  qualified teams and (as they play) scores. So we normally just read team
 *  names + scores straight from the API for the Knockout tab.
 *
 *  This map exists for two reasons:
 *    (a) PREVIEW — before the API fills knockout fixtures, we can show which
 *        group-slot feeds which match (e.g. "2A vs 2B" for match 73), so the
 *        Knockout tab isn't blank.
 *    (b) VALIDATION — we can sanity-check that the API's knockout pairings line
 *        up with the official bracket adjacency, and flag if they don't.
 *
 *  Pairings (R32, matches 73–88) and the full adjacency (R16→Final, 89–104)
 *  are corroborated across Wikipedia ("2026 FIFA World Cup knockout stage")
 *  and Fox Sports' bracket. The 8 third-place slots are marked '3X' because
 *  WHICH third-placed group fills them depends on FIFA's Annex C permutation
 *  table — which we deliberately do NOT hard-code (495 rows, error-prone).
 *  The API resolves those for us. See research notes in REBUILD_NOTES.md.
 *  --------------------------------------------------------------------------
 */

/**
 * Round of 32 slot definitions, keyed by match number.
 * Each slot is one of:
 *   { type:'W',  group:'A' }  → Winner of Group A   (1A)
 *   { type:'RU', group:'B' }  → Runner-up of Group B (2B)
 *   { type:'3rd', pool:['A','B','C','D','F'] } → a 3rd-placed team from that pool
 */
var R32 = {
  73: { home: { type: 'RU', group: 'A' }, away: { type: 'RU', group: 'B' } },
  74: { home: { type: 'W', group: 'E' }, away: { type: '3rd', pool: ['A', 'B', 'C', 'D', 'F'] } },
  75: { home: { type: 'W', group: 'F' }, away: { type: 'RU', group: 'C' } },
  76: { home: { type: 'W', group: 'C' }, away: { type: 'RU', group: 'F' } },
  77: { home: { type: 'W', group: 'I' }, away: { type: '3rd', pool: ['C', 'D', 'F', 'G', 'H'] } },
  78: { home: { type: 'RU', group: 'E' }, away: { type: 'RU', group: 'I' } },
  79: { home: { type: 'W', group: 'A' }, away: { type: '3rd', pool: ['C', 'E', 'F', 'H', 'I'] } },
  80: { home: { type: 'W', group: 'L' }, away: { type: '3rd', pool: ['E', 'H', 'I', 'J', 'K'] } },
  81: { home: { type: 'W', group: 'D' }, away: { type: '3rd', pool: ['B', 'E', 'F', 'I', 'J'] } },
  82: { home: { type: 'W', group: 'G' }, away: { type: '3rd', pool: ['A', 'E', 'H', 'I', 'J'] } },
  83: { home: { type: 'RU', group: 'K' }, away: { type: 'RU', group: 'L' } },
  84: { home: { type: 'W', group: 'H' }, away: { type: 'RU', group: 'J' } },
  85: { home: { type: 'W', group: 'B' }, away: { type: '3rd', pool: ['E', 'F', 'G', 'I', 'J'] } },
  86: { home: { type: 'W', group: 'J' }, away: { type: 'RU', group: 'H' } },
  87: { home: { type: 'W', group: 'K' }, away: { type: '3rd', pool: ['D', 'E', 'I', 'J', 'L'] } },
  88: { home: { type: 'RU', group: 'D' }, away: { type: 'RU', group: 'G' } }
};

/**
 * Adjacency for matches 89–104. W## = winner of match ##, L## = loser of ##.
 * This is the complete left/right bracket tree.
 */
var BRACKET_TREE = {
  // Round of 16
  89: { home: 'W74', away: 'W77' },
  90: { home: 'W73', away: 'W75' },
  91: { home: 'W76', away: 'W78' },
  92: { home: 'W79', away: 'W80' },
  93: { home: 'W83', away: 'W84' },
  94: { home: 'W81', away: 'W82' },
  95: { home: 'W86', away: 'W88' },
  96: { home: 'W85', away: 'W87' },
  // Quarter-finals
  97: { home: 'W89', away: 'W90' },
  98: { home: 'W93', away: 'W94' },
  99: { home: 'W91', away: 'W92' },
  100: { home: 'W95', away: 'W96' },
  // Semi-finals
  101: { home: 'W97', away: 'W98' },
  102: { home: 'W99', away: 'W100' },
  // Third-place playoff + Final
  103: { home: 'L101', away: 'L102' },
  104: { home: 'W101', away: 'W102' }
};

/** Human-readable label for a R32 slot, used for the preview pre-fill. */
function slotLabel_(slot) {
  if (slot.type === 'W') return 'Winner ' + slot.group;
  if (slot.type === 'RU') return 'Runner-up ' + slot.group;
  if (slot.type === '3rd') return '3rd (' + slot.pool.join('/') + ')';
  return '?';
}

/**
 * Build preview text for every knockout match (73–104) from the bracket map.
 * Returns { 73: {home, away}, ... } of label strings. Used only when the API
 * has not yet populated knockout team names.
 */
function buildKnockoutPreview_() {
  var out = {};
  for (var m in R32) {
    out[m] = { home: slotLabel_(R32[m].home), away: slotLabel_(R32[m].away) };
  }
  for (var k in BRACKET_TREE) {
    var node = BRACKET_TREE[k];
    out[k] = { home: refLabel_(node.home), away: refLabel_(node.away) };
  }
  return out;
}

/** "W74" → "Winner M74", "L101" → "Loser M101". */
function refLabel_(ref) {
  var kind = ref.charAt(0) === 'W' ? 'Winner' : 'Loser';
  return kind + ' M' + ref.substring(1);
}
