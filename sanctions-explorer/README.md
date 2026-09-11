# AI Sanctions Explorer

An independent, customizable research explorer built for Write.law. The included dataset contains 2,036 decision-level records from Damien Charlotin’s AI Hallucination Cases Database, in its September 10, 2026 snapshot.

## Open and customize

Open `index.html` in a current browser. It contains the complete application and dataset; no install, account, API key, build service, or network request is required. Source links need internet access.

Use **Customize & import** to change the project name, introduction, appearance, and optional teaching sections. Upload a CSV or JSON dataset and review the column mapping before applying it. Monetary entries in other datasets need not use Charlotin’s special `1 = unknown` convention; the importer asks explicitly.

Browser settings do not change the public website for other visitors. **Export portable website** produces a self-contained copy with the active data and settings. **Export project JSON** preserves the raw data and mapping for another editing session. Neither export includes review notes or exercise progress.

## Features

The app includes monthly and cumulative charts, shared filters, searchable and paginated decision views, source-linked details, saved selections, two-record comparison, jurisdiction charts and a U.S. tile map, error/outcome/tool/field charts, single-currency monetary distributions, chart and data exports, twelve new fictional training exercises, a local quotation comparator, review checklists, and an evidence log.

The 450-order study page contains selected published aggregate findings from Kyle Bahr’s expanded project. It is explicitly separate from the 2,036 decision-level source records and does not respond to dataset filters. This is a functional independent rebuild, not a pixel-for-pixel reproduction or a copy of every original essay, research directory, or exercise. Private lawyer-level coding workbooks are not included.

## Source files

`src/app.js` contains views and interaction handling. `src/core.js` contains normalization, filtering, CSV handling, money parsing, and text comparison. `src/content.js` contains the original fictional exercises, checklists, and attributed study aggregates. `src/styles.css` controls appearance; `src/shell.html` provides the page shell. `build.py` assembles these with `data/source.csv` into the portable `index.html`.

To rebuild with Python 3:

```
python3 build.py
```

To check data handling with Node 18 or newer:

```
node tests/core.test.cjs
```

`tests/browser.py` uses Playwright to exercise all nine views at desktop and phone sizes and test filtering, comparisons, exports, importing, and portability. Pass a published URL to test that deployment. By default it loads the built HTML directly as browser content. The local environment’s network-navigation restrictions do not apply to ordinary use of the generated file.

A new source CSV can be passed with `python3 build.py --csv path/to/source.csv`. Update the snapshot metadata in `build.py` at the same time. The application does not silently refresh its data and has no scheduled background job.

## Source and attribution

**AI Hallucination Cases Database, Damien Charlotin**, https://www.damiencharlotin.com/hallucinations/ — licensed under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. The included source CSV was downloaded on September 11, 2026 UTC from https://www.damiencharlotin.com/hallucinations/hallucinations/download.csv. The source page identified its last update as September 10, 2026. `data/metadata.json` includes the SHA-256 fingerprint of the downloaded CSV.

Changes include a new interface and presentation, new explanations and exercises, limited court-label-based U.S. state inference, grouping source items once per record, a corrected display spelling for “Government Lawyer,” and case-insensitive grouping of outcome-chart labels. The original source values remain available in the dataset. A `1` monetary value in this source denotes an unknown amount; it is not included in numeric monetary summaries. Different currencies are never aggregated.

Selected study aggregates are attributed to **Kyle Bahr**, https://kylebahr.netlify.app/2000/expanded/, September 2, 2026 edition. Their sample of 450 U.S. lawyer-related orders differs from the full public database. Single-pass AI-assisted coding was not accompanied by a second coder or an intercoder-reliability assessment. This version does not imply either source author’s endorsement.

The original site’s source code, embedded fonts, and proprietary person-level files are not redistributed. The application uses system fonts.

## Limits

Source records are decisions, not necessarily unique incidents, people, or final sanctions. The dataset has no denominator for all AI uses and cannot establish error rates or product reliability. Alleged and disputed flags are retained. The source descriptions and underlying decisions have not all been independently verified. Read the orders and check their status and applicable rules before relying on a record.

The new practice exercises are fictional teaching examples, not jurisdiction-specific legal advice or accredited CLE. The quotation tool compares text, not legal meaning. Completing a checklist does not certify that a document is correct.

No analytics, external dependencies, or application API calls are used. Settings, exercise progress, and saved identifiers may be stored in this browser. Pasted passages, reviewer labels, imported datasets, and evidence notes are not automatically persisted. Treat exported files according to their contents; do not publish confidential material.
