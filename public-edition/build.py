"""Build the public edition from the verified guide and editable editorial files.
Run from repository root: python public-edition/build.py
Requires Node.js and mistune==3.2.1. It does not publish or authenticate.
"""
from pathlib import Path
import base64, copy, hashlib, html, importlib.util, json, re, subprocess, sys, urllib.request
import mistune

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
BASE=ROOT/'ai-guide-revised/index.html'
BASE_SHA='be11c3d012c00f81404f7374910b42d3d3a29ac1524037fa46d06076f608bb96'
LOGO_URL='https://lwfiles.mycourse.app/writedotlaw-public/83ed958a73471953e5ca7b5a5b789709.png'
LOGO_SHA='ffecf37ac38220fecca9f2ae1bb0f488fce16c0e86adb2dfe59b8fa8595b6292'
OUT=HERE/'dist'; MODULES=HERE/'editable-site'; OUT.mkdir(exist_ok=True);MODULES.mkdir(exist_ok=True)
base=BASE.read_bytes()
assert hashlib.sha256(base).hexdigest()==BASE_SHA,'Production base changed. Review it before rebuilding.'
text=base.decode()
scripts=re.findall(r'<script>([\s\S]*?)</script>',text)
styles=re.findall(r'<style>([\s\S]*?)</style>',text)
assert len(scripts)==5 and len(styles)==1,'Unexpected base structure'
names=['SOURCES','PARTS','CHAPTERS','METHOD','GLOSSARY','PROMPTS','ORDER_FIELDS','ORDER_PRESET','FEE_ORIGINAL','FEE_OPTIONS','STONEBRIDGE','FALCON','AIISM_TEXT','AIISM_LENSES','CHECKLIST','PLAYBOOK_FIELDS','SHIPPING','REFLECTIONS','LABS','PRIORITY_FACTS','PRIORITY_OPTIONS','RESOURCE_GUIDANCE','AREA_HELP','FIELD_EXAMPLES','NEXT_RESOURCE']
extract="const vm=require('vm'),fs=require('fs');const x=JSON.parse(fs.readFileSync(0,'utf8'));const c=vm.createContext({});for(const s of x.scripts)vm.runInContext(s,c);const d={};for(const n of x.names)d[n]=vm.runInContext(n,c);console.log(JSON.stringify(d));"
result=subprocess.run(['node','-e',extract],input=json.dumps({'scripts':scripts[:3],'names':names}),text=True,capture_output=True,check=True)
original=json.loads(result.stdout);data=copy.deepcopy(original)
spec=importlib.util.spec_from_file_location('edition_data',HERE/'edit_data.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
data=module.apply(data)
for part in data['PARTS']:part['tag']=part['title']
for source in data['SOURCES']:source['description']=source.get('note',source['description'])

class Renderer(mistune.HTMLRenderer):
    def block_code(self,code,info=None):
        if (info or '').strip()=='prompt':
            return '<div class="prompt-box"><div class="prompt-top"><span>Instructions to adapt</span><button class="text-btn" data-copy-parent=".prompt-box">Copy instructions</button></div><pre>'+html.escape(code.strip())+'</pre></div>\n'
        return super().block_code(code,info)
md=mistune.create_markdown(renderer=Renderer(escape=False))
references={
 'ethics':[{'title':'ABA Formal Opinion 512 (2024)','url':'https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf'}],
 'basics':[{'title':'Anthropic: Effective context engineering for AI agents','url':'https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents'}],
 'harness':[{'title':'Anthropic: Effective context engineering for AI agents','url':'https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents'}],
 'graphing':[{'title':'Anthropic: Building effective agents','url':'https://www.anthropic.com/engineering/building-effective-agents'}],
 'agents':[{'title':'Anthropic: Building effective agents','url':'https://www.anthropic.com/engineering/building-effective-agents'}],
 'process':[{'title':'NIST AI Risk Management Framework','url':'https://www.nist.gov/itl/ai-risk-management-framework'}],
 'building':[{'title':'NIST Generative AI Profile','url':'https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence'}],
 'writing':[{'title':'Write.law: Level up your law','url':'https://write.law/blog/level-up-your-law'},{'title':'Write.law: The power of words','url':'https://write.law/blog/power-of-words'}],
 'aiisms':[{'title':'Write.law: The quest to take legal writing from art to science','url':'https://write.law/blog/the-quest-to-take-legal-writing-from-art-to-science'}]
}
inventory=[]
for chapter,old in zip(data['CHAPTERS'],original['CHAPTERS']):
    file=HERE/'chapters'/(chapter['id']+'.md');source=file.read_text()
    header,_,body=source.partition('\n## ')
    title=re.search(r'^# (.+)$',header,re.M).group(1)
    desc=re.search(r'^> (.+)$',header,re.M).group(1)
    nav=re.search(r'^@nav (.+)$',header,re.M).group(1)
    parts=re.split(r'(?m)^## ', '## '+body)
    sections=[]
    for section in parts[1:]:
        heading,_,prose=section.partition('\n')
        # Use an HTML block so the markdown renderer does not wrap a widget in a paragraph.
        prose=re.sub(r'\{\{widget:([a-z]+)\}\}',r'<div data-widget="\1"></div>',prose)
        sections.append({'h':heading.strip(),'html':md(prose.strip())})
    assert len(sections)==len(old['sections']),f'Section count changed for {chapter["id"]}'
    for a,b in zip(old['sections'],sections):
        assert re.findall(r'data-widget="([^"]+)"',a['html'])==re.findall(r'data-widget="([^"]+)"',b['html']),f'Widget moved in {chapter["id"]}'
        assert re.findall(r'data-save="([^"]+)"',a['html'])==re.findall(r'data-save="([^"]+)"',b['html']),f'Saved field changed in {chapter["id"]}'
    chapter.update(title=title,nav=nav,desc=desc,sections=sections,references=references.get(chapter['id'],[]))
    inventory.append({'id':chapter['id'],'title':title,'sections':len(sections),'words':len(re.findall(r'\b[\w’\'-]+\b',source))})

# Complete resource guidance is retained, with course-only framing removed.
g=data['RESOURCE_GUIDANCE']
g['workorder']['first']='Work through the assignment and the authority the agent needs. The question-mark buttons give examples for the twelve fields.'
g['aiisms']['need']='A deliberately weak practice passage is supplied. There is no document-upload step.'
g['process']['need']='Bring a familiar process you can describe without sensitive information. A fictional intake process is one example.'
data['AREA_HELP']['read']['body']='<p>The page contents link to each section. Use the chapter controls to save a note, mark your progress, or bookmark the reading.</p><p>An activity in the chapter and its separate page share the same response. The chapter question reveals a prepared explanation; it is for your own review, not a grade. Source notes appear at the end of the chapter.</p>'
for group in data['REFLECTIONS']:
    group['source']=group['source'].replace('Fall guide','AI-enabled lawyering').replace('Student guide','AI foundations')

# Preserve source passages and material conditions exactly, including intentionally weak prose.
for key in ['FEE_ORIGINAL','PRIORITY_FACTS','PRIORITY_OPTIONS','AIISM_TEXT','ORDER_PRESET']:
    assert data[key]==original[key],key+' changed'
for key in ['STONEBRIDGE','FALCON']:
    for field in ['original','revision','checks']:
        assert data[key][field]==original[key][field],key+'.'+field+' changed'
for key in ['CHAPTERS','LABS','PROMPTS']:
    assert [x['id'] for x in data[key]]==[x['id'] for x in original[key]],key+' IDs changed'
assert [g['questions'] for g in data['REFLECTIONS']]==[g['questions'] for g in original['REFLECTIONS']],'Reflection question ordering changed'
assert len(data['CHAPTERS'])==16 and sum(len(c['sections']) for c in data['CHAPTERS'])==84

js=lambda name:'const '+name+' = '+json.dumps(data[name],ensure_ascii=False,indent=2)+';\n'
scripts[0]='/* Write.law public edition: chapter text and source notes. */\n'+''.join(js(n) for n in ['SOURCES','PARTS','CHAPTERS'])
extra_names=re.findall(r'(?m)^const (\w+)\s*=',scripts[1]);assert set(extra_names).issubset(data)
scripts[1]='/* Write.law public edition: reference and practice data. */\n'+''.join(js(n) for n in extra_names)
guidance_tail=scripts[2][scripts[2].index('function helpButton'):]
scripts[2]=''.join(js(n) for n in ['RESOURCE_GUIDANCE','AREA_HELP','FIELD_EXAMPLES'])+guidance_tail

# Rewrite display strings without changing action names or saved keys.
widget_replacements={
 'Based on the Fall guide, pp. 5–6, and the semester checklist. The explanation follows your selected answers and is not legal authorization.':'The before-use questions come from Joe Regalia’s responsible-use teaching. The explanation follows your selections; it does not approve the use.',
 'The five questions come from the semester checklist, p. 2. Its reference to research with science students does not establish the same effect in law school.':'This is a suggested self-assessment practice. Four minutes is not an established threshold for legal performance. See the source notes for the limits of the classroom research.',
 'The questions correspond to the twelve work-order fields in the Fall guide. Use the question-mark buttons for examples. Your answers prepare instructions; actual permissions must be set in the application that will perform the work.':'Use the question-mark buttons for examples of the twelve assignment fields. Your answers prepare instructions; permissions must be configured in the application that will perform the work.',
 'The twelve fields come from the Fall guide, p. 11. The vendor example was written for the workflow exercise. This form does not launch an agent or implement approval controls.':'This form prepares an assignment. It does not launch an agent or implement approval controls. The vendor preset is a fictional example.',
 'The nine stages follow the Fall guide, pp. 12–13. The form and sequence display were created for this platform. The proposal still needs appropriate review and testing.':'The form records your proposed process and repeats the sequence you enter. The proposal still needs appropriate review and testing.',
 'The six review areas come from the Fall guide, p. 15. Completing this worksheet is not a legal, security, or deployment certification.':'The six areas organize your review. Completing this worksheet is not a legal, security, or deployment certification.',
 'The six areas come from the Fall guide, p. 16. Entries save in this browser. Download a backup from My saved work to restore them elsewhere.':'Entries save in this browser. Download a backup from My saved work to restore them elsewhere.',
 'Semester reflection':'Continuing reflection',
 'Write in the field for the current part of the semester and leave the others for later. Each question has separate saved answers; changing the selection does not erase an earlier response.':'Write your current view, then return after relevant experience. Each question has separate saved answers; changing the selection does not erase an earlier response.',
 'This collection includes the Fall guide’s twelve questions and adapted selections from the Student guide’s five discussion areas. The questions are intended for reflection, not as settled answers.':'These questions are adapted from Joe Regalia’s teaching materials. They invite reflection and discussion; they do not have an answer key.',
 "[['start','At the start'],['mid','At the midpoint'],['end','At the end']]":"[['start','My initial view'],['mid','After relevant experience'],['end','A later reflection']]",
 '`${t}: my view`':'t',
 'Based on the companion graphing guide and the Fall guide, pp. 10–14. Evidence variations are fictional teaching material. The diagram itself does not implement software permissions.':'This is a fictional teaching demonstration. Evidence variations and responses are prepared examples. The diagram does not implement permissions in another application.',
 'The order follows slide 8 of Skills & AI-isms. Explanations and sample instructions were written for this guide. These practices are separate from the five-stage responsible-use framework.':'These collaboration practices help with individual exchanges. The five-stage responsible-use process covers the broader assignment; the related chapter explains the difference.',
 'Adapted from Skills & AI-isms, pp. 15–39, and the semester checklist. The form assembles text; it does not run AI or evaluate the prompt. Current fields save automatically, and “Save this version” keeps one separate snapshot.':'The form assembles text; it does not run AI or evaluate the prompt. Current fields save automatically, and “Save this version” keeps a separate copy.',
 'a permitted tool, a classmate, or a later review':'a permitted tool, a colleague or classmate, or a later review',
 'A law student developing rule synthesis, application, and source-reading skills.':'A lawyer or law student practicing how to interpret sources and apply a rule.'
}
for old,new in widget_replacements.items():
    assert old in scripts[3], 'Expected widget wording not found: '+old[:75]
    scripts[3]=scripts[3].replace(old,new)
app_replacements={
 'they are not submitted to your instructor or sent to an AI model.':'they are not sent to Write.law, an instructor, an employer, or an AI model.',
 'Professor Joe Regalia':'Joe Regalia · Write.law',
 'They are not legal advice or instructor approval.':'They are not legal advice or approval of an AI use.',
 "'my-ai-lawyering-notes.txt'":"'WriteLaw-AI-Guide-Notes.txt'",
 "'ai-field-guide-backup.json'":"'WriteLaw-AI-Guide-Backup.json'"
}
for old,new in app_replacements.items():
    scripts[4]=scripts[4].replace(old,new)
# Keep the internal import identifier regalia-ai-field-guide and APP_KEY untouched.
scripts[4]=scripts[4].replace(' · The AI-Enabled Lawyer`;',' · Write.law AI Guide`;')

# Each replacement is a full, top-level function. Check the exact function boundary.
ui=(HERE/'ui.js').read_text()
starts=list(re.finditer(r'(?m)^function (\w+)\(',ui))
for i,match in enumerate(starts):
    block=ui[match.start():starts[i+1].start() if i+1<len(starts) else len(ui)].strip()
    name=match.group(1);target=2 if name=='resourceIntro' else 4
    old=re.search(r'(?m)^function '+re.escape(name)+r'\(',scripts[target]);assert old,'Missing function '+name
    boundary=re.search(r'(?m)^(?:function |async function |const |let |document\.|window\.|initHelp\()',scripts[target][old.end():])
    end=old.end()+boundary.start() if boundary else len(scripts[target])
    previous=scripts[target][old.start():end].rstrip()
    assert previous.endswith('}'), 'Unsafe function boundary for '+name
    scripts[target]=scripts[target][:old.start()]+block+'\n'+scripts[target][end:]

logo_file=HERE/'assets/writelaw-logo.png';logo_file.parent.mkdir(exist_ok=True)
if not logo_file.exists():
    with urllib.request.urlopen(LOGO_URL,timeout=40) as response:
        assert response.status==200
        logo_file.write_bytes(response.read(100000))
logo=logo_file.read_bytes();assert hashlib.sha256(logo).hexdigest()==LOGO_SHA,'Official logo changed'
logo_uri='data:image/png;base64,'+base64.b64encode(logo).decode()
scripts=[s.replace('__WRITELAW_LOGO__',logo_uri) for s in scripts]
# Replace decorative green colors; semantic warning/error colors remain intact.
color_map={'#244b3d':'#2255ff','#15382e':'#080a36','#d8edab':'#dde5ff','#233b33':'#080a36','#66746a':'#616784','#dce2d6':'#dce1ee','#edf2e5':'#eef2ff','#f7f7f1':'#f7f8fc','#fffef9':'#ffffff','#173628':'#080a36','#1e4034':'#080a36','#193b2c':'#080a36','#e8f0da':'#eef2ff','#c0d7b1':'#bacaff','#c1d3c5':'#bacaff','#f2f5e7':'#f5f7ff','#bccfbd':'#b6bfd8'}
css=styles[0]
for old,new in color_map.items():css=css.replace(old,new)
css+='\n'+(HERE/'edition.css').read_text().replace('--sidebar:274px','--side:274px')
# Metadata and the shell are edited separately from the preserved behavior.
shell=text
shell=re.sub(r'<style>[\s\S]*?</style>','<link rel="stylesheet" href="style.css">',shell,count=1)
script_files=['content.js','extras.js','guidance.js','widgets.js','app.js']
iterator=iter(script_files)
shell=re.sub(r'<script>[\s\S]*?</script>',lambda m:'<script src="'+next(iterator)+'"></script>',shell)
shell=shell.replace('<meta name="theme-color" content="#244b3d">','<meta name="theme-color" content="#2255ff">')
shell=re.sub(r'<meta name="description"[^>]+>','<meta name="description" content="A Write.law guide by Joe Regalia for lawyers and law students. Work through legal examples, improve AI-assisted writing, and plan assignments you can review.">',shell)
shell=re.sub(r'<meta property="og:title"[^>]+>','<meta property="og:title" content="The AI-Enabled Lawyer | Write.law">',shell)
shell=re.sub(r'<meta property="og:description"[^>]+>','<meta property="og:description" content="Joe Regalia’s guide to using AI in legal work, with explained exercises and practical worksheets for lawyers and law students.">',shell)
shell=re.sub(r'<title>.*?</title>','<title>The AI-Enabled Lawyer | Write.law</title>',shell,count=1)
shell=shell.replace('%23244b3d','%232255ff').replace('%23d8edab','%23ffffff')
shell=shell.replace('Opening the field guide…','Opening the Write.law guide…').replace('Search the field guide','Search the Write.law guide')
shell=shell.replace('This interactive field guide needs JavaScript','This Write.law guide needs JavaScript')
(MODULES/'index.html').write_text(shell)
(MODULES/'style.css').write_text(css)
for filename,script in zip(script_files,scripts):
    (MODULES/filename).write_text(script)
    subprocess.run(['node','--check',str(MODULES/filename)],check=True,capture_output=True,text=True)
final=shell.replace('<link rel="stylesheet" href="style.css">','<style>'+css+'</style>')
for filename,script in zip(script_files,scripts):
    final=final.replace('<script src="'+filename+'"></script>','<script>'+script.replace('</script','<\\/script')+'</script>')
assert '__WRITELAW_LOGO__' not in final and '{{widget:' not in final
assert "const APP_KEY='regalia-field-guide.v1'" in final
assert "raw.app!=='regalia-ai-field-guide'" in final
assert 'for law students</span>' not in final and 'Semester reflection' not in final
(OUT/'index.html').write_text(final)
(OUT/'vercel.json').write_text(json.dumps({'headers':[{'source':'/(.*)','headers':[{'key':'Cache-Control','value':'public, max-age=0, must-revalidate'}]}]},indent=2))
report={'edition':'Write.law public edition','author':'Joe Regalia','baseSha256':BASE_SHA,'sha256':hashlib.sha256(final.encode()).hexdigest(),'bytes':len(final.encode()),'chapterCount':len(inventory),'sectionCount':sum(c['sections'] for c in data['CHAPTERS'] if False) if False else 84,'wordCount':sum(c['words'] for c in inventory),'chapters':inventory,'exerciseSourcePassagesPreserved':True,'chapterSectionAddressesPreserved':True,'savedStateFormatPreserved':True,'chapterIds':[c['id'] for c in data['CHAPTERS']],'activityIds':[l['id'] for l in data['LABS']],'glossaryTerms':len(data['GLOSSARY']),'deploymentStatus':'not-published-by-this-build'}
(OUT/'release.json').write_text(json.dumps(report,indent=2))
(HERE/'edited-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['chapters','chapterIds','activityIds']},indent=2))
