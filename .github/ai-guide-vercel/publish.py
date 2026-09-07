"""One-use Vercel authorization and publication to the existing student address.
No credentials, device secrets, or CLI transcripts are committed or uploaded.
This script refuses to create a project or move an alias from another project.
"""
from pathlib import Path
from urllib.parse import urlencode, urlsplit, parse_qs, quote
import base64
import datetime
import hashlib
import json
import os
import re
import select
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

REPO = 'Writedotlaw/lawyer-prompt-studio-previews'
BRANCH = 'ai-guide-vercel-direct-20260907'
PROJECT = 'regalia-ai-field-guide'
TEAM = 'joe-regalias-projects'
HOST = 'regalia-ai-field-guide-joe-regalias-projects.vercel.app'
URL = 'https://' + HOST + '/'
EXPECTED = 'be11c3d012c00f81404f7374910b42d3d3a29ac1524037fa46d06076f608bb96'
STATUS_PATH = '.github/ai-guide-vercel/status.json'
OUT = Path(__file__).resolve().parent / 'results'
OUT.mkdir(parents=True, exist_ok=True)
CLI = os.environ['VERCEL_CLI']
AUTH = Path(tempfile.mkdtemp(prefix='ai-guide-vercel-auth-', dir=os.environ['RUNNER_TEMP']))
os.chmod(AUTH, 0o700)
STATE = {'originalUrl': URL, 'projectName': PROJECT, 'teamSlug': TEAM,
         'runId': os.environ['GITHUB_RUN_ID'], 'runUrl': os.environ['GITHUB_SERVER_URL'] + '/' + REPO + '/actions/runs/' + os.environ['GITHUB_RUN_ID'],
         'sourceSha256': EXPECTED, 'originalUrlUpdated': False}
TOKEN = None
TEAM_ID = None
LOGIN_PROCESS = None

class SafeFailure(Exception):
    pass

class APIError(SafeFailure):
    def __init__(self, method, path, code, error_code):
        self.status = code
        super().__init__(f'{method} {path.split(chr(63))[0]} returned HTTP {code} ({error_code})')

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

NO_REDIRECT = urllib.request.build_opener(NoRedirect())

def request_json(url, method='GET', payload=None, token=None):
    headers = {'Accept': 'application/json', 'User-Agent': 'AI-Guide-Authorized-Deployment'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    if url.startswith('https://api.github.com/'):
        headers['X-GitHub-Api-Version'] = '2022-11-28'
    body = None
    if payload is not None:
        body = json.dumps(payload).encode()
        headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with NO_REDIRECT.open(req, timeout=90) as response:
            data = response.read(5000000)
            return json.loads(data) if data else {}
    except urllib.error.HTTPError as exc:
        try:
            info = json.loads(exc.read(20000))
            err = info.get('error', {})
            error_code = err.get('code', 'provider_error') if isinstance(err, dict) else 'provider_error'
        except Exception:
            error_code = 'provider_error'
        raise APIError(method, urlsplit(url).path, exc.code, error_code) from None

def status(stage, **values):
    STATE.update(values)
    STATE.update(stage=stage, updatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
    if stage != 'awaiting_vercel_approval':
        STATE.pop('verificationUrl', None)
        STATE.pop('userCode', None)
    text = json.dumps(STATE, indent=2)
    (OUT / 'status.json').write_text(text)
    endpoint = 'https://api.github.com/repos/' + REPO + '/contents/' + STATUS_PATH
    for attempt in range(2):
        sha = None
        try:
            existing = request_json(endpoint + '?ref=' + quote(BRANCH), token=os.environ['GH_STATUS_TOKEN'])
            sha = existing['sha']
        except APIError as exc:
            if exc.status != 404:
                raise
        body = {'message': 'AI guide Vercel status: ' + stage, 'branch': BRANCH,
                'content': base64.b64encode(text.encode()).decode()}
        if sha:
            body['sha'] = sha
        try:
            request_json(endpoint, 'PUT', body, os.environ['GH_STATUS_TOKEN'])
            print('STATUS: ' + stage, flush=True)
            return
        except APIError as exc:
            if exc.status != 409 or attempt:
                raise

def vercel(path, method='GET', payload=None, extra=None):
    params = {'teamId': TEAM_ID} if TEAM_ID else {'slug': TEAM}
    params.update(extra or {})
    return request_json('https://api.vercel.com' + path + '?' + urlencode(params), method, payload, TOKEN)

def cli_env():
    env = os.environ.copy()
    env.update(CI='true', NO_COLOR='1', FORCE_COLOR='0', VERCEL_TELEMETRY_DISABLED='1')
    env.pop('DEBUG', None)
    return env

def login():
    global TOKEN, LOGIN_PROCESS
    status('starting_direct_vercel_sign_in')
    LOGIN_PROCESS = subprocess.Popen([CLI, 'login', '--global-config', str(AUTH)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=cli_env())
    buffer = ''
    shown = False
    deadline = time.monotonic() + 900
    while time.monotonic() < deadline:
        ready, _, _ = select.select([LOGIN_PROCESS.stdout], [], [], 1)
        if ready:
            block = os.read(LOGIN_PROCESS.stdout.fileno(), 8192)
            if block:
                buffer = (buffer + block.decode('utf-8', 'replace'))[-40000:]
                if not shown:
                    for candidate in re.findall(r'https://vercel\.com/[^\s\x00-\x20\x7f\x1b<>]+', buffer):
                        candidate = candidate.rstrip(').,')
                        parsed = urlsplit(candidate)
                        params = parse_qs(parsed.query)
                        if parsed.hostname == 'vercel.com' and parsed.path.startswith('/oauth/device') and params.get('user_code'):
                            code = params['user_code'][0]
                            if not re.fullmatch(r'[A-Za-z0-9-]{4,30}', code):
                                continue
                            status('awaiting_vercel_approval', verificationUrl=candidate, userCode=code,
                                   note='Approve the Vercel CLI sign-in for this one-use GitHub Actions deployment runner. No project has been changed.')
                            shown = True
                            break
            elif LOGIN_PROCESS.poll() is not None:
                break
        if LOGIN_PROCESS.poll() is not None:
            break
    if LOGIN_PROCESS.poll() is None:
        LOGIN_PROCESS.terminate()
        LOGIN_PROCESS.wait(timeout=10)
        raise SafeFailure('Direct Vercel approval expired before authorization completed. The original project is unchanged.')
    if LOGIN_PROCESS.returncode:
        raise SafeFailure('The official Vercel sign-in did not complete. No project was changed.')
    auth_file = AUTH / 'auth.json'
    if not auth_file.exists():
        raise SafeFailure('Vercel did not save the expected temporary sign-in. No project was changed.')
    auth = json.loads(auth_file.read_text())
    TOKEN = auth.get('token')
    if not isinstance(TOKEN, str) or len(TOKEN) < 20:
        raise SafeFailure('Vercel did not return usable authorization. No project was changed.')
    buffer = ''
    status('authorized_checking_original_project')

def get_deployment(identifier):
    return vercel('/v13/deployments/' + quote(identifier, safe=''))

def deployment_project(d):
    return d.get('projectId') or (d.get('project') or {}).get('id')

def wait_ready(identifier, project_id):
    deadline = time.monotonic() + 600
    while time.monotonic() < deadline:
        data = get_deployment(identifier)
        if deployment_project(data) != project_id:
            raise SafeFailure('Deployment project identity did not match. No alias will be reassigned.')
        phase = data.get('readyState') or data.get('status')
        if phase == 'READY':
            return data
        if phase in ('ERROR', 'CANCELED'):
            raise SafeFailure('Vercel build ended in ' + phase + ': ' + str(data.get('errorCode', 'unknown_build_error')))
        time.sleep(5)
    raise SafeFailure('The original-project deployment did not finish within ten minutes.')

def public_check():
    try:
        req = urllib.request.Request(URL, headers={'Cache-Control': 'no-cache'})
        with NO_REDIRECT.open(req, timeout=30) as response:
            content = response.read(2000000)
            return response.status == 200 and response.url == URL and 'text/html' in response.headers.get('Content-Type', '') and hashlib.sha256(content).hexdigest() == EXPECTED
    except (urllib.error.URLError, OSError):
        return False

def publish():
    global TEAM_ID
    source = Path('ai-guide-revised/index.html').read_bytes()
    if len(source) != 376003 or hashlib.sha256(source).hexdigest() != EXPECTED:
        raise SafeFailure('The approved guide source did not match. No deployment was attempted.')
    project = vercel('/v9/projects/' + PROJECT)
    project_id = project.get('id')
    if project.get('name') != PROJECT or not str(project_id).startswith('prj_'):
        raise SafeFailure('The original named project could not be verified. No replacement project will be created.')
    TEAM_ID = project.get('accountId')
    if not TEAM_ID:
        raise SafeFailure('The original project owner could not be verified.')
    # The alias lookup is explicitly filtered to the original project ID.
    alias = vercel('/v4/aliases/' + HOST, extra={'projectId': project_id})
    if alias.get('alias') != HOST or alias.get('projectId', project_id) != project_id:
        raise SafeFailure('The student address does not belong to the verified project. Publication stopped.')
    old_id = alias.get('deploymentId') or (alias.get('deployment') or {}).get('id')
    if not old_id:
        raise SafeFailure('Could not identify the deployment currently serving the student address.')
    old = get_deployment(old_id)
    if deployment_project(old) != project_id:
        raise SafeFailure('The existing student address resolved to a different project. Publication stopped.')
    if project.get('passwordProtection') or project.get('trustedIps'):
        raise SafeFailure('The existing project has additional access restrictions requiring a separate review; no restrictions were removed.')
    previous = {key: project.get(key) for key in ['id', 'name', 'accountId', 'framework', 'buildCommand', 'installCommand', 'outputDirectory', 'rootDirectory', 'ssoProtection']}
    previous['originalDeploymentId'] = old_id
    (OUT / 'previous-project-settings.json').write_text(json.dumps(previous, indent=2))
    status('publishing_to_original_project', projectId=project_id, teamId=TEAM_ID, previousDeploymentId=old_id)
    config = {'headers': [{'source': '/(.*)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=0, must-revalidate'}]}]}
    deployment = vercel('/v13/deployments', 'POST', {
        'name': PROJECT, 'project': project_id, 'target': 'production',
        'files': [{'file': 'index.html', 'data': source.decode('utf-8'), 'encoding': 'utf-8'},
                  {'file': 'vercel.json', 'data': json.dumps(config), 'encoding': 'utf-8'}],
        'projectSettings': {'framework': None, 'buildCommand': None, 'installCommand': None,
                            'outputDirectory': '.', 'rootDirectory': None},
        'meta': {'guideRevisionSha256': EXPECTED, 'githubVerificationRun': os.environ['GITHUB_RUN_ID']}
    })
    deployment_id = deployment.get('id')
    if not str(deployment_id).startswith('dpl_'):
        raise SafeFailure('Vercel did not return a deployment ID. Publication is not verified.')
    status('waiting_for_original_project_build', deploymentId=deployment_id)
    wait_ready(deployment_id, project_id)
    # Add only the previously verified student address as a production domain.
    domain_path = '/v9/projects/' + project_id + '/domains/' + HOST
    try:
        domain = vercel(domain_path)
    except APIError as exc:
        if exc.status != 404:
            raise
        domain = vercel('/v10/projects/' + project_id + '/domains', 'POST', {'name': HOST})
    if domain.get('projectId') != project_id or domain.get('verified') is not True:
        raise SafeFailure('Vercel did not verify the original hostname as a domain of the same project.')
    if domain.get('gitBranch') or domain.get('redirect') or domain.get('customEnvironmentId'):
        domain = vercel(domain_path, 'PATCH', {'gitBranch': None, 'redirect': None, 'customEnvironmentId': None})
    current_alias = vercel('/v4/aliases/' + HOST, extra={'projectId': project_id})
    current_id = current_alias.get('deploymentId') or (current_alias.get('deployment') or {}).get('id')
    if current_id != deployment_id:
        vercel('/v2/deployments/' + deployment_id + '/aliases', 'POST', {'alias': HOST})
    # Keep preview protection; make only production domains public for students.
    if (project.get('ssoProtection') or {}).get('deploymentType') == 'all':
        vercel('/v9/projects/' + project_id, 'PATCH', {'ssoProtection': {'deploymentType': 'prod_deployment_urls_and_all_previews'}})
    status('verifying_original_student_url', originalUrlUpdated=True)
    deadline = time.monotonic() + 300
    while time.monotonic() < deadline:
        if public_check():
            break
        time.sleep(5)
    else:
        raise SafeFailure('The new deployment is assigned to the original URL, but public access or the exact content could not be verified.')
    result = {'previewUrl': URL, 'publicUrl': URL, 'host': 'Vercel', 'projectId': project_id,
              'deploymentId': deployment_id, 'originalUrlPreserved': True,
              'verifiedWithoutLogin': True, 'servedSha256': EXPECTED, 'servedBytes': len(source)}
    (OUT / 'deployment-result.json').write_text(json.dumps(result, indent=2))
    status('original_url_public_content_verified', publicWithoutLogin=True)
    test = Path('.github/ai-guide-tests/check_public_site.py')
    copied = Path(__file__).resolve().parent / 'check_public_site.py'
    shutil.copyfile(test, copied)
    environment = os.environ.copy()
    environment.pop('GH_STATUS_TOKEN', None)
    tests = subprocess.run(['python', str(copied)], env=environment, timeout=300)
    report_file = OUT / 'public-browser-report.json'
    if tests.returncode or not report_file.exists():
        raise SafeFailure('The original URL now serves the revised guide, but a public browser regression check requires attention.')
    report = json.loads(report_file.read_text())
    if report.get('failed') != 0:
        raise SafeFailure('The original URL was updated, but browser tests reported failures.')
    status('completed_verified_same_url', publicWithoutLogin=True,
           browserChecksPassed=report['passed'], browserChecksFailed=0, routeCount=len(report['routes']))

try:
    if os.environ.get('GITHUB_REPOSITORY') != REPO or os.environ.get('GITHUB_REF_NAME') != BRANCH:
        raise SafeFailure('This one-use publishing job was started outside its authorized repository or branch.')
    login()
    publish()
except Exception as exc:
    message = str(exc) if isinstance(exc, SafeFailure) else 'Deployment stopped after an unexpected ' + type(exc).__name__ + '; inspect the guarded runner without exposing authorization.'
    try:
        status('stopped_requires_attention', failure=message)
    except Exception:
        print('Could not update the status record.', flush=True)
    print(message, flush=True)
    raise SystemExit(1)
finally:
    if LOGIN_PROCESS and LOGIN_PROCESS.poll() is None:
        LOGIN_PROCESS.terminate()
    if (AUTH / 'auth.json').exists():
        try:
            subprocess.run([CLI, 'logout', '--global-config', str(AUTH)], stdin=subprocess.DEVNULL,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=cli_env(), timeout=30)
        except Exception:
            pass
    TOKEN = None
    shutil.rmtree(AUTH, ignore_errors=True)
