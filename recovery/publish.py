"""Publish only the exact, user-approved revised guide, never the gallery repository."""
from __future__ import annotations
import base64
import hashlib
import io
import json
import lzma
import os
from pathlib import Path
import subprocess
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
SITE = ROOT / 'site'
EXPECTED = 'be11c3d012c00f81404f7374910b42d3d3a29ac1524037fa46d06076f608bb96'
PART_HASHES = [
 '14ba39fb2519e7ab1c49ac0c9742f50af5ae56a1e6b45252dc095e57a93fb9e6',
 '67e925bfd423a40a033b705b508efffb021749e864f5b3f7b34815b6511be470',
 '1860c8609394521f499a6ece1c508787fbe7f119e458d89b0b5d457a56366470',
 '78363b5a122cdfa909e25e8be05b01abc8c760d50de798c9a2c677afe0f12440',
 '33216d193fd5bbbf40711219d78d0e74b3882f31606b86d5e74eb65947fe6ed9',
 '345a47c225b42a146f876544641954bdb69430b43b856e42419ff3927d81fa0e',
 '4716ef18b0f3ba6068d489fc07a525f9a6e0d9f89232725f52513c1989e82c6e',
 'd3e01b90aa9db5948ab53bb7d608550529b90622497213cd32ff241b37f068c7',
 '8f98ec38e62f605ebe86581fdbe7ce3529534e1962cb38306f3df545bd48d0af',
 'db10c0d907a1f9ec25d17a2082b9bd8ca55c9c57bf794a0d2b1216767d184272',
 'aca7b3a471dacf13e4f3a22a2dfc8316555624dde94ad1e7c010e25f5e4c4966',
 '185a39938995cf111438494e3de8d0e3407abcc948be5f52c434e679546ffdd3',
]
PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAyWqZJRHxJahYrwAo/bhJ
fXhKdQ583otQv96jeXpib3V0XZ30yuQt89Lstny8CTyLz8zCE8Lr/ED+uSqVHpri
jvcjGKZWV7Eu3z5RB9R3qPUJCittJz578wzwXjt9VnErVt4Rk2fgBInZFEmeUoT7
cyQGOys94tf/MnlkmcuM1KWot0PvcfhySnY+Pi010d7sA12SU/tuNj0m1on6cvAz
FinlGaNsefVjNP9bkubtpLEJEL4oiIosXNCSJ7b97mCrce+yJJ/x4Co23PU8p9c5
yk6a5lIi+7dcJQCFpSYiKz9Pj2G8ZULYJ/vzMee9GrdhbtBVQJdDisbP2ZVKEUCl
1RCD/SDJ280tP/uzb0SK6RN1UzlFq1QTuzhJkDUIq+dg2vJ2/CulGPFD7eRfu1ua
P6QWYSyxRsmU5zYiyJqD0Qj3MHNHLSr+9Z4X+Vfk4A7j91liIdYuOK/qlVCs0ZB1
ssactThRQRHaW6iq/jzrCZ3zuZAjdZKmsYnrl5oC2f2W54edScE2I6hSCZmv6cXS
4AdDi66WfNN+/rv2zkdiUP88eA2u/ChTBM2f9a+6nTg5FydLP6v9E3/SBq0ywEIL
hcrmjmp/61cL9FRprXaRPYIFMTdvpLsBsZc8Zm759PVg5lozLoaqXAFG6P4kFYos
Ef9Ck0pJNdzgZtipYxlqLgUCAwEAAQ==
-----END PUBLIC KEY-----
'''
CONFIG = {
 'framework': None, 'buildCommand': '', 'installCommand': '', 'outputDirectory': '.',
 'headers': [{'source': '/(.*)', 'headers': [
  {'key': 'X-Content-Type-Options', 'value': 'nosniff'},
  {'key': 'Referrer-Policy', 'value': 'no-referrer'},
  {'key': 'Permissions-Policy', 'value': 'camera=(), microphone=(), geolocation=()'},
  {'key': 'Content-Security-Policy', 'value': "default-src 'none'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'"},
  {'key': 'X-Guide-Edition', 'value': 'revised-2026-09-06'},
  {'key': 'Cache-Control', 'value': 'public, max-age=0, must-revalidate'},
 ]}]
}

def encrypt_metadata(raw: bytes) -> None:
    """Public artifacts must never expose the capability to claim the deployment."""
    key = ROOT / 'management-public.pem'
    key.write_text(PUBLIC_KEY)
    blocks = []
    for i in range(0, len(raw), 300):
        result = subprocess.run([
            'openssl', 'pkeyutl', '-encrypt', '-pubin', '-inkey', str(key),
            '-pkeyopt', 'rsa_padding_mode:oaep', '-pkeyopt', 'rsa_oaep_md:sha256',
            '-pkeyopt', 'rsa_mgf1_md:sha256',
        ], input=raw[i:i+300], capture_output=True, check=True)
        blocks.append(base64.b64encode(result.stdout).decode('ascii'))
    (OUT / 'management.encrypted.json').write_text(json.dumps({
        'algorithm': 'RSA-OAEP-SHA256', 'blocks': blocks
    }, indent=2))

def prepare() -> bytes:
    OUT.mkdir(exist_ok=True)
    SITE.mkdir(exist_ok=True)
    parts, checks = [], []
    for i, expected in enumerate(PART_HASHES):
        path = ROOT / 'payload' / f'part-{i:02}.b64'
        raw = path.read_bytes().strip()
        actual = hashlib.sha256(raw).hexdigest()
        valid = len(raw) == (9200 if i == 11 else 10000) and actual == expected
        checks.append({'file': path.name, 'bytes': len(raw), 'sha256': actual, 'valid': valid})
        parts.append(raw)
        print(f'Payload {i+1:02}/12: {"verified" if valid else "HASH MISMATCH"}', flush=True)
    (OUT / 'integrity.json').write_text(json.dumps(checks, indent=2))
    if not all(c['valid'] for c in checks):
        raise ValueError('Payload transfer failed integrity validation. Nothing was deployed.')
    html = lzma.decompress(base64.b64decode(b''.join(parts), validate=True))
    if len(html) != 376003 or hashlib.sha256(html).hexdigest() != EXPECTED:
        raise ValueError('Reconstructed HTML differs from the approved revision. Nothing was deployed.')
    (SITE / 'index.html').write_bytes(html)
    (SITE / 'vercel.json').write_text(json.dumps(CONFIG, indent=2))
    (SITE / 'release.json').write_text(json.dumps({
        'title': 'The AI-Enabled Lawyer',
        'edition': 'Revised reading, exercises, navigation, and help',
        'release': 'revised-2026-09-06', 'indexSha256': EXPECTED,
        'indexBytes': len(html), 'buildDependencies': [], 'liveAiCalls': False,
    }, indent=2))
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode='w:gz') as archive:
        for name in ['index.html', 'vercel.json', 'release.json']:
            archive.add(SITE / name, arcname=name, recursive=False)
    print(f'Approved revision verified: {len(html)} bytes, SHA-256 {EXPECTED}', flush=True)
    return buf.getvalue()

def publish(package: bytes) -> str:
    """Same documented request as Vercel's official deploy-codex.sh helper."""
    endpoint = 'https://codex-deploy-skills.vercel.sh/api/deploy'
    boundary = 'guide-' + uuid.uuid4().hex
    body = (
        f'--{boundary}\r\nContent-Disposition: form-data; name="framework"\r\n\r\nnull\r\n'
        f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="project.tgz"\r\n'
        'Content-Type: application/gzip\r\n\r\n'
    ).encode() + package + f'\r\n--{boundary}--\r\n'.encode()
    req = urllib.request.Request(endpoint, data=body, method='POST', headers={
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'User-Agent': 'RegaliaGuide-Publishing/1.0',
    })
    print('Submitting the approved static guide to Vercel.', flush=True)
    try:
        with urllib.request.urlopen(req, timeout=240) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        encrypt_metadata(exc.read())
        raise RuntimeError(f'Deployment service returned HTTP {exc.code}. Private diagnostics are encrypted.') from None
    encrypt_metadata(raw)
    data = json.loads(raw)
    url = data.get('previewUrl', '')
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != 'https' or not (parsed.hostname or '').endswith('.vercel.app'):
        raise RuntimeError('Vercel did not return a valid public deployment URL. Response stored encrypted.')
    public = {
        'previewUrl': url, 'deploymentId': data.get('deploymentId'),
        'projectId': data.get('projectId'), 'indexSha256': EXPECTED,
        'accountOwnership': 'claimable', 'status': 'created-not-yet-verified',
    }
    (OUT / 'deployment-result.json').write_text(json.dumps(public, indent=2))
    print('PUBLIC_DEPLOYMENT_URL=' + url, flush=True)
    # A 4xx, login redirect, placeholder or stale page is NOT a successful deployment.
    for attempt in range(1, 61):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={
                'User-Agent': 'RegaliaGuide-PublicVerification/1.0', 'Cache-Control': 'no-cache'
            }), timeout=20) as response:
                served = response.read(2000000)
                actual = hashlib.sha256(served).hexdigest()
                same_host = urllib.parse.urlsplit(response.url).hostname == parsed.hostname
                if response.status == 200 and same_host and actual == EXPECTED:
                    public.update(status='public-http-200-verified', httpStatus=200,
                        servedBytes=len(served), servedSha256=actual,
                        editionHeader=response.headers.get('X-Guide-Edition'),
                        verifiedWithoutLogin=True)
                    (OUT / 'deployment-result.json').write_text(json.dumps(public, indent=2))
                    print('PUBLIC_SITE_VERIFIED: HTTP 200, no login, exact approved revision.', flush=True)
                    summary = os.environ.get('GITHUB_STEP_SUMMARY')
                    if summary:
                        with open(summary, 'a') as out:
                            out.write(f'## Revised AI student guide\n\nPublic URL: {url}\n\nHTTP 200 without login. Exact revised HTML verified by SHA-256.\n')
                    return url
                print(f'Waiting for approved revision ({attempt}/60); HTTP {response.status}.', flush=True)
        except (urllib.error.URLError, TimeoutError):
            print(f'Waiting for deployment ({attempt}/60).', flush=True)
        time.sleep(5)
    raise RuntimeError('Public deployment did not serve the approved revision within the verification window.')

if __name__ == '__main__':
    package = prepare()
    if '--verify-only' not in __import__('sys').argv:
        publish(package)
