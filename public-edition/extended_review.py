"""Additional pre-publication checks against a local HTTP server. No storage mocks."""
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import threading,json,re,hashlib,sys
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parent
out=root/'review-evidence';out.mkdir(exist_ok=True)
new=(root/'dist/index.html').read_bytes();old=(root.parent/'ai-guide-revised/index.html').read_bytes()
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body=old if self.path.startswith('/legacy') else new
        self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(body)
    def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',8766),Handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
checks=[];errors=[];bodies={};external=[]
def check(name,passed,detail=''):
    checks.append({'name':name,'passed':bool(passed),'detail':str(detail)})
    if not passed: print('FAIL',name,detail,flush=True)
data=json.loads((root/'edited-data.json').read_text())
routes=['#/','#/chapters','#/labs','#/templates','#/prompts','#/glossary','#/notebook','#/sources','#/help']+['#/read/'+c['id'] for c in data['CHAPTERS']]+['#/lab/'+l['id'] for l in data['LABS']]
base='http://127.0.0.1:8766/'
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    context=browser.new_context(viewport={'width':1440,'height':1024},reduced_motion='reduce')
    page=context.new_page();page.set_default_timeout(10000)
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.on('request',lambda r:external.append(r.url) if not r.url.startswith((base,'data:','blob:')) else None)
    page.goto(base);page.wait_for_selector('#main h1');page.screenshot(path=str(out/'WriteLaw-Home-Desktop.png'),full_page=True)
    for width in [1440,1024,768,390]:
        page.set_viewport_size({'width':width,'height':950})
        for route in routes:
            page.goto(base+route,wait_until='domcontentloaded');page.wait_for_selector('#main h1')
            check(str(width)+': '+route+' fits',page.evaluate('document.documentElement.scrollWidth <= innerWidth+2'))
            if width==1440:
                bodies[route]=page.locator('#main').inner_text()
                check('Write.law footer '+route,page.locator('.wl-footer-logo').count()==1)
        if width==390:
            page.goto(base+'#/read/graphing');page.screenshot(path=str(out/'WriteLaw-Reading-Mobile.png'))
    page.set_viewport_size({'width':1440,'height':1024})
    for route,label in [('#/read/graphing','Workflow-Chapter'),('#/read/writing','Writing-Chapter'),('#/templates','Templates'),('#/lab/graph','Workflow-Exercise'),('#/help','Help')]:
        page.goto(base+route);page.wait_for_selector('#main h1');page.screenshot(path=str(out/('WriteLaw-'+label+'.png')))
        if route=='#/read/writing':
            page.locator('#section-1').scroll_into_view_if_needed();page.screenshot(path=str(out/'WriteLaw-Writing-Exercise.png'))
    page.goto(base+'#/lab/workorder');page.locator('[data-help="field:order-tools"]').click();page.screenshot(path=str(out/'WriteLaw-Field-Help.png'));page.keyboard.press('Escape')
    page.locator('[data-action="theme"]').first.click();page.screenshot(path=str(out/'WriteLaw-Dark-Worksheet.png'));page.locator('[data-action="theme"]').first.click()
    # Preserve responses through an actual old-to-new page change on the same origin.
    legacy=browser.new_context(viewport={'width':1200,'height':900})
    q=legacy.new_page();q.on('dialog',lambda dialog:dialog.accept());q.on('pageerror',lambda e:errors.append(str(e)))
    q.goto(base+'legacy#/lab/graph');q.wait_for_selector('[data-save="graph-lesson"]')
    note='Compatibility check: preserve the distinction between sent and received notice.'
    q.locator('[data-save="graph-lesson"]').fill(note)
    q.goto(base+'legacy#/read/think');q.locator('[data-save="note-think"]').fill('My earlier first-pass reflection remains useful.')
    q.goto(base+'#/lab/graph');q.wait_for_selector('[data-save="graph-lesson"]')
    check('Previous-edition graph response remains on update',q.locator('[data-save="graph-lesson"]').input_value()==note)
    q.goto(base+'#/read/think')
    check('Previous-edition chapter note remains on update',q.locator('[data-save="note-think"]').input_value()=='My earlier first-pass reflection remains useful.')
    q.goto(base+'#/notebook')
    with q.expect_download() as download:q.locator('[data-action="export-md"]').click()
    download.value.save_as(str(out/'test-readable-export.txt'))
    check('Readable export is Write.law branded','Write.law' in (out/'test-readable-export.txt').read_text())
    with q.expect_download() as download:q.locator('[data-action="export-json"]').click()
    download.value.save_as(str(out/'test-backup.json'))
    backup=json.loads((out/'test-backup.json').read_text())
    check('Backup format remains compatible',backup['app']=='regalia-ai-field-guide' and backup['version']==1 and backup['state']['fields']['graph-lesson']==note)
    known={c['id']:len(c['sections']) for c in data['CHAPTERS']};labids={l['id'] for l in data['LABS']};hrefs=set()
    for route in routes:
        page.goto(base+route)
        hrefs.update(page.locator('a[href^="#/"]').evaluate_all('(es)=>es.map(e=>e.getAttribute("href"))'))
    for href in sorted(hrefs):
        route=href.split('?')[0].split('/');valid=True
        if len(route)>2 and route[1]=='read':
            valid=route[2] in known
            if '?section=' in href:
                section=href.split('?section=')[1]
                valid=valid and (section=='quiz' or section.isdigit() and int(section)<known[route[2]])
        elif len(route)>2 and route[1]=='lab':valid=route[2] in labids
        elif route[1] not in ['', 'chapters','labs','templates','prompts','glossary','notebook','sources','help']:valid=False
        check('Internal destination '+href,valid)
    for route,body in bodies.items():
        if route!='#/sources':
            check('No course-only narrator '+route,not re.search(r'Fall guide|Semester reflection|Student edition|current part of the semester',body))
    check('No external asset or analytics requests',not external,external)
    check('No JavaScript errors',not errors,errors)
    browser.close()
server.shutdown()
report={'scope':'Local pre-publication review','deployed':False,'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'routes':len(routes),'widths':[1440,1024,768,390],'links':len(hrefs),'sourceSha256':hashlib.sha256(new).hexdigest(),'checks':checks,'pageErrors':errors,'externalRequests':external}
(out/'extended-report.json').write_text(json.dumps(report,indent=2))
(out/'rendered-copy.json').write_text(json.dumps(bodies,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
if report['failed']:sys.exit(1)
