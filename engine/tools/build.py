"""Arma los props de un video (tiempos por palabra, escenas, subtítulos) y lo renderiza.

Uso:
  python3 tools/build.py videos/v01.json            # props + render + loudnorm
  python3 tools/build.py videos/v01.json --still 120 # solo un cuadro de prueba
  python3 tools/build.py videos/v01.json --safe      # con guías de zona segura

Voces: public/tts/<key>.mp3 + <key>.json (alineación por carácter de ElevenLabs).
"""
import json
import os
import re
import subprocess
import sys
import unicodedata

FPS = 30
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PUB = os.path.join(ROOT, 'public')
OUT = os.path.join(ROOT, '..', 'videos')
CHROME = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'

# Cómo se escribe en pantalla -> cómo se le pasa a la voz (palabra por palabra).
TTS_MAP = {
    'Lead': 'Lid', 'Master': 'Máster', 'lead': 'lid', 'leads': 'lids', 'Leads': 'Lids',
    'SISTEMA': 'sistema', 'LEADS': 'lids', 'CRM': 'CRM', 'INMOBILIARIO': 'inmobiliario',
    'GoHighLevel': 'Go High Level', 'CRA': 'ce erre a', 'CRAs': 'ce erre as',
}

# Palabras que siempre se resaltan en los subtítulos (además de las del video y los números).
BASE_KEYWORDS = ['Lead', 'Master', 'WhatsApp', 'CRM', 'Meta', 'GoHighLevel', 'control', 'citas', 'ventas',
                 'curiosos', 'Excel', 'demanda', 'dinero', 'reporte', 'robando', 'renunció', 'noche']

GAP = 0.12  # segundos entre escenas
TAIL = 0.18  # aire después de la última sílaba de cada escena


def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^\w]', '', s).lower()


def tts_tokens(text):
    """Devuelve (palabras para la voz, palabras para pantalla alineadas 1 a 1).

    Si una palabra se pronuncia con varias (GoHighLevel -> Go High Level), en pantalla
    la primera lleva el texto original y las demás quedan vacías.
    """
    voice, disp = [], []
    for tok in text.split():
        m = re.match(r'^([«"¿¡(]*)(.*?)([.,;:!?»")…]*)$', tok)
        pre, core, post = m.groups()
        parts = TTS_MAP.get(core, core).split(' ')
        for j, part in enumerate(parts):
            voice.append((pre if j == 0 else '') + part + (post if j == len(parts) - 1 else ''))
            disp.append(tok if j == 0 else '')
    return voice, disp


def to_tts(text):
    return ' '.join(tts_tokens(text)[0])


def words_from_alignment(al):
    """Agrupa la alineación por carácter en palabras con inicio y fin."""
    words = []
    cur = ''
    s = None
    e = None
    for ch, cs, ce in zip(al['chars'], al['start'], al['end']):
        if ch.isspace():
            if cur:
                words.append((cur, s, e))
            cur, s, e = '', None, None
            continue
        if s is None:
            s = cs
        cur += ch
        e = ce
    if cur:
        words.append((cur, s, e))
    return words


def probe_dur(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


# Gráficos literales: mínimo en pantalla (cuadros) antes de que termine la escena.
INS_MIN = {'report': 75, 'cita': 66, 'note': 66, 'crm': 60, 'call': 60, 'tasks': 54}
INS_SFX = {'report': ('sfx/notif.wav', 10, 0.14), 'cita': ('sfx/pop.wav', 10, 0.1), 'note': ('sfx/type.wav', 14, 0.07),
           'crm': ('sfx/whoosh.wav', 0, 0.08), 'call': ('sfx/pop.wav', 4, 0.1), 'tasks': ('sfx/pop.wav', 6, 0.1)}


def inserts(raw, dur_s):
    """Ordena los insertos, encadena su fin con el siguiente y dice cuánto alargar la escena."""
    ins = sorted([dict(x) for x in raw], key=lambda x: x['at'])
    kept = []
    for x in ins:
        if kept and x['at'] - kept[-1]['at'] < 40:
            print(f"  ! inserto {x['kind']} muy pegado al anterior; lo quito")
            continue
        kept.append(x)
    for j, x in enumerate(kept[:-1]):
        x.setdefault('to', kept[j + 1]['at'])
    extra = 0.0
    if kept and 'to' not in kept[-1]:
        need = kept[-1]['at'] + INS_MIN.get(kept[-1]['kind'], 54) - dur_s * FPS
        if need > 0:
            extra = need / FPS
    return kept, extra


def insert_sfx(x):
    out = [{'src': 'sfx/whoosh.wav', 'at': x['at'], 'vol': 0.07}]
    src, off, vol = INS_SFX.get(x['kind'], (None, 0, 0))
    if src and src != 'sfx/whoosh.wav':
        out.append({'src': src, 'at': x['at'] + off, 'vol': vol})
    p = x.get('p', {})
    if x['kind'] == 'cita' and p.get('mode', 'confirm') == 'confirm':
        out.append({'src': 'sfx/ding.wav', 'at': p.get('confirmAt', x['at'] + 42), 'vol': 0.12})
    if x['kind'] == 'crm' and not p.get('stale'):
        out.append({'src': 'sfx/pop.wav', 'at': (p.get('move') or {}).get('at', x['at'] + 26), 'vol': 0.11})
    return out


# ---------------------------------------------------------------------------- UGC
# Video de la modelo hablando a cámara: su voz manda. Cada escena empieza en una palabra de ella
# ("at": "@palabra", se busca después del inicio de la escena anterior) y dura hasta la siguiente.
# layout: face (ella completa + "over" encima) | split (sistema arriba, ella abajo) | full (gráfico).
UGC_SPLIT_CAP_Y = 925
# Escala y desplazamiento del contenido en el panel de arriba según lo que se muestra (tarjeta o celular).
# Los celulares se cortan abajo a propósito: lo importante está arriba de la pantalla.
SPLIT_FIT = {'crm': (0.78, 24), 'note': (0.85, 4), 'cita': (0.84, 6), 'call': (0.88, -6), 'tasks': (0.92, -16),
             'report': (0.85, 22), 'phonelist': (0.86, 18), 'stack': (0.8, 10)}
UGC_LEAD = 0.07  # el corte entra un poco antes de la palabra


def build_ugc(spec, safe=False):
    u = spec['ugc']
    vdur = probe_dur(os.path.join(PUB, u['src']))
    total = int(vdur * FPS)
    fix = spec.get('fix', {})
    raw = json.load(open(os.path.join(PUB, u['words'])))
    W = [{'w': fix.get(x['w'], x['w']), 's': x['s'], 'e': x['e']} for x in raw]
    keywords = {norm(k) for k in spec.get('keywords', []) + BASE_KEYWORDS}

    def find(v, after):
        m = re.match(r'^@([^#+\-:]+)(?:#(\d+))?(:e)?([+\-]\d+)?$', v)
        word, nth, end, off = m.group(1), int(m.group(2) or 1), m.group(3), int(m.group(4) or 0)
        hits = [x for x in W if norm(x['w']) == norm(word) and x['s'] >= after - 1e-3]
        if len(hits) < nth:
            raise SystemExit(f'  ! ancla no encontrada: {v} después de {after:.2f} s')
        x = hits[nth - 1]
        return (x['e'] if end else x['s']), off

    starts = []
    after = 0.0
    for i, sc in enumerate(spec['scenes']):
        a = sc.get('at', 0)
        if i == 0:
            st = 0.0
        elif isinstance(a, (int, float)):
            st = float(a)
        else:
            t, off = find(a, after)
            st = max(0.0, t - UGC_LEAD) + off / FPS
        starts.append(round(st * FPS))
        after = st
    starts.append(total)

    scenes, segs, cap_ys, hidden = [], [], [], []
    prev_layout = None
    nface = 0
    for i, sc in enumerate(spec['scenes']):
        start_f, end_f = starts[i], starts[i + 1]
        dur_f = end_f - start_f
        st_s = start_f / FPS
        layout = sc.get('layout', 'face')

        def anchor(v, st_s=st_s, start_f=start_f):
            if not isinstance(v, str) or not v.startswith('@'):
                return v
            t, off = find(v, st_s)
            return max(0, round(t * FPS) - start_f + off)

        def resolve(obj):
            if isinstance(obj, dict):
                return {k: resolve(v) for k, v in obj.items()}
            if isinstance(obj, list):
                return [resolve(v) for v in obj]
            return anchor(obj)

        p = resolve(sc.get('p', {}))
        sfx = [dict(x, at=anchor(x.get('at', 0))) for x in sc.get('sfx', [])]
        if layout != prev_layout and layout != 'face' and not sc.get('quiet'):
            sfx.append({'src': 'sfx/whoosh.wav', 'at': 0, 'vol': 0.07})
        ins, _ = inserts(resolve(sc.get('ins', [])), dur_f / FPS)
        for x in ins:
            sfx += insert_sfx(x)
        zoom = sc.get('zoom')
        if layout == 'face':
            if zoom is None:
                zoom = 1.0 if nface % 2 == 0 else spec.get('jump', 1.12)
            nface += 1
        out = {'type': sc.get('type', 'over' if layout == 'face' else 'ui'), 'from': start_f, 'dur': dur_f, 'p': p,
               'sfx': sfx, 'captions': sc.get('captions', True), 'layout': layout}
        if ins:
            out['ins'] = ins
        if layout == 'split':
            out['enter'] = prev_layout != 'split'
            fits = [SPLIT_FIT[x['kind']] for x in ins if x['kind'] in SPLIT_FIT] or ([SPLIT_FIT[out['type']]] if out['type'] in SPLIT_FIT else [])
            if fits:
                out['k'], out['ty'] = min(fits)
            for k in ('k', 'ty'):
                if k in sc:
                    out[k] = sc[k]
            cap_ys.append([st_s, end_f / FPS, sc.get('capY', UGC_SPLIT_CAP_Y)])
        elif 'capY' in sc:
            cap_ys.append([st_s, end_f / FPS, sc['capY']])
        if sc.get('captions') is False:
            hidden.append([st_s, end_f / FPS])
        scenes.append(out)
        segs.append({'from': start_f, 'to': end_f, 'mode': layout, **({'zoom': zoom} if zoom else {})})
        prev_layout = layout

    words = [{'w': x['w'], 's': x['s'], 'e': x['e'], 'hl': norm(x['w']) in keywords or bool(re.search(r'\d', x['w']))}
             for x in W if x['w']]
    props = {
        'id': spec['id'], 'totalFrames': total, 'scenes': scenes, 'words': words,
        'music': {'src': spec['music'], 'vol': spec.get('musicVol', 0.05), 'from': 0} if spec.get('music') else None,
        'safeDebug': safe,
        'base': {'src': u['src'], 'faceX': u['face'][0], 'faceY': u['face'][1], 'faceTop': u['face'][2],
                 'zoom': u.get('zoom', 1.2), 'splitZoom': u.get('splitZoom', 1.0), 'splitHead': u.get('splitHead', 40), 'segs': segs, 'vol': u.get('vol', 1.0)},
        'capYs': cap_ys,
    }
    os.makedirs(os.path.join(ROOT, 'build'), exist_ok=True)
    path = os.path.join(ROOT, 'build', f"{spec['id']}.props.json")
    json.dump(props, open(path, 'w'), ensure_ascii=False, indent=1)
    print(f"{spec['id']}: {total} frames ({total / FPS:.1f} s), {len(scenes)} escenas (UGC)")
    return props, path


def build(spec_path, safe=False):
    spec = json.load(open(spec_path))
    if 'ugc' in spec:
        return build_ugc(spec, safe)
    keywords = {norm(k) for k in spec.get('keywords', []) + BASE_KEYWORDS}
    scenes = []
    all_words = []
    t0 = 0.0
    music_from = 0
    for i, sc in enumerate(spec['scenes']):
        if sc['type'] == 'clip':
            # Clip de IA con su propio audio: dura lo que dura el video (o 'cut' segundos).
            p = dict(sc['p'])
            vid = os.path.join(PUB, p['src'])
            vdur = probe_dur(vid) - p.get('startFrom', 0) / FPS
            dur_s = min(vdur, sc.get('cut', vdur)) + (GAP if i < len(spec['scenes']) - 1 else 0)
            start_f = round(t0 * FPS)
            dur_f = round((t0 + dur_s) * FPS) - start_f
            wpath = os.path.join(PUB, p.get('words', '')) if p.get('words') else None
            for x in (json.load(open(wpath)) if wpath and os.path.exists(wpath) else []):
                if x['s'] * FPS >= dur_f:
                    continue
                all_words.append({'w': x['w'], 's': round(t0 + x['s'], 3), 'e': round(t0 + min(x['e'], dur_s), 3),
                                  'hl': norm(x['w']) in keywords or bool(re.search(r'\d', x['w']))})
            scenes.append({'type': 'clip', 'from': start_f, 'dur': dur_f, 'p': p,
                           'sfx': [x for x in sc.get('sfx', []) if isinstance(x.get('at', 0), int)],
                           'captions': sc.get('captions', True)})
            t0 += dur_s
            music_from = round(t0 * FPS) if spec.get('musicAfterClips', True) else 0
            continue
        key = sc['key']
        tempo = sc.get('tempo', spec.get('tempo', 1.0))
        mp3 = os.path.join(PUB, 'tts', f'{key}.mp3')
        audio_rel = f'tts/{key}.mp3'
        factor = tempo  # cuánto se acorta el tiempo de la voz
        if sc.get('fx') == 'aguda':
            # Voz de parodia: más aguda, con vibrato, sin alargarla.
            tag = f'{key}@aguda.mp3'
            out = os.path.join(PUB, 'tts', tag)
            if not os.path.exists(out):
                af = 'asetrate=44100*1.3,aresample=44100,atempo=0.92,vibrato=f=6:d=0.25'
                subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', mp3, '-af', af, '-b:a', '192k', out], check=True)
            mp3, audio_rel = out, f'tts/{tag}'
            factor = 1.3 * 0.92
        elif abs(tempo - 1.0) > 1e-3:
            # Acelera la voz sin cambiar el tono (quita aire, más ritmo).
            tag = f'{key}@{int(round(tempo * 100))}.mp3'
            fast = os.path.join(PUB, 'tts', tag)
            if not os.path.exists(fast):
                subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', mp3, '-af', f'atempo={tempo}', '-b:a', '192k', fast], check=True)
            mp3, audio_rel = fast, f'tts/{tag}'
        al = json.load(open(os.path.join(PUB, 'tts', f'{key}.json')))
        al = {'chars': al['chars'], 'start': [x / factor for x in al['start']], 'end': [x / factor for x in al['end']]}
        tw = words_from_alignment(al)
        disp = tts_tokens(sc['text'])[1]
        if len(tw) != len(disp):
            print(f'  ! {key}: {len(tw)} palabras de voz vs {len(disp)} en pantalla; uso las de la voz')
            disp = [w for w, _, _ in tw]
        last_end = tw[-1][2] if tw else probe_dur(mp3)
        dur_s = last_end + TAIL + sc.get('tail', 0) + (GAP if i < len(spec['scenes']) - 1 else 0)
        dur_s = max(dur_s, sc.get('min', 0))
        local = [(d, s, e) for d, (_, s, e) in zip(disp, tw)]

        def anchor(v, local=local):
            if not isinstance(v, str) or not v.startswith('@'):
                return v
            m = re.match(r'^@([^#+\-]+)(?:#(\d+))?(:e)?([+\-]\d+)?$', v)
            word, nth, end, off = m.group(1), int(m.group(2) or 1), m.group(3), int(m.group(4) or 0)
            hits = [x for x in local if norm(x[0]) == norm(word)]
            if len(hits) < nth:
                print(f'  ! ancla no encontrada: {v} en {key}')
                return 0
            w = hits[nth - 1]
            return max(0, round((w[2] if end else w[1]) * FPS) + off)

        def resolve(obj):
            if isinstance(obj, dict):
                return {k: resolve(v) for k, v in obj.items()}
            if isinstance(obj, list):
                return [resolve(v) for v in obj]
            return anchor(obj)

        p = resolve(sc.get('p', {}))
        sfx = [dict(x, at=anchor(x.get('at', 0))) for x in sc.get('sfx', [])]
        ins, extra = inserts(resolve(sc.get('ins', [])), dur_s)
        dur_s += extra
        for x in ins:
            sfx += insert_sfx(x)
        start_f = round(t0 * FPS)
        dur_f = round((t0 + dur_s) * FPS) - start_f
        scenes.append({
            'type': sc['type'], 'from': start_f, 'dur': dur_f, 'p': p,
            'audio': audio_rel, 'sfx': sfx, 'captions': sc.get('captions', True),
        })
        if ins:
            scenes[-1]['ins'] = ins
        for d, s, e in local:
            if not d:
                continue  # parte extra de una palabra que se pronuncia con varias
            all_words.append({'w': d, 's': round(start_f / FPS + s, 3), 'e': round(start_f / FPS + e, 3),
                              'hl': norm(d) in keywords or bool(re.search(r'\d', d))})
        t0 += dur_s
    total = round(t0 * FPS)
    props = {
        'id': spec['id'], 'totalFrames': total, 'scenes': scenes, 'words': all_words,
        'music': {'src': spec['music'], 'vol': spec.get('musicVol', 0.1), 'from': music_from} if spec.get('music') else None,
        'safeDebug': safe,
    }
    os.makedirs(os.path.join(ROOT, 'build'), exist_ok=True)
    path = os.path.join(ROOT, 'build', f"{spec['id']}.props.json")
    json.dump(props, open(path, 'w'), ensure_ascii=False, indent=1)
    print(f"{spec['id']}: {total} frames ({total / FPS:.1f} s), {len(scenes)} escenas")
    return props, path


def render(spec_id, props_path, still=None):
    os.makedirs(OUT, exist_ok=True)
    base = ['npx', 'remotion']
    common = [f'--props={props_path}', f'--browser-executable={CHROME}', '--log=error']
    if still is not None:
        out = os.path.join(ROOT, 'build', f'{spec_id}-f{still}.png')
        cmd = base + ['still', 'src/index.ts', 'Reel', out, f'--frame={still}'] + common
        subprocess.run(cmd, cwd=ROOT, check=True)
        return out
    raw = os.path.join(ROOT, 'build', f'{spec_id}.raw.mp4')
    cmd = base + ['render', 'src/index.ts', 'Reel', raw, '--codec=h264', '--crf=18',
                  '--concurrency=3', '--audio-bitrate=320k', '--timeout=240000'] + common
    # A veces un cuadro se queda esperando una imagen; se reintenta hasta 3 veces.
    for attempt in range(3):
        if subprocess.run(cmd, cwd=ROOT).returncode == 0:
            break
        print(f'  ! render falló (intento {attempt + 1}), reintentando')
    else:
        raise RuntimeError(f'render falló 3 veces: {spec_id}')
    final = os.path.join(OUT, f'{spec_id}.mp4')
    # Entrega a -14 LUFS con limitador a -1 dBTP.
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', raw, '-c:v', 'copy',
                    '-af', 'loudnorm=I=-14:TP=-1:LRA=11', '-ar', '48000', '-c:a', 'aac', '-b:a', '256k',
                    '-movflags', '+faststart', final], check=True)
    return final


if __name__ == '__main__':
    spec_path = sys.argv[1]
    safe = '--safe' in sys.argv
    still = None
    if '--still' in sys.argv:
        still = [int(x) for x in sys.argv[sys.argv.index('--still') + 1].split(',')]
    props, path = build(spec_path, safe)
    if still is not None:
        for s in still:
            print(render(props['id'], path, s))
    elif '--props-only' not in sys.argv:
        print(render(props['id'], path))
