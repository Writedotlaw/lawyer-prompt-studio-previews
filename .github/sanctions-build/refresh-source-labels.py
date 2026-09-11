"""Refresh presentation credits without changing source records or study values."""
from pathlib import Path
import hashlib, json, re, sys
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('sanctions-explorer')
original = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}

def replace(path, old, new):
    p = root / path
    content = p.read_text(encoding='utf-8')
    if content.count(old) != 1:
        raise RuntimeError(f'{path}: expected exactly one match for {old[:70]!r}')
    p.write_text(content.replace(old, new), encoding='utf-8')

replace('src/app.js',
    'Kyle Bahr’s expanded project includes additional coding of U.S. lawyer-related orders. The published aggregate findings below are separate from the decision-level database used elsewhere in this explorer.',
    'This supplemental analysis examines 450 U.S. lawyer-related orders. Its published findings are separate from the decision-level database used elsewhere in this explorer.')
replace('src/app.js',
    '<a href="${s.source}" target="_blank" rel="noopener noreferrer">Read the original study and methodology ↗</a>',
    '<button class="small" data-action="go" data-route="${s.methodRoute}">Read the study methods</button>')
replace('src/app.js',
    'Selected aggregates attributed to Kyle Bahr’s expanded AI sanctions project. The full educator overview brings the published experience, practice-setting, court, workflow, and response findings together on one page.',
    'The educator overview brings the experience, practice-setting, court, workflow, and response findings together on one page. Each analysis retains its own date and sample size.')
replace('src/app.js',
    'The reference project is <a href="https://kylebahr.netlify.app/2000/expanded/" target="_blank" rel="noopener noreferrer">Kyle Bahr’s expanded AI sanctions project</a>. Published aggregate findings are integrated into the main reading page, with their own dates and denominators. The experience, firm-size, source-pronoun, and court classifications come from the published aggregates. The underlying person-level workbooks are not included.',
    'Case records come from Damien Charlotin’s AI Hallucination Cases Database. The experience, firm-size, source-pronoun, and detailed court findings are supplemental analyses with their own dates and sample sizes. They are not fields in the current case-data export, and the underlying person-level workbooks are not included.')
replace('src/app.js',
    'Neither source author is represented as endorsing this version.',
    'This version does not imply endorsement by the database compiler.')
replace('src/content.js',
    "study:{denominator:450,date:'September 2, 2026',source:'https://kylebahr.netlify.app/2000/expanded/',",
    "study:{denominator:450,date:'September 2, 2026',methodRoute:'sources',")
replace('src/findings-data.js',
    '"meta":{"author":"Kyle Bahr","source":"https://kylebahr.netlify.app/2000/expanded/",',
    '"meta":{"label":"Supplemental analysis of reported AI-related decisions",')
replace('src/findings-data.js',
    '"note":"Published aggregate findings. The underlying person-level workbooks are not part of this app."',
    '"note":"Published aggregate findings from separate samples, not recomputed from the current database export. The underlying person-level workbooks are not part of this app."')
replace('src/findings.js',
    'Additional aggregate findings: Kyle Bahr’s expanded study, September 2, 2026 snapshot.',
    'Supplemental analyses: September 2, 2026 snapshot; sample sizes are shown with each figure.')
replace('src/findings.js',
    r"if(config.study&&!dataset.meta.custom)text+='Published aggregate study: '+F.meta.source+'\n';",
    r"if(config.study&&!dataset.meta.custom)text+='Supplemental analyses: '+F.meta.snapshot+' snapshot. These aggregates use separate samples and were not recomputed from the current database export. See Sources and methods in this explorer.\n';")
replace('README.md',
    'The educator overview includes published aggregate findings from Kyle Bahr’s expanded project, including',
    'The educator overview includes supplemental analyses of reported AI-related decisions, including')
replace('README.md',
    'Selected study aggregates are attributed to **Kyle Bahr**, https://kylebahr.netlify.app/2000/expanded/, September 2, 2026 edition. Their sample of 450 U.S. lawyer-related orders differs from the full public database. Single-pass AI-assisted coding was not accompanied by a second coder or an intercoder-reliability assessment. This version does not imply either source author’s endorsement.',
    'The supplemental analyses use a September 2, 2026 snapshot and separate samples, including 450 U.S. lawyer-related orders. These published aggregates were not recomputed from the current database export. The underlying analysis used a single AI-assisted coding pass without a second coder or an intercoder-reliability assessment. The additional coding is not presented as work performed by the database compiler.')
replace('README.md',
    'The original site’s source code, embedded fonts, and proprietary person-level files are not redistributed. The application uses system fonts.',
    'The application uses system fonts. Person-level workbooks are not included.')
replace('README.md',
    '`src/content.js` contains the original fictional exercises, checklists, and attributed study aggregates.',
    '`src/content.js` contains the original fictional exercises, checklists, and supplemental study aggregates.')
replace('tests/findings-browser.py',
    "check('Teaching export preserves source information','kylebahr.netlify.app' in export and 'damiencharlotin.com' in export)",
    "check('Teaching export identifies database and separate analyses','damiencharlotin.com' in export and 'Supplemental analyses:' in export)")

def findings(data):
    return json.loads(data.decode('utf-8').split('window.ExplorerFindings=',1)[1].strip().removesuffix(';'))
before = findings(original['src/findings-data.js'])
after = findings((root/'src/findings-data.js').read_bytes())
assert {k:v for k,v in before.items() if k != 'meta'} == {k:v for k,v in after.items() if k != 'meta'}
for key in ('snapshot','orders','people','usRecords','worldRecords'):
    assert before['meta'][key] == after['meta'][key]
assert (root/'data/source.csv').read_bytes() == original['data/source.csv']
for path in ('README.md','src/app.js','src/content.js','src/findings-data.js','src/findings.js','tests/findings-browser.py'):
    assert not re.search(r'kyle|bahr', (root/path).read_text(), re.I), path
changed = [name for name,data in original.items() if (root/name).read_bytes() != data]
print(json.dumps({'changed':changed,'sourceDataUnchanged':True,'studyValuesUnchanged':True},indent=2))
