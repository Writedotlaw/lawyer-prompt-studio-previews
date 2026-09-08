"""Read-only browser regression checks for the reading-first guide.
With --url, tests the public HTTPS site. Without it, serves local files for CI.
Uses real browser storage and real downloads; never mocks storage or outcomes.
"""
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from threading import Thread
import argparse,datetime,hashlib,json,os,re,sys,traceback,urllib.request
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--url');parser.add_argument('--chromium');args=parser.parse_args()
source=(R/'dist/index.html').read_bytes();base_source=(R.parent/'public-edition/dist/index.html').read_bytes()
release=json.loads((R/'dist/release.json').read_text());data=json.loads((R/'edited-data.json').read_text())
OUT=R/('public-evidence' if args.url else 'test-evidence');OUT.mkdir(exist_ok=True)
server=None
if args.url:
 URL=args.url.rstrip('/')+'/';scope='Public HTTPS production verification'
 assert URL=='https://regalia-ai-field-guide-joe-regalias-projects.vercel.app/','Unexpected publication target'
else:
 class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
   body=base_source if self.path.startswith('/legacy') else source
   self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(body)
  def log_message(self,*a):pass
 server=ThreadingHTTPServer(('127.0.0.1',8765),Handler);Thread(target=server.serve_forever,daemon=True).start();URL='http://127.0.0.1:8765/';scope='Local HTTP pre-publication tests'
checks=[];errors=[];external=[];routes=['#/','#/chapters','#/labs','#/templates','#/prompts','#/glossary','#/notebook','#/sources','#/help','#/questions']+['#/read/'+c['id'] for c in data['CHAPTERS']]+['#/lab/'+l['id'] for l in data['LABS']]
all_hrefs=set();read_text={}
def check(name,ok,detail=''):
 checks.append({'check':name,'passed':bool(ok),'detail':str(detail)[:1200]})
 print(('PASS ' if ok else 'FAIL ')+name,flush=True)
def run(name,fn):
 try:fn()
 except Exception as e:check(name,False,str(e));print(traceback.format_exc()[-1200:],flush=True)
def go(p,fragment):
 p.goto(URL+fragment,wait_until='domcontentloaded');p.wait_for_selector('#main h1');p.wait_for_timeout(70)
def action(p,a):p.locator('[data-action="'+a+'"]').first.click();p.wait_for_timeout(80)
def norm(t):return re.sub(r'\s+',' ',t).strip()
with sync_playwright() as pw:
 kw={'headless':True}
 if args.chromium:kw['executable_path']=args.chromium
 browser=pw.chromium.launch(**kw)
 context=browser.new_context(viewport={'width':1440,'height':1024},reduced_motion='reduce',accept_downloads=True)
 p=context.new_page();p.set_default_timeout(9000);p.on('dialog',lambda d:d.accept());p.on('pageerror',lambda e:errors.append(str(e)))
 p.on('request',lambda r:external.append(r.url) if not r.url.startswith((URL,'data:','blob:')) else None)
 def http_check():
  with urllib.request.urlopen(URL,timeout=30) as r:
   served=r.read(2000000)
   check('Anonymous response is HTTP 200',r.status==200)
   check('Address has not redirected to another origin',r.url==URL)
   check('Served HTML is the exact reviewed revision',hashlib.sha256(served).hexdigest()==release['sha256'],len(served))
 run('Public/source HTTP comparison',http_check)
 for width,height in [(1440,1024),(1024,900),(768,1024),(390,844)]:
  p.set_viewport_size({'width':width,'height':height})
  for fragment in routes:
   def visit(fragment=fragment):
    go(p,fragment)
    title=p.locator('#main h1').first.inner_text()
    check(f'{width}px {fragment}: page renders',len(title)>2 and 'not found' not in title.lower(),title)
    check(f'{width}px {fragment}: no document overflow',p.evaluate('document.documentElement.scrollWidth<=innerWidth+2'))
    if width==1440:
     all_hrefs.update(p.locator('a[href^="#/"]').evaluate_all('(es)=>es.map(e=>e.getAttribute("href"))'))
     if fragment.startswith('#/read/'):
      cid=fragment.split('/')[-1];c=next(c for c in data['CHAPTERS'] if c['id']==cid)
      read=p.locator('.chapter-reading');read_text[cid]=read.inner_text()
      check(cid+': all sections are in the reading',read.locator('[data-section-reading]').count()==len(c['sections']))
      check(cid+': no activity or form required',read.locator('[data-widget],input,textarea,select,[data-action="quiz"]').count()==0)
      check(cid+': no teaching hidden in disclosures',read.locator('details').count()==0)
      check(cid+': navigation exposes all sixteen chapters',p.locator('.gf-nav-reading a[href^="#/read/"]').count()==16)
      check(cid+': onward reading appears before optional practice',p.evaluate('!!(document.querySelector(".next-chapters").compareDocumentPosition(document.querySelector(".gf-companions"))&Node.DOCUMENT_POSITION_FOLLOWING)'))
    if width==390 and fragment=='#/':p.screenshot(path=str(OUT/'Guide-First-Home-Mobile.png'),full_page=True)
   run(f'{width}px route {fragment}',visit)
 p.set_viewport_size({'width':1440,'height':1024})
 def guide_focus():
  go(p,'#/')
  check('Homepage links to every chapter',p.locator('.gf-content-chapter').count()==16)
  check('Homepage primary reading choices precede companions',p.evaluate('!!(document.querySelector(".gf-home-contents").compareDocumentPosition(document.querySelector(".gf-companion-footer"))&Node.DOCUMENT_POSITION_FOLLOWING)'))
  check('No primary activity hero remains',p.locator('.wl-example,.wl-task-routes,[data-widget]').count()==0)
  check('Companion navigation is initially secondary',not p.locator('.gf-companion-nav').evaluate('(e)=>e.open'))
  p.screenshot(path=str(OUT/'Guide-First-Home-Desktop.png'),full_page=False)
  for cid in ['method','prompting','writing','agents','graphing']:
   go(p,'#/read/'+cid);p.screenshot(path=str(OUT/(cid+'-reading-desktop.png')))
  check('All six collaboration practices are visible',all(x in read_text['method'] for x in ['First, do some work.','Direct with guidance and examples.','Choose with options and iterations.','Lean on expansion, pressure testing, and identification.','Scale the work for yourself and the AI.','Prompt in a way that incorporates those decisions.']))
  check('All ten prompting principles are in the reading',all(x in read_text['prompting'] for x in ['1. Provide the role','2. Provide context','3. Use annotated','4. Use menus','5. Set parameters','6. Iterate','7. Break down','8. Use AI','9. Reset','10. Avoid AI-isms']))
  check('The five-stage framework remains distinct',all(x in read_text['method'].lower() for x in ['human-first frame','ai-assisted expansion','lawyer-grade audit','human revision and judgment','document and improve']))
  check('Work-order fields and complete example are readable',all(x in read_text['agents'] for x in ['1. Client outcome','12. Record and version',data['ORDER_PRESET']['outcome']]))
  check('Original and revised Stonebridge passages are readable',all(norm(data['STONEBRIDGE'][k]) in norm(read_text['writing']) for k in ['original','revision']))
  check('Original and revised Falcon passages are readable',all(norm(data['FALCON'][k]) in norm(read_text['writing']) for k in ['original','revision']))
  check('All fee comparisons are readable',all(norm(x['text']) in norm(read_text['writing']) for x in data['FEE_OPTIONS']))
  check('Employee-departure facts are readable without choosing priorities',norm(data['PRIORITY_FACTS']) in norm(read_text['think']))
  check('The deliberately weak AI-isms passage is readable',norm(data['AIISM_TEXT']) in norm(read_text['aiisms']))
  go(p,'#/questions')
  check('Full question reference is readable without a form',p.locator('.gf-open-question').count()==103 and p.locator('#main select,#main textarea').count()==0)
  go(p,'#/read/agents');p.locator('.gf-workorder').scroll_into_view_if_needed();p.screenshot(path=str(OUT/'Readable-Work-Order.png'))
  go(p,'#/read/writing?section=3');p.screenshot(path=str(OUT/'Readable-Stonebridge.png'))
 run('Guide-first hierarchy and full teaching',guide_focus)
 def links():
  ids={c['id']:len(c['sections']) for c in data['CHAPTERS']};labs={l['id'] for l in data['LABS']}
  for href in sorted(all_hrefs):
   bits=href.split('?')[0].split('/');ok=True
   if len(bits)>2 and bits[1]=='read':
    ok=bits[2] in ids
    if '?section=' in href:
     sec=href.split('?section=')[1];ok=ok and (sec=='quiz' or sec.isdigit() and int(sec)<ids[bits[2]])
   elif len(bits)>2 and bits[1]=='lab':ok=bits[2] in labs
   else:ok=bits[1] in ['', 'chapters','labs','templates','prompts','glossary','notebook','sources','help','questions']
   check('Internal destination '+href,ok)
  go(p,'#/read/method?section=quiz')
  check('Earlier quiz links still open the optional question',p.locator('.gf-optional-check').evaluate('(e)=>e.open') and p.locator('#quiz-method').is_visible())
  go(p,'#/chapters?part=2')
  check('Contents jump opens the requested part',p.locator('#part-2').evaluate('(e)=>{const r=e.getBoundingClientRect();return r.top>=0&&r.top<innerHeight}'))
  go(p,'#/questions?group=3')
  check('Question subject jump reaches the section',p.locator('#questions-3').evaluate('(e)=>{const r=e.getBoundingClientRect();return r.top>=0&&r.top<innerHeight}'))
 run('Internal links and earlier destinations',links)
 def help_and_search():
  go(p,'#/chapters');button=p.locator('#topbar [data-help]').first;button.click()
  check('Help explains that the reading is complete',p.locator('#help-dialog').evaluate('(e)=>e.open') and 'complete' in p.locator('.help-body').inner_text())
  p.keyboard.press('Escape');check('Escape returns focus to help',not p.locator('#help-dialog').evaluate('(e)=>e.open') and button.evaluate('(e)=>e===document.activeElement'))
  button.focus();p.wait_for_timeout(150);check('Keyboard focus exposes help tooltip',p.locator('#guide-tooltip').is_visible());p.keyboard.press('Escape')
  action(p,'search');check('Search suggestions start with chapters',all(x.startswith('#/read/') for x in p.locator('.search-result').evaluate_all('(es)=>es.map(e=>e.getAttribute("href"))')))
  p.locator('#global-search').fill('projected savings');p.wait_for_timeout(130)
  check('Search finds the substantive worked comparison',p.locator('.search-result[href^="#/read/writing"]').count()>0)
  p.locator('.search-result[href^="#/read/writing"]').first.click();p.wait_for_timeout(100)
  check('Search opens a reading destination',p.url.startswith(URL+'#/read/writing'))
  go(p,'#/lab/workorder');p.locator('[data-help="field:order-tools"]').click();check('Optional field help remains available',p.locator('#help-dialog').evaluate('(e)=>e.open'));p.keyboard.press('Escape')
 run('Help, keyboard controls, and reading search',help_and_search)
 def graph():
  go(p,'#/lab/graph');action(p,'graph-reset');p.locator('[data-action="graph-node"][data-step="5"]').click()
  check('Inspecting a workflow task does not complete it',p.evaluate('graphState.step===-1 && graphState.selected===5'))
  for _ in range(3):action(p,'graph-next')
  check('Missing receipt evidence stops drafting',p.evaluate('graphState.step===3') and p.locator('[data-action="graph-next"]').is_disabled())
  action(p,'graph-qualify');check('Qualified approach still requires approval',p.evaluate('graphState.step===3'))
  action(p,'graph-next');check('Human approval advances the task',p.evaluate('graphState.step===4'))
  for _ in range(3):action(p,'graph-next')
  check('The complete optional workflow remains usable',p.evaluate('graphState.step===7'))
  action(p,'graph-evidence');check('New evidence returns the affected work for review',p.evaluate('graphState.step===2 && graphState.updated'))
  action(p,'graph-next');check('New evidence does not silently approve the outcome',p.evaluate('graphState.step===3'))
 run('Preserved optional workflow behavior',graph)
 def saving():
  note='Reading-first release check: preserve the receipt distinction.'
  go(p,'#/lab/graph');p.locator('[data-save="graph-lesson"]').fill(note);p.wait_for_timeout(200);p.reload(wait_until='domcontentloaded');p.wait_for_selector('[data-save="graph-lesson"]')
  check('Optional exercise response survives a real reload',p.locator('[data-save="graph-lesson"]').input_value()==note)
  go(p,'#/read/think');p.locator('.gf-note>summary').click();p.locator('[data-save="note-think"]').fill('A note from reading without an exercise.');p.wait_for_timeout(100);p.reload(wait_until='domcontentloaded');p.wait_for_selector('.gf-note');p.locator('.gf-note>summary').click()
  check('Chapter note survives a real reload',p.locator('[data-save="note-think"]').input_value()=='A note from reading without an exercise.')
  go(p,'#/notebook')
  with p.expect_download() as download:action(p,'export-json')
  backup=OUT/'test-backup.json';download.value.save_as(str(backup))
  raw=json.loads(backup.read_text());check('Backup preserves the existing app identity',raw['app']=='regalia-ai-field-guide' and raw['version']==1)
  with p.expect_download() as download:action(p,'export-md')
  txt=OUT/'test-notes.txt';download.value.save_as(str(txt));check('Readable export includes saved entries',note in txt.read_text())
  fresh=browser.new_context(viewport={'width':1280,'height':900});q=fresh.new_page();q.on('dialog',lambda d:d.accept());q.on('pageerror',lambda e:errors.append(str(e)));go(q,'#/notebook');q.locator('#import-file').set_input_files(str(backup));q.wait_for_timeout(150);go(q,'#/lab/graph');check('Backup restores an optional response in a fresh browser',q.locator('[data-save="graph-lesson"]').input_value()==note);q.reload(wait_until='domcontentloaded');q.wait_for_selector('[data-save="graph-lesson"]');check('Restored work survives reload',q.locator('[data-save="graph-lesson"]').input_value()==note);fresh.close()
  if not args.url:
   legacy=browser.new_context(viewport={'width':1280,'height':900});q=legacy.new_page();q.goto(URL+'legacy#/lab/graph');q.wait_for_selector('[data-save="graph-lesson"]');q.locator('[data-save="graph-lesson"]').fill('Prior edition response');q.goto(URL+'legacy#/read/think');q.wait_for_selector('[data-save="note-think"]');q.locator('[data-save="note-think"]').fill('Prior edition chapter note');go(q,'#/lab/graph');check('Same-origin update keeps a prior-edition response',q.locator('[data-save="graph-lesson"]').input_value()=='Prior edition response');go(q,'#/read/think');q.locator('.gf-note>summary').click();check('Same-origin update keeps a prior-edition chapter note',q.locator('[data-save="note-think"]').input_value()=='Prior edition chapter note');legacy.close()
 run('Real storage and backup compatibility',saving)
 def mobile():
  mctx=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,reduced_motion='reduce');m=mctx.new_page();m.on('pageerror',lambda e:errors.append(str(e)));go(m,'#/');action(m,'menu');check('Mobile navigation opens',m.locator('body').evaluate('(e)=>e.classList.contains("sidebar-open")'));m.locator('#sidebar a[href="#/read/method"]').click();m.wait_for_timeout(100);check('Mobile readers can open a chapter directly',m.locator('.chapter-reading').count()==1)
  m.locator('#topbar [data-help]').first.tap();check('Help opens by touch',m.locator('#help-dialog').evaluate('(e)=>e.open'));m.locator('#help-dialog [data-action="close-help"]').first.tap()
  go(m,'#/read/writing?section=3');m.screenshot(path=str(OUT/'Guide-First-Reading-Mobile.png'))
  go(m,'#/lab/graph');m.locator('[data-action="graph-node"][data-step="3"]').tap();check('Optional mobile graph reveals the task explanation',m.locator('.graph-detail').evaluate('(e)=>{const r=e.getBoundingClientRect();return r.top>=0&&r.top<innerHeight}'))
  mctx.close()
 run('Mobile touch controls',mobile)
 def preferences():
  go(p,'#/read/method');old=p.locator('html').get_attribute('data-theme');action(p,'theme');new=p.locator('html').get_attribute('data-theme');p.reload(wait_until='domcontentloaded');p.wait_for_selector('#main h1');check('Theme preference survives reload',new!=old and p.locator('html').get_attribute('data-theme')==new);p.screenshot(path=str(OUT/'Guide-First-Reading-Dark.png'));action(p,'theme');action(p,'focus');check('Focused reading remains available',p.locator('body').evaluate('(e)=>e.classList.contains("reader-focus")'));action(p,'focus')
 run('Reading preferences',preferences)
 check('No external model, analytics, or asset requests',not external,external)
 check('No JavaScript errors',not errors,errors)
 report={'scope':scope,'publicUrl':URL,'publicProduction':bool(args.url),'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sourceSha256':release['sha256'],'routeCount':len(routes),'viewportWidths':[1440,1024,768,390],'readingSections':84,'requiredExercises':0,'storageMocked':False,'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'pageErrors':errors,'externalRequests':external,'checks':checks}
 (OUT/'browser-report.json').write_text(json.dumps(report,indent=2));(OUT/'rendered-reading.json').write_text(json.dumps(read_text,ensure_ascii=False,indent=2))
 print('GUIDE_FIRST_TEST_RESULT='+json.dumps({k:v for k,v in report.items() if k not in ['checks','pageErrors','externalRequests']}),flush=True)
 browser.close()
if server:server.shutdown()
if report['failed']:sys.exit(1)
