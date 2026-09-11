"""Check the consolidated reading page, its data boundaries, and its links."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json,sys
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'tests/results';out.mkdir(exist_ok=True)
url=sys.argv[1] if len(sys.argv)>1 else ''
checks=[];errors=[]
def check(name,condition):
 checks.append({'name':name,'passed':bool(condition)})
 print(('PASS ' if condition else 'FAIL ')+name,flush=True)
 if not condition:raise AssertionError(name)
def goto(page,route):
 page.evaluate('(r)=>location.hash=r',route);page.wait_for_timeout(150)
try:
 with sync_playwright() as p:
  opts={'headless':True,'args':['--no-sandbox']}
  if Path('/usr/bin/chromium').exists():opts['executable_path']='/usr/bin/chromium'
  browser=p.chromium.launch(**opts);page=browser.new_page(viewport={'width':1440,'height':1000},accept_downloads=True)
  page.on('pageerror',lambda e:errors.append(str(e)))
  if url:page.goto(url)
  else:page.set_content((ROOT/'index.html').read_text(),wait_until='domcontentloaded')
  page.wait_for_timeout(200)
  check('Educator release marker',page.locator('[data-version="educator-overview-v2"]').count()==1)
  check('One main heading',page.locator('h1').count()==1)
  for section in ['people','experience','courts','workflows','errors','responses','trends','teaching']:
   el=page.locator('#finding-'+section)
   check('Section present without drilling: '+section,el.count()==1 and el.is_visible())
   check('Section is not collapsed: '+section,el.evaluate('(e)=>!e.closest("details:not([open])")'))
  text=page.locator('main').inner_text()
  for name,string in [('Current pro se count','1,172'),('Current lawyer and staff count','819'),('Current US record count','1,393'),('Experience median','21 years'),('Experience denominator','394'),('Practice size denominator','395'),('Court study denominator','1,378'),('Source pronouns denominator','420'),('Both snapshot dates','Sep 10, 2026'),('Study snapshot date','September 2, 2026')]:check(name,string in text)
  check('No full-study link required to read experience',page.locator('#finding-experience .barrow').count()>=13)
  check('Court types and court rankings already visible',page.locator('#finding-courts .barrow').count()>=26)
  check('Only six primary destinations',page.locator('nav[aria-label="Primary"]>a').count()==6)
  page.locator('[data-action="jump-finding"][data-target="experience"]').click();page.wait_for_timeout(450)
  check('Jump stays on overview',page.evaluate('App.getState().route')=='overview')
  check('Jump is shareable',page.evaluate('location.hash.includes("section=experience")'))
  check('Jump focus is the section heading',page.evaluate('document.activeElement.id')=='finding-title-experience')
  goto(page,'overview?section=courts');page.wait_for_timeout(450)
  check('Direct section link scrolls to court heading',page.locator('#finding-courts').bounding_box()['y']<160)
  goto(page,'decisions?country=Canada');check('Case filter works',page.evaluate('App.getData().filtered')==217)
  goto(page,'overview?country=Canada');check('Reading page keeps full counts','1,172' in page.locator('#finding-people').inner_text())
  check('Overview explains filter boundary','do not narrow this reading page' in page.locator('main').inner_text())
  with page.expect_download() as dl:page.locator('[data-action="chart-data"]').click()
  dl.value.save_as(str(out/'overview-months.csv'));check('Monthly export uses whole snapshot',sum(int(line.split(',')[1].strip('"')) for line in (out/'overview-months.csv').read_text(encoding='utf-8-sig').splitlines()[1:])==2036)
  page.locator('[data-action="month-filter"]').first.click();check('Overview month click clears unrelated case filter',not page.evaluate('App.getState().filters.country'))
  goto(page,'overview');page.locator('[data-action="finding-cases"]').nth(1).click()
  check('Pro se drilldown uses its exact cohort',page.evaluate('App.getData().filtered')==1172)
  goto(page,'overview');page.locator('[data-action="finding-cases"]').first.click()
  check('Lawyer drilldown uses its exact cohort',page.evaluate('App.getData().filtered')==819)
  goto(page,'overview');page.locator('.teaching-case [data-action="case"]').first.click()
  check('Teaching case opens source-backed record',page.locator('[role="dialog"]').is_visible());page.keyboard.press('Escape')
  with page.expect_download() as dl:page.locator('[data-action="findings-export"]').click()
  dl.value.save_as(str(out/'teaching-findings.txt'));export=(out/'teaching-findings.txt').read_text()
  check('Teaching export contains experience and courts','21 years' in export and '1,378' in export)
  check('Teaching export preserves source information','kylebahr.netlify.app' in export and 'damiencharlotin.com' in export)
  page.emulate_media(media='print');check('Print hides jump navigation',not page.locator('.finding-jumps').is_visible());check('Print retains experience figures',page.locator('#finding-experience').is_visible());page.emulate_media(media='screen')
  for width in [1440,1024,768,390,360]:
   page.set_viewport_size({'width':width,'height':900});page.evaluate('scrollTo(0,0)')
   check('No page overflow at '+str(width),page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'))
   check('All eight main sections remain present at '+str(width),page.locator('.finding-heading').count()==8)
   if width in [1440,390]:page.screenshot(path=str(out/('educator-'+str(width)+'.png')),full_page=False)
  page.set_viewport_size({'width':1440,'height':1000});goto(page,'settings');page.locator('[name="study"]').uncheck();page.locator('#settings-form [type="submit"]').click();goto(page,'overview')
  check('Study can be hidden without hiding dataset',page.locator('#finding-experience').count()==0 and page.locator('#finding-people').count()==1)
  goto(page,'settings');page.locator('[name="study"]').check();page.locator('#settings-form [type="submit"]').click()
  sample='title,date,country,participant\nAlpha,2026-09-01,USA,Researcher\nBeta,2026-09-02,Canada,Editor\n'
  page.locator('#import-file').set_input_files({'name':'other-study.csv','mimeType':'text/csv','buffer':sample.encode()});page.wait_for_selector('#import-form')
  page.locator('[name="map-actors"]').select_option('participant');page.locator('#import-form [type="submit"]').click();goto(page,'overview')
  check('Imported overview uses mapped participant categories','Researcher' in page.locator('#finding-people').inner_text())
  check('No fixed lawyer study mixed with import',page.locator('#finding-experience').count()==0 and '21 years' not in page.locator('main').inner_text())
  check('No legal teaching assertions added to custom dataset',page.locator('#finding-teaching').count()==0)
  check('No JavaScript errors throughout',not errors)
  browser.close()
finally:
 report={'url':url or 'local HTML','passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'checks':checks,'pageErrors':errors}
 (out/'findings-browser-report.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
