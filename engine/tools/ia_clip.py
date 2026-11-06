"""Genera un plano de IA (personas) con gemini-omni por la Interactions API nativa de Gemini.

Requiere: pip install -U google-genai  y la key en la variable GEMINI_API_KEY (nunca se imprime).
Ojo: si el entorno tiene un secreto de red que mete `Authorization: Bearer` en
generativelanguage.googleapis.com, Google responde 401 y hay que quitar ese secreto.

Uso:
  python3 tools/ia_clip.py start <nombre> "<prompt>" [segundos] [modelo]
  python3 tools/ia_clip.py wait <nombre>      -> public/clips/<nombre>.mp4
  python3 tools/ia_clip.py spec <spec.json>   -> lanza y espera todos los planos del campo "ia"
"""
import base64
import json
import os
import sys
import time
import urllib.request

from google import genai

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CLIPS = os.path.join(ROOT, 'public', 'clips')
JOBS = os.path.join(CLIPS, '_jobs.json')
MODEL = 'gemini-omni-1.2-flash'
DONE_BAD = ('failed', 'cancelled', 'incomplete', 'budget_exceeded')


_CLIENT = None


def gemini_key():
    # En el entorno lead-master-video la variable quedó guardada como EMINI_API_KEY.
    return os.environ.get('GEMINI_API_KEY') or os.environ.get('EMINI_API_KEY')


def client():
    global _CLIENT
    if _CLIENT is not None:
        return _CLIENT
    key = gemini_key()
    if not key:
        raise SystemExit('Falta GEMINI_API_KEY')
    _CLIENT = genai.Client(api_key=key)
    return _CLIENT


def jobs():
    return json.load(open(JOBS)) if os.path.exists(JOBS) else {}


def save_jobs(j):
    os.makedirs(CLIPS, exist_ok=True)
    json.dump(j, open(JOBS, 'w'), ensure_ascii=False, indent=1)


def start(name, prompt, seconds='8', model=MODEL):
    it = client().interactions.create(
        model=model,
        input=prompt,
        background=True,
        response_modalities=['video'],
        response_format={'type': 'video', 'aspect_ratio': '9:16', 'resolution': '720p',
                         'duration': f'{seconds}s', 'delivery': 'inline'},
    )
    j = jobs()
    j[name] = {'id': it.id, 'model': model, 'prompt': prompt, 'seconds': seconds, 'created': time.time()}
    save_jobs(j)
    print(name, it.id, it.status)
    return it.id


def _video_bytes(it):
    v = getattr(it, 'output_video', None)
    if v is None:
        for step in getattr(it, 'outputs', None) or getattr(it, 'steps', None) or []:
            for c in getattr(step, 'content', None) or [step]:
                if getattr(c, 'type', None) == 'video':
                    v = c
    if v is None:
        raise SystemExit('La interacción terminó sin video: ' + it.model_dump_json()[:800])
    if v.data:
        return base64.b64decode(v.data) if isinstance(v.data, str) else bytes(v.data)
    r = urllib.request.Request(v.uri, headers={'x-goog-api-key': gemini_key()})
    with urllib.request.urlopen(r, timeout=300) as resp:
        return resp.read()


def wait(name, timeout=900):
    iid = jobs()[name]['id']
    c = client()
    t0 = time.time()
    while time.time() - t0 < timeout:
        it = c.interactions.get(iid)
        if it.status == 'completed':
            data = _video_bytes(it)
            out = os.path.join(CLIPS, f'{name}.mp4')
            open(out, 'wb').write(data)
            print(name, 'listo', out, len(data))
            return out
        if it.status in DONE_BAD:
            raise SystemExit(f'{name} falló ({it.status}): {it.model_dump_json()[:800]}')
        time.sleep(10)
    raise SystemExit(f'{name}: sigue en proceso')


def from_spec(path):
    spec = json.load(open(path))
    for ia in spec.get('ia', []):
        if not os.path.exists(os.path.join(CLIPS, ia['clip'] + '.mp4')):
            start(ia['clip'], ia['prompt'])
    for ia in spec.get('ia', []):
        if not os.path.exists(os.path.join(CLIPS, ia['clip'] + '.mp4')):
            wait(ia['clip'])


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'start':
        start(*sys.argv[2:])
    elif cmd == 'wait':
        wait(sys.argv[2])
    elif cmd == 'spec':
        from_spec(sys.argv[2])
