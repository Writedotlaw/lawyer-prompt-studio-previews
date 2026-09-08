"""Final presentation adjustments after build.py; no publication or authentication."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
css='''
/* Final review: keep task icons compact and help text readable. */
.wl-route-card>.feature-icon{display:flex;width:36px;height:36px;min-width:36px;align-items:center;justify-content:center;flex:none}
.wl-route-card>.feature-icon svg{width:21px;height:21px}
.wl-example .wl-flow-review{font-size:12px;line-height:1.65}
.wl-chapter-sources>.inside{padding:20px 23px}
.wl-source-links a{overflow-wrap:anywhere}
#guide-tooltip{background:#080a36;color:#fff;border-color:#34437b}
'''
style=root/'editable-site/style.css';text=style.read_text()
if 'Final review: keep task icons' not in text:style.write_text(text+css)
guidance=root/'editable-site/guidance.js'
guidance.write_text(guidance.read_text().replace('<strong>What this produces:</strong> ',''))
shell=(root/'editable-site/index.html').read_text()
final=shell.replace('<link rel="stylesheet" href="style.css">','<style>'+style.read_text()+'</style>')
for name in ['content.js','extras.js','guidance.js','widgets.js','app.js']:
    script=(root/'editable-site'/name).read_text().replace('</script','<\\/script')
    final=final.replace('<script src="'+name+'"></script>','<script>'+script+'</script>')
(root/'dist/index.html').write_text(final)
f=root/'dist/release.json';report=json.loads(f.read_text());report.update(sha256=hashlib.sha256(final.encode()).hexdigest(),bytes=len(final.encode()),presentationReview='Official wordmark and brand colors; desktop and mobile presentation reviewed.')
f.write_text(json.dumps(report,indent=2))
print('REVIEWED_BUILD',report['sha256'],report['bytes'])
