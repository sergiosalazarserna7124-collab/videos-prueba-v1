"""Lista de voces que faltan generar (para correr en el sandbox de Composio con ElevenLabs).

Uso: python3 tools/tts_jobs.py  -> videos/_tts_jobs.json
Cada trabajo: key, voice_id, text (ya con la pronunciación de TTS_MAP), prev/next para continuidad.
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import PUB, to_tts  # noqa: E402
from specs import VOICE_IDS  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def main():
    jobs = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'videos', '*.json'))):
        if os.path.basename(f).startswith('_') or os.path.basename(f) == 'v01.json':
            continue
        spec = json.load(open(f))
        scenes = spec['scenes']
        for i, sc in enumerate(scenes):
            if os.path.exists(os.path.join(PUB, 'tts', f"{sc['key']}.json")):
                continue
            voice = sc.get('voice', spec.get('voice', 'fernando'))
            same = lambda j: 0 <= j < len(scenes) and scenes[j].get('voice', spec.get('voice')) == voice and scenes[j].get('fx') == sc.get('fx')
            job = {'key': sc['key'], 'voice_id': VOICE_IDS[voice], 'text': to_tts(sc['text'])}
            if same(i - 1):
                job['prev'] = to_tts(scenes[i - 1]['text'])
            if same(i + 1):
                job['next'] = to_tts(scenes[i + 1]['text'])
            if sc.get('fx') == 'aguda':
                job['style'] = 0.8  # el gurú exagerado
            jobs.append(job)
    out = os.path.join(ROOT, 'videos', '_tts_jobs.json')
    json.dump(jobs, open(out, 'w'), ensure_ascii=False, indent=0)
    print(f'{len(jobs)} trabajos, {sum(len(j["text"]) for j in jobs)} caracteres -> {out}')


if __name__ == '__main__':
    main()
