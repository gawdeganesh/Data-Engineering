/**
 * ============================================================================
 *  14_VenueLocal.gs  ·  (1) chronological re-sort of the Group Stage rows, and
 *                       (2) convert the KO column from Central Time to each
 *                       venue's own local time.
 *
 *  RUN ORDER (once):
 *    1. Inline edits already applied in 05_Sheet.gs (locateMatchTab_ ko alias)
 *       and 09_Locks.gs (parseKickoff_ tz arg + venue-aware lock call site).
 *    2. resortGroupStageChrono()           // while KO is still CT
 *    3. convertKickoffTimesToVenueLocal()  // rewrites values in place
 *  Do NOT run resortGroupStageChrono() again after step 3 (column is now
 *  mixed-zone). The converter leaves rows in place, so order stays correct.
 * ============================================================================
 */

/** Re-sort the Group Stage match rows into true chronological order (Date + KO),
 *  treating KO as a single timezone (CT). Run this BEFORE the venue-local convert. */
function resortGroupStageChrono() {
  var sh  = sheetByName_(CONFIG.TAB_GROUP);
  var loc = locateMatchTab_(sh);
  if (loc.col.date <= 0 || loc.col.ko <= 0) { toast_('Could not find Date / KO columns; nothing sorted.'); return; }

  var values = loc.values || sh.getDataRange().getValues();
  var firstRow = -1, lastRow = -1;
  for (var r = loc.dataStartRow - 1; r < values.length; r++) {
    var num = values[r][loc.col.num - 1];
    if (num === '' || num === null || isNaN(Number(num))) continue;
    if (firstRow < 0) firstRow = r + 1;
    lastRow = r + 1;
  }
  if (firstRow < 0) { toast_('No match rows found.'); return; }
  var n = lastRow - firstRow + 1;

  var dates = sh.getRange(firstRow, loc.col.date, n, 1).getDisplayValues();
  var kos   = sh.getRange(firstRow, loc.col.ko,   n, 1).getDisplayValues();
  var keys = [];
  for (var i = 0; i < n; i++) keys.push([chronoKey_(dates[i][0], kos[i][0])]);

  var helperCol = sh.getLastColumn() + 1;
  sh.getRange(firstRow, helperCol, n, 1).setValues(keys);
  sh.getRange(firstRow, 1, n, helperCol).sort({ column: helperCol, ascending: true });
  sh.deleteColumn(helperCol);

  diagLog_('Re-sorted ' + n + ' Group Stage rows by Date + KO.');
  toast_('Group Stage re-sorted chronologically (' + n + ' rows).');
}

/** Chrono key from a date like "Thu, Jun 11" + a time like "22:00". */
function chronoKey_(dateText, koText) {
  var mon = monthIndexFromText_(dateText);
  var dm  = String(dateText).match(/(\d{1,2})\s*$/) || String(dateText).match(/(\d{1,2})/);
  var t   = parseHHMM_(koText);
  if (mon < 0 || !dm) return Number.MAX_SAFE_INTEGER;
  return new Date(CONFIG.EDITION_YEAR, mon, Number(dm[1]), t ? t.hh : 0, t ? t.mm : 0).getTime();
}

/** Venue -> IANA timezone. June 2026: US/Canada on DST, Mexico has no DST. */
function zoneForVenue_(venue) {
  var v = String(venue).toLowerCase();
  if (/azteca|mexico city|akron|guadalajara|bbva|monterrey/.test(v)) return 'America/Mexico_City';
  if (/vancouver|bc place/.test(v))                                   return 'America/Vancouver';
  if (/inglewood|sofi|santa clara|levi|seattle|lumen/.test(v))        return 'America/Los_Angeles';
  if (/houston|nrg|arlington|at&t|kansas city|arrowhead/.test(v))     return 'America/Chicago';
  if (/toronto|east rutherford|metlife|foxbor|gillette|philadelphia|lincoln financial|atlanta|mercedes|miami|hard rock/.test(v))
                                                                      return 'America/New_York';
  return null; // unknown -> caller skips the row and logs it
}

var KO_LOCAL_FLAG = 'KO_CONVERTED_TO_VENUE_LOCAL';

/** Rewrite Group Stage KO (and Date) from CT to each venue's local time, in place. */
function convertKickoffTimesToVenueLocal() {
  var props = PropertiesService.getScriptProperties();
  if (props.getProperty(KO_LOCAL_FLAG) === 'yes') {
    var ui = null;
    try { ui = SpreadsheetApp.getUi(); } catch (e) {}   // no UI when run from the editor
    if (ui && ui.alert('Already converted', 'KO was already converted to venue-local once. ' +
          'Running again double-shifts it. Continue only if you reverted. Proceed?',
          ui.ButtonSet.YES_NO) !== ui.Button.YES) { toast_('Cancelled.'); return; }
  }

  var sh = sheetByName_(CONFIG.TAB_GROUP), loc = locateMatchTab_(sh);
  if (loc.col.ko <= 0 || loc.col.venue <= 0 || loc.col.date <= 0) { toast_('Need Date, KO and Venue columns; aborting.'); return; }

  var matches = readMatches_(sh, loc), done = 0, unknown = [];
  Object.keys(matches).forEach(function (k) {
    var m = matches[k];
    var venue = String(sh.getRange(m.rowIndex, loc.col.venue).getDisplayValue()).trim();
    var zone  = zoneForVenue_(venue);
    if (!zone) { unknown.push('row ' + m.rowIndex + ' "' + venue + '"'); return; }
    var instant = parseKickoff_(m.dateText, m.koText); // CT (default) -> absolute instant
    if (!instant) return;
    sh.getRange(m.rowIndex, loc.col.ko).setNumberFormat('@').setValue(Utilities.formatDate(instant, zone, 'HH:mm'));
    sh.getRange(m.rowIndex, loc.col.date).setNumberFormat('@').setValue(Utilities.formatDate(instant, zone, 'EEE, MMM d'));
    done++;
  });

  sh.getRange(loc.headerRow, loc.col.ko).setValue('KO (local)');
  var t = sh.getRange(1, 1), s = String(t.getValue());
  if (/times in CT/i.test(s)) t.setValue(s.replace(/times in CT/i, 'times in each venue local time'));

  props.setProperty(KO_LOCAL_FLAG, 'yes');
  diagLog_('Venue-local: converted ' + done + '. Unknown: ' + (unknown.length ? unknown.join('; ') : 'none'));
  toast_('Done - ' + done + ' kickoff(s) now show venue-local time.' +
         (unknown.length ? ' ' + unknown.length + ' unknown venue(s) skipped (see log).' : ''));
}


/** Re-sort Group Stage rows by TRUE kickoff instant, AFTER the column is venue-local.
 *  Parses each row's local time in its venue zone, so mixed zones sort correctly. */
function resortGroupStageByVenueInstant() {
  var sh = sheetByName_(CONFIG.TAB_GROUP), loc = locateMatchTab_(sh);
  if (loc.col.date <= 0 || loc.col.ko <= 0 || loc.col.venue <= 0) { toast_('Missing columns; nothing sorted.'); return; }
  var values = loc.values || sh.getDataRange().getValues();
  var firstRow = -1, lastRow = -1;
  for (var r = loc.dataStartRow - 1; r < values.length; r++) {
    var num = values[r][loc.col.num - 1];
    if (num === '' || num === null || isNaN(Number(num))) continue;
    if (firstRow < 0) firstRow = r + 1;
    lastRow = r + 1;
  }
  if (firstRow < 0) { toast_('No match rows.'); return; }
  var n = lastRow - firstRow + 1;
  var dates  = sh.getRange(firstRow, loc.col.date,  n, 1).getDisplayValues();
  var kos    = sh.getRange(firstRow, loc.col.ko,    n, 1).getDisplayValues();
  var venues = sh.getRange(firstRow, loc.col.venue, n, 1).getDisplayValues();
  var keys = [];
  for (var i = 0; i < n; i++) {
    var zone = zoneForVenue_(venues[i][0]) || CONFIG.TIMEZONE;
    var inst = parseKickoff_(dates[i][0], kos[i][0], zone);
    keys.push([inst ? inst.getTime() : Number.MAX_SAFE_INTEGER]);
  }
  var helperCol = sh.getLastColumn() + 1;
  sh.getRange(firstRow, helperCol, n, 1).setValues(keys);
  sh.getRange(firstRow, 1, n, helperCol).sort({ column: helperCol, ascending: true });
  sh.deleteColumn(helperCol);
  diagLog_('Re-sorted ' + n + ' rows by true kickoff instant (venue-aware).');
  toast_('Re-sorted ' + n + ' rows by actual kickoff time.');
}


/** ONE-OFF: column is currently venue-local on a base that was 1h too early.
 *  Recover each instant from its venue zone, add 1 hour, write back as Central,
 *  relabel to KO (CT), drop the venue-local flag, then re-sort chronologically. */
function fixToCentralPlusOneHour() {
  var sh = sheetByName_(CONFIG.TAB_GROUP), loc = locateMatchTab_(sh);
  if (loc.col.ko <= 0 || loc.col.venue <= 0 || loc.col.date <= 0) { toast_('Missing columns; aborting.'); return; }
  var matches = readMatches_(sh, loc), done = 0;
  Object.keys(matches).forEach(function (k) {
    var m = matches[k];
    var zone = zoneForVenue_(String(sh.getRange(m.rowIndex, loc.col.venue).getDisplayValue()).trim()) || CONFIG.TIMEZONE;
    var inst = parseKickoff_(m.dateText, m.koText, zone);
    if (!inst) return;
    inst = new Date(inst.getTime() + 3600000); // +1 hour
    sh.getRange(m.rowIndex, loc.col.ko).setNumberFormat('@').setValue(Utilities.formatDate(inst, CONFIG.TIMEZONE, 'HH:mm'));
    sh.getRange(m.rowIndex, loc.col.date).setNumberFormat('@').setValue(Utilities.formatDate(inst, CONFIG.TIMEZONE, 'EEE, MMM d'));
    done++;
  });
  sh.getRange(loc.headerRow, loc.col.ko).setValue('KO (CT)');
  var t = sh.getRange(1, 1), s = String(t.getValue());
  if (/times in each venue local time/i.test(s)) t.setValue(s.replace(/times in each venue local time/i, 'times in CT'));
  PropertiesService.getScriptProperties().deleteProperty(KO_LOCAL_FLAG);
  diagLog_('Corrected ' + done + ' kickoffs to Central (+1h); relabeled to KO (CT).');
  toast_('Done - ' + done + ' kickoffs now correct Central time.');
  resortGroupStageChrono();
}
