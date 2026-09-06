"""Publish only byte-verified guide files; protect deployment ownership credentials."""
from pathlib import Path
import base64, bz2, hashlib, json, os, tarfile, time
from urllib.parse import urlparse
import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
ROOT = Path(__file__).resolve().parent
OUT, SITE = ROOT / 'verified-results', ROOT / 'verified-site'
OUT.mkdir(exist_ok=True)
SITE.mkdir(exist_ok=True)
public_key = serialization.load_pem_public_key((ROOT/'ownership-public.pem').read_bytes())
def encrypted_record(data):
    key, nonce = AESGCM.generate_key(bit_length=256), os.urandom(12)
    aad = b'joe-regalia-revised-guide-2026-09-06'
    cipher = AESGCM(key).encrypt(nonce, json.dumps(data).encode(), aad)
    wrapped = public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    b64 = lambda b: base64.b64encode(b).decode()
    (OUT/'ownership-encrypted.json').write_text(json.dumps({'algorithm':'RSA-OAEP-SHA256+AES-256-GCM','wrappedKey':b64(wrapped),'nonce':b64(nonce),'ciphertext':b64(cipher),'aad':b64(aad)},indent=2))
manifest = json.loads((ROOT/'verified-release.json').read_text())
parts=[]
for item in manifest['parts']:
    text=Path(item['path']).read_text().strip()
    if item['path'].endswith('guide-11.b64'):
        text=text.replace('VDJzdeZpI32vid','VDJzdeZp32vid',1)
    digest=hashlib.sha256(text.encode()).hexdigest()
    assert len(text)==item['characters'] and digest==item['sha256'], f"Transport mismatch: {item['path']}, length={len(text)}, SHA256={digest}"
    parts.append(text)
html=bz2.decompress(base64.b64decode(''.join(parts),validate=True))
expected=manifest['indexSha256']
assert len(html)==manifest['indexBytes'] and hashlib.sha256(html).hexdigest()==expected
(SITE/'index.html').write_bytes(html)
print(f'VERIFIED_SOURCE: {len(html)} bytes, SHA256={expected}',flush=True)
headers=[{'key':'X-Content-Type-Options','value':'nosniff'},{'key':'Referrer-Policy','value':'no-referrer'},{'key':'Permissions-Policy','value':'camera=(), microphone=(), geolocation=()'},{'key':'Content-Security-Policy','value':"default-src 'none'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'"},{'key':'X-Guide-Edition','value':manifest['release']},{'key':'Cache-Control','value':'public, max-age=0, must-revalidate'}]
(SITE/'vercel.json').write_text(json.dumps({'framework':None,'buildCommand':'','installCommand':'','outputDirectory':'.','headers':[{'source':'/(.*)','headers':headers}]},indent=2))
release={k:manifest[k] for k in ['release','indexBytes','indexSha256']}
release.update(title='The AI-Enabled Lawyer',edition='Revised reading, exercises, navigation, and help',liveAiCalls=False)
(SITE/'release.json').write_text(json.dumps(release,indent=2))
archive=ROOT/'verified-guide.tgz'
with tarfile.open(archive,'w:gz') as tar:
    for item in sorted(SITE.iterdir()): tar.add(item,arcname='./'+item.name)
with archive.open('rb') as stream:
    response=requests.post('https://codex-deploy-skills.vercel.sh/api/deploy',files={'file':('verified-guide.tgz',stream,'application/gzip')},data={'framework':'null'},timeout=240)
try: result=response.json()
except ValueError: result={'nonJsonResponse':response.text[:10000]}
encrypted_record({'httpStatus':response.status_code,'response':result,'headers':dict(response.headers)})
def schema(value):
    if isinstance(value,dict): return {k:schema(v) for k,v in value.items()}
    if isinstance(value,list): return [schema(v) for v in value[:3]]
    return type(value).__name__
diagnostic={'httpStatus':response.status_code,'responseSchema':schema(result)}
(OUT/'service-schema.json').write_text(json.dumps(diagnostic,indent=2))
print('SERVICE_SCHEMA: '+json.dumps(diagnostic),flush=True)
assert response.status_code<400, f'Deployment service HTTP {response.status_code}; encrypted diagnostic retained'
candidates=[]
def walk(value):
    if isinstance(value,dict):
        for key,child in value.items():
            if isinstance(child,str) and key.lower() in ['previewurl','url','deploymenturl']:
                url=child if child.startswith('https://') else 'https://'+child
                parsed=urlparse(url)
                if parsed.hostname and (parsed.hostname.endswith('.vercel.app') or parsed.hostname.endswith('.vercel.sh')) and not parsed.query and parsed.path in ['', '/']:
                    candidates.append(url.rstrip('/'))
            elif isinstance(child,(dict,list)): walk(child)
    elif isinstance(value,list):
        for child in value: walk(child)
walk(result)
assert candidates, 'No public deployment URL in response; full response retained encrypted'
preview=candidates[0]
public={'previewUrl':preview,'indexSha256':expected,'indexBytes':len(html),'release':manifest['release'],'signedOutHttpVerified':False}
for key in ['deploymentId','projectId']:
    if key in result: public[key]=result[key]
(OUT/'deployment.json').write_text(json.dumps(public,indent=2))
print('DEPLOYED_URL: '+preview,flush=True)
last_status=None
for attempt in range(60):
    try:
        page=requests.get(preview,timeout=30)
        last_status=page.status_code
        actual=hashlib.sha256(page.content).hexdigest()
        if last_status==200 and actual==expected:
            public.update(signedOutHttpVerified=True,actualSha256=actual,finalUrl=page.url,contentType=page.headers.get('content-type'))
            break
        if last_status==200: (OUT/'unexpected-response.html').write_bytes(page.content)
        print(f'Waiting: HTTP {last_status}, attempt {attempt+1}, hash={actual}',flush=True)
    except requests.RequestException as error: print('Waiting: '+type(error).__name__,flush=True)
    time.sleep(5)
(OUT/'deployment.json').write_text(json.dumps(public,indent=2))
assert public['signedOutHttpVerified'],f'Exact public HTML not verified; last HTTP={last_status}'
r=requests.get(preview+'/release.json',timeout=30)
assert r.status_code==200 and r.json()['indexSha256']==expected
print('PUBLIC_CONTENT_VERIFIED: exact revised HTML, no login, release manifest matches',flush=True)
if os.environ.get('GITHUB_STEP_SUMMARY'):
    with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as f: f.write(f'## Revised guide\n\n{preview}\n\nExact public content verified: `{expected}`.\n')
