"""Programa reels en el Social Planner de GoHighLevel (la key la pone el proxy del entorno).

Uso desde Python:  from ghl import subir_video, programar
"""
import json
import subprocess
import urllib.request
import urllib.error

LOC = 'XXxOHLaqkCAyEZoiS4eW'          # subcuenta "Sergio Salazar MKT LLC"
USER = 'WBBWH0A4h3zso1yRRDX6'         # sergio salazar
BASE = 'https://services.leadconnectorhq.com'
H = {'Authorization': 'Bearer proxy-injected', 'Version': '2021-07-28', 'Accept': 'application/json'}
CUENTAS = {
    'ig_leaad_master': '6ac644b3cd5b03630e6643e6_XXxOHLaqkCAyEZoiS4eW_17841438576648556_profile',
    'ig_sergio_salazaar': '6ac644b3cd5b03630e6643e6_XXxOHLaqkCAyEZoiS4eW_17841410694405520_profile',
    'fb_sergio': '6ac644b2cd5b03630e664385_XXxOHLaqkCAyEZoiS4eW_348238158383886_page',
    'tiktok': '6aef78a7322b72268e7bedaa_XXxOHLaqkCAyEZoiS4eW_000UiYC7ZSzLmEOImgdav4Dr8OzOuviy91Z_business',
    'youtube': '6aef78c2500565d789d7b443_XXxOHLaqkCAyEZoiS4eW_UCOb3Wk4rHdTOuf9KF8270bw_profile',
}
# Instagram: una sola publicación desde @sergio_salazaar con @leaad_master de colaborador (pedido de Sergio,
# 8 nov: dos publicaciones iguales en cada cuenta Meta las toma como contenido duplicado).
TODAS = ['ig_sergio_salazaar', 'fb_sergio', 'tiktok', 'youtube']
COLABORADOR_IG = 'leaad_master'
SIN_IG = ['fb_sergio', 'tiktok', 'youtube']


def subir_video(ruta, nombre):
    out = subprocess.run(['curl', '-sS', '-X', 'POST', f'{BASE}/medias/upload-file',
                          '-H', f"Authorization: {H['Authorization']}", '-H', f"Version: {H['Version']}",
                          '-F', f'file=@{ruta};type=video/mp4', '-F', 'hosted=false', '-F', f'name={nombre}'],
                         capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    if 'url' not in d:
        raise RuntimeError(out[:400])
    return d['url']


def programar(video_url, texto, cuando_utc, cuentas, titulo_yt):
    body = {
        'accountIds': [CUENTAS[c] for c in cuentas], 'userId': USER, 'type': 'reel', 'status': 'scheduled',
        'scheduleDate': cuando_utc, 'summary': texto,
        'media': [{'url': video_url, 'type': 'video/mp4'}],
    }
    if 'ig_sergio_salazaar' in cuentas and 'ig_leaad_master' not in cuentas:
        body['instagramPostDetails'] = {'collaborators': {CUENTAS['ig_sergio_salazaar']: [COLABORADOR_IG]}}
    if 'youtube' in cuentas:
        body['youtubePostDetails'] = {'type': 'short', 'title': titulo_yt[:95], 'privacyLevel': 'public'}
    r = urllib.request.Request(f'{BASE}/social-media-posting/{LOC}/posts', data=json.dumps(body).encode(), method='POST',
                               headers={**H, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(r, timeout=120) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'{e.code} {e.read().decode()[:600]}')
