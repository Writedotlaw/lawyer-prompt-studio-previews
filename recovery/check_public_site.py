"""Public-origin browser checks. No storage mocks, no login, no fabricated results."""
from pathlib import Path
import json
import sys
import traceback
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent / 'results'
RESULT = json.loads((OUT / 'deployment-result.json').read_text())
URL = RESULT['previewUrl'].rstrip('/')
checks, errors = [], []

def check(name, passed, detail=''):
    checks.append({'check': name, 'passed': bool(passed), 'detail': str(detail)[:1000]})
    print(('PASS: ' if passed else 'FAIL: ') + name, flush=True)

def run(name, task):
    try:
        task()
    except Exception as exc:
        check(name, False, str(exc))
        print(traceback.format_exc()[-1600:], flush=True)

def go(page, fragment):
    page.goto(URL + '/' + fragment, wait_until='domcontentloaded')
    page.wait_for_selector('#main h1', timeout=15000)
    page.wait_for_timeout(130)

def action(page, name):
    page.locator('[data-action="' + name + '"]').first.click()
    page.wait_for_timeout(80)

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    desktop = browser.new_context(viewport={'width':1440,'height':1000}, reduced_motion='reduce')
    p = desktop.new_page()
    p.set_default_timeout(8000)
    p.on('pageerror', lambda e: errors.append(str(e)))
    p.on('dialog', lambda d: d.accept())
    response = p.goto(URL, wait_until='domcontentloaded')
    p.wait_for_selector('#main h1')
    check('Public homepage opens in a fresh browser without a login', response.status == 200 and p.url.startswith(URL))
    check('Revised navigation is present', all(t in p.locator('#sidebar').inner_text() for t in ['Exercises','Templates & worksheets','My saved work']))
    p.screenshot(path=str(OUT/'public-home-desktop.png'), full_page=False)
    chapters = p.evaluate('CHAPTERS.map(x=>({id:x.id,title:x.title}))')
    labs = p.evaluate('LABS.map(x=>({id:x.id,title:x.title}))')
    routes = ['#/','#/chapters','#/labs','#/templates','#/prompts','#/glossary','#/notebook','#/sources','#/help']
    routes += ['#/read/'+x['id'] for x in chapters]
    routes += ['#/lab/'+x['id'] for x in labs]
    routes = list(dict.fromkeys(routes))
    for fragment in routes:
        def visit(fragment=fragment):
            go(p, fragment)
            title = p.locator('#main h1').first.inner_text()
            check('Desktop route '+fragment, len(title)>2 and 'not found' not in title.lower(), title)
            check('Desktop fits '+fragment, p.evaluate('document.documentElement.scrollWidth <= innerWidth + 2'))
        run('Desktop route '+fragment, visit)
    def help_check():
        go(p, '#/templates')
        button=p.locator('#topbar [data-help]').first
        button.click()
        check('Area help opens by click',p.locator('#help-dialog').evaluate('(e)=>e.open') and len(p.locator('.help-body').inner_text())>100)
        p.keyboard.press('Escape')
        check('Escape closes help and restores focus',not p.locator('#help-dialog').evaluate('(e)=>e.open') and button.evaluate('(e)=>e===document.activeElement'))
        button.focus()
        p.wait_for_timeout(180)
        check('Help explanation available on keyboard focus',p.locator('#guide-tooltip').is_visible())
        p.keyboard.press('Escape')
        go(p,'#/lab/workorder')
        p.locator('[data-help="field:order-tools"]').click()
        check('Work-order field help explains permissions',len(p.locator('.help-body').inner_text())>100)
        p.keyboard.press('Escape')
    run('Public help controls',help_check)
    def graph_check():
        go(p,'#/lab/graph')
        action(p,'graph-reset')
        p.locator('[data-action="graph-node"][data-step="5"]').click()
        check('Inspecting a workflow task does not complete it',p.evaluate('graphState.step===-1 && graphState.selected===5'))
        for _ in range(3): action(p,'graph-next')
        check('Missing receipt evidence stops drafting',p.evaluate('graphState.step===3') and p.locator('[data-action="graph-next"]').is_disabled())
        action(p,'graph-qualify')
        check('Selecting a qualified approach still requires approval',p.evaluate('graphState.step===3') and 'Approve' in p.locator('[data-action="graph-next"]').inner_text())
        action(p,'graph-next')
        check('Explicit human approval advances the example',p.evaluate('graphState.step===4'))
        for _ in range(3): action(p,'graph-next')
        check('Prepared workflow reaches its conclusion',p.evaluate('graphState.step===7'))
        action(p,'graph-evidence')
        check('New receipt evidence returns affected work for reconsideration',p.evaluate('graphState.step===2 && graphState.updated'))
        action(p,'graph-next')
        check('New evidence does not silently approve the recommendation',p.evaluate('graphState.step===3') and 'Approve' in p.locator('[data-action="graph-next"]').inner_text())
        p.screenshot(path=str(OUT/'public-workflow-desktop.png'),full_page=False)
    run('Public workflow decisions',graph_check)
    def persistence_check():
        go(p,'#/lab/graph')
        note='Public deployment verification: keep sending and receipt separate.'
        p.locator('[data-save="graph-lesson"]').fill(note)
        p.wait_for_timeout(400)
        check('Exercise response is written to browser storage',p.evaluate('JSON.parse(localStorage.getItem("regalia-field-guide.v1")).fields["graph-lesson"]')==note)
        p.reload(wait_until='domcontentloaded')
        p.wait_for_selector('[data-save="graph-lesson"]')
        check('Exercise response survives a real page reload',p.locator('[data-save="graph-lesson"]').input_value()==note)
        go(p,'#/notebook')
        check('Saved work contains the exercise response',note in p.locator('#main').inner_text())
        with p.expect_download() as pending:
            action(p,'export-json')
        backup=pending.value
        backup.save_as(str(OUT/'test-browser-backup.json'))
        check('Restorable backup downloads from the public origin',Path(OUT/'test-browser-backup.json').stat().st_size>50)
    run('Hosted saved-work persistence and export',persistence_check)
    def search_check():
        go(p,'#/')
        action(p,'search')
        p.locator('#global-search').fill('receipt')
        p.wait_for_timeout(180)
        check('Full-guide search finds receipt-related material',p.locator('.search-result').count()>0)
        p.locator('.search-result').first.click()
        p.wait_for_timeout(130)
        check('Search result opens its destination',not p.locator('#search-dialog').evaluate('(e)=>e.open') and p.locator('#main h1').count()==1)
    run('Hosted search',search_check)
    def theme_check():
        old=p.locator('html').get_attribute('data-theme')
        action(p,'theme')
        new=p.locator('html').get_attribute('data-theme')
        check('Theme toggle works',new!=old)
        p.reload(wait_until='domcontentloaded')
        p.wait_for_selector('#main h1')
        check('Theme preference persists on reload',p.locator('html').get_attribute('data-theme')==new)
    run('Hosted reading preferences',theme_check)
    mobile = browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,reduced_motion='reduce')
    m=mobile.new_page();m.set_default_timeout(8000)
    m.on('pageerror',lambda e:errors.append(str(e)))
    for fragment in routes:
        def visit_mobile(fragment=fragment):
            go(m,fragment)
            title=m.locator('#main h1').first.inner_text()
            check('Mobile route '+fragment,len(title)>2 and 'not found' not in title.lower(),title)
            check('Mobile fits '+fragment,m.evaluate('document.documentElement.scrollWidth <= innerWidth + 2'))
        run('Mobile route '+fragment,visit_mobile)
    def mobile_interactions():
        go(m,'#/')
        m.screenshot(path=str(OUT/'public-home-mobile.png'),full_page=False)
        action(m,'menu')
        check('Mobile navigation opens',m.locator('body').evaluate('(e)=>e.classList.contains("sidebar-open")'))
        m.locator('#sidebar a[href="#/templates"]').click()
        m.wait_for_timeout(150)
        check('Mobile navigation opens the selected section','Templates' in m.locator('#main h1').inner_text())
        m.locator('#topbar [data-help]').first.tap()
        check('Help opens by touch',m.locator('#help-dialog').evaluate('(e)=>e.open'))
        m.locator('#help-dialog [data-action="close-help"]').first.tap()
        go(m,'#/lab/graph')
        m.locator('[data-action="graph-node"][data-step="3"]').tap()
        check('Mobile task selection brings its explanation into view',m.locator('.graph-detail').evaluate('(e)=>{const r=e.getBoundingClientRect();return r.top>=0&&r.top<innerHeight}'))
        m.locator('[data-action="graph-back"]').tap()
        check('Mobile task panel returns to the diagram',m.locator('[data-action="graph-node"][data-step="3"]').evaluate('(e)=>{const r=e.getBoundingClientRect();return r.top>=0&&r.top<innerHeight}'))
    run('Public touch interactions',mobile_interactions)
    check('No JavaScript page errors in desktop or mobile runs',not errors,json.dumps(errors))
    report={'publicUrl':URL,'withoutLogin':True,'storageMocked':False,'routes':routes,
        'desktop':{'width':1440,'height':1000},'mobile':{'width':390,'height':844},
        'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),
        'checks':checks,'pageErrors':errors}
    (OUT/'public-browser-report.json').write_text(json.dumps(report,indent=2))
    print('PUBLIC_BROWSER_SUMMARY='+json.dumps({k:report[k] for k in ['publicUrl','passed','failed','withoutLogin','storageMocked']}),flush=True)
    browser.close()
    if report['failed']:
        sys.exit(1)
