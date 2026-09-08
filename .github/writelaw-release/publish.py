"""One-use publication to the original, already shared Vercel address.
Only the named project and its existing alias may be changed. Auth files and
CLI transcripts are never committed or uploaded. No domains are purchased.
"""
from pathlib import Path
from urllib.parse import urlencode,quote,urlsplit,parse_qs
import base64,datetime,hashlib,json,os,re,select,shutil,subprocess,tempfile,time,urllib.error,urllib.request

REPO='Writedotlaw/lawyer-prompt-studio-previews'
BRANCH='writelaw-public-edition-20260908'
PROJECT='prj_SKkHjbAtHdWQhjnfov6foMH3UVNM'
PROJECT_NAME='regalia-ai-field-guide'
TEAM='team_FXURc9T9dJtajS46bqouoGxa'
HOST='regalia-ai-field-guide-joe-regalias-projects.vercel.app'
URL='https://'+HOST+'/'
EXPECTED=os.environ['APPROVED_GUIDE_SHA']
BASE_SHA='be11c3d012c00f81404f7374910b42d3d3a29ac1524037fa46d06076f608bb96'
STATUS_PATH='.github/writelaw-release/status.json'
OUT=Path(__file__).resolve().parent/'results';OUT.mkdir(exist_ok=True)
AUTH=Path(tempfile.mkdtemp(prefix='writelaw-vercel-auth-',dir=os.environ['RUNNER_TEMP']));AUTH.chmod(0o700)
CLI=os.environ['VERCEL_CLI'];TOKEN=None;LOGIN=None
STATE={'edition':'Write.law public edition','originalUrl':URL,'originalUrlUpdated':False,'projectId':PROJECT,'teamId':TEAM,'sourceSha256':EXPECTED,'runId':os.environ['GITHUB_RUN_ID'],'runUrl':'https://github.com/'+REPO+'/actions/runs/'+os.environ['GITHUB_RUN_ID']}
class Failure(Exception):pass
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):return None
http=urllib.request.build_opener(NoRedirect())
def request(url,method='GET',body=None,token=None):
    headers={'Accept':'application/json','Content-Type':'application/json','User-Agent':'WriteLaw-Authorized-Publication'}
    if token:headers['Authorization']='Bearer '+token
    if url.startswith('https://api.github.com/'):headers['X-GitHub-Api-Version']='2022-11-28'
    req=urllib.request.Request(url,data=json.dumps(body).encode() if body is not None else None,headers=headers,method=method)
    try:
        with http.open(req,timeout=90) as response:
            raw=response.read(5000000);return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as error:
        raise Failure(method+' '+urlsplit(url).path+' returned HTTP '+str(error.code)) from None

def status(stage,**values):
    STATE.update(values);STATE.update(stage=stage,updatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
    if stage!='awaiting_vercel_approval':
        for key in ['verificationUrl','userCode','approvalNote']:STATE.pop(key,None)
    content=json.dumps(STATE,indent=2);(OUT/'status.json').write_text(content)
    endpoint='https://api.github.com/repos/'+REPO+'/contents/'+STATUS_PATH
    for attempt in range(3):
        old=None
        try:old=request(endpoint+'?ref='+quote(BRANCH),token=os.environ['GH_STATUS_TOKEN']).get('sha')
        except Failure as error:
            if 'HTTP 404' not in str(error):raise
        body={'message':'Write.law publication status: '+stage,'branch':BRANCH,'content':base64.b64encode(content.encode()).decode()}
        if old:body['sha']=old
        try:request(endpoint,'PUT',body,os.environ['GH_STATUS_TOKEN']);break
        except Failure as error:
            if 'HTTP 409' not in str(error) or attempt==2:raise
    print('STATUS: '+stage,flush=True)

def api(path,method='GET',body=None,extra=None):
    params={'teamId':TEAM};params.update(extra or {})
    return request('https://api.vercel.com'+path+'?'+urlencode(params),method,body,TOKEN)

def public_digest():
    try:
        req=urllib.request.Request(URL,headers={'Cache-Control':'no-cache','User-Agent':'WriteLaw-Public-Verification'})
        with http.open(req,timeout=30) as response:
            body=response.read(2000000)
            if response.status!=200 or response.url!=URL or 'text/html' not in response.headers.get('Content-Type',''):return None
            return hashlib.sha256(body).hexdigest()
    except (OSError,urllib.error.URLError):return None

def login():
    global TOKEN,LOGIN
    status('starting_direct_vercel_sign_in')
    env=os.environ.copy();env.update(CI='true',NO_COLOR='1',FORCE_COLOR='0',VERCEL_TELEMETRY_DISABLED='1');env.pop('DEBUG',None)
    LOGIN=subprocess.Popen([CLI,'login','--global-config',str(AUTH)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=env)
    transcript='';shown=False;deadline=time.monotonic()+900
    while time.monotonic()<deadline:
        ready,_,_=select.select([LOGIN.stdout],[],[],1)
        if ready:
            block=os.read(LOGIN.stdout.fileno(),8192)
            if block:
                transcript=(transcript+block.decode('utf-8','replace'))[-40000:]
                if not shown:
                    for candidate in re.findall(r'https://vercel\.com/[^\s\x00-\x20\x7f\x1b<>]+',transcript):
                        candidate=candidate.rstrip(').,');parsed=urlsplit(candidate);code=parse_qs(parsed.query).get('user_code',[''])[0]
                        if parsed.hostname=='vercel.com' and parsed.path.startswith('/oauth/device') and re.fullmatch(r'[A-Za-z0-9-]{4,30}',code):
                            status('awaiting_vercel_approval',verificationUrl=candidate,userCode=code,approvalNote='Approve the Vercel CLI sign-in for the temporary deployment runner. It will update only the existing guide project and original address.')
                            shown=True;break
            elif LOGIN.poll() is not None:break
        if LOGIN.poll() is not None:break
    if LOGIN.poll() is None:
        LOGIN.terminate();LOGIN.wait(timeout=10);raise Failure('The direct sign-in expired before approval. The existing site is unchanged.')
    if LOGIN.returncode:raise Failure('The Vercel sign-in did not complete. The existing site is unchanged.')
    file=AUTH/'auth.json'
    if not file.exists():raise Failure('The expected temporary authorization was not created.')
    TOKEN=json.loads(file.read_text()).get('token')
    if not isinstance(TOKEN,str) or len(TOKEN)<20:raise Failure('Vercel did not return usable authorization.')
    transcript='';status('authorized_checking_existing_project')

def publish():
    source=Path('public-edition/dist/index.html').read_bytes()
    if hashlib.sha256(source).hexdigest()!=EXPECTED:raise Failure('The source does not match the reviewed release. Nothing was deployed.')
    project=api('/v9/projects/'+PROJECT)
    if project.get('id')!=PROJECT or project.get('name')!=PROJECT_NAME or project.get('accountId')!=TEAM:raise Failure('The existing project identity did not match. No replacement will be created.')
    alias=api('/v4/aliases/'+HOST,extra={'projectId':PROJECT})
    if alias.get('alias')!=HOST or alias.get('projectId',PROJECT)!=PROJECT:raise Failure('The shared address does not belong to the verified project.')
    old=alias.get('deploymentId') or (alias.get('deployment') or {}).get('id')
    if not old:raise Failure('The current deployment could not be identified.')
    existing=api('/v13/deployments/'+quote(old,safe=''))
    if (existing.get('projectId') or (existing.get('project') or {}).get('id'))!=PROJECT:raise Failure('The current address resolves to another project.')
    digest=public_digest()
    if digest not in [BASE_SHA,EXPECTED]:raise Failure('The current public site differs from the edition reviewed for this update. No publication was attempted.')
    status('publishing_to_existing_project',previousDeploymentId=old)
    config=Path('public-edition/dist/vercel.json').read_text()
    deployment=api('/v13/deployments','POST',{'name':PROJECT_NAME,'project':PROJECT,'target':'production','files':[{'file':'index.html','data':source.decode(),'encoding':'utf-8'},{'file':'vercel.json','data':config,'encoding':'utf-8'}],'projectSettings':{'framework':None,'buildCommand':None,'installCommand':None,'outputDirectory':'.','rootDirectory':None},'meta':{'guideEdition':'Write.law public edition','guideRevisionSha256':EXPECTED,'githubVerificationRun':os.environ['GITHUB_RUN_ID']}})
    did=deployment.get('id')
    if not str(did).startswith('dpl_'):raise Failure('Vercel did not return a deployment identifier.')
    status('waiting_for_build',deploymentId=did)
    deadline=time.monotonic()+600
    while time.monotonic()<deadline:
        current=api('/v13/deployments/'+did)
        if (current.get('projectId') or (current.get('project') or {}).get('id'))!=PROJECT:raise Failure('The returned deployment belongs to another project.')
        phase=current.get('readyState') or current.get('status')
        if phase=='READY':break
        if phase in ['ERROR','CANCELED']:raise Failure('The build ended in '+phase+'.')
        time.sleep(5)
    else:raise Failure('The build did not become ready within ten minutes.')
    current_alias=api('/v4/aliases/'+HOST,extra={'projectId':PROJECT})
    if current_alias.get('projectId',PROJECT)!=PROJECT:raise Failure('The original alias changed ownership; publication stopped.')
    current_id=current_alias.get('deploymentId') or (current_alias.get('deployment') or {}).get('id')
    if current_id!=did:api('/v2/deployments/'+did+'/aliases','POST',{'alias':HOST})
    status('verifying_original_url',originalUrlUpdated=True)
    deadline=time.monotonic()+300
    while time.monotonic()<deadline:
        if public_digest()==EXPECTED:break
        time.sleep(5)
    else:raise Failure('The new release is assigned to the original address, but its public contents could not be confirmed.')
    evidence={'previewUrl':URL,'publicUrl':URL,'host':'Vercel','edition':'Write.law public edition','projectId':PROJECT,'deploymentId':did,'originalUrlPreserved':True,'verifiedWithoutLogin':True,'servedSha256':EXPECTED,'servedBytes':len(source)}
    (OUT/'deployment-result.json').write_text(json.dumps(evidence,indent=2))
    status('original_url_content_verified',publicWithoutLogin=True)
    check=Path(__file__).resolve().parent/'check_public_site.py'
    shutil.copyfile('.github/ai-guide-tests/check_public_site.py',check)
    env=os.environ.copy();env.pop('GH_STATUS_TOKEN',None)
    tests=subprocess.run(['python',str(check)],env=env,timeout=300)
    report=OUT/'public-browser-report.json'
    if tests.returncode or not report.exists():raise Failure('The new edition is public at the original address, but a browser check needs attention.')
    result=json.loads(report.read_text())
    if result.get('failed')!=0:raise Failure('The release is public, but browser checks reported a failure.')
    status('completed_verified_same_url',publicWithoutLogin=True,browserChecksPassed=result['passed'],browserChecksFailed=0,routeCount=len(result['routes']),customDomainChanged=False)

try:
    if os.environ.get('GITHUB_REPOSITORY')!=REPO or os.environ.get('GITHUB_REF_NAME')!=BRANCH:raise Failure('The publication job was started outside its authorized repository or branch.')
    if not re.fullmatch('[a-f0-9]{64}',EXPECTED):raise Failure('The approved release digest is missing or invalid.')
    if hashlib.sha256(Path('public-edition/dist/index.html').read_bytes()).hexdigest()!=EXPECTED:raise Failure('The staged guide does not match the approved release.')
    login();publish()
except Exception as error:
    message=str(error) if isinstance(error,Failure) else 'Publication stopped after '+type(error).__name__+'. Review the sanitized runner result.'
    try:status('stopped_requires_attention',failure=message)
    except Exception:print('The status record could not be updated.',flush=True)
    print(message,flush=True);raise SystemExit(1)
finally:
    if LOGIN and LOGIN.poll() is None:LOGIN.terminate()
    if (AUTH/'auth.json').exists():
        try:subprocess.run([CLI,'logout','--global-config',str(AUTH)],stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=20)
        except Exception:pass
    TOKEN=None;shutil.rmtree(AUTH,ignore_errors=True)
