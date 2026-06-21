# WorldCup2026_Prediction_League

A Google Sheets–based 2026 World Cup score-prediction league (Ganesh · Siddhesh · Aniket),
with a bound Google Apps Script engine that handles scoring, standings, knockout bracket
auto-fill, locks, and bonus calls.

## Contents

- **`WorldCup2026_Prediction_League.xlsx`** — export of the Google Sheet (6 tabs: How to Play,
  Group Stage, Leaderboard, Bonus Calls, Knockout, Standings).
- **`apps-script/`** — source of the container-bound Apps Script project.
  - `appsscript.json` — manifest
  - `00_Config.gs` … `14_VenueLocal.gs` — script source files

## Source

- Spreadsheet ID: `1vdqaOf9cirw0QWJlEwivZUUiXkWhGyauWXcDYNdJWhQ`
- Apps Script project ID: `1db_NTTr38Dg6BioEQ_TQBPlaahHN4s0Jz_8KS6g_MmcoUxltZqhf9miP`

## Working with the Apps Script

The `apps-script/` folder is laid out for [`clasp`](https://github.com/google/clasp).
To sync changes back to the live project:

```bash
cd apps-script
clasp clone 1db_NTTr38Dg6BioEQ_TQBPlaahHN4s0Jz_8KS6g_MmcoUxltZqhf9miP   # first time
clasp push                                                              # upload local edits
```
