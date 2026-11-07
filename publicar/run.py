import json, os, sys, time
sys.path.insert(0, os.path.dirname(__file__))
from ghl import subir_video, programar
plan = json.load(open('plan_ghl.json'))
LOG = 'ghl_programado.json'
hecho = json.load(open(LOG)) if os.path.exists(LOG) else {}
for p in plan:
    k = f"{p['when']}|{p['title']}"
    if k in hecho: continue
    url = p.get('video_src')
    if not url:
        url = subir_video(p['video_file'], os.path.basename(p['video_file']))
    try:
        r = programar(url, p['caption'], p['utc'], p['cuentas'], p['yt'])
        post = r['results']['post']
        hecho[k] = {'id': post['_id'], 'utc': p['utc'], 'cuentas': p['cuentas'], 'video': url}
        print('OK ', p['when'], p['title'][:50], len(p['cuentas']), 'cuentas')
    except Exception as e:
        print('ERR', p['when'], p['title'][:50], str(e)[:300])
    json.dump(hecho, open(LOG, 'w'), ensure_ascii=False, indent=1)
    time.sleep(0.4)
print(len(hecho), 'de', len(plan), 'programadas')
