"""Publish only the verified revised student guide; never publish repository root."""
from pathlib import Path
import base64, bz2, hashlib, json, os, tarfile, time
from urllib.parse import urlparse
import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'verified-results'
SITE = ROOT / 'verified-site'
OUT.mkdir(exist_ok=True)
SITE.mkdir(exist_ok=True)
manifest = json.loads((ROOT / 'verified-release.json').read_text())
parts = []
for entry in manifest['parts']:
    text = Path(entry['path']).read_text().strip()
    # Correct a single transport transcription, then require the ORIGINAL hash.
    if entry['path'].endswith('guide-11.b64'):
        text = text.replace('VDJzdeZpI32vid', 'VDJzdeZp32vid', 1)
    digest = hashlib.sha256(text.encode()).hexdigest()
    if len(text) != entry['characters'] or digest != entry['sha256']:
        raise RuntimeError(f"Transport mismatch: {entry['path']}; length={len(text)}; SHA256={digest}")
    parts.append(text)
html = bz2.decompress(base64.b64decode(''.join(parts), validate=True))
expected = manifest['indexSha256']
assert len(html) == manifest['indexBytes'], 'HTML length mismatch'
assert hashlib.sha256(html).hexdigest() == expected, 'HTML content mismatch'
(SITE / 'index.html').write_bytes(html)
print(f'VERIFIED_SOURCE: {len(html)} bytes, SHA256={expected}', flush=True)
headers = [
    {'key': 'X-Content-Type-Options', 'value': 'nosniff'},
    {'key': 'Referrer-Policy', 'value': 'no-referrer'},
    {'key': 'Permissions-Policy', 'value': 'camera=(), microphone=(), geolocation=()'},
    {'key': 'Content-Security-Policy', 'value': "default-src 'none'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'"},
    {'key': 'X-Guide-Edition', 'value': manifest['release']},
    {'key': 'Cache-Control', 'value': 'public, max-age=0, must-revalidate'},
]
config = {'framework': None, 'buildCommand': '', 'installCommand': '', 'outputDirectory': '.', 'headers': [{'source': '/(.*)', 'headers': headers}]}
(SITE / 'vercel.json').write_text(json.dumps(config, indent=2))
release = {k: manifest[k] for k in ['release', 'indexBytes', 'indexSha256']}
release.update(title='The AI-Enabled Lawyer', edition='Revised reading, exercises, navigation, and help', liveAiCalls=False)
(SITE / 'release.json').write_text(json.dumps(release, indent=2))
archive = ROOT / 'verified-guide.tgz'
with tarfile.open(archive, 'w:gz') as tar:
    for item in sorted(SITE.iterdir()):
        tar.add(item, arcname='./' + item.name)

# Vercel's published agent-skills deployment service. No account credentials used.
endpoint = 'https://codex-deploy-skills.vercel.sh/api/deploy'
with archive.open('rb') as stream:
    response = requests.post(endpoint, files={'file': ('verified-guide.tgz', stream, 'application/gzip')}, data={'framework': 'null'}, timeout=240)
try:
    result = response.json()
except ValueError:
    raise RuntimeError(f'Deployment service returned non-JSON, HTTP {response.status_code}')
# Never log a claim URL or other ownership material in this public repository.
if result.get('claimUrl'):
    print('::add-mask::' + result['claimUrl'], flush=True)
if response.status_code >= 400 or result.get('error'):
    (OUT / 'deployment-error.json').write_text(json.dumps({'httpStatus': response.status_code, 'error': str(result.get('error', 'request failed'))[:1500]}, indent=2))
    raise RuntimeError(f'Deployment failed, HTTP {response.status_code}; see sanitized artifact')
preview = result.get('previewUrl')
if not preview or urlparse(preview).scheme != 'https':
    raise RuntimeError('Deployment response did not include an HTTPS previewUrl')

public_key_pem = b'''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA+hPogAK+DAxgbnHV8VbM
E8UESfq/8E0y/IU573yzMpJdrJ4hl++KwBQLR/7Hu9xLH1EqTHB/JCP59io8JRF7
emsX+I90gGejrG+C1Ifmvu7gfE0tM82jbgZ38MprYC2I3SKihxcaQweOTWeP2ure
x6Sd7JQDpfTQjzYcm17y4qikXtuHLGBP1R9zTCq7VIFZoJN3bBV8FvGzqkxIYpqW
2k2iF4x47lCxBUFYI1MHvMjpkZ0ICL6RxXFr2/hfY5XbZ7h9v2uxqoZwRQRzifv7
729EiF9QUOQ68oHi+KgE0PaCiE3zn00cNMmYFZYmc7mOEIIYVPghOLSTUuaOMGGkf
g8GMcW3Ef35dlz1dZTcqW6h5AgPyRn5z94O1kdT7cLQ7HWnhtDGsbQUl2Rf7JN7V
OhfI1mEePx6VsqIzVsZLuA79G2eBvDRb5BdenSex69EEEBArJUHWPEPqrdVVm/Kf
RFGBEs1fsUERXydsWwtFr5oQq/O5K+qoiui/Ze5IW/sWhFNVguK40AQr4bt9nLmV
9lSbYpf5/+CG9C2CXCNfm+9dHXbPAOcaPfcDaUsGvrSzbilbXEG0ntEIAYqucPkq
xrfp3KjsGG/i5KT5kwqtn+XktyI8wqchFcHYiuY3aXghr2sqgV1fGCRzD9NsWGrw
kI/DwT+o7WM/oT5HG31AdLsCAwEAAQ==
-----END PUBLIC KEY-----
'''.replace(b'mc7mOEIIYVP', b'mc7mOEIYVP')
public_key = serialization.load_pem_public_key(public_key_pem)
key, nonce = AESGCM.generate_key(bit_length=256), os.urandom(12)
aad = b'joe-regalia-revised-guide-2026-09-06'
ciphertext = AESGCM(key).encrypt(nonce, json.dumps(result).encode(), aad)
wrapped_key = public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
b64 = lambda b: base64.b64encode(b).decode()
(OUT / 'ownership-encrypted.json').write_text(json.dumps({'algorithm': 'RSA-OAEP-SHA256+AES-256-GCM', 'wrappedKey': b64(wrapped_key), 'nonce': b64(nonce), 'ciphertext': b64(ciphertext), 'aad': b64(aad)}, indent=2))
public = {'previewUrl': preview, 'indexSha256': expected, 'indexBytes': len(html), 'release': manifest['release'], 'signedOutHttpVerified': False}
for k in ['deploymentId', 'projectId']:
    if k in result:
        public[k] = result[k]
(OUT / 'deployment.json').write_text(json.dumps(public, indent=2))
print('DEPLOYED_URL: ' + preview, flush=True)
last_status = None
for attempt in range(60):
    try:
        page = requests.get(preview, timeout=30)
        last_status = page.status_code
        actual = hashlib.sha256(page.content).hexdigest()
        if last_status == 200 and actual == expected:
            public.update(signedOutHttpVerified=True, actualSha256=actual, finalUrl=page.url, contentType=page.headers.get('content-type'))
            break
        if last_status == 200:
            (OUT / 'unexpected-response.html').write_bytes(page.content)
            print('HTTP200 waiting for exact revision; received SHA256=' + actual, flush=True)
        else:
            print(f'Waiting for published content: HTTP {last_status}, attempt {attempt + 1}', flush=True)
    except requests.RequestException as error:
        print('Waiting for publication: ' + type(error).__name__, flush=True)
    time.sleep(5)
(OUT / 'deployment.json').write_text(json.dumps(public, indent=2))
assert public['signedOutHttpVerified'], f'Could not confirm exact HTML publicly; last HTTP={last_status}'
release_response = requests.get(preview.rstrip('/') + '/release.json', timeout=30)
assert release_response.status_code == 200 and release_response.json()['indexSha256'] == expected
print('PUBLIC_CONTENT_VERIFIED: exact revised HTML, no login, release manifest matches', flush=True)
summary = os.environ.get('GITHUB_STEP_SUMMARY')
if summary:
    with open(summary, 'a') as f:
        f.write(f'## Revised guide published\n\n{preview}\n\nPublic HTML verified byte for byte: `{expected}`. Browser interaction tests follow.\n')
