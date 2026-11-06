"""Subtítulos de un plano de IA: qué dice y en qué segundo (lista [{"w","s","e"}]).

1) Gemini transcribe el audio del clip con tiempos por palabra.
2) ffmpeg silencedetect da los tramos con voz; los tiempos de Gemini se ajustan a esos tramos.
Requiere GEMINI_API_KEY (nunca se imprime).

Uso: python3 tools/clip_words.py <nombre>   -> public/clips/<nombre>.words.json
     python3 tools/clip_words.py <nombre> --texto "lo que dice"   (sin transcribir: reparte el texto
     conocido sobre los tramos con voz; útil cuando la transcripción falla o sale corrida)
"""
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CLIPS = os.path.join(ROOT, 'public', 'clips')
MODELS = ['gemini-3.1-pro-preview', 'gemini-3.5-flash', 'gemini-3.8-flash', 'gemini-3.7-flash', 'gemini-flash-latest']
PROMPT = ('Transcribe exactly the Spanish speech in this audio, word by word, with start and end time in seconds '
          'for each word. Keep punctuation (¡! ¿? , .) attached to words. Return only JSON: '
          '[{"w": "...", "s": 0.0, "e": 0.0}]. Ignore non-speech sounds.')


def transcribe(wav):
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('EMINI_API_KEY')
    b = base64.b64encode(open(wav, 'rb').read()).decode()
    body = {'contents': [{'parts': [{'inline_data': {'mime_type': 'audio/wav', 'data': b}}, {'text': PROMPT}]}],
            'generationConfig': {'responseMimeType': 'application/json', 'temperature': 0}}
    for m in MODELS:
        r = urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent',
                                   data=json.dumps(body).encode(),
                                   headers={'x-goog-api-key': key, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(r, timeout=240) as resp:
                d = json.loads(resp.read())
            return json.loads(d['candidates'][0]['content']['parts'][0]['text'])
        except urllib.error.HTTPError as e:
            print(f'  {m}: {e.code}, pruebo otro modelo')
        except (TimeoutError, urllib.error.URLError) as e:
            print(f'  {m}: {type(e).__name__}, pruebo otro modelo')
    raise SystemExit('Ningún modelo pudo transcribir')


def speech_segments(wav, dur):
    out = subprocess.run(['ffmpeg', '-v', 'info', '-i', wav, '-af', 'silencedetect=noise=-30dB:d=0.25', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r'silence_start: ([0-9.]+)', out)]
    ends = [float(x) for x in re.findall(r'silence_end: ([0-9.]+)', out)]
    sil = list(zip(starts, ends + [dur] * (len(starts) - len(ends))))
    segs, t = [], 0.0
    for a, b in sil:
        if a > t:
            segs.append([t, a])
        t = b
    if t < dur:
        segs.append([t, dur])
    merged = []
    for s in segs:  # une tramos separados por pausas cortas
        if merged and s[0] - merged[-1][1] < 0.35:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    return [s for s in merged if s[1] - s[0] >= 0.35]  # ignora ruidos cortos (grillos, golpes)


def groups_of(words, gap=0.3):
    g = [[words[0]]]
    for w in words[1:]:
        if w['s'] - g[-1][-1]['e'] > gap:
            g.append([w])
        else:
            g[-1].append(w)
    return g


def fit(ws, a, b):
    s0, e0 = ws[0]['s'], ws[-1]['e']
    span = max(1e-3, e0 - s0)
    return [{'w': w['w'], 's': round(a + (w['s'] - s0) / span * (b - a), 3), 'e': round(a + (w['e'] - s0) / span * (b - a), 3)} for w in ws]


def main(name):
    mp4 = os.path.join(CLIPS, f'{name}.mp4')
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4],
                               capture_output=True, text=True).stdout)
    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, 'a.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp4, '-vn', '-ac', '1', '-ar', '16000', wav], check=True)
        words = [w for w in transcribe(wav) if w.get('w')]
        segs = speech_segments(wav, dur)
    # Parte las palabras en tantos grupos como tramos con voz haya, cortando en las pausas más largas
    # que vio Gemini, y ajusta cada grupo a su tramo real.
    n = len(segs)
    if n >= 2 and len(words) >= n:
        gaps = sorted(range(1, len(words)), key=lambda k: words[k]['s'] - words[k - 1]['e'], reverse=True)[:n - 1]
        cuts = [0] + sorted(gaps) + [len(words)]
        gs = [words[cuts[k]:cuts[k + 1]] for k in range(n)]
        out = [x for g, (a, b) in zip(gs, segs) for x in fit(g, a, b)]
    elif segs:
        out = fit(words, segs[0][0], segs[-1][1])
    else:
        out = [{'w': w['w'], 's': round(w['s'], 3), 'e': round(w['e'], 3)} for w in words]
    path = os.path.join(CLIPS, f'{name}.words.json')
    json.dump(out, open(path, 'w'), ensure_ascii=False)
    print(name, ' '.join(f"{w['w']}@{w['s']}" for w in out))
    return path


def from_text(name, text):
    mp4 = os.path.join(CLIPS, f'{name}.mp4')
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4],
                               capture_output=True, text=True).stdout)
    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, 'a.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp4, '-vn', '-ac', '1', '-ar', '16000', wav], check=True)
        segs = speech_segments(wav, dur) or [[0.0, dur]]
    sents = [x.strip() for x in re.split(r'(?<=[.?!…:])\s+', text.strip()) if x.strip()]
    # agrupa frases en tantos grupos como tramos, en orden, equilibrando por largo
    n = min(len(segs), len(sents))
    segs = segs[:n]
    total = sum(len(x) for x in sents)
    target = [(b - a) for a, b in segs]
    tsum = sum(target)
    groups, cur, acc, k = [], [], 0, 0
    for i, snt in enumerate(sents):
        cur.append(snt)
        acc += len(snt)
        left = len(sents) - i - 1
        if k < n - 1 and (acc / total >= sum(target[:k + 1]) / tsum or left == n - 1 - k):
            groups.append(' '.join(cur)); cur = []; k += 1
    groups.append(' '.join(cur))
    out = []
    for g, (a, b) in zip(groups, segs):
        ws = g.split()
        L = sum(len(w) for w in ws)
        t = a
        for w in ws:
            d = (b - a) * len(w) / L
            out.append({'w': w, 's': round(t, 3), 'e': round(t + d, 3)})
            t += d
    path = os.path.join(CLIPS, f'{name}.words.json')
    json.dump(out, open(path, 'w'), ensure_ascii=False)
    print(name, ' '.join(f"{w['w']}@{w['s']}" for w in out))
    return path


if __name__ == '__main__':
    if '--texto' in sys.argv:
        i = sys.argv.index('--texto')
        from_text(sys.argv[1], sys.argv[i + 1])
    else:
        for n in sys.argv[1:]:
            main(n)
