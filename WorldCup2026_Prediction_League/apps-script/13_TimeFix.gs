/**
 * ============================================================================
 *  13_TimeFix.gs  ·  One-time fix: kickoff times were entered in ET but the
 *                    column is labeled "KO (CT)". Convert the VALUES to true
 *                    Central by subtracting 1 hour. Midnight (00:00) games
 *                    roll back to 23:00 the previous day (Date column updated).
 * ============================================================================
 *  WHY: "How to Play" says times are US Eastern; the Group Stage header says
 *  "KO (CT)". So the numbers are ET, mislabeled CT. After this runs ONCE, the
 *  column genuinely holds CT — consistent with CONFIG.TIMEZONE = America/Chicago
 *  so the kickoff-lock fires at the right moment.
 *
 *  SAFETY:
 *   • Guarded by a Script Property flag so a second run can't silently shift
 *     another hour (it asks for explicit confirmation).
 *   • Writes KO back as zero-padded TEXT ("14:00") so the value can't be
 *     re-interpreted as a different time-of-day, and parseKickoff_ reads it
 *     reliably.
 *   • Only the Group Stage tab has a kickoff-time column; Knockout is skipped.
 * ============================================================================
 */

var KO_CONVERTED_FLAG = 'KO_CONVERTED_TO_CT';

/** Menu entry point. */
function convertKickoffTimesToCT() {
  var ui = SpreadsheetApp.getUi();
  var props = PropertiesService.getScriptProperties();

  if (props.getProperty(KO_CONVERTED_FLAG) === 'yes') {
    var again = ui.alert('Already converted once',
      'Kickoff times were already converted ET → CT in this project. Running ' +
      'again would subtract ANOTHER hour. Are you sure you want to continue?',
      ui.ButtonSet.YES_NO);
    if (again !== ui.Button.YES) { toast_('Conversion cancelled.'); return; }
  } else {
    var ok = ui.alert('Convert kickoff times ET → CT?',
      'This subtracts 1 hour from every kickoff time on the Group Stage tab so ' +
      'the "KO (CT)" column truly shows Central time. Midnight (00:00) games ' +
      'roll back to 23:00 the previous day (their Date is updated too). ' +
      'It edits the Date and KO columns in place. Proceed?',
      ui.ButtonSet.YES_NO);
    if (ok !== ui.Button.YES) { toast_('Conversion cancelled.'); return; }
  }

  var n = shiftTabKickoffs_(sheetByName_(CONFIG.TAB_GROUP), -1);
  props.setProperty(KO_CONVERTED_FLAG, 'yes');
  diagLog_('Converted ' + n + ' kickoff time(s) ET → CT (−1h).');
  toast_('Done — converted ' + n + ' kickoff time(s) to CT. Re-check the column.');
}

/**
 * Shift every kickoff time on a tab by deltaHours (e.g. −1 for ET→CT).
 * Returns the count of rows changed. Reads DISPLAY values so it works whether
 * the cells are stored as text or as time values; writes KO back as text.
 */
function shiftTabKickoffs_(sh, deltaHours) {
  var loc = locateMatchTab_(sh);
  if (loc.col.ko <= 0) return 0;                 // no kickoff-time column
  var matches = readMatches_(sh, loc);
  var count = 0;

  Object.keys(matches).forEach(function (key) {
    var m = matches[key];
    var koStr = String(sh.getRange(m.rowIndex, loc.col.ko).getDisplayValue()).trim();
    var t = parseHHMM_(koStr);
    if (!t) return;                              // unparseable / blank

    var shifted = shiftClock_(t.hh, t.mm, deltaHours);
    var newKo = pad2_(shifted.hh) + ':' + pad2_(shifted.mm);

    // Write as plain text so Sheets can't re-coerce it to another time value.
    sh.getRange(m.rowIndex, loc.col.ko).setNumberFormat('@').setValue(newKo);

    // Day rollover (e.g. 00:00 → 23:00 previous day) → fix the Date cell.
    if (shifted.dayDelta !== 0 && loc.col.date > 0) {
      var dispDate = String(sh.getRange(m.rowIndex, loc.col.date).getDisplayValue()).trim();
      var newDate = shiftDateText_(dispDate, shifted.dayDelta);
      if (newDate) sh.getRange(m.rowIndex, loc.col.date).setNumberFormat('@').setValue(newDate);
    }
    count++;
  });
  return count;
}

/** "15:00" → {hh:15, mm:0}; null if no HH:MM found. */
function parseHHMM_(s) {
  var m = String(s).match(/(\d{1,2}):(\d{2})/);
  if (!m) return null;
  return { hh: Number(m[1]), mm: Number(m[2]) };
}

/** Shift a wall-clock time by deltaHours, returning new {hh, mm, dayDelta}. */
function shiftClock_(hh, mm, deltaHours) {
  var dayDelta = 0;
  hh += deltaHours;
  while (hh < 0) { hh += 24; dayDelta -= 1; }
  while (hh >= 24) { hh -= 24; dayDelta += 1; }
  return { hh: hh, mm: mm, dayDelta: dayDelta };
}

function pad2_(n) { return (n < 10 ? '0' : '') + n; }

/**
 * "Sat, Jun 13" + dayDelta(-1) → "Fri, Jun 12". Reformats with correct weekday.
 * Uses UTC math so no timezone/DST shifts the calendar date. Year = EDITION_YEAR.
 */
function shiftDateText_(dateText, dayDelta) {
  var mon = monthIndexFromText_(dateText);
  var dm = String(dateText).match(/(\d{1,2})\s*$/) || String(dateText).match(/(\d{1,2})/);
  if (mon < 0 || !dm) return null;
  var day = Number(dm[1]);
  var d = new Date(Date.UTC(CONFIG.EDITION_YEAR, mon, day));
  d.setUTCDate(d.getUTCDate() + dayDelta);
  var weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  return weekdays[d.getUTCDay()] + ', ' + months[d.getUTCMonth()] + ' ' + d.getUTCDate();
}

/** Month index 0–11 from a date string like "Thu, Jun 11" (weekday stripped first). */
function monthIndexFromText_(s) {
  var t = String(s).replace(/^[A-Za-z]{3,},?\s*/, '').toLowerCase();
  var months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
  for (var i = 0; i < 12; i++) { if (t.indexOf(months[i]) >= 0) return i; }
  return -1;
}
