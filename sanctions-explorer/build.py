"""Build the portable, dependency-free explorer from an attributed CSV snapshot."""
import csv, json, pathlib, argparse, hashlib, shutil
ROOT=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--csv',default=str(ROOT/'data/source.csv'));a=p.parse_args()
raw=pathlib.Path(a.csv).read_bytes()
with pathlib.Path(a.csv).open(encoding='utf-8-sig',newline='') as f:
    reader=csv.reader(f); columns=next(reader); rows=list(reader)
assert len(rows)>0 and all(len(r)==len(columns) for r in rows)
meta={'name':'AI Hallucination Cases Database','author':'Damien Charlotin','source':'https://www.damiencharlotin.com/hallucinations/','sourceBase':'https://www.damiencharlotin.com/','license':'CC BY 4.0','licenseUrl':'https://creativecommons.org/licenses/by/4.0/','snapshot':'2026-09-10','retrieved':'2026-09-11','oneIsUnknown':True,'sha256':hashlib.sha256(raw).hexdigest(),'note':'Public decision-level records. This is a fixed snapshot, not a live feed.'}
data={'meta':meta,'columns':columns,'rows':rows}
config={'name':'AI Sanctions Explorer','organization':'Write.law','intro':'Explore the court decisions behind the discussion about AI and legal work. Follow patterns across the records, read what happened in individual cases, and use the examples in your own teaching.','accent':'#217963','study':True,'practice':True,'theme':'paper'}
def j(value):return json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
html=(ROOT/'src/shell.html').read_text()
html=html.replace('/*__STYLES__*/',(ROOT/'src/styles.css').read_text()).replace('/*__CORE__*/',(ROOT/'src/core.js').read_text()).replace('/*__CONTENT__*/',(ROOT/'src/content.js').read_text()).replace('/*__APP__*/',(ROOT/'src/app.js').read_text()).replace('__DATA__',j(data)).replace('__CONFIG__',j(config))
(ROOT/'index.html').write_text(html)
(ROOT/'data/metadata.json').write_text(json.dumps(meta,indent=2))
print(f'Built index.html: {len(rows):,} source records; {len(html.encode()):,} bytes')
