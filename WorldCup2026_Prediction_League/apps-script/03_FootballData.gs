/**
 * ============================================================================
 *  03_FootballData.gs  ·  football-data.org v4 client
 * ============================================================================
 *  ONE call gets the whole tournament:
 *      GET https://api.football-data.org/v4/competitions/WC/matches?season=2026
 *  Header: X-Auth-Token: <token>
 *
 *  Free tier: World Cup IS included (code WC / id 2000), 10 requests/minute,
 *  but Scores/Schedules are DELAYED on free — final scores arrive fine, live
 *  in-play lags. So: one call per run, cache a few minutes, pace via trigger.
 *
 *  This module emits the SAME normalized fixture shape the rest of the project
 *  already consumes (homeName/awayName/homeGoals/awayGoals/penHome/penAway/
 *  decidedOnPens/finished/inPlay/round/timestamp/status/id), so no downstream
 *  file needed structural changes when we swapped providers.
 * ============================================================================
 */

/**
 * Resolve the API token. Prefers a Script Property (private), then the inline
 * CONFIG.API_KEY. Throws a friendly error only if BOTH are empty.
 */
function getApiKey_() {
  var key = PropertiesService.getScriptProperties().getProperty(CONFIG.API_KEY_PROP);
  if (!key && CONFIG.API_KEY) key = CONFIG.API_KEY;
  if (!key) {
    throw new Error(
      'No API token found. Run "World Cup ▸ Set API key…" and paste your ' +
      'football-data.org token, or set CONFIG.API_KEY in 00_Config.gs.'
    );
  }
  return key;
}

/**
 * Fetch all World Cup matches and return the normalized array.
 * @param {boolean} force  bypass the short-lived cache
 * @return {Array<Object>}
 */
function fetchAllFixtures_(force) {
  var cache = CacheService.getScriptCache();
  var cacheKey = 'wc_fixtures_' + CONFIG.WC_SEASON;
  if (!force) {
    var cached = cache.get(cacheKey);
    if (cached) {
      try { return JSON.parse(cached); } catch (e) { /* refetch */ }
    }
  }

  var url = CONFIG.API_BASE + '/competitions/' + CONFIG.WC_COMPETITION +
            '/matches?season=' + CONFIG.WC_SEASON;
  var headers = {}; headers[CONFIG.API_HEADER] = getApiKey_();

  var res = UrlFetchApp.fetch(url, {
    method: 'get',
    headers: headers,
    muteHttpExceptions: true
  });

  var code = res.getResponseCode();
  var body = res.getContentText();

  // Quota telemetry. football-data headers: X-RequestsAvailable (no hyphen
  // before Available) and X-RequestCounter-Reset. Lowercase keys to be safe.
  var rawHeaders = res.getAllHeaders();
  var h = {};
  Object.keys(rawHeaders).forEach(function (k) { h[k.toLowerCase()] = rawHeaders[k]; });
  if (h['x-requestsavailable'] !== undefined) {
    diagLog_('football-data requests available this minute: ' + h['x-requestsavailable']);
  }

  // Friendly errors for the common football-data failure codes.
  if (code === 429) {
    throw new Error('football-data rate limit hit (HTTP 429). Free tier is 10/min — ' +
                    'wait ' + (h['x-requestcounter-reset'] || '60') + 's and retry.');
  }
  if (code === 403) {
    throw new Error('football-data HTTP 403 (forbidden): token invalid, or this ' +
                    'resource is not on your plan. Body: ' + body.slice(0, 200));
  }
  if (code !== 200) {
    throw new Error('football-data HTTP ' + code + ': ' + body.slice(0, 300));
  }

  var json;
  try { json = JSON.parse(body); }
  catch (e) { throw new Error('football-data returned non-JSON: ' + body.slice(0, 200)); }

  if (json.errorCode || json.error) {
    throw new Error('football-data error: ' + (json.message || JSON.stringify(json).slice(0, 200)));
  }

  var raw = json.matches || [];
  var normalized = raw.map(normalizeFixture_);
  diagLog_('Fetched ' + normalized.length + ' WC matches from football-data.org.');

  try {
    cache.put(cacheKey, JSON.stringify(normalized), 300);
  } catch (e) {
    diagLog_('Fixture cache skipped (' + e.message + ') — payload may exceed 100KB; ' +
             'each run will hit the API. Watch the per-minute quota.');
  }
  return normalized;
}

/** football-data status values that mean the match has a FINAL result. */
var FINISHED_STATUS = { FINISHED: true, AWARDED: true };
/** Status values that mean the match is currently being played. */
var INPLAY_STATUS = { IN_PLAY: true, PAUSED: true, EXTRA_TIME: true, PENALTY_SHOOTOUT: true, SUSPENDED: true };

/**
 * Map a football-data `stage` enum to a friendly round label that stageOf_()
 * (08_Knockout) parses, and that the knockout/bonus filters recognize.
 */
function roundLabelFromStage_(stage) {
  switch (String(stage || '').toUpperCase()) {
    case 'GROUP_STAGE': return 'Group Stage';
    case 'LAST_32': return 'Round of 32';
    case 'LAST_16': return 'Round of 16';
    case 'QUARTER_FINALS': return 'Quarter-finals';
    case 'SEMI_FINALS': return 'Semi-finals';
    case 'THIRD_PLACE': return 'Third place';
    case 'FINAL': return 'Final';
    default: return String(stage || '');
  }
}

/**
 * Flatten one football-data match into the normalized shape.
 *
 * Penalty handling (IMPORTANT): football-data's score.fullTime INCLUDES the
 * shootout for PSO games (e.g. fullTime 7–6 with penalties 6–5). The rules want
 * the on-pitch 120' scoreline, so we compute fullTime − penalties (→ 1–1) when
 * a shootout occurred, with a guard: if that subtraction is negative or makes
 * the sides unequal, fullTime wasn't shootout-inclusive, so use fullTime as-is.
 * Either way a shootout game yields the (drawn) 120' line, never the shootout.
 */
function normalizeFixture_(m) {
  var status = m.status || 'SCHEDULED';
  var score = m.score || {};
  var ft = score.fullTime || {};
  var pen = score.penalties || {};
  var decidedOnPens = (score.duration === 'PENALTY_SHOOTOUT') ||
                      (pen.home !== null && pen.home !== undefined);

  var ftH = numOrNull_(scoreSide_(ft, 'home'));
  var ftA = numOrNull_(scoreSide_(ft, 'away'));
  var penH = numOrNull_(scoreSide_(pen, 'home'));
  var penA = numOrNull_(scoreSide_(pen, 'away'));

  var onH = ftH, onA = ftA;
  if (decidedOnPens && ftH !== null && ftA !== null && penH !== null && penA !== null) {
    var sh = ftH - penH, sa = ftA - penA;
    if (sh >= 0 && sa >= 0 && sh === sa) { onH = sh; onA = sa; } // fullTime included shootout
    // else: fullTime was already the 120' score → leave onH/onA = fullTime
  }

  var utc = m.utcDate || null;
  var ts = utc ? Date.parse(utc) : 0; // ISO 8601 with 'Z' → unambiguous UTC ms

  return {
    id: m.id,
    dateIso: utc,
    timestamp: ts,
    status: status,
    finished: !!FINISHED_STATUS[status],
    inPlay: !!INPLAY_STATUS[status],
    stage: m.stage || '',
    round: roundLabelFromStage_(m.stage),
    group: m.group || null,
    homeName: m.homeTeam && m.homeTeam.name,
    awayName: m.awayTeam && m.awayTeam.name,
    homeTla: m.homeTeam && m.homeTeam.tla,
    awayTla: m.awayTeam && m.awayTeam.tla,
    homeGoals: onH,
    awayGoals: onA,
    penHome: penH,
    penAway: penA,
    decidedOnPens: decidedOnPens
  };
}

/** Read a score side, tolerating both v4 (home/away) and legacy (homeTeam/awayTeam) keys. */
function scoreSide_(obj, side) {
  if (!obj) return null;
  if (obj[side] !== undefined) return obj[side];                 // v4: .home / .away
  var legacy = side === 'home' ? 'homeTeam' : 'awayTeam';
  if (obj[legacy] !== undefined) return obj[legacy];             // legacy v2-style
  return null;
}

/** Lightweight key-check helper used by Diagnostics (property OR inline). */
function apiKeyIsSet_() {
  return !!PropertiesService.getScriptProperties().getProperty(CONFIG.API_KEY_PROP) || !!CONFIG.API_KEY;
}
