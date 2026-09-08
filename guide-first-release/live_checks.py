"""Public-origin checks for the reading-first guide. No login or storage mocks."""
from pathlib import Path
import datetime,hashlib,json,os,sys,urllib.request
from playwright.sync_api import sync_playwright
OUT=Path(__file__).resolve().parent/'results'
RESULT=json.loads((OUT/'deployment-result.json').read_text())
URL=RESULT['publicUrl'].rstrip('/')+'/'
EXPECTED=RESULT['servedSha256']
checks=[];errors=[];requests=[]
def check(name,passed,detail=''):
    checks.append({'check':name,'passed':bool(passed),'detail':str(detail)[:1500]})
    print(('PASS: ' if passed else 'FAIL: ')+name,flush=True)
def expand(locator):
    for _ in range(8):
        closed=locator.locator('xpath=ancestor::details[not(@open)][last()]/summary')
        if not closed.count():break
        closed.click()
def go(page,route):
    page.goto(URL+route,wait_until='domcontentloaded')
    page.wait_for_selector('#main h1')
    page.wait_for_timeout(100)
def action(page,name):
    target=page.locator('[data-action="'+name+'"]').first
    expand(target);target.click();page.wait_for_timeout(90)
with urllib.request.urlopen(urllib.request.Request(URL,headers={'Cache-Control':'no-cache'}),timeout=30) as response:
    body=response.read(2000000)
    check('Original public URL returns HTTP 200 without a redirect',response.status==200 and response.url==URL)
    check('Published HTML exactly matches the approved reading-first edition',hashlib.sha256(body).hexdigest()==EXPECTED)
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    context=browser.new_context(viewport={'width':1440,'height':1000},reduced_motion='reduce')
    p=context.new_page();p.set_default_timeout(12000)
    p.on('pageerror',lambda error:errors.append(str(error)))
    p.on('dialog',lambda dialog:dialog.accept())
    p.on('request',lambda req:requests.append(req.url) if not req.url.startswith((URL,'data:','blob:')) else None)
    go(p,'#/')
    chapters=p.evaluate('CHAPTERS.map(c=>({id:c.id,sections:c.sections.length}))')
    labs=p.evaluate('LABS.map(l=>l.id)')
    routes=['#/','#/chapters','#/labs','#/templates','#/prompts','#/glossary','#/notebook','#/sources','#/help','#/questions']+['#/read/'+c['id'] for c in chapters]+['#/lab/'+x for x in labs]
    check('Homepage provides a link to each chapter',all(p.locator('#main a[href="#/read/'+c['id']+'"]').count()>0 for c in chapters))
    check('Write.law branding remains visible',p.locator('img[alt="Write.law"]').count()>0)
    p.screenshot(path=str(OUT/'Reading-First-Home-Desktop.png'),full_page=True)
    for width in [1440,1024,768,390]:
        p.set_viewport_size({'width':width,'height':950})
        for route in routes:
            try:
                go(p,route)
                check(str(width)+'px '+route+' renders',len(p.locator('#main h1').first.inner_text())>2)
                check(str(width)+'px '+route+' fits the screen',p.evaluate('document.documentElement.scrollWidth<=innerWidth+2'))
            except Exception as error:check(str(width)+'px '+route,False,error)
        if width==390:
            go(p,'#/');p.screenshot(path=str(OUT/'Reading-First-Home-Mobile.png'))
            go(p,'#/sources');p.screenshot(path=str(OUT/'Reading-First-Sources-Mobile.png'))
    p.set_viewport_size({'width':1440,'height':1000})
    for chapter in chapters:
        go(p,'#/read/'+chapter['id'])
        sections=p.locator('#main section[id^="section-"]')
        check(chapter['id']+': all reading sections are present',sections.count()==chapter['sections'])
        check(chapter['id']+': no form or widget interrupts the reading',sections.locator('textarea,input,select,[data-widget]').count()==0)
        check(chapter['id']+': substantive reading is not inside disclosures',sections.locator('details').count()==0)
    go(p,'#/read/writing');p.screenshot(path=str(OUT/'Reading-First-Writing.png'),full_page=True)
    go(p,'#/read/method');p.screenshot(path=str(OUT/'Reading-First-Collaboration.png'),full_page=True)
    go(p,'#/questions')
    check('Professional questions are available without filling out a form',p.locator('#main textarea,#main input,#main select').count()==0 and len(p.locator('#main').inner_text())>3000)
    try:
        go(p,'#/lab/graph');action(p,'graph-reset')
        for _ in range(3):action(p,'graph-next')
        check('Optional workflow stops at missing receipt evidence',p.evaluate('graphState.step===3') and p.locator('[data-action="graph-next"]').is_disabled())
        action(p,'graph-qualify')
        check('Qualified approach still needs approval',p.evaluate('graphState.step===3'))
        action(p,'graph-next')
        check('Explicit approval advances the optional workflow',p.evaluate('graphState.step===4'))
        for _ in range(3):action(p,'graph-next')
        check('Optional workflow can still be completed',p.evaluate('graphState.step===7'))
        action(p,'graph-evidence')
        check('New evidence returns affected work for review',p.evaluate('graphState.step===2 && graphState.updated'))
        note='Reading-first publication check: retain source support and unresolved questions.'
        field=p.locator('[data-save="graph-lesson"]');expand(field);field.fill(note)
        p.wait_for_timeout(250);p.reload(wait_until='domcontentloaded');p.wait_for_selector('[data-save="graph-lesson"]')
        check('Existing optional response fields save across reloads',p.locator('[data-save="graph-lesson"]').input_value()==note)
        go(p,'#/read/think');field=p.locator('[data-save="note-think"]');expand(field);field.fill('Keep my initial judgment distinct from the suggested answer.')
        p.wait_for_timeout(250);p.reload(wait_until='domcontentloaded');p.wait_for_selector('[data-save="note-think"]',state='attached')
        check('Chapter notes save across reloads',p.locator('[data-save="note-think"]').input_value()=='Keep my initial judgment distinct from the suggested answer.')
        go(p,'#/notebook')
        with p.expect_download() as download:action(p,'export-json')
        backup=OUT/'fictional-test-backup.json';download.value.save_as(str(backup))
        saved=json.loads(backup.read_text())
        check('Backup keeps the existing application identity',saved.get('app')=='regalia-ai-field-guide')
        fresh=browser.new_context(viewport={'width':1280,'height':900})
        q=fresh.new_page();q.on('dialog',lambda dialog:dialog.accept());q.on('pageerror',lambda error:errors.append(str(error)))
        go(q,'#/notebook');q.locator('#import-file').set_input_files(str(backup));q.wait_for_timeout(250)
        go(q,'#/lab/graph')
        check('A backup restores responses in a fresh browser',q.locator('[data-save="graph-lesson"]').input_value()==note)
        fresh.close()
    except Exception as error:check('Optional resources and saved work',False,error)
    try:
        go(p,'#/');action(p,'search');p.locator('#global-search').fill('receipt');p.wait_for_timeout(150)
        check('Guide search returns substantive content',p.locator('.search-result').count()>0)
        p.locator('.search-result').first.click();p.wait_for_timeout(150)
        check('Search opens its destination',not p.locator('#search-dialog').evaluate('(e)=>e.open'))
        p.locator('#topbar [data-help]').first.click()
        check('Contextual help remains available',p.locator('#help-dialog').evaluate('(e)=>e.open'))
        p.keyboard.press('Escape')
    except Exception as error:check('Search and help',False,error)
    check('No JavaScript page errors',not errors,json.dumps(errors))
    check('No external model, analytics, or asset requests',not requests,json.dumps(requests))
    browser.close()
report={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Original public Vercel URL','publicUrl':URL,'publicProduction':True,'servedSha256':EXPECTED,'routes':routes,'routeCount':len(routes),'widths':[1440,1024,768,390],'withoutLogin':True,'storageMocked':False,'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'checks':checks,'pageErrors':errors,'externalRequests':requests}
(OUT/'public-browser-report.json').write_text(json.dumps(report,indent=2))
print('LIVE_READING_FIRST_RESULT='+json.dumps({k:v for k,v in report.items() if k not in ['checks','routes']}),flush=True)
if report['failed']:sys.exit(1)
