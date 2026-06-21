/**
 * ============================================================================
 *  WORLD CUP 2026 PREDICTION LEAGUE — Apps Script rebuild
 *  00_Config.gs   ·   Central configuration + the "what each section does" map
 * ============================================================================
 *
 *  WHAT THIS PROJECT DOES (read this once)
 *  --------------------------------------------------------------------------
 *  The spreadsheet has 6 tabs. This script is the engine that the old (lost)
 *  script used to be. Its jobs, by tab:
 *
 *   • How to Play   – static rules. Script never touches it.
 *   • Group Stage   – 72 matches. Script writes ACTUAL scores (Act H / Act A)
 *                     pulled from API-Football, and (optionally) the per-player
 *                     points — but ONLY into cells that are not formulas and
 *                     not locked. It also stamps the Lock column at kickoff.
 *   • Standings     – 12 group tables. Script can compute these from the Group
 *                     Stage actuals (formula-aware: skips formula cells). It
 *                     always computes them internally to resolve the bracket.
 *   • Knockout      – matches 73–104. Once the group stage finishes, the API
 *                     itself returns the knockout fixtures with real team names
 *                     and scores; the script writes Home/Away/Act from the API.
 *                     A verified bracket map (73→104) is included as a fallback
 *                     / preview before the API populates those rows.
 *   • Bonus Calls   – auto-fills the "ACTUAL RESULTS" block that can be derived
 *                     (Winner, Runner-up, Third, USA-escaped-group). The three
 *                     subjective ones (Golden Boot, Golden Ball, Surprise team)
 *                     stay manual, exactly as the tab says.
 *   • Leaderboard   – formulas own it. Script never writes it; it only PROTECTS
 *                     it (you asked for this tab to be locked).
 *
 *  LOCK / PROTECTION FEATURES (you asked for these)
 *  --------------------------------------------------------------------------
 *   1. Strict-Mode kickoff lock: when a match's kickoff time has passed, the
 *      script puts 'L' in that row's Lock column, greys the row, and protects
 *      the three players' prediction cells so no one can edit after kickoff.
 *   2. Bonus Calls + Leaderboard tabs are protected (locked) as whole sheets.
 *
 *  The whole thing is driven by ONE API call per run and a time trigger.
 * ============================================================================
 */

/** Script-wide configuration. Edit values here, not scattered through the code. */
var CONFIG = {
  // --- football-data.org (v4) -----------------------------------------------
  // Two ways to supply the token (getApiKey_ checks them in this order):
  //   1) Script Properties under the name API_KEY_PROP — the private option;
  //      set it via "World Cup ▸ Set API key…". Nothing sensitive in code.
  //   2) API_KEY below — the simple option; paste your token here directly.
  //      (Visible to anyone who can open the Apps Script editor for this sheet.)
  // The World Cup is on the FREE tier (code WC / id 2000, 10 req/min). Note:
  // free-tier scores are DELAYED — final results land fine, live in-play lags.
  API_KEY_PROP: 'FOOTBALLDATA_TOKEN',              // name of the Script Property
  API_KEY: '041f977f4d80432983ba0d4d0d23612f',                                     // paste your football-data.org token here
  API_BASE: 'https://api.football-data.org/v4',
  API_HEADER: 'X-Auth-Token',                      // football-data auth header
  WC_COMPETITION: 'WC',                            // FIFA World Cup competition code (id 2000)
  WC_SEASON: 2026,                                 // edition year

  // --- Tab names (must match the spreadsheet exactly) -----------------------
  TAB_HOWTO: 'How to Play',
  TAB_STANDINGS: 'Standings',
  TAB_GROUP: 'Group Stage',
  TAB_KNOCKOUT: 'Knockout',
  TAB_BONUS: 'Bonus Calls',
  TAB_LEADERBOARD: 'Leaderboard',

  // Diagnostics logging. By default the script writes NO new tab — logs go to
  // the Apps Script execution log (View ▸ Executions) and the Diagnostics
  // dialog. Flip CREATE_DIAG_TAB to true ONLY if you want a hidden "_diag" tab
  // added inside this same spreadsheet for a persistent on-sheet log.
  CREATE_DIAG_TAB: false,
  TAB_DIAG: '_diag',

  // --- Behaviour switches ---------------------------------------------------
  // If TRUE, the script will compute & write per-player points and standings
  // into any cell that is currently EMPTY (it never overwrites a formula).
  // Leave TRUE — it is harmless when your formulas are intact (those cells are
  // skipped) and a lifesaver if the scoring formulas were also lost.
  WRITE_POINTS: true,
  WRITE_STANDINGS: true,

  // If TRUE, stamp 'L' in the Lock column and protect predictions at kickoff.
  ENABLE_KICKOFF_LOCK: true,
  // Grey fill applied to locked rows.
  LOCK_GREY: '#d9d9d9',
  // Gold fill for an active Joker's points cell (cosmetic, matches the rules text).
  JOKER_GOLD: '#ffd966',

  // Protect these whole tabs (you asked for these to be locked).
  PROTECT_TABS: ['Bonus Calls', 'Leaderboard'],
  // If TRUE protection is "warning only" (a dialog, but edit still possible).
  // If FALSE, only the script owner can edit the protected tabs/cells.
  PROTECT_WARNING_ONLY: false,

  // Players, in the order their column-blocks appear on Group Stage / Knockout.
  PLAYERS: ['Ganesh', 'Siddhesh', 'Aniket'],

  // Spreadsheet timezone used for kickoff parsing (matches the sheet's "CT").
  TIMEZONE: 'America/Chicago',
  EDITION_YEAR: 2026
};

/** Scoring tiers (per "How to Play"). Joker doubles ONLY positive scores. */
var SCORING = {
  EXACT: 5,            // dead-on scoreline
  RESULT_AND_GD: 4,    // right winner AND right goal difference
  RESULT_ONLY: 3,      // right winner/draw, wrong margin
  WRONG: 0,
  NO_PREDICTION: -1,   // no prediction on a played match
  JOKER_FLAG: 'J',
  LOCK_FLAG: 'L'
};
