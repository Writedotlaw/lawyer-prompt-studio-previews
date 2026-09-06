"""Test the actual HTTPS deployment in fresh Chromium contexts, without mocked storage."""
from pathlib import Path
import json, traceback
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'verified-results'
meta = json.loads((OUT / 'deployment.json').read_text())
assert meta.get('signedOutHttpVerified'), 'HTTP source verification must pass first'
base = meta['previewUrl'].rstrip('/')
checks, errors = [], []
def check(name, condition, detail=None):
    checks.append({'check': name, 'passed': bool(condition), 'detail': detail})
    print(('PASS: ' if condition else 'FAIL: ') + name, flush=True)
def go(page, hash):
    page.evaluate('(h)=>{location.hash=h;route();}', hash)
    page.wait_for_timeout(120)
    page.locator('#main h1').first.wait_for(state='visible')
def act(page, action):
    page.locator('[data-action="' + action + '"]').first.click()

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width': 1440, 'height': 1000}, reduced_motion='reduce', accept_downloads=True)
    page = context.new_page()
    page.set_default_timeout(8000)
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.on('dialog', lambda dialog: dialog.accept())
    response = page.goto(base, wait_until='networkidle')
    check('Homepage loads publicly without authentication', response.status == 200 and page.locator('#main h1').count() == 1)
    check('Revised area names are displayed', all(s in page.locator('body').inner_text() for s in ['Exercises', 'Templates & worksheets', 'My saved work']))
    check('Real HTTPS local storage is available', page.evaluate('storageOK && typeof localStorage.setItem === "function"'))
    page.screenshot(path=str(OUT / 'published-desktop.png'), full_page=True)
    chapters = page.evaluate('CHAPTERS.map(c=>c.id)')
    labs = page.evaluate('LABS.map(l=>l.id)')
    routes = ['#/', '#/chapters', '#/labs', '#/templates', '#/prompts', '#/glossary', '#/notebook', '#/sources', '#/help'] + ['#/read/'+c for c in chapters] + ['#/lab/'+l for l in labs]
    for hash in routes:
        go(page, hash)
        check('Desktop route opens: '+hash, page.locator('#main h1').count() == 1 and 'not found' not in page.locator('#main h1').inner_text().lower())
    try:
        go(page, '#/lab/workorder')
        # The public area uses the same help controls as embedded chapter tools.
        field_help = page.locator('[data-help="field:order-tools"]')
        if field_help.count() == 0:
            for lab in labs:
                go(page, '#/lab/'+lab)
                if page.locator('[data-help="field:order-tools"]').count():
                    break
        field_help = page.locator('[data-help="field:order-tools"]').first
        field_help.click()
        check('Field help opens by click', page.locator('#help-dialog').evaluate('(e)=>e.open'))
        check('Field help provides an explanation', len(page.locator('#help-dialog').inner_text()) > 120)
        page.screenshot(path=str(OUT / 'published-field-help.png'))
        page.keyboard.press('Escape')
        check('Help closes with Escape', not page.locator('#help-dialog').evaluate('(e)=>e.open'))
        field_help.focus()
        page.wait_for_timeout(700)
        check('Help is keyboard focusable', field_help.evaluate('(e)=>document.activeElement===e'))
    except Exception as error:
        check('Contextual help interaction', False, str(error))
    try:
        go(page, '#/lab/graph')
        page.locator('[data-action="graph-node"][data-step="5"]').click()
        check('Inspecting a workflow task does not advance it', page.evaluate('graphState.step===-1&&graphState.selected===5'))
        for _ in range(3): act(page, 'graph-next')
        check('Missing receipt evidence stops the workflow', page.evaluate('graphState.step===3') and page.locator('[data-action="graph-next"]').is_disabled())
        act(page, 'graph-qualify')
        check('Qualified approach still needs human approval', page.evaluate('graphState.step===3') and 'Approve' in page.locator('[data-action="graph-next"]').inner_text())
        act(page, 'graph-next')
        check('Explicit approval advances the example', page.evaluate('graphState.step===4'))
        note = 'Hosted verification: confirm receipt before calculating the cure period.'
        page.locator('[data-save="graph-lesson"]').fill(note)
        page.wait_for_timeout(700)
        go(page, '#/read/graphing')
        check('Chapter and standalone activity share the same response', page.locator('[data-save="graph-lesson"]').input_value() == note)
        page.reload(wait_until='networkidle')
        check('Saved response survives a hosted-page reload', page.locator('[data-save="graph-lesson"]').input_value() == note)
        page.screenshot(path=str(OUT / 'published-chapter.png'))
        go(page, '#/notebook')
        check('Saved response appears in notebook data', page.locator('[data-save="graph-lesson"]').input_value() == note)
        with page.expect_download() as download:
            act(page, 'export-json')
        backup_path = OUT / 'test-backup.json'
        download.value.save_as(str(backup_path))
        backup = json.loads(backup_path.read_text())
        check('Backup download contains the saved response', backup['state']['fields']['graph-lesson'] == note)
        with page.expect_download() as download:
            act(page, 'export-md')
        notes_path = OUT / 'test-readable-notes.txt'
        download.value.save_as(str(notes_path))
        check('Readable notes download contains the saved response', note in notes_path.read_text())
        reopened = context.new_page()
        reopened.goto(base+'/#/read/graphing', wait_until='networkidle')
        check('Saved response is available in a new tab on the same site', reopened.locator('[data-save="graph-lesson"]').input_value() == note)
        reopened.close()
    except Exception as error:
        check('Workflow and saved-work interactions', False, str(error))
    try:
        go(page, '#/lab/stonebridge')
        page.locator('[data-save="stonebridge-draft"]').fill('We need supporting materials before confirming that the dividend is permitted.')
        page.locator('[data-action="reveal-case"][data-case="stonebridge"]').click()
        check('Writing exercise reveals prepared discussion after an attempt', page.evaluate('state.fields["stonebridge-revealed"]===true'))
        act(page, 'search')
        page.fill('#global-search', 'missing receipt')
        page.wait_for_timeout(400)
        check('Search returns relevant resources', page.locator('.search-result').count() > 0)
        page.keyboard.press('Enter')
        page.wait_for_timeout(200)
        check('Search opens its selected destination', not page.locator('#search-dialog').evaluate('(e)=>e.open'))
    except Exception as error:
        check('Writing and search interactions', False, str(error))
    mobile_context = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True, reduced_motion='reduce')
    mobile = mobile_context.new_page()
    mobile.set_default_timeout(8000)
    mobile.on('pageerror', lambda error: errors.append(str(error)))
    mobile.goto(base, wait_until='networkidle')
    mobile.screenshot(path=str(OUT / 'published-mobile.png'), full_page=True)
    for hash in routes:
        go(mobile, hash)
        width = mobile.evaluate('({viewport:innerWidth,body:document.documentElement.scrollWidth})')
        check('Mobile route fits viewport: '+hash, width['body'] <= width['viewport'] + 2, width)
    try:
        go(mobile, '#/help')
        check('Mobile help explains saved work', 'backup' in mobile.locator('#main').inner_text().lower())
        mobile.locator('#topbar [data-help]').first.tap()
        check('Help opens on touch devices', mobile.locator('#help-dialog').evaluate('(e)=>e.open'))
        mobile.screenshot(path=str(OUT / 'published-mobile-help.png'))
    except Exception as error:
        check('Mobile touch help', False, str(error))
    check('No browser JavaScript errors', not errors, errors)
    browser.close()
report = {'url':base,'sourceSha256':meta['indexSha256'],'chapters':len(chapters),'activities':len(labs),'routes':len(routes),'checks':checks,'pageErrors':errors}
report['passed'] = sum(c['passed'] for c in checks)
report['failed'] = sum(not c['passed'] for c in checks)
(OUT / 'hosted-browser-report.json').write_text(json.dumps(report, indent=2))
print(json.dumps({k:report[k] for k in ['url','chapters','activities','routes','passed','failed']}, indent=2), flush=True)
assert report['failed'] == 0, 'Some hosted-browser checks failed; inspect the report before claiming completion.'
