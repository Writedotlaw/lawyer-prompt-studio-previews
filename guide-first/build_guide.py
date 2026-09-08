"""Build the reading-first Write.law edition from the verified public-edition source.
No network access, authentication, or deployment occurs in this build.
"""
from pathlib import Path
import copy,hashlib,html,json,re,subprocess,sys
import mistune
from sections import PATCHES,APPEND
from reference import QUESTION_GROUPS,GLOSSARY_ADDITIONS,COVERAGE,EDITORIAL_NOTES
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
BASE=ROOT/'public-edition/dist/index.html'
EXPECTED_BASE='fff210bd1dfc317c2f80f493e0a30c6c72e55d8cec15c5468e1162776eafe16e'
OUT=HERE/'dist';OUT.mkdir(exist_ok=True)
MODULES=HERE/'editable-site';MODULES.mkdir(exist_ok=True)
base=BASE.read_bytes();assert hashlib.sha256(base).hexdigest()==EXPECTED_BASE,'Baseline differs from the published edition.'
text=base.decode();scripts=re.findall(r'<script>([\s\S]*?)</script>',text);styles=re.findall(r'<style>([\s\S]*?)</style>',text)
assert len(scripts)==5 and len(styles)==1
names=[]
for script in scripts[:3]: names+=re.findall(r'(?m)^const (\w+)\s*=',script)
extract="const vm=require('vm'),fs=require('fs');const x=JSON.parse(fs.readFileSync(0,'utf8'));const c=vm.createContext({});for(const s of x.scripts)vm.runInContext(s,c);const d={};for(const n of x.names)d[n]=vm.runInContext(n,c);console.log(JSON.stringify(d));"
data=json.loads(subprocess.run(['node','-e',extract],input=json.dumps({'scripts':scripts[:3],'names':names}),text=True,capture_output=True,check=True).stdout)
original=copy.deepcopy(data)
esc=lambda x:html.escape(str(x),quote=True)
def paras(t):return ''.join('<p>'+esc(x).replace('\n','<br>')+'</p>' for x in t.split('\n\n'))
def example(title,body,source):return f'<div class="gf-example" data-reading-example="true"><header><h3>{esc(title)}</h3></header><div class="gf-example-body">{body}</div><p class="gf-source-caption">{esc(source)}</p></div>'
def table(caption,headers,rows):
    return '<div class="gf-table-wrap" tabindex="0" role="region" aria-label="'+esc(caption)+'"><table class="gf-reading-table"><caption>'+esc(caption)+'</caption><thead><tr>'+''.join('<th scope="col">'+esc(t)+'</th>' for t in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(cell)+'</td>' for cell in row)+'</tr>' for row in rows)+'</tbody></table></div>'
source_slides='Source: Leveling Up Your AI Prompting, slides '
READ={
 'priority-facts':example('The supplied employee-departure facts',paras(data['PRIORITY_FACTS']),source_slides+'11–13. No controlling law is supplied.'),
 'fee-original':example('Original sentence',paras(data['FEE_ORIGINAL']),source_slides+'20.'),
 'fee-options':example('Compare the different requests', ''.join('<div class="gf-option"><h4>'+esc(o['label'])+'</h4>'+paras(o['text'])+'<p class="gf-explanation">'+esc(o['note'])+'</p></div>' for o in data['FEE_OPTIONS']),source_slides+'21–24. Commentary developed for this guide.'),
 'aiism-passage':example('A deliberately weak passage',paras(data['AIISM_TEXT']),source_slides+'67 and 72. The diagnosis below is prepared commentary, not an authorship determination.')
}
for id,key in [('stonebridge','STONEBRIDGE'),('falcon','FALCON')]:
    slide=56 if id=='stonebridge' else 57
    READ[id+'-original']=example('Original '+('Stonebridge' if slide==56 else 'Falcon Medical')+' passage',paras(data[key]['original']),source_slides+str(slide)+'.')
    READ[id+'-revision']=example('A prepared revision for comparison',paras(data[key]['revision']),'Prepared for this guide from the supplied facts; not an original-source answer key.')
READ['dog-before']=example('Original practice introduction',paras('This action arises from the design, marketing, and sale of a dog toy by Respondent VIP Products. The product at issue is a squeaky chew toy that was made to resemble, in certain respects, a bottle of Jack Daniel’s whiskey, including aspects of the bottle’s label, wording, and overall appearance, even though the toy does not copy the Jack Daniel’s product in every detail or exact particular.\n\nAs part of that design, the toy uses the phrase “Bad Spaniels” in place of the words “Jack Daniel’s,” and it also replaces the phrase “Old No. 7 Brand Tennessee Sour Mash Whiskey” with the phrase “The Old No. 2 On Your Tennessee Carpet,” while otherwise retaining a number of features and design elements that are intended to evoke the Jack Daniel’s bottle and the commercial impression associated with it.\n\nThis case concerns the creation, promotion, and sale of that product and the legal issues alleged to result from the similarities between the toy and the Jack Daniel’s bottle and label.'),source_slides+'40 and 43.')
READ['dog-after']=example('The opinion excerpt supplied in the workshop',paras('This case is about dog toys and whiskey, two items seldom appearing in the same sentence. Respondent VIP Products makes a squeaky, chewable dog toy designed to look like a bottle of Jack Daniel’s whiskey. Though not entirely. On the toy, for example, the words “Jack Daniel’s” become “Bad Spaniels.” And the descriptive phrase “Old No. 7 Brand Tennessee Sour Mash Whiskey” turns into “The Old No. 2 On Your Tennessee Carpet.”'),source_slides+'41; the workshop identifies Justice Elena Kagan’s prose in the following discussion. The excerpt illustrates writing, not a rule for the other examples.')
READ['workflow']=table('A readable version of the fictional vendor-review workflow.', ['Task','What the work produces','What happens next'],[
 ['Define the question','The client’s objective, approved materials, and the decision the work should support.','The lawyer selects the scope before the reviews begin.'],
 ['Review the contract and amendment','A requirements table with the relevant language, exceptions, source locations, and open questions.','These findings go to the comparison, not directly to a final recommendation.'],
 ['Review records and correspondence','A timeline distinguishing established evidence, allegations, disputed facts, and missing information.','It preserves the distinction between sending and receipt.'],
 ['Compare the findings','Each requirement is connected with its supporting evidence or a stated gap.','A material gap returns to the lawyer for a decision.'],
 ['Resolve the next step','The lawyer decides whether to investigate, seek more material, or approve a qualified approach.','New evidence alone does not count as approval.'],
 ['Draft the recommendation','A draft using approved findings and the lawyer’s decisions, with material limits preserved.','The draft goes through a source check and human review.'],
 ['Check and approve','Unsupported assertions and lost qualifications are corrected; the lawyer decides what may be used.','A material problem returns the affected work for correction.'],
 ['Revisit when evidence changes','The timeline, comparison, and recommendation are reconsidered as needed.','Reviewed work is reused only where the change does not undermine it.']])
labels=['Client outcome','Assignment and scope','Inputs and trusted sources','Tools and permissions','Deliverable','Quality standard','Evidence requirement','Prohibited behavior','Escalation triggers','Human approval points','Test set','Record and version']
READ['workorder']='<dl class="gf-workorder">'+''.join('<dt>'+str(i+1)+'. '+esc(label)+'</dt><dd>'+esc(data['ORDER_FIELDS'][i][2])+'</dd>' for i,label in enumerate(labels))+'</dl><p class="gf-source-caption">Source: The AI-Enabled Lawyer, p. 11. The labels retain the source framework; the explanations adapt it for this guide.</p>'
READ['workorder-example']=example('A worked assignment for the fictional vendor matter',''.join('<div class="gf-option"><h4>'+esc(label)+'</h4>'+paras(data['ORDER_PRESET'][data['ORDER_FIELDS'][i][0]])+'</div>' for i,label in enumerate(labels)), 'Prepared example developed for the workflow guide. It does not configure a tool or authorize a live use.')
class Renderer(mistune.HTMLRenderer):
    def block_code(self,code,info=None):
        if (info or '').strip()=='prompt':
            return '<div class="prompt-box"><div class="prompt-top"><span>Example instructions</span><button class="text-btn" data-copy-parent=".prompt-box">Copy instructions</button></div><pre>'+esc(code.strip())+'</pre></div>\n'
        return super().block_code(code,info)
md=mistune.create_markdown(renderer=Renderer(escape=False))
def compile_markdown(s):
    # Expand the readable blocks before parsing, using block HTML rather than nested paragraphs.
    s=re.sub(r'\{\{read:([a-z-]+)\}\}',lambda m:'\n'+READ[m[1]]+'\n',s)
    return md(s)
changed=[]
for c in data['CHAPTERS']:
    before=copy.deepcopy(c['sections']);cid=c['id']
    for idx,patch in PATCHES.get(cid,{}).items():
        c['sections'][idx]={'h':patch['h'],'html':compile_markdown(patch['markdown'])}
    for idx,addition in APPEND.get(cid,{}).items(): c['sections'][idx]['html']+='\n'+compile_markdown(addition)
    for idx,sec in enumerate(c['sections']):
        assert '{{' not in sec['html'], (cid,idx,'unexpanded placeholder')
        assert not re.search(r'data-widget=|<textarea|<select|data-save=',sec['html']), (cid,idx,'activity remains in reading')
        # The section addresses remain stable even when the heading is developed.
        if sec!=before[idx]:changed.append({'chapter':cid,'section':idx,'title':sec['h']})
    assert len(c['sections'])==len(before)
    if cid=='method':c['desc']='Your own skills give the exchange direction. These six practices explain how to develop alternatives, challenge an idea, and improve the work across more than one response.'
    if cid=='lawyer':c['desc']='AI gives us more ways to work with legal knowledge. Our contribution is deciding what deserves attention, how the assistance should be used, and what will help the person behind the problem.'
    if cid=='writing':c['desc']='Learn how to direct and evaluate a revision through complete worked examples, from a fee-table sentence to a client recommendation. The writing choices and their consequences are visible before any optional practice.'
    if cid=='ethics':
        c.setdefault('references',[]).append({'title':'ABA Model Rule 5.2: Responsibilities of a Subordinate Lawyer','url':'https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_5_2_responsibilities_of_a_subordinate_lawyer/'})
    # Normalize old instructions referring to widgets no longer embedded in reading.
    for s in c['sections']:
        s['html']=s['html'].replace('Use the <a href="#/lab/process">process worksheet</a> to plan an assignment of your own.','The optional <a href="#/lab/process">process worksheet</a> helps you plan an assignment of your own.')
for c in data['CHAPTERS']:
    if c['id']=='think':c['sources']=[['fall','pp. 6–9'],['student','pp. 11–12'],['short','p. 2'],['slides','pp. 8–13']]
    if c['id']=='writing':c['sources']=[['slides','pp. 20–24, 40–57, 78–87']]
    if c['id']=='prompting':c['sources']=[['slides','pp. 14–19, 32–39'],['student','pp. 5–6']]
    if c['id']=='agents':c['sources']=[['fall','pp. 10–11'],['student','p. 8']]
    if c['id']=='leadership':c['sources']=[['fall','pp. 1–3, 17–18'],['student','pp. 13–19']]
    if c['id']=='basics':c['sources']=[['student','pp. 2–10, 19–22']]
for entry in GLOSSARY_ADDITIONS:
    assert entry[0] not in [x[0] for x in data['GLOSSARY']]
    data['GLOSSARY'].append(entry)
data['GLOSSARY'].sort(key=lambda x:x[0].lower())
for p in data['PARTS']:
    if p['name']=='Foundations':p['desc']='How lawyers add value, how the tools work, and how to protect independent judgment while choosing a responsible use.'
    if p['name']=='Systems':p['desc']='The working methods for prompting, legal writing, source management, workflows, and supervision of AI agents.'
    if p['name']=='Building':p['desc']='How legal insight can improve a service and become a useful tool, with testing before anyone depends on it.'
    if p['name']=='Leadership':p['desc']='How to preserve what we learn, develop people, and decide what AI should change about the profession.'
for k in ['home','chapters','read']:
    data['AREA_HELP'][k]['body']='<p>The chapters contain the complete guidance and worked examples. You can read them without filling in a form, choosing an answer, or opening an exercise.</p><p>The full chapter list is available in the navigation on every page and on the contents page. Optional exercises, worksheets, and saved notes support the guide. They retain their earlier addresses and saved responses.</p>'
data['AREA_HELP']['home']['tip']='Browse the complete guide. Exercises and worksheets are optional companions.'
data['AREA_HELP']['chapters']['title']='Read the guide in order or by subject'
data['AREA_HELP']['read']['tip']='The full explanation is in the reading. Optional practice and notes follow the chapter.'
data['AREA_HELP']['questions']={'title':'Questions for the profession','tip':'Read the full set of open questions from the source guides.','body':'<p>These are questions to keep thinking about, not settled legal conclusions or a quiz. All subjects are readable without writing a response. The optional reflection worksheet retains your earlier saved answers.</p>'}
# Safe serialization for inline script elements.
def const(n,v):return 'const '+n+' = '+json.dumps(v,ensure_ascii=False,indent=2).replace('</script','<\\/script')+';\n'
scripts[0]='/* Write.law guide-first edition: complete reading and source-grounded references. */\n'+''.join(const(n,data[n]) for n in ['SOURCES','PARTS','CHAPTERS'])+const('READING_QUESTIONS',QUESTION_GROUPS)+const('SOURCE_COVERAGE',COVERAGE)+const('EDITORIAL_DECISIONS',EDITORIAL_NOTES)
extra_names=re.findall(r'(?m)^const (\w+)\s*=',scripts[1]);scripts[1]=''.join(const(n,data[n]) for n in extra_names)
gnames=re.findall(r'(?m)^const (\w+)\s*=',scripts[2][:scripts[2].index('function helpButton')]);tail=scripts[2][scripts[2].index('function helpButton'):];scripts[2]=''.join(const(n,data[n]) for n in gnames)+tail
logo=re.search(r'data:image/png;base64,[A-Za-z0-9+/=]+',scripts[4]).group()
ui=(HERE/'reading-ui.js').read_text().replace('__LOGO__',logo)

def bounds(script,name):
    m=re.search(r'(?m)^function '+re.escape(name)+r'\(',script)
    if not m:return None
    b=re.search(r'(?m)^(?:function |async function |const |let |document\.|window\.|initHelp\()',script[m.end():]);end=m.end()+b.start() if b else len(script)
    assert script[m.start():end].rstrip().endswith('}'),name
    return m.start(),end
starts=list(re.finditer(r'(?m)^function (\w+)\(',ui));new_functions=[]
for i,m in enumerate(starts):
    block=ui[m.start():starts[i+1].start() if i+1<len(starts) else len(ui)].strip()+'\n'
    name=m.group(1);loc=bounds(scripts[4],name)
    if loc:scripts[4]=scripts[4][:loc[0]]+block+scripts[4][loc[1]:]
    else:new_functions.append(block)
# Insert new declarations before initialization.
scripts[4]='\n'.join(new_functions)+scripts[4]
# New reference route, existing routes untouched.
scripts[4]=scripts[4].replace("['chapters','labs','templates','prompts','glossary','notebook','sources','help']","['chapters','labs','templates','prompts','glossary','notebook','sources','help','questions']")
scripts[4]=scripts[4].replace('sources:renderSources};','sources:renderSources,questions:renderQuestions};')
scripts[4]=scripts[4].replace("sources:'Sources & guide notes'","sources:'Sources & guide notes',questions:'Questions for the profession'")
scripts[4]=scripts[4].replace("sources:'Sources',help:","sources:'Sources',questions:'Questions for the profession',help:")
scripts[4]=scripts[4].replace("home:'Start here',chapters:'Chapters'","home:'About the guide',chapters:'Contents'")
scripts[4]=scripts[4].replace("target?.scrollIntoView({behavior:'instant',block:'start'});","if(target){const holder=target.closest('details');if(holder)holder.open=true;target.scrollIntoView({behavior:'instant',block:'start'});}")
scripts[4]=scripts[4].replace("else if(source)document.getElementById(`source-${source}`)","else if(currentRoute.type==='questions'&&currentRoute.params.has('group'))document.getElementById('questions-'+currentRoute.params.get('group'))?.scrollIntoView({behavior:'instant'});else if(currentRoute.type==='chapters'&&currentRoute.params.has('part'))document.getElementById('part-'+currentRoute.params.get('part'))?.scrollIntoView({behavior:'instant'});else if(source)document.getElementById(`source-${source}`)")
# Teach help to describe the hierarchy accurately.
scripts[4]=scripts[4].replace('Read a chapter to understand a method. Try an exercise with supplied material, or use a template to prepare an assignment of your own. You can begin wherever the work calls for it.','The chapters contain the complete guidance and worked examples. Read them in order or consult a subject. Exercises, worksheets, and personal notes are optional companions.')
scripts[4]=scripts[4].replace('An exercise inside a chapter and the same exercise on its own page share one saved response.','The chapters now show the worked examples directly. Separate exercises remain optional and keep their earlier saved responses.')
scripts[4]=scripts[4].replace('Why are there exercises inside the chapters and on separate pages?','Where did the exercises embedded in the chapters go?')
scripts[4]=scripts[4].replace('They are two ways to reach the same activity. The chapter lets you practice while reading. The separate page gives you room to focus on the exercise. Both use the same saved response.','The chapter now gives you the full explanation and worked comparison without requiring an attempt. Links after the reading open the optional exercises. Their earlier addresses and saved responses are unchanged.')
scripts[4]=scripts[4].replace('For a focused session, the homepage offers routes through writing, workflow planning, and the decision to use AI.','For a focused session, the homepage and navigation give you the complete chapter list by subject.')
scripts[4]=scripts[4].replace('For an introduction, read the first chapter and follow its links when you reach an activity.','For an introduction, read the first chapter and continue through the guide. You can skip every optional activity and still receive the complete teaching.')
scripts[4]=scripts[4].replace('An activity in the chapter and its separate page share the same response.','The optional activities linked after each chapter preserve their existing saved responses.')
# Readable coverage notes on the sources page, not on every paragraph.
coverage_func='''function renderSourceCoverage(){return `<section class="reference-prose gf-scope-notes" id="guide-source-coverage"><h2>What the guide carries forward from the sources</h2><p>The reading-first revision checks the substantive guidance against all four supplied documents and the original workflow discussion. The entries below identify where that guidance appears without a required activity. The original source documents are not reproduced in full.</p>${SOURCE_COVERAGE.map(r=>`<div class="gf-coverage-row"><small>${esc(r[0])} · ${esc(r[1])}</small><h3>${esc(r[2])}</h3><p>${r[3].split('; ').map(c=>`<a class="inline-link" href="${['questions','glossary','sources'].includes(c)?'#/'+c:'#/read/'+c}">${esc(c==='harness'?'Organize the materials':CHAPTERS.find(x=>x.id===c)?.nav||c)}</a>`).join(' · ')}. ${esc(r[5])}.</p></div>`).join('')}<h2>Editorial distinctions and limits</h2>${EDITORIAL_DECISIONS.map(t=>`<p>${esc(t)}</p>`).join('')}<h3>Further-reading leads retained from the introductory guide</h3><p>The introductory source points to Ethan Mollick’s <em>Co-Intelligence</em> and <em>One Useful Thing</em>, Andrej Karpathy’s lectures, Anthropic’s prompting documentation, the AI Hallucination Cases Database, ABA Formal Opinion 512, and Bob Ambrogi’s <em>LawSites</em>. These are the author’s source reading leads, not a newly verified ranking of current resources.</p></section>`;}\n'''
scripts[4]=coverage_func+scripts[4]
loc=bounds(scripts[4],'renderSources');assert loc
block=scripts[4][loc[0]:loc[1]].replace('${footer()}','${renderSourceCoverage()}${footer()}')
scripts[4]=scripts[4][:loc[0]]+block+scripts[4][loc[1]:]
css=styles[0]+'\n'+(HERE/'reading.css').read_text()
# Keep the exact existing shell, including the same local-storage behavior.
shell=re.sub(r'<style>[\s\S]*?</style>','<link rel="stylesheet" href="style.css">',text,count=1)
files=['content.js','extras.js','guidance.js','widgets.js','app.js'];it=iter(files)
shell=re.sub(r'<script>[\s\S]*?</script>',lambda m:'<script src="'+next(it)+'"></script>',shell)
shell=shell.replace('A Write.law guide by Joe Regalia for lawyers and law students. Work through legal examples, improve AI-assisted writing, and plan assignments you can review.','Joe Regalia’s Write.law guide to AI and legal work. Read the complete guidance on judgment, writing, workflows, and better legal services, with optional practice resources.')
shell=shell.replace('Joe Regalia’s guide to using AI in legal work, with explained exercises and practical worksheets for lawyers and law students.','Joe Regalia’s collected guidance on AI and legal work, with complete explanations and worked examples for lawyers and law students.')
(MODULES/'index.html').write_text(shell);(MODULES/'style.css').write_text(css)
final=shell.replace('<link rel="stylesheet" href="style.css">','<style>'+css+'</style>')
for f,s in zip(files,scripts):
    (MODULES/f).write_text(s)
    subprocess.run(['node','--check',str(MODULES/f)],capture_output=True,text=True,check=True)
    final=final.replace('<script src="'+f+'"></script>','<script>'+s.replace('</script','<\\/script')+'</script>')
assert "const APP_KEY='regalia-field-guide.v1'" in final
assert "raw.app!=='regalia-ai-field-guide'" in final
for key in ['FEE_ORIGINAL','FEE_OPTIONS','STONEBRIDGE','FALCON','PRIORITY_FACTS','PRIORITY_OPTIONS','AIISM_TEXT','ORDER_FIELDS','ORDER_PRESET','REFLECTIONS']:
    assert data[key]==original[key],key+' source or saved reference changed'
assert [x['id'] for x in data['CHAPTERS']]==[x['id'] for x in original['CHAPTERS']]
words=lambda s:len(re.findall(r'\b[\w’\'-]+\b',re.sub('<[^>]+>',' ',s)))
reading_words=sum(words(' '.join(s['html'] for s in c['sections'])) for c in data['CHAPTERS'])
report={'edition':'Write.law reading-first guide','date':'2026-09-08','baseSha256':EXPECTED_BASE,'sha256':hashlib.sha256(final.encode()).hexdigest(),'bytes':len(final.encode()),'chapterCount':len(data['CHAPTERS']),'sectionCount':sum(len(c['sections']) for c in data['CHAPTERS']),'readingWords':reading_words,'changedSections':len(changed),'readingQuestionCount':sum(len(g[2]) for g in QUESTION_GROUPS),'glossaryTerms':len(data['GLOSSARY']),'sourceCoverageEntries':len(COVERAGE),'existingChapterSectionAddressesPreserved':True,'exerciseSourcePassagesPreserved':True,'savedStateFormatPreserved':True,'requiredExercises':0,'chapterWidgets':0,'deployedByThisBuild':False,'chapters':[{'id':c['id'],'title':c['title'],'sections':len(c['sections']),'readingWords':words(' '.join(s['html'] for s in c['sections']))} for c in data['CHAPTERS']]}
(OUT/'index.html').write_text(final);(OUT/'release.json').write_text(json.dumps(report,indent=2))
(OUT/'vercel.json').write_text(json.dumps({'headers':[{'source':'/(.*)','headers':[{'key':'Cache-Control','value':'public, max-age=0, must-revalidate'}]}]},indent=2))
(HERE/'edited-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(HERE/'change-inventory.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2))
audit=['# Write.law reading-first guide: source coverage and editorial decisions','','This audit identifies where the supplied guidance is developed in the reading. It is not a claim that every historical statistic, slide illustration, or placeholder was adopted as current guidance.','',f"The build contains {report['chapterCount']} chapters, {report['sectionCount']} reading sections, {report['readingQuestionCount']} readable questions, and {report['glossaryTerms']} glossary entries. No chapter requires an exercise, form, or quiz.",'','## Coverage','']
for r in COVERAGE:audit += ['### '+r[0]+' · '+r[1],r[2]+'.','Reading: '+r[3]+'; section(s) '+r[4]+'. '+r[5]+'.','']
audit+=['## Editorial decisions and limits','']
for n in EDITORIAL_NOTES:audit +=[n,'']
(HERE/'Source-Coverage.md').write_text('\n'.join(audit))
print(json.dumps({k:v for k,v in report.items() if k!='chapters'},indent=2))
