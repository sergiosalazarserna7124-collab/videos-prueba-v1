"""TikTok rechaza videos alojados fuera de un dominio verificado (p. ej. static.metricool.com).
Este script sube cada video a la biblioteca de GoHighLevel y cambia las publicaciones programadas
que lo usan para que apunten a esa copia.

Uso: python3 cambiar_video.py mapa.json
  mapa.json = {"<archivo metricool>.mp4": "<url de donde bajarlo>", ...}
"""
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ghl import BASE, H, LOC, USER, subir_video  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
PROG = os.path.join(AQUI, 'ghl_programado.json')
TMP = os.environ.get('TMPDIR_VIDEOS', '/tmp/videos_ghl')


def call(m, path, body=None):
    r = urllib.request.Request(BASE + path, data=json.dumps(body).encode() if body is not None else None,
                               headers={**H, 'Content-Type': 'application/json'}, method=m)
    try:
        with urllib.request.urlopen(r, timeout=120) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {'ERR': e.code, 'body': e.read().decode()[:400]}


def cambiar(pid, url):
    g = call('GET', f'/social-media-posting/{LOC}/posts/{pid}')
    p = g.get('results', {}).get('post') or g
    if p.get('deleted') or p.get('status') != 'scheduled':
        return f"no se toca ({p.get('status')}, deleted={p.get('deleted')})"
    body = {'accountIds': p['accountIds'], 'userId': USER, 'type': p['type'], 'status': 'scheduled',
            'scheduleDate': p['scheduleDate'], 'summary': p['summary'], 'media': [{'url': url, 'type': 'video/mp4'}]}
    if p.get('youtubePostDetails'):
        body['youtubePostDetails'] = {k: p['youtubePostDetails'][k] for k in ('type', 'title', 'privacyLevel')}
    d = call('PUT', f'/social-media-posting/{LOC}/posts/{pid}', body)
    return 'ok' if d.get('success') else f'ERROR {d}'


def main(mapa):
    os.makedirs(TMP, exist_ok=True)
    prog = json.load(open(PROG))
    for nombre, origen in json.load(open(mapa)).items():
        usos = [k for k, v in prog.items() if v['video'].endswith('/' + nombre)]
        if not usos:
            continue
        ruta = os.path.join(TMP, nombre)
        subprocess.run(['curl', '-sSL', '--max-time', '300', '--retry', '3', '-o', ruta, origen], check=True)
        nueva = subir_video(ruta, 'mc-' + nombre)
        for k in usos:
            print(k, '->', cambiar(prog[k]['id'], nueva), flush=True)
            prog[k]['video'] = nueva
            prog[k]['video_metricool'] = 'https://static.metricool.com/planner/202611/' + nombre
        json.dump(prog, open(PROG, 'w'), ensure_ascii=False, indent=1)
        os.remove(ruta)


if __name__ == '__main__':
    main(sys.argv[1])
