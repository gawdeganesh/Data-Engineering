/**
 * ============================================================================
 *  04_TeamNames.gs  ·  Reconcile API team names ↔ sheet team names
 * ============================================================================
 *  football-data.org's exact strings for some nations differ from the sheet
 *  ("USA" vs "United States", "Korea Republic" vs "South Korea", etc.).
 *  Strategy (no silent mismatches):
 *    1. normalize both sides: lowercase, strip diacritics, drop non-alphanum
 *    2. apply an alias table of known variants → the sheet's canonical name
 *    3. anything still unmatched is logged to the hidden _diag tab so you can
 *       add one alias line — the script never guesses a wrong team.
 * ============================================================================
 */

/**
 * Alias map: normalized API/variant spelling → EXACT sheet team name.
 * Add a line here if the _diag tab reports an unmatched API name.
 */
var TEAM_ALIASES = {
  'usa': 'United States',
  'unitedstates': 'United States',
  'unitedstatesofamerica': 'United States',
  'korearepublic': 'South Korea',
  'southkorea': 'South Korea',
  'czechrepublic': 'Czechia',
  'czechia': 'Czechia',
  'turkey': 'Türkiye',
  'turkiye': 'Türkiye',
  'cotedivoire': 'Ivory Coast',
  'ivorycoast': 'Ivory Coast',
  'caboverde': 'Cape Verde',
  'capeverde': 'Cape Verde',
  'congodr': 'DR Congo',
  'drcongo': 'DR Congo',
  'democraticrepublicofcongo': 'DR Congo',
  'bosniaandherzegovina': 'Bosnia-Herzegovina',
  'bosniaherzegovina': 'Bosnia-Herzegovina',
  'bosnia': 'Bosnia-Herzegovina',
  'iriran': 'Iran',
  'iran': 'Iran',
  'iranislamicrepublic': 'Iran'
};

/** Normalize a team name for comparison: lowercase, de-accent, alnum only. */
function normName_(name) {
  if (name === null || name === undefined) return '';
  var s = String(name);
  // Strip diacritics via NFD when available (V8 supports normalize()).
  try { s = s.normalize('NFD').replace(/[̀-ͯ]/g, ''); } catch (e) { /* older runtime */ }
  return s.toLowerCase().replace(/[^a-z0-9]/g, '');
}

/**
 * TLA (3-letter) → sheet name. football-data exposes a stable `tla` per team
 * that doesn't change with spelling (Turkey→Türkiye etc.), so it's a reliable
 * secondary key when the name doesn't match. Covers only the tricky nations;
 * everything else resolves by name.
 */
var TEAM_TLA = {
  USA: 'United States',
  KOR: 'South Korea',
  CZE: 'Czechia',
  TUR: 'Türkiye',
  CIV: 'Ivory Coast',
  CPV: 'Cape Verde',
  COD: 'DR Congo',
  BIH: 'Bosnia-Herzegovina',
  IRN: 'Iran',
  CUW: 'Curaçao'
};

/**
 * Build a resolver that maps an API team to the sheet's canonical name.
 * The returned function accepts (name) or (name, tla); tla is the stable
 * fallback key when the name doesn't normalize to a known team.
 * @param {Array<string>} sheetTeams  every team name as written on the sheet
 * @return {function(string, string=):(string|null)}
 */
function makeTeamResolver_(sheetTeams) {
  // Index the sheet's own names by their normalized form (self-match first).
  var byNorm = {};
  sheetTeams.forEach(function (t) {
    if (t) byNorm[normName_(t)] = t;
  });

  return function resolve(apiName, tla) {
    var n = normName_(apiName);
    if (n && byNorm[n]) return byNorm[n];                 // exact normalized match
    if (n && TEAM_ALIASES[n]) return TEAM_ALIASES[n];      // known name alias
    if (tla) {                                             // stable TLA fallback
      var t = String(tla).toUpperCase();
      if (TEAM_TLA[t] && byNorm[normName_(TEAM_TLA[t])]) return TEAM_TLA[t];
      if (TEAM_TLA[t]) return TEAM_TLA[t];
    }
    return null;                                           // unmatched → caller logs it
  };
}

/** Collect the full set of team names written on the Group Stage tab. */
function collectSheetTeams_(groupGrid, col) {
  var set = {};
  groupGrid.forEach(function (row) {
    var h = row[col.home], a = row[col.away];
    if (h) set[h] = true;
    if (a) set[a] = true;
  });
  return Object.keys(set);
}
