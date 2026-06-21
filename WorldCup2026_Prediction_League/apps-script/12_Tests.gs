/**
 * ============================================================================
 *  12_Tests.gs  ·  Self-contained tests for the pure logic (no API/Sheet)
 * ============================================================================
 *  Run `runAllTests` from the Apps Script editor and read the Logs.
 *  These validate the scoring engine against the REAL group-stage results and
 *  predictions read from the sheet (matches 1–8), and against your Leaderboard
 *  group totals (Ganesh 11, Siddhesh 23, Aniket 16).
 * ============================================================================
 */

function runAllTests() {
  var failures = [];
  function check(name, got, want) {
    var ok = JSON.stringify(got) === JSON.stringify(want);
    Logger.log((ok ? 'PASS' : 'FAIL') + ' · ' + name + ' · got=' + JSON.stringify(got) + ' want=' + JSON.stringify(want));
    if (!ok) failures.push(name);
  }

  /* ---- scoring tiers ---- */
  check('exact', scorePrediction_(2, 1, 2, 1, false, true).points, 5);
  check('result+GD (2-0 vs 3-1)', scorePrediction_(2, 0, 3, 1, false, true).points, 4);
  check('result only (2-1 vs 3-0)', scorePrediction_(2, 1, 3, 0, false, true).points, 3);
  check('wrong winner', scorePrediction_(2, 1, 0, 1, false, true).points, 0);
  check('draw exact', scorePrediction_(1, 1, 1, 1, false, true).points, 5);
  check('draw result only (1-1 vs 2-2)', scorePrediction_(1, 1, 2, 2, false, true).points, 3);
  check('no prediction played', scorePrediction_(null, null, 1, 0, false, true).points, -1);
  check('pending (no actual)', scorePrediction_(2, 1, null, null, false, false).points, 0);

  /* ---- Joker: doubles positive only ---- */
  check('joker doubles exact', scorePrediction_(2, 1, 2, 1, true, true).points, 10);
  check('joker doubles result-only', scorePrediction_(2, 1, 3, 0, true, true).points, 6);
  check('joker does NOT rescue wrong', scorePrediction_(2, 1, 0, 1, true, true).points, 0);
  check('joker does NOT double no-pred penalty', scorePrediction_(null, null, 1, 0, true, true).points, -1);

  /* ---- real sheet data: matches 1–8, three players ---- */
  // [actH, actA, predH, predA, jokerBool]  — from the Group Stage tab I read.
  var DATA = {
    Ganesh: [
      [2,0, 2,0,false], // M1 Mex 2-0 RSA → exact 5
      [2,1, 1,1,false], // M2 KOR 2-1 CZE → pred 1-1 draw vs home win → wrong 0
      [1,1, 1,0,false], // M3 CAN 1-1 BIH → pred home win vs draw → wrong 0
      [4,1, 2,1,false], // M4 USA 4-1 PAR → result+GD? GD pred +1 actual +3 → result only 3
      [1,1, 0,2,false], // M6 QAT 1-1 SUI → pred away win vs draw → 0
      [1,1, 1,2,false], // M7 BRA 1-1 MAR → pred away win vs draw → 0
      [0,1, 0,2,false], // M8 HAI 0-1 SCO → away win both, GD -1 vs -2 → result only 3
      [2,0, 1,2,false]  // M5 AUS 2-0 TUR → pred away win vs home win → 0
    ],
    Siddhesh: [
      [2,0, 2,1,false], // M1 → home win, GD +1 vs +2 → result only 3
      [2,1, 2,1,false], // M2 → exact 5
      [1,1, 1,1,false], // M3 → exact 5
      [4,1, 3,2,false], // M4 → home win GD +1 vs +3 → result only 3
      [1,1, 0,2,false], // M6 → away win vs draw → 0
      [1,1, 2,2,false], // M7 → draw vs draw, GD 0=0 → result+GD = 4 (matches sheet's S Pts=4)
      [0,1, 0,2,false], // M8 → away win GD -1 vs -2 → result only 3
      [2,0, 1,2,false]  // M5 → away win vs home win → 0
    ],
    Aniket: [
      [2,0, 2,0,false], // M1 → exact 5
      [2,1, 2,1,false], // M2 → exact 5
      [1,1, 2,1,false], // M3 → home win vs draw → 0
      [4,1, 1,0,false], // M4 → home win GD +1 vs +3 → result only 3
      [1,1, 0,2,false], // M6 → 0
      [1,1, 2,1,false], // M7 → home win vs draw → 0
      [0,1, 0,2,false], // M8 → away win GD -1 vs -2 → result only 3
      [2,0, 0,1,false]  // M5 → away win vs home win → 0
    ]
  };
  var expectedTotals = { Ganesh: 11, Siddhesh: 23, Aniket: 16 };
  Object.keys(DATA).forEach(function (p) {
    var total = DATA[p].reduce(function (sum, row) {
      return sum + scorePrediction_(row[2], row[3], row[0], row[1], row[4], true).points;
    }, 0);
    check('group total ' + p, total, expectedTotals[p]);
  });

  /* ---- team-name normalization ---- */
  check('norm Türkiye', normName_('Türkiye'), 'turkiye');
  check('norm Curaçao', normName_('Curaçao'), 'curacao');
  check('norm Côte dIvoire', normName_("Côte d'Ivoire"), 'cotedivoire');
  var resolve = makeTeamResolver_(['United States', 'South Korea', 'Czechia', 'Türkiye', 'Ivory Coast', 'DR Congo']);
  check('resolve USA', resolve('USA'), 'United States');
  check('resolve Korea Republic', resolve('Korea Republic'), 'South Korea');
  check('resolve Czech Republic', resolve('Czech Republic'), 'Czechia');
  check('resolve Turkey', resolve('Turkey'), 'Türkiye');
  check('resolve Cote dIvoire', resolve("Côte d'Ivoire"), 'Ivory Coast');
  check('resolve Congo DR', resolve('Congo DR'), 'DR Congo');
  check('resolve unknown→null', resolve('Atlantis'), null);

  /* ---- kickoff parsing (ABSOLUTE INSTANT, not just calendar fields) ---- */
  // Match 1: Jun 11 2026, 15:00 Central. June = CDT (UTC−5) → 20:00 UTC.
  // Epoch = 1781208000 s = 1781208000000 ms. This catches the timezone bug
  // that calendar-field checks alone would miss.
  var ko = parseKickoff_('Thu, Jun 11', '15:00');
  check('kickoff parses', !!ko, true);
  check('kickoff epoch (15:00 CDT = 20:00 UTC)', ko ? ko.getTime() : -1, 1781208000000);
  // A January date would be CST (UTC−6); guards the DST branch indirectly.
  var koWinter = parseKickoff_('Thu, Jan 15', '12:00'); // 12:00 CST = 18:00 UTC
  check('kickoff winter epoch (12:00 CST = 18:00 UTC)', koWinter ? koWinter.getTime() : -1, Date.UTC(2026, 0, 15, 18, 0, 0));

  Logger.log(failures.length ? ('❌ ' + failures.length + ' FAILED: ' + failures.join(', ')) : '✅ ALL TESTS PASSED');
  return failures;
}
