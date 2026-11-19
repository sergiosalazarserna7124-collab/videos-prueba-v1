"""Arma el plan de publicaciones en GoHighLevel a partir de la cola de la otra sesión + los videos J01-J06."""
import json, datetime
SRC = '/tmp/claude-0/-home-user-videos-prueba-v1/75cb41ef-6804-55fe-a6ec-f6f7b26c893d/scratchpad/igq_other.json'
d = json.load(open(SRC)); items = [v for v in d.values() if isinstance(v, list)][0]
IG_SOLO = {'Idea 3 · Este CRM se mueve solo', 'Idea 12 · Orgullo GoHighLevel'}
MOVER = {  # los que ya pasaron hoy sin publicarse
    ('2026-11-07T08:00', 'Idea 13 · Pagaste GoHighLevel'): '2026-11-07T15:00',
    ('2026-11-07T10:00', 'Deja de pelear para que llenen el CRM'): '2026-11-07T17:00',
    ('2026-11-07T10:00', 'Idea 3 · Este CRM se mueve solo'): '2026-11-07T17:00',
    ('2026-11-07T12:00', 'Idea 1 · Monterrey'): '2026-11-07T19:15',
    ('2026-11-07T14:00', 'Idea 12 · Orgullo GoHighLevel'): '2026-11-07T21:30',
    ('2026-11-07T14:00', 'El lead en 5 minutos vs. en 2 horas'): '2026-11-07T21:30',
}
def yt_title(cap):
    t = cap.split('\n')[0].strip().strip('«»"“”')
    return (t[:92] + '…') if len(t) > 95 else t
plan = []
for it in items:
    if it['when'] < '2026-11-07': continue
    when = MOVER.get((it['when'], it['title']), it['when'])
    if when <= '2026-11-07T14:40':
        print('SIN HORA NUEVA', it['when'], it['title']); continue
    if it['title'] in IG_SOLO: cuentas = ['ig_leaad_master', 'ig_sergio_salazaar']
    elif it['status'] == 'no_instagram': cuentas = ['fb_sergio', 'tiktok', 'youtube']
    else: cuentas = ['ig_leaad_master', 'ig_sergio_salazaar', 'fb_sergio', 'tiktok', 'youtube']
    plan.append({'when': when, 'title': it['title'], 'video_src': it['video'], 'caption': it['caption'], 'cuentas': cuentas, 'yt': yt_title(it['caption'])})
J = [
 ('J01-nadie-llena-el-crm-de-mi-inmobiliaria','2026-11-08T19:15','Nadie llena el CRM de mi inmobiliaria',
  "«¡Asesores inmobiliarios! Nadie llena el CRM, nadie completa las notas. ¿Qué pasó con mis leads?»\n¿Te suena en tu inmobiliaria? Con Lead Master, el WhatsApp y las llamadas de tus asesores se conectan y, en automático, la IA llena el CRM, escribe la nota de cada lead y te manda el reporte. Sin que nadie llene nada.\nComenta CRM y te mando cómo funciona.\n#inmobiliarias #asesoresinmobiliarios #crm #leads #bienesraices"),
 ('J02-mejor-al-rato-el-crm-sin-actualizar','2026-11-09T19:15','Mejor al rato: el asesor que nunca actualiza el CRM',
  "«¡Ahhh! Soy asesor inmobiliario, no secretario. ¿Otra vez anotar lo de este lead? Mejor al rato.»\nY en la noche ya no se acuerda con qué lead habló. Con Lead Master, el WhatsApp y las llamadas de tus asesores se conectan y la IA escribe la nota de cada lead en automático. Cada mañana tu asesor recibe su lista del día.\nComenta CRM y te mando cómo funciona.\n#inmobiliarias #asesoresinmobiliarios #crm #leads #bienesraices"),
 ('J03-se-lo-ofrezco-a-mi-compadre','2026-11-10T19:15','Se lo ofrezco a mi compadre: tus leads por fuera',
  "«Los asesores inmobiliarios no perdemos leads: si aquí no hay desarrollo, se lo ofrezco a mi compadre.»\nLos leads son de tu inmobiliaria, no de tu asesor. Con Lead Master el WhatsApp de cada asesor está conectado, las llamadas quedan grabadas y te llega un aviso automático si pasa algo raro con un lead. Si el asesor se va, los leads se quedan.\nComenta LEADS y te mando cómo funciona.\n#inmobiliarias #asesoresinmobiliarios #leads #crm #desarrollosinmobiliarios"),
 ('J04-mil-leads-y-nadie-sabe-que-paso','2026-11-11T19:15','Mil leads y nadie sabe qué pasó',
  "«Metí cien mil pesos en anuncios: mil leads. ¿Y mis asesores inmobiliarios qué hicieron con ellos?» «Jefa, esos leads estaban malísimos…» ¿Seguro?\nCon Lead Master ves en automático qué pasó con cada lead: a quién se llamó, quién contestó, quién agendó y a quién nadie llamó.\nComenta LEADS y te mando cómo funciona.\n#inmobiliarias #metaads #asesoresinmobiliarios #leads #marketinginmobiliario"),
 ('J05-300-leads-y-cero-ventas','2026-11-12T19:15','300 leads y cero ventas: decide con datos',
  "«¡Meta dice trescientos leads! Asesores inmobiliarios, ¿qué pasó con ellos? ¿Por qué no vendemos?»\nMeta te dice cuántos leads llegaron, no qué pasó después. Lead Master se conecta al WhatsApp y a las llamadas de tu equipo y en automático te muestra qué pasó en cada cita y las objeciones más comunes. Decide con datos, no con miedo.\nComenta LEADS y te mando cómo funciona.\n#inmobiliarias #metaads #asesoresinmobiliarios #leads #ventas"),
 ('J06-leads-que-nunca-compran-avisale-a-meta','2026-11-13T19:15','Leads que nunca compran: avísale a Meta, paso a paso',
  "«Ya estoy cansado. A mis asesores inmobiliarios les llegan leads preguntando por un terreno… y nunca compran.» ¿Le estás diciendo a Meta cuáles de esos leads sí agendan?\nPaso a paso con Lead Master: el lead llega solo, Lead Master se conecta al WhatsApp y a las llamadas de tus asesores, detecta la cita y le avisa a Meta en automático para que te traiga más compradores.\nComenta META y te mando cómo funciona.\n#inmobiliarias #terrenos #metaads #asesoresinmobiliarios #leads"),
]
for fid, when, yt, cap in J:
    plan.append({'when': when, 'title': fid, 'video_file': f'/home/user/videos-prueba-v1/videos/{fid}-celular.mp4', 'caption': cap,
                 'cuentas': ['ig_leaad_master', 'ig_sergio_salazaar', 'fb_sergio', 'tiktok', 'youtube'], 'yt': yt})
plan.sort(key=lambda x: x['when'])
for p in plan:
    bog = datetime.datetime.fromisoformat(p['when'])
    p['utc'] = (bog + datetime.timedelta(hours=5)).strftime('%Y-%m-%dT%H:%M:00.000Z')
json.dump(plan, open('plan_ghl.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(plan), 'publicaciones')
for day, n in sorted(Counter(p['when'][:10] for p in plan).items()): print(day, n)
print('sin video:', [p['title'] for p in plan if not (p.get('video_src') or p.get('video_file'))])
