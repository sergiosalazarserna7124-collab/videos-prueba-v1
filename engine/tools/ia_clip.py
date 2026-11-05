"""Genera un plano de IA (personas) con Gemini por la ruta compatible con OpenAI.

La key la pone el proxy del entorno (Authorization: Bearer); aquí va un marcador.
Uso:
  python3 tools/ia_clip.py start <nombre> "<prompt>" [segundos] [modelo]
  python3 tools/ia_clip.py wait <nombre>      -> public/clips/<nombre>.mp4
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error

BASE = 'https://generativelanguage.googleapis.com/v1beta/openai'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CLIPS = os.path.join(ROOT, 'public', 'clips')
JOBS = os.path.join(CLIPS, '_jobs.json')
MODEL = 'gemini-omni-1.2-flash'


def req(method, path, body=None, raw=False):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(BASE + path, data=data, method=method,
                               headers={'Authorization': 'Bearer proxy-injected', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(r, timeout=300) as resp:
            out = resp.read()
            return out if raw else json.loads(out)
    except urllib.error.HTTPError as e:
        raise SystemExit(f'{e.code} {e.read().decode()[:1500]}')


def jobs():
    return json.load(open(JOBS)) if os.path.exists(JOBS) else {}


def start(name, prompt, seconds='8', model=MODEL):
    os.makedirs(CLIPS, exist_ok=True)
    res = req('POST', '/videos', {'model': model, 'prompt': prompt, 'seconds': str(seconds), 'size': '720x1280'})
    j = jobs()
    j[name] = {'id': res.get('id'), 'model': model, 'prompt': prompt, 'seconds': seconds, 'created': time.time()}
    json.dump(j, open(JOBS, 'w'), ensure_ascii=False, indent=1)
    print(name, json.dumps(res)[:400])


def wait(name, timeout=600):
    vid = jobs()[name]['id']
    t0 = time.time()
    while time.time() - t0 < timeout:
        st = req('GET', f'/videos/{vid}')
        s = st.get('status')
        if s in ('completed', 'succeeded'):
            data = req('GET', f'/videos/{vid}/content', raw=True)
            out = os.path.join(CLIPS, f'{name}.mp4')
            open(out, 'wb').write(data)
            print(name, 'listo', out, len(data))
            return out
        if s in ('failed', 'cancelled', 'canceled'):
            raise SystemExit(f'{name} falló: {json.dumps(st)[:800]}')
        time.sleep(8)
    raise SystemExit(f'{name}: sigue en proceso')


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'start':
        start(*sys.argv[2:])
    elif cmd == 'wait':
        wait(sys.argv[2])
