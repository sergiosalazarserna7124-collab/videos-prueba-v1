"""Specs de los reels aprobados (guiones del doc "Guiones LeadMaster v2").

Cada video es una lista de escenas. Cada escena tiene el texto que dice la voz (tal cual el guion),
el tipo de animación y en qué palabra entra cada elemento ("@palabra", "@palabra#2", "@palabra+5").

Uso:  python3 tools/specs.py          -> escribe videos/<id>.json
"""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FER = 'fernando'
ANT = 'antonio'
VOICE_IDS = {FER: 'dlGxemPxFMTY7iXagmOj', ANT: 'htFfPSZGJwjBv1CL0aMD'}

W, P, D, I, S, N, ST, R = ('sfx/whoosh.wav', 'sfx/pop.wav', 'sfx/ding.wav', 'sfx/impact.wav', 'sfx/stamp.wav',
                           'sfx/notif.wav', 'sfx/scratch.wav', 'sfx/riser.wav')


def fx(src, at, vol):
    return {'src': src, 'at': at, 'vol': vol}


# ---------- constructores de escenas ----------

def photo(text, img, lines, lineAts=None, kicker=None, stamp=None, size=None, drift=None, pos=None, accent=None, **kw):
    p = {'img': img, 'lines': lines}
    if lineAts: p['lineAts'] = lineAts
    if kicker: p['kicker'] = kicker
    if stamp: p['stamp'] = stamp
    if size: p['size'] = size
    if drift: p['drift'] = drift
    if pos: p['pos'] = pos
    if accent: p['accent'] = accent
    sfx = []
    for a in (lineAts or [])[1:]:
        sfx.append(fx(P, a, 0.1))
    if stamp:
        sfx.append(fx(S, stamp['at'], 0.28))
    return dict(type='photo', text=text, p=p, sfx=sfx, **kw)


def stack(text, items, img=None, title=None, num=False, **kw):
    p = {'items': items}
    if img: p['img'] = img
    if title: p['title'] = title
    if num: p['num'] = True
    return dict(type='stack', text=text, p=p, sfx=[fx(P, it['at'], 0.12) for it in items], **kw)


def stat(text, items, img=None, foot=None, title=None, stacked=None, **kw):
    p = {'items': items}
    if img: p['img'] = img
    if foot: p['foot'] = foot
    if title: p['title'] = title
    if stacked is not None: p['stacked'] = stacked
    return dict(type='stat', text=text, p=p, sfx=[fx(D, it['at'], 0.09) for it in items], **kw)


def quote(text, said, img, who='Dueño de inmobiliaria', **kw):
    return dict(type='quote', text=text, p={'text': said, 'img': img, 'who': who}, sfx=[], **kw)


def panel(text, rows, title=None, right=None, **kw):
    p = {'rows': rows}
    if title: p['title'] = title
    if right: p['right'] = right
    return dict(type='panel', text=text, p=p, sfx=[fx(D, r['at'], 0.08) for r in rows], **kw)


def flow(text, nodes, title=None, img=None, **kw):
    p = {'nodes': nodes}
    if title: p['title'] = title
    if img: p['img'] = img
    return dict(type='flow', text=text, p=p, sfx=[fx(P, n['at'], 0.12) for n in nodes], **kw)


def bars(text, rows, title=None, right=None, at=6, foot=None, **kw):
    p = {'rows': rows, 'at': at}
    if title: p['title'] = title
    if right: p['right'] = right
    if foot: p['foot'] = foot
    return dict(type='bars', text=text, p=p, sfx=[fx(R, at, 0.08)], **kw)


def phonelist(text, items, bg, title=None, sub=None, clock=None, **kw):
    p = {'items': items, 'bg': bg}
    if title: p['title'] = title
    if sub: p['sub'] = sub
    if clock: p['clock'] = clock
    return dict(type='phonelist', text=text, p=p, sfx=[fx(N if i == 0 else P, it['at'], 0.14 if i == 0 else 0.11) for i, it in enumerate(items)], **kw)


def chat(text, messages, bg, contact, sub=None, style=None, label=None, **kw):
    p = {'messages': messages, 'bg': bg, 'contact': contact}
    if sub: p['sub'] = sub
    if style: p['style'] = style
    if label: p['label'] = label
    return dict(type='chat', text=text, p=p, sfx=[fx(N if m['from'] == 'in' else P, m['at'], 0.16 if m['from'] == 'in' else 0.1) for m in messages], **kw)


def floatchats(text, img, lines, lineAts=None, bubbles=None, **kw):
    p = {'img': img, 'lines': lines, 'titleTop': 640}
    if lineAts: p['lineAts'] = lineAts
    if bubbles: p['bubbles'] = bubbles
    return dict(type='floatchats', text=text, p=p, sfx=[fx(R, 0, 0.07)] + ([fx(I, lineAts[-1], 0.12)] if lineAts else []), **kw)


def events(text, evs, toastAt=None, toast=None, toastSub=None, **kw):
    p = {'events': evs}
    sfx = [fx(P, e['at'], 0.1) for e in evs]
    if toastAt is not None:
        p['toastAt'] = toastAt
        sfx.append(fx(D, toastAt, 0.12))
    if toast: p['toast'] = toast
    if toastSub: p['toastSub'] = toastSub
    return dict(type='events', text=text, p=p, sfx=sfx, **kw)


def compare(text, rows, left='GoHighLevel', right='Lead Master', title=None, **kw):
    p = {'rows': rows, 'left': left, 'right': right}
    if title: p['title'] = title
    return dict(type='compare', text=text, p=p, sfx=[fx(P, r['at'], 0.11) for r in rows], **kw)


def mock(text, lines, img='guru', **kw):
    return dict(type='mock', text=text, p={'lines': lines, 'img': img}, sfx=[fx(P, l['at'], 0.12) for l in lines],
                fx='aguda', voice=FER, **kw)


def cta(text, top, button='Dale clic abajo', tail=1.0, **kw):
    return dict(type='cta', text=text, p={'mode': 'ad', 'top': top, 'button': button}, sfx=[fx(I, 6, 0.14)], tail=tail, **kw)


def wa(advisor, lead, summary, status, color, at, ch='wa', raw=False):
    r = {'ch': ch, 'advisor': advisor, 'lead': lead, 'summary': summary, 'status': status, 'color': color, 'at': at}
    if raw: r['raw'] = True
    return r


def call(advisor, lead, summary, status, color, at, raw=False):
    return wa(advisor, lead, summary, status, color, at, ch='call', raw=raw)


def it(t, at, color='cyan', k=None, n=None, sub=None):
    d = {'t': t, 'at': at, 'color': color}
    if k: d['k'] = k
    if n is not None: d['n'] = n
    if sub: d['sub'] = sub
    return d


def num(value, label, at, color='cyan', prefix=None, suffix=None):
    d = {'value': value, 'label': label, 'at': at, 'color': color}
    if prefix: d['prefix'] = prefix
    if suffix: d['suffix'] = suffix
    return d


def node(t, at, color='cyan', sub=None):
    d = {'t': t, 'at': at, 'color': color}
    if sub: d['sub'] = sub
    return d


EV_BASE = [
    {'name': 'Contactado con respuesta', 'count': 184, 'at': 0},
    {'name': 'Zoom agendado', 'count': 31, 'at': 4},
    {'name': 'Cita presencial agendada', 'count': 46, 'at': 8},
    {'name': 'Vendido', 'count': 4, 'at': 12},
]

VIDEOS = []


def video(vid, prefix, title, scenes, voice=FER, music='pulse', tempo=1.1, keywords=()):
    VIDEOS.append(dict(vid=vid, prefix=prefix, title=title, scenes=scenes, voice=voice, music=music, tempo=tempo,
                       keywords=list(keywords)))


# =====================================================================
# Tus guiones de anuncios (A–F)
# =====================================================================

video('A-por-que-tu-crm-no-funciona', 'a', 'Por qué tu CRM no funciona', [
    photo('Si tienes una inmobiliaria y ya pagaste un CRM, esto te va a doler: 8 de cada 10 inmobiliarias que implementan un CRM no lo terminan usando.',
          'excel_night', ['8 DE CADA 10', '[NO USAN] SU CRM'], kicker='Inmobiliarias'),
    stack('Si ya lo viviste, lo sabes. Tus asesores no actualizan las etapas, no ponen notas, no crean tareas.',
          [it('Nadie las actualiza', '@etapas', 'amber', k='Etapas'), it('Nadie las pone', '@notas', 'amber', k='Notas'),
           it('Nadie las crea', '@tareas', 'red', k='Tareas')], img='office_agents'),
    floatchats('Para ellos el CRM es una carga, así que hablan con el lead desde su WhatsApp y a ti nadie te reporta nada.',
               'advisor_car', ['TODO PASA', 'EN SU [WHATSAPP]'], ['@hablan', '@WhatsApp']),
    stat('Y terminas con marketing celebrando mil leads, muy pocas cartas oferta y, a veces, cero ventas.',
         [num(1000, 'leads que celebra marketing', '@mil'), num(0, 'ventas', '@cero', 'red')], img='meeting'),
    photo('Sin saber si el lead era malo o si el asesor hizo un mal trabajo, no puedes arreglar nada.',
          'owner_stressed', ['¿LEAD MALO', 'O [MAL ASESOR]?'], [0, '@asesor']),
    panel('Por eso creamos un sistema que monitorea todo lo que hace tu equipo comercial. Tus asesores solo hablan con el lead desde su WhatsApp; el sistema registra cada chat y cada intento, mueve la etapa y pone la nota.',
          [wa('Valeria Ríos', 'Diana Trejo', 'Busca 2 recámaras en Tulum. Visita el jueves a las 5 pm.', 'Etapa: cita', 'green', '@registra'),
           call('Diego Herrera', 'Adriana Solís', '3 intentos de llamada sin respuesta. Siguiente intento: hoy 6 pm.', 'En seguimiento', 'amber', '@intento'),
           wa('Paola Gutiérrez', 'Lucía Hernández', 'Pidió precios de preventa. Nota escrita por la IA.', 'Nota lista', 'cyan', '@nota')],
          title='Tu equipo, en automático'),
    phonelist('Y cada semana tú recibes qué pasó con cada prospecto: a quién llamaron, quién nunca contestó y a quién dejaron en el olvido.',
              [it('A quién llamaron', '@llamaron', 'green', n=142), it('Quién nunca contestó', '@contestó', 'amber', n=38),
               it('Leads en el olvido', '@olvido', 'red', n=21)], 'owner_phone_report', title='Reporte semanal', sub='Lead Master · lunes 8:00'),
    cta('Si tienes una inmobiliaria con al menos 5 asesores y quieres más recorridos, cartas oferta y ventas, dale clic al botón de abajo.',
        '+5 ASESORES'),
], tempo=1.12, keywords=['etapas', 'notas', 'tareas', 'carga', 'cero', 'malo', 'monitorea', 'olvido'])

video('B-marketing-y-ventas-siempre-pelean', 'b', 'Marketing y ventas siempre pelean', [
    photo('Así son las juntas de marketing y ventas en tu inmobiliaria.', 'marketing_sales_fight', ['MARKETING', 'VS [VENTAS]'],
          kicker='Tu inmobiliaria'),
    chat('Marketing dice: «Conseguimos mil leads y ventas no vendió». Tus asesores dicen: «Los leads son basura, nadie contesta».',
         [{'from': 'in', 'text': 'Marketing: Conseguimos mil leads y ventas no vendió.', 'at': '@Conseguimos'},
          {'from': 'out', 'text': 'Asesores: Los leads son basura, nadie contesta.', 'at': '@Los'}],
         'meeting', 'Junta comercial', sub='Marketing, Ventas, Tú'),
    stack('Marketing dice que es mentira, que se tardan en llamar. Los asesores juran que les marcaron diez veces.',
          [it('Se tardan en llamar', '@mentira', 'purple', k='Marketing'), it('Les marcamos 10 veces', '@juran', 'amber', k='Asesores')],
          img='office_agents'),
    photo('Y tú, que pagas los anuncios y la agencia, sales de la junta sin saber a quién creerle. Y así cada semana.',
          'owner_stressed', ['¿A QUIÉN', 'LE [CREES]?'], ['@quién', '@creerle']),
    panel('Este sistema, que ya usan más de 15 inmobiliarias en México, Estados Unidos y Colombia, te dice qué pasó con cada lead: cuál se perdió porque era malo y cuál por culpa del asesor.',
          [wa('Andrés Molina', 'Lucía Hernández', 'No buscaba comprar: pidió información por error.', 'Lead malo', 'amber', '@malo'),
           call('Diego Herrera', 'Adriana Solís', 'Pidió que le llamaran el martes. Nadie le llamó.', 'Culpa del asesor', 'red', '@culpa')],
          title='Qué pasó con cada lead', right='+15 inmobiliarias'),
    phonelist('Tus asesores solo hablan y llaman desde su WhatsApp; el sistema registra cada chat, cada llamada y cada cita, y le dice a cada uno a quién llamar y a quién darle seguimiento.',
              [it('Chats registrados', '@chat', 'cyan', n=48), it('Llamadas registradas', '@llamada', 'purple', n=31),
               it('Citas', '@cita', 'green', n=6), it('A quién llamar hoy', '@llamar', 'amber', n=12)],
              'advisor_woman', title='Mi trabajo', sub='Registrado solo'),
    cta('Si tienes una inmobiliaria con más de 5 asesores y estás cansado de perder dinero, dale clic al botón de abajo.', '¿+5 ASESORES?'),
], music='drive', keywords=['marketing', 'basura', 'mentira', 'creerle', 'malo', 'culpa'])

video('C-por-que-te-llegan-puros-curiosos', 'c', 'Por qué a tu inmobiliaria le llegan puros curiosos', [
    photo('Esta es la razón por la que a tu inmobiliaria le siguen llegando puros curiosos y no personas que agendan una cita.',
          'scrolling_ads', ['PUROS [CURIOSOS]', 'Y CERO CITAS'], kicker='Inmobiliarias'),
    stack('Nunca le dices a Meta cuáles de las personas que te escribieron agendaron, cuáles apartaron y cuáles compraron.',
          [it('Quién agendó', '@agendaron', 'cyan'), it('Quién apartó', '@apartaron', 'purple'), it('Quién compró', '@compraron', 'green')],
          img='laptop_dashboard', title='LO QUE META NO SABE'),
    floatchats('Solo le dices «mándame mensajes» o «mándame formularios». Y Meta hace exactamente eso: te llena de curiosos que escriben y desaparecen.',
               'office_agents', ['«MÁNDAME', '[FORMULARIOS]»'], ['@mensajes', '@formularios'],
               bubbles=['¿Precio?', 'Info', '¿Sigue disponible?', 'Le piqué sin querer', 'Solo estoy viendo']),
    photo('Por eso tu asesor te dice «es que no me contestan».', 'advisor_car', ['«ES QUE NO', 'ME [CONTESTAN]»'], [0, '@contestan']),
    events('Lo que necesitas es un filtro. Cuando un lead agenda una cita, Lead Master se lo avisa a Meta en automático: «este lead pasó a cita agendada».',
           [{'name': 'Contactado con respuesta', 'count': 184, 'at': 0}, {'name': 'Cita agendada', 'count': 46, 'at': 4, 'hot': True},
            {'name': 'Apartado', 'count': 9, 'at': 8}, {'name': 'Vendido', 'count': 4, 'at': 12}],
           toastAt='@pasó', toast='Evento recibido: Cita agendada', toastSub='Campaña Mérida · hace 1 min'),
    flow('Meta empieza a buscar personas con más probabilidad de agendar un recorrido o un Zoom. Y cuando junta suficientes citas, le pides: «mándame solo gente parecida a la que sí agenda».',
         [node('Lead agenda cita', 0), node('Meta recibe el evento', '@buscar', 'purple'),
          node('Busca gente que agenda', '@recorrido', 'purple', sub='recorridos y Zooms'), node('Más citas, menos curiosos', '@parecida', 'green')]),
    cta('Deja de buscar a quien llena formularios. Nosotros lo instalamos y lo configuramos; tú no tocas nada. Dale clic al botón de abajo.',
        'TÚ NO TOCAS NADA'),
], keywords=['curiosos', 'filtro', 'formularios', 'contestan', 'agendada', 'agenda'])

video('D-los-crm-murieron-llegaron-los-cra', 'd', 'Los CRM inmobiliarios murieron: llegaron los CRA', [
    photo('Los CRM para el mundo inmobiliario han muerto. Llegaron los CRA: CRM que se llenan solos.',
          'excel_night', ['LOS CRM', '[MURIERON]'], kicker='Inmobiliarias', stamp={'text': 'LLEGARON LOS CRA', 'at': '@CRA', 'color': 'cyan', 'size': 80}),
    photo('La única ventaja de un CRM era saber qué pasaba con cada lead. Pero esa información se pierde el día que tu asesor deja de poner notas y de mover etapas.',
          'notebook', ['SIN NOTAS', 'NO HAY [DATOS]'], ['@pierde', '@notas']),
    photo('Y siempre deja de hacerlo, porque le da pereza capturar datos.', 'advisor_notebook', ['LE DA', '[PEREZA]'], [0, '@pereza']),
    photo('Ahí se fueron a la basura los miles de dólares que pagaste por tu CRM.', 'owner_stressed', ['MILES DE', '[DÓLARES]'],
          [0, '@dólares'], stamp={'text': 'A LA BASURA', 'at': '@basura'}),
    panel('Un CRA no depende de que nadie llene nada. Escucha las llamadas de cada asesor, lee su WhatsApp y registra solo el presupuesto, la zona, qué busca el lead y en qué etapa va.',
          [call('Andrés Molina', 'Diana Trejo', 'Presupuesto definido · Zona: Polanco · Busca 3 recámaras', 'Registrado solo', 'green', '@Escucha'),
           wa('Valeria Ríos', 'Lucía Hernández', 'Zona: Tulum · Busca depa para vivir · Etapa: interesada', 'Etapa: interesada', 'cyan', '@zona')],
          title='CRA: se llena solo'),
    phonelist('Y le dice en tiempo real a cada asesor qué hacer con cada lead. Antes tu equipo trabajaba para el CRM; ahora el CRA trabaja para tu equipo.',
              [it('Llama a Diana Trejo', '@dice', 'red', n=1, sub='Quedó de confirmar visita hoy'),
               it('Manda opciones a Lucía', '@qué', 'amber', n=2, sub='Lo prometiste ayer'),
               it('El CRA trabaja para ti', '@trabaja', 'green')], 'advisor_woman', title='Qué hacer ahora', sub='En tiempo real'),
    cta('Dale clic a este anuncio y te lo instalamos en tu inmobiliaria.', 'UN CRM QUE SE LLENA SOLO'),
], music='drive', keywords=['CRA', 'murieron', 'pereza', 'basura', 'solos', 'solo'])

video('E-asi-recibirias-tus-reportes', 'e', 'Así recibirías los reportes si usaras Lead Master', [
    photo('Así es como recibirías los reportes de tu inmobiliaria si usaras Lead Master.', 'owner_phone_report',
          ['ASÍ RECIBIRÍAS', 'TUS [REPORTES]'], kicker='Si usaras Lead Master'),
    floatchats('Hoy tus asesores empiezan el día sin un paso a paso. No saben a quién llamar ni a quién darle seguimiento, y no se acuerdan de lo que prometieron la semana pasada.',
               'advisor_woman', ['¿A QUIÉN', '[LLAMO] HOY?'], ['@llamar', '@prometieron']),
    photo('Abren WhatsApp, buscan entre cientos de chats y se les pasan leads. Y tú, para saber qué pasó, tienes que preguntar uno por uno o pelear con un Excel que nadie llena.',
          'excel_night', ['Y TÚ, PELEANDO', 'CON UN [EXCEL]'], ['@tú', '@Excel']),
    phonelist('Con Lead Master, cada mañana cada asesor recibe por WhatsApp su lista del día: a quién llamar, quién le pidió que lo buscara hoy y con quién tiene recorrido o Zoom.',
              [it('A quién llamar', '@llamar', 'red', n=9), it('Te pidió que lo buscaras hoy', '@pidió', 'amber', n=3),
               it('Recorridos y Zooms', '@recorrido', 'green', n=2)], 'advisor_woman', title='Tu lista de hoy', sub='WhatsApp · 8:00 am', clock='8:00'),
    phonelist('En la tarde recibe el resumen de lo que hizo.',
              [it('Resumen del día.pdf', '@resumen', 'purple', sub='14 llamadas · 6 contactados · 2 citas')], 'advisor_car',
              title='Tu día', sub='7:00 pm', clock='7:00'),
    phonelist('Y tú, como dueño, recibes todos los días en tu WhatsApp el reporte del equipo: cuántos leads entraron, a quién llamó cada asesor, quién se quedó sin contacto y cuántas citas salieron.',
              [it('Leads que entraron', '@entraron', 'cyan', n=37), it('Llamadas del equipo', '@llamó', 'purple', n=84),
               it('Sin contacto', '@contacto', 'red', n=6), it('Citas', '@citas', 'green', n=5)],
              'owner_phone_report', title='Reporte del equipo', sub='Lead Master · todos los días'),
    cta('Así ya no se te pasa ningún lead. Dale clic a este anuncio y te lo instalamos.', 'NINGÚN LEAD SE TE PASA'),
], voice=ANT, keywords=['reportes', 'reporte', 'lista', 'resumen', 'Excel'])

video('F-que-es-lead-master-en-un-minuto', 'f', 'Qué es Lead Master, en un minuto', [
    photo('Si tienes una inmobiliaria, te explico en un minuto qué es Lead Master y por qué ya lo usan más de 15 inmobiliarias en México, Colombia y Estados Unidos.',
          'showroom', ['LEAD MASTER', 'EN [UN MINUTO]'], kicker='Inmobiliarias'),
    flow('Uno: junta todos tus leads de portales, referidos y anuncios, y los reparte entre tus asesores; si uno no atiende a tiempo, pasa al siguiente.',
         [node('Portales · referidos · anuncios', '@portales'), node('Lead Master', '@reparte', 'purple'),
          node('Asesor asignado', '@asesores', 'cyan'), node('Si no atiende, pasa al siguiente', '@siguiente', 'amber')], title='1 · TODOS TUS LEADS'),
    panel('Dos: como vive en el WhatsApp y las llamadas de cada asesor, sabe a quién contactaron, a quién no y cuánto tardaron.',
          [wa('Valeria Ríos', 'Diana Trejo', 'Contactada en 4 minutos.', 'Contactado', 'green', '@contactaron'),
           call('Diego Herrera', 'Adriana Solís', 'Sin llamada en 26 horas.', 'Sin contacto', 'red', '@no'),
           wa('Paola Gutiérrez', 'Lucía Hernández', 'Primer mensaje a las 3 h 10 min.', 'Tarde', 'amber', '@tardaron')],
          title='2 · Qué pasó con cada lead'),
    phonelist('Tres: cada día le dice a cada asesor a quién llamar.',
              [it('Lo urgente', '@día', 'red', n=3), it('Nunca los has buscado', '@llamar', 'amber', n=5)], 'advisor_woman',
              title='3 · Mi trabajo', sub='Qué debo hacer hoy'),
    phonelist('Cuatro: te da los reportes sin que nadie llene nada.',
              [it('Reporte semanal.pdf', '@reportes', 'purple', sub='214 leads · 19 citas · 4 apartados')], 'owner_phone_report',
              title='4 · Tus reportes', sub='Sin que nadie llene nada'),
    events('Cinco: le avisa a Meta quién sí agenda y compra, para que te traiga más compradores y menos curiosos.',
           EV_BASE, toastAt='@agenda', toast='Evento recibido: Zoom agendado', toastSub='5 · Meta aprende quién compra'),
    cta('Leads ordenados, asesores que saben qué hacer y tú con el control, sin perseguir a nadie. Dale clic y te lo instalamos en tu inmobiliaria.',
        'TÚ CON EL CONTROL'),
], voice=ANT, music='drive', tempo=1.12, keywords=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco'])

# =====================================================================
# Fórmula ganadora de Laura (G1–G6)
# =====================================================================

video('G1-si-yo-tuviera-una-inmobiliaria', 'g1', 'Si yo tuviera una inmobiliaria en México con más de 5 asesores', [
    photo('Si yo tuviera una inmobiliaria en México con más de 5 asesores y no supiera qué hacen con los leads que les doy, esto es lo que haría para tener control total de mi equipo y vender más.',
          'gdl_development', ['ESTO ES LO', 'QUE [YO HARÍA]'], kicker='Inmobiliaria con +5 asesores'),
    photo('Porque hoy le das los leads a tu equipo y ahí se pierde la pista: no sabes a quién llamaron, cuánto tardaron ni qué le dijeron.',
          'office_agents', ['¿A QUIÉN LLAMARON?', '¿QUÉ LE [DIJERON]?'], ['@llamaron', '@dijeron'], size=104),
    phonelist('Lo primero que haría es instalar un sistema que le diga a cada asesor a quién llamar y en qué momento, sin que él lo decida.',
              [it('Llamar a Diana Trejo', '@llamar', 'red', n=1, sub='Ahora'), it('Llamar a Lucía Hernández', '@momento', 'amber', n=2, sub='11:30 am')],
              'headset_calls', title='1 · Mi trabajo', sub='El sistema decide el orden'),
    bars('Ese mismo sistema registra cuántas llamadas hace, cuánto tarda en marcar y qué habla en cada una.',
         [{'name': 'Paola Gutiérrez', 'value': 34, 'sub': 'llamadas'}, {'name': 'Valeria Ríos', 'value': 27, 'sub': 'llamadas'},
          {'name': 'Diego Herrera', 'value': 9, 'sub': 'llamadas'}, {'name': 'Andrés Molina', 'value': 4, 'sub': 'llamadas'}],
         title='Llamadas de hoy', at='@registra'),
    phonelist('Lo segundo: recordatorios para que haga todos los intentos que le pido, y si no los hace, que me avise.',
              [it('Te faltan 2 intentos con Adriana Solís', '@recordatorios', 'amber'), it('Aviso al dueño: intentos sin hacer', '@avise', 'red')],
              'advisor_car', title='2 · Recordatorios', sub='Hasta que se cumplan'),
    panel('Y lo último: entender qué hace mi mejor vendedor y cómo maneja cada objeción, para que todo el equipo siga ese mismo camino.',
          [call('Paola Gutiérrez', 'Diana Trejo', 'Objeción: «está muy caro». Comparó con lo que paga de renta y la invitó a ver el proyecto.', 'Cita agendada', 'green', '@objeción')],
          title='3 · Tu mejor vendedor', right='Cómo maneja objeciones'),
    cta('Ese sistema es Lead Master. Si quieres que te lo instalemos en tu inmobiliaria, dale clic al link de abajo.', 'TE LO INSTALAMOS',
        button='Dale clic al link'),
], keywords=['control', 'primero', 'segundo', 'último', 'objeción', 'vendedor'])

video('G2-no-puedo-creer-que-todavia-confies', 'g2', 'No puedo creer que todavía confíes en lo que te dicen', [
    photo('No puedo creer que teniendo una inmobiliaria con más de 5 asesores todavía confíes en lo que tus asesores te dicen que hacen.',
          'owner_stressed', ['¿TODAVÍA LES', '[CREES]?'], [0, '@confíes'], kicker='Inmobiliaria con +5 asesores'),
    chat('Te dicen que llamaron, que el lead no contestó, que le mandaron seguimiento. Pero no tienes forma de comprobarlo.',
         [{'from': 'in', 'text': 'Sí le marqué, jefe. No contestó.', 'at': '@llamaron'},
          {'from': 'in', 'text': 'Ya le mandé seguimiento.', 'at': '@seguimiento'}],
         'advisor_car', 'Diego Herrera', sub='Asesor'),
    photo('Y lo peor: hay asesores que se van de tu inmobiliaria y se llevan tus leads, clientes que tú pagaste, porque nunca tuviste control de lo que estaban haciendo.',
          'empty_desk', ['SE VAN', 'CON TUS [LEADS]'], ['@van', '@leads'], stamp={'text': 'LEADS QUE TÚ PAGASTE', 'at': '@pagaste', 'size': 72}),
    panel('Lead Master registra cada llamada, cada chat y cada interacción, sin que el asesor llene nada y sin depender de lo que él te reporte.',
          [call('Diego Herrera', 'Adriana Solís', 'Llamada 10:42 · 0:00 · no contestó · no volvió a marcar.', 'Sin seguimiento', 'red', '@llamada'),
           wa('Valeria Ríos', 'Diana Trejo', 'Mandó 3 opciones y agendó visita.', 'Sigue el proceso', 'green', '@chat')],
          title='Lo que sí pasó'),
    stack('Sabes quién llamó, cuándo, qué dijo y si está siguiendo el proceso. Y si se va, el historial se queda contigo.',
          [it('Quién llamó y cuándo', '@quién'), it('Qué dijo', '@dijo', 'purple'), it('Si sigue el proceso', '@proceso', 'green'),
           it('El historial se queda contigo', '@historial', 'amber')], img='meeting'),
    cta('Recuerda: los leads son tuyos, no de tu asesor. Si quieres dejar de perder dinero por no tener control, dale clic al link de abajo.',
        'LOS LEADS SON TUYOS', button='Dale clic al link'),
], music='drive', keywords=['confíes', 'comprobarlo', 'peor', 'pagaste', 'historial', 'tuyos'])

video('G3-si-crees-que-se-roban-los-leads', 'g3', 'Si crees que tus asesores se roban los leads', [
    photo('Si tienes una inmobiliaria en México con más de 5 asesores y crees que se roban los leads que les das, esto es lo que yo haría para tener control.',
          'advisor_car', ['¿SE ROBAN', 'TUS [LEADS]?'], kicker='Inmobiliaria con +5 asesores'),
    photo('Porque mientras el lead viva en el WhatsApp personal y en el celular de cada asesor, no ves qué le dijeron, si le ofrecieron otro proyecto ni si lo están trabajando por fuera.',
          'advisor_night', ['TODO EN SU', '[CELULAR]'], ['@WhatsApp', '@celular'], stamp={'text': 'POR FUERA', 'at': '@fuera'}),
    flow('Lo primero: conectar el WhatsApp de cada asesor a mi CRM. Solo las conversaciones con leads; lo personal no.',
         [node('WhatsApp del asesor', '@WhatsApp'), node('Tu CRM', '@CRM', 'green'), node('Solo chats con leads', '@Solo', 'amber', sub='lo personal no')],
         title='1 · WHATSAPP CONECTADO'),
    phonelist('Lo segundo: que todas las llamadas salgan del sistema, con el número del asesor, y queden grabadas. Ya no hay llamadas por fuera que yo no vea.',
              [it('Diego Herrera → Adriana Solís', '@llamadas', 'green', sub='4:12 min · grabada'),
               it('Paola Gutiérrez → Diana Trejo', '@grabadas', 'green', sub='2:05 min · grabada'),
               it('Llamadas por fuera', '@fuera', 'cyan', n=0)], 'headset_calls', title='2 · Llamadas grabadas', sub='Desde el sistema'),
    stack('Y lo último: que si un lead se queda sin seguimiento o pasa algo raro, me llegue un aviso. Si el asesor se va, el historial se queda en mi inmobiliaria.',
          [it('Lead sin seguimiento', '@seguimiento', 'amber', k='Aviso'), it('Algo raro con un lead', '@raro', 'red', k='Aviso'),
           it('El historial se queda', '@historial', 'green', k='Si se va')], img='empty_desk', title='3 · AVISOS'),
    cta('Eso hace Lead Master. Si quieres que te ayudemos a instalarlo, dale clic al link de abajo.', 'TUS LEADS, PROTEGIDOS',
        button='Dale clic al link'),
], keywords=['roban', 'fuera', 'grabadas', 'aviso', 'raro', 'historial'])

video('G4-si-yo-vendiera-desarrollos', 'g4', 'Si yo vendiera desarrollos y mis leads no contestaran', [
    photo('Si yo vendiera desarrollos con más de 5 asesores y mis leads de Meta no contestaran, esto es lo que haría.',
          'monterrey_tower', ['«LOS LEADS NO', '[CONTESTAN]»'], kicker='Desarrollos · +5 asesores'),
    photo('Porque «los leads no contestan» casi nunca es todo el problema. Le pediste a Meta formularios y te mandó gente que llena formularios.',
          'scrolling_ads', ['PEDISTE', '[FORMULARIOS]'], ['@pediste', '@formularios']),
    stat('Y en las inmobiliarias que medimos, la mitad de los leads esperó más de 2 horas por el primer contacto.',
         [num(2, 'esperó la mitad de los leads por el primer contacto', '@2', 'red', prefix='+', suffix=' h')],
         foot='6,497 leads de 11 inmobiliarias en 60 días'),
    flow('Lo primero: que cada lead le llegue al asesor en el momento, y si no hay llamada en el tiempo que yo pongo, que pase a otro.',
         [node('Entra el lead', '@lead'), node('Le llega al asesor', '@asesor', 'cyan'),
          node('¿No llamó a tiempo?', '@pase', 'amber', sub='pasa a otro asesor')], title='1 · AL INSTANTE'),
    events('Lo segundo: que el sistema detecte en el chat cuando un lead agenda un recorrido o un Zoom y se lo avise a Meta, para que mis anuncios busquen gente así.',
           [{'name': 'Recorrido agendado', 'count': 23, 'at': '@recorrido', 'hot': True}, {'name': 'Zoom agendado', 'count': 31, 'at': '@Zoom'},
            {'name': 'Apartado', 'count': 6, 'at': '@avise'}],
           toastAt='@avise', toast='Evento recibido: Recorrido agendado', toastSub='2 · Meta busca gente así'),
    bars('Y lo último: medir cada campaña hasta el final, con citas, apartados y ventas, no solo leads.',
         [{'name': 'Campaña Tulum', 'value': 19, 'sub': 'citas'}, {'name': 'Campaña Mérida', 'value': 11, 'sub': 'citas'},
          {'name': 'Campaña CDMX', 'value': 3, 'sub': 'citas'}], title='3 · Citas por campaña', at='@campaña'),
    cta('Eso es Lead Master. Dale clic al link de abajo y te lo instalamos.', 'TE LO INSTALAMOS', button='Dale clic al link'),
], music='drive', keywords=['contestan', 'formularios', 'recorrido', 'Zoom', 'campaña'])

video('G5-no-puedo-creer-que-pagues-un-crm-que-nadie-llena', 'g5', 'No puedo creer que sigas pagando un CRM que nadie llena', [
    photo('No puedo creer que tu inmobiliaria siga pagando un CRM que tus asesores no llenan.',
          'excel_night', ['UN CRM QUE', '[NADIE LLENA]'], kicker='Inmobiliarias'),
    stack('Pagaste la licencia, pagaste la instalación, hiciste juntas y pusiste multas.',
          [it('Licencia pagada', '@licencia', 'amber'), it('Instalación pagada', '@instalación', 'amber'), it('Juntas y multas', '@juntas', 'red')],
          img='meeting'),
    photo('Y el CRM sigue vacío: sin notas, sin etapas, con leads de hace meses en «nuevo».',
          'notebook', ['SIN NOTAS.', 'SIN [ETAPAS].'], ['@notas', '@etapas'], stamp={'text': 'VACÍO', 'at': '@vacío', 'size': 110}),
    quote('«El talón de Aquiles de todos es poner notas», nos dijo un dueño. Y con un CRM vacío, decides a ciegas.',
          'El talón de Aquiles de todos es poner notas.', 'owner_stressed'),
    panel('Con Lead Master el CRM se llena solo. La IA lee el WhatsApp y escucha las llamadas de cada asesor; escribe la nota, el presupuesto, la zona y las objeciones; mueve la etapa y crea la tarea del siguiente paso.',
          [wa('Valeria Ríos', 'Diana Trejo', 'Nota: busca 2 recámaras en Tulum · Objeción: precio · Siguiente paso: recorrido el jueves.', 'Etapa movida', 'green', '@escribe'),
           call('Andrés Molina', 'Lucía Hernández', 'Tarea creada: mandar planos el lunes.', 'Tarea creada', 'cyan', '@tarea')],
          title='La IA llenó esto'),
    photo('Tu asesor solo habla con el lead. Y tú recibes cada día el reporte de lo que pasó.', 'owner_relaxed',
          ['TU ASESOR', 'SOLO [HABLA]'], [0, '@habla']),
    cta('Antes tu equipo trabajaba para el CRM; ahora el CRM trabaja para tu equipo. Dale clic al link de abajo.', 'EL CRM TRABAJA PARA TI',
        button='Dale clic al link'),
], keywords=['vacío', 'multas', 'notas', 'solo', 'ciegas'])

video('G6-si-la-mitad-de-mis-leads-llegara-de-noche', 'g6', 'Si casi la mitad de mis leads llegara de noche', [
    photo('Si yo tuviera una inmobiliaria con más de 5 asesores y casi la mitad de mis leads llegara de noche o en fin de semana, esto es lo que haría.',
          'woman_night_phone', ['LEADS DE', '[NOCHE]'], kicker='Inmobiliaria con +5 asesores'),
    stat('Porque así pasa: de 6,497 leads que medimos, el 47% llegó fuera de horario, y la mitad de esos esperó más de 10 horas por la primera respuesta.',
         [num(47, 'llegó fuera de horario', '@47%', 'amber', suffix='%'), num(10, 'esperó la mitad por la primera respuesta', '@10', 'red', prefix='+', suffix=' h')],
         foot='6,497 leads medidos en Lead Master'),
    photo('Para entonces ya le habían escrito a otra inmobiliaria.', 'night_building', ['YA LE ESCRIBIÓ', 'A [OTRA]'], [0, '@otra']),
    flow('Lo primero: una guardia en la noche y los fines de semana, con los leads asignados solos.',
         [node('Lead a las 11 pm', 0), node('Asesor de guardia', '@guardia', 'purple'), node('Asignado solo', '@asignados', 'green')],
         title='1 · GUARDIA'),
    phonelist('Lo segundo: que a primera hora cada asesor tenga en su lista los leads de la noche, con un tiempo para llamar, y si no llama, que pasen a otro.',
              [it('Leads de la noche', '@noche', 'red', n=4), it('Tiempo para llamar', '@tiempo', 'amber', sub='20 minutos'),
               it('Si no llamas, pasa a otro', '@pasen', 'purple')], 'advisor_woman', title='2 · Mi trabajo', sub='8:00 am', clock='8:00'),
    bars('Y lo último: ver cada semana cuánto tarda cada asesor en responder, para saber quién está dejando enfriar los leads.',
         [{'name': 'Paola Gutiérrez', 'value': 6, 'sub': 'min'}, {'name': 'Valeria Ríos', 'value': 14, 'sub': 'min'},
          {'name': 'Diego Herrera', 'value': 95, 'sub': 'min', 'color': 'red'}], title='3 · Tiempo de respuesta', at='@tarda'),
    cta('Eso hace Lead Master. Dale clic al link de abajo y te lo instalamos en tu inmobiliaria.', 'NINGÚN LEAD SE ENFRÍA',
        button='Dale clic al link'),
], music='drive', keywords=['noche', 'guardia', 'horario', 'enfriar'])

# =====================================================================
# Las 25 ideas nuevas
# =====================================================================

video('01-si-yo-tuviera-una-inmobiliaria-en-guadalajara', 'n01', 'Si yo tuviera una inmobiliaria en Guadalajara', [
    photo('Si yo tuviera una inmobiliaria en Guadalajara con más de 5 asesores y no supiera qué hacen con los leads que les doy, esto es lo que haría para tener control y vender más.',
          'gdl_development', ['ESTO ES LO', 'QUE [YO HARÍA]'], kicker='Guadalajara · +5 asesores'),
    floatchats('Porque hoy, seguramente, inviertes en anuncios, los leads le llegan al WhatsApp de cada asesor y ahí se pierde la pista.',
               'office_agents', ['SE PIERDE', 'LA [PISTA]'], ['@pierde', '@pista']),
    photo('No sabes a quién le contestaron, a quién nunca llamaron y a quién dejaron en visto. Y cuando preguntas, todos te dicen que bien.',
          'owner_stressed', ['¿A QUIÉN DEJARON', 'EN [VISTO]?'], ['@contestaron', '@visto'], size=104,
          stamp={'text': '«TODO BIEN, JEFE»', 'at': '@bien', 'color': 'amber', 'size': 84}),
    flow('Primero, conectaría el WhatsApp y las llamadas de cada asesor al CRM, para que todo quede registrado sin que nadie capture nada.',
         [node('WhatsApp de cada asesor', '@WhatsApp'), node('Llamadas', '@llamadas', 'purple'),
          node('CRM', '@registrado', 'green', sub='sin que nadie capture')], title='1 · TODO REGISTRADO'),
    panel('Segundo, dejaría que la IA llene la nota, el presupuesto, la zona y la etapa de cada lead.',
          [wa('Valeria Ríos', 'Diana Trejo', 'Presupuesto definido · Zona: Zapopan · Busca casa con jardín', 'Nota escrita', 'green', '@nota'),
           call('Andrés Molina', 'Lucía Hernández', 'Zona: Providencia · Etapa: cita para el sábado', 'Etapa movida', 'cyan', '@etapa')],
          title='2 · La IA llena el CRM'),
    phonelist('Tercero, pediría que todos los días me llegue a mi WhatsApp el reporte: cuántos leads entraron, a quién llamó cada asesor y quién se quedó sin contacto. Eso es Lead Master.',
              [it('Leads que entraron', '@entraron', 'cyan', n=23), it('Llamadas del equipo', '@llamó', 'purple', n=61),
               it('Sin contacto', '@contacto', 'red', n=5)], 'owner_phone_report', title='3 · Reporte del día', sub='Lead Master · 8:00 pm'),
    cta('Si tienes una inmobiliaria con más de 5 asesores, dale clic al botón de abajo y te lo instalamos.', '+5 ASESORES'),
], keywords=['Guadalajara', 'pista', 'visto', 'Primero', 'Segundo', 'Tercero'])

video('02-vendes-desarrollos-y-tienes-este-problema', 'n02', 'Vendes desarrollos y tienes este problema', [
    photo('Si vendes desarrollos inmobiliarios, seguro tienes este problema.', 'construction', ['¿VENDES', '[DESARROLLOS]?'],
          kicker='Desarrollos inmobiliarios'),
    stat('Lanzas un proyecto, metes dinero en anuncios y te llegan 500 leads en un mes.',
         [num(500, 'leads en el primer mes del lanzamiento', '@500')], img='aerial_community'),
    photo('Pero la sala de ventas sigue vacía. Tus asesores dicen que los leads son malos y que nadie contesta. Marketing dice que no les llaman a tiempo.',
          'empty_salesroom', ['SALA DE VENTAS', '[VACÍA]'], [0, '@vacía']),
    photo('Y tú no tienes cómo saber quién tiene la razón.', 'marketing_sales_fight', ['¿QUIÉN TIENE', 'LA [RAZÓN]?'], [0, '@razón']),
    stat('Cuando medimos 6,497 leads de 11 inmobiliarias, 1 de cada 3 nunca habló con una persona. No eran malos: nadie los atendió.',
         [num(6497, 'leads medidos en 11 inmobiliarias', '@6,497'), num(1, 'nunca habló con una persona', '@nunca', 'red', suffix=' de cada 3')]),
    panel('Lead Master se conecta al WhatsApp y a las llamadas de tus asesores y te dice qué pasó con cada lead del lanzamiento: quién contestó, quién agendó recorrido, quién se descartó y por qué, y a quién nadie llamó.',
          [wa('Valeria Ríos', 'Diana Trejo', 'Agendó recorrido para el sábado.', 'Recorrido', 'green', '@agendó'),
           call('Andrés Molina', 'Lucía Hernández', 'Descartado: buscaba renta, no compra.', 'Descartado', 'amber', '@descartó'),
           wa('Diego Herrera', 'Adriana Solís', 'Nadie la llamó en 4 días.', 'Sin contacto', 'red', '@nadie')],
          title='Tu lanzamiento, lead por lead'),
    events('Y le avisa a Meta quién sí agenda, para que tus campañas te traigan más de esos.',
           [{'name': 'Recorrido agendado', 'count': 38, 'at': 0, 'hot': True}, {'name': 'Apartado', 'count': 7, 'at': 4}],
           toastAt='@agenda', toast='Evento recibido: Recorrido agendado', toastSub='Lanzamiento · hace 3 min'),
    cta('Si estás vendiendo un desarrollo y quieres llenar tu sala de ventas, dale clic al botón de abajo.', 'LLENA TU SALA DE VENTAS'),
], music='drive', tempo=1.12, keywords=['desarrollos', 'vacía', 'razón', 'lanzamiento', 'recorrido'])

video('03-este-crm-se-mueve-solo', 'n03', 'Este CRM se mueve solo', [
    photo('Este CRM se mueve solo. Y está hecho para inmobiliarias.', 'laptop_dashboard', ['ESTE CRM', 'SE MUEVE [SOLO]'],
          kicker='Para inmobiliarias'),
    stack('Si tienes una inmobiliaria, ya sabes cómo termina todo CRM. La primera semana tus asesores lo llenan. La segunda dejan de poner notas. Al mes, el pipeline es una mentira:',
          [it('Lo llenan', '@primera', 'green', k='Semana 1'), it('Dejan de poner notas', '@segunda', 'amber', k='Semana 2'),
           it('El pipeline es una mentira', '@mes', 'red', k='Mes 1')], img='excel_night'),
    photo('leads de hace tres meses siguen en «nuevo» y nadie sabe en qué quedó cada uno. Y tú decides con datos que nadie actualizó.',
          'owner_stressed', ['3 MESES', 'EN [«NUEVO»]'], [0, '@nuevo']),
    chat('Mira lo que pasa con Lead Master. Tu asesora le escribe al lead por WhatsApp, como siempre. El lead le cuenta que busca un departamento de dos recámaras en Tulum y que puede ver el proyecto el jueves.',
         [{'from': 'out', 'text': 'Hola Lucía, ¿qué estás buscando?', 'at': '@escribe'},
          {'from': 'in', 'text': 'Un depa de 2 recámaras en Tulum.', 'at': '@busca'},
          {'from': 'in', 'text': 'Puedo ir a ver el proyecto el jueves.', 'at': '@jueves'}],
         'advisor_woman', 'Lucía Hernández', sub='Lead · Tulum'),
    panel('Sin que ella toque nada, el sistema anota qué busca, la zona y el presupuesto, escribe la nota, mueve la etapa y le deja lista la cita del jueves para confirmar. Tu CRM, por fin, dice la verdad.',
          [wa('Valeria Ríos', 'Lucía Hernández', 'Busca 2 recámaras · Zona: Tulum · Presupuesto definido', 'Datos anotados', 'cyan', '@anota'),
           wa('Valeria Ríos', 'Lucía Hernández', 'Nota escrita por la IA · Etapa: cita', 'Etapa movida', 'green', '@etapa'),
           wa('Valeria Ríos', 'Lucía Hernández', 'Cita del jueves lista', 'Confirmar en un clic', 'amber', '@confirmar')],
          title='CRM · Lucía Hernández', right='Se llenó solo'),
    cta('Dale clic al botón de abajo y te lo instalamos en tu inmobiliaria.', 'TU CRM DICE LA VERDAD'),
], keywords=['solo', 'mentira', 'nuevo', 'verdad'])

video('04-separa-curiosos-de-compradores', 'n04', 'El sistema que separa a los curiosos de los compradores', [
    photo('Este es el sistema que separa a los curiosos de los compradores en tu inmobiliaria, antes de que tus asesores pierdan el día.',
          'showing_tour', ['CURIOSOS VS', '[COMPRADORES]'], kicker='Inmobiliarias'),
    floatchats('Te llegan cientos de mensajes: «¿cuánto cuesta?», «¿sigue disponible?», «mándame info». Tus asesores contestan uno por uno, como pueden.',
               'office_agents', ['CIENTOS DE', '[MENSAJES]'], [0, '@mensajes'],
               bubbles=['¿Cuánto cuesta?', '¿Sigue disponible?', 'Mándame info', '¿Aceptan mascotas?', 'Solo estoy viendo']),
    photo('Y mientras le responden al que solo está viendo, la persona que sí quiere comprar se queda esperando. Cuando por fin le contestan, ya agendó con otra inmobiliaria.',
          'couple_tour', ['EL COMPRADOR', 'SE [FUE]'], ['@comprar', '@otra'], stamp={'text': 'AGENDÓ CON OTRA', 'at': '@otra+8', 'size': 80}),
    panel('Lead Master lee cada conversación y saca lo que importa: qué busca, en qué zona, con qué presupuesto y qué tan pronto quiere comprar. Con eso, cada asesor sabe a quién atender primero.',
          [wa('Valeria Ríos', 'Diana Trejo', 'Quiere comprar este mes · Zona: Polanco · Presupuesto definido', 'Atender primero', 'green', '@busca'),
           wa('Diego Herrera', 'Lucía Hernández', 'Solo preguntó el precio.', 'Después', 'amber', '@primero')],
          title='Prioridad de hoy'),
    events('Y cuando un lead agenda una cita, el sistema se lo avisa a Meta, para que tus anuncios busquen más gente así y menos curiosos.',
           [{'name': 'Cita agendada', 'count': 52, 'at': 0, 'hot': True}, {'name': 'Apartado', 'count': 7, 'at': 6}],
           toastAt='@avisa', toast='Evento recibido: Cita agendada', toastSub='Más gente así, menos curiosos'),
    cta('Si tu inmobiliaria recibe más de 100 leads al mes, dale clic al botón de abajo.', '+100 LEADS AL MES'),
], music='drive', keywords=['curiosos', 'compradores', 'primero', 'esperando'])

video('05-departamentos-de-mas-de-150-mil-dolares', 'n05', 'Si vendes departamentos de más de 150 mil dólares', [
    photo('Si vendes departamentos de más de 150 mil dólares y no tienes este sistema, estás perdiendo compradores serios entre cientos de mensajes.',
          'living_ocean', ['COMPRADORES', '[SERIOS]'], kicker='Depas de +150 mil USD'),
    photo('La persona que tiene el dinero para comprar no le escribe solo a tu inmobiliaria. Le escribe a tres o cuatro al mismo tiempo.',
          'couple_tour', ['LE ESCRIBE A', '[4 INMOBILIARIAS]'], [0, '@cuatro']),
    photo('Y casi siempre compra con la que le contesta primero, le resuelve las dudas y la invita a ver el proyecto.',
          'showing_tour', ['GANA LA QUE', 'CONTESTA [PRIMERO]'], [0, '@primero']),
    stat('En las inmobiliarias que medimos, la mitad de los leads esperó más de 2 horas por el primer contacto. Solo 17 de cada 100 recibieron respuesta en 5 minutos.',
         [num(2, 'esperó la mitad por el primer contacto', '@2', 'red', prefix='+', suffix=' h'),
          num(17, 'de cada 100 recibieron respuesta en 5 minutos', '@17', 'amber')], foot='6,497 leads de 11 inmobiliarias'),
    flow('Con Lead Master, cada lead llega directo al asesor que le toca, con aviso por WhatsApp. Si no hay llamada en el tiempo que tú decides, pasa al siguiente asesor.',
         [node('Lead nuevo', 0), node('Aviso por WhatsApp al asesor', '@WhatsApp', 'cyan'),
          node('¿Sin llamada a tiempo?', '@siguiente', 'amber', sub='pasa al siguiente asesor')]),
    bars('Y tú ves cuánto tarda cada uno en responder, con cada lead.',
         [{'name': 'Paola Gutiérrez', 'value': 4, 'sub': 'min'}, {'name': 'Valeria Ríos', 'value': 9, 'sub': 'min'},
          {'name': 'Andrés Molina', 'value': 38, 'sub': 'min'}, {'name': 'Diego Herrera', 'value': 126, 'sub': 'min', 'color': 'red'}],
         title='Tiempo de respuesta', at='@tarda'),
    cta('Dale clic al botón de abajo y te lo instalamos en tu inmobiliaria en 7 días.', 'LISTO EN 7 DÍAS'),
], keywords=['serios', 'primero', 'dólares'])

video('06-el-problema-no-es-la-cantidad-de-leads', 'n06', 'El problema no es la cantidad de leads', [
    photo('El problema de tu inmobiliaria no es la cantidad de leads que te llegan.', 'dashboard_tv', ['NO TE FALTAN', '[LEADS]'],
          kicker='Inmobiliarias'),
    stack('Cuando las ventas no salen, todos piden lo mismo: más leads, mejores leads, otra agencia.',
          [it('Más leads', '@más', 'amber'), it('Mejores leads', '@mejores', 'amber'), it('Otra agencia', '@agencia', 'red')],
          img='meeting', title='LO QUE TODOS PIDEN'),
    stat('Pero cuando medimos 6,497 leads de 11 inmobiliarias durante 60 días, 1 de cada 3 nunca habló con una persona. No contestaron mal: nadie los llamó.',
         [num(1, 'nunca habló con una persona', '@1', 'red', suffix=' de cada 3')], foot='6,497 leads de 11 inmobiliarias en 60 días'),
    stat('Y lo más raro es que se quedaron sin contacto más los que llegaron en horario de oficina que los de la noche. Estás pagando leads que tu propio equipo no atiende.',
         [num(40, 'sin contacto en horario de oficina', '@oficina', 'red', suffix='%'), num(33, 'sin contacto de noche', '@noche', 'amber', suffix='%')]),
    panel('Lead Master te dice, el mismo día y con nombre, qué leads nadie ha llamado, quién los tiene asignados y cuánto llevan esperando. Y a cada asesor le marca a quién buscar primero.',
          [wa('Diego Herrera', 'Adriana Solís', 'Esperando desde hace 5 horas.', 'Sin contacto', 'red', '@nadie'),
           call('Andrés Molina', 'Lucía Hernández', 'Esperando desde hace 26 horas.', 'Sin contacto', 'red', '@asignados'),
           wa('Valeria Ríos', 'Diana Trejo', 'Buscar primero.', 'Urgente', 'amber', '@primero')], title='Sin contacto hoy'),
    cta('Antes de comprar más leads, atiende los que ya pagaste. Dale clic al botón de abajo.', 'ATIENDE LOS QUE YA PAGASTE'),
], music='drive', keywords=['oficina', 'pagando', 'raro'])

video('07-tus-asesores-se-pueden-estar-robando-tus-leads', 'n07', 'Tus asesores se pueden estar robando tus leads', [
    photo('Tus asesores inmobiliarios se pueden estar robando los leads que pagaste y tú ni cuenta te das.',
          'advisor_car', ['TE PUEDEN ESTAR', '[ROBANDO] LEADS'], kicker='Inmobiliarias'),
    photo('Le escriben al lead desde su WhatsApp personal y le llaman desde su celular. Ahí pierdes el control.',
          'advisor_night', ['SU WHATSAPP.', 'SU [CELULAR].'], ['@WhatsApp', '@celular'], stamp={'text': 'SIN CONTROL', 'at': '@control'}),
    stack('No sabes qué le dijeron, si le ofrecieron otro proyecto o si lo están trabajando por fuera. Y el día que renuncian, se van con todas esas conversaciones.',
          [it('¿Qué le dijeron?', '@dijeron', 'amber'), it('¿Le ofrecieron otro proyecto?', '@ofrecieron', 'red'),
           it('¿Lo trabajan por fuera?', '@fuera', 'red')], img='empty_desk'),
    quote('Un director comercial nos lo dijo así: «la forma en la que se roban los leads es precisamente por las llamadas».',
          'La forma en la que se roban los leads es precisamente por las llamadas.', 'headset_calls', who='Director comercial de un desarrollo'),
    flow('Con Lead Master, el WhatsApp de cada asesor queda conectado a tu CRM: solo se guardan las conversaciones con leads, lo personal no. Las llamadas salen del sistema, con el número del asesor, y quedan grabadas. Y si un lead se queda sin seguimiento o pasa algo raro, te avisa.',
         [node('WhatsApp del asesor', '@WhatsApp'), node('Solo chats con leads', '@personal', 'amber', sub='lo personal no'),
          node('Llamadas desde el sistema', '@llamadas', 'purple', sub='grabadas'), node('Aviso si pasa algo raro', '@raro', 'red')]),
    cta('Los leads son tuyos, tú los pagaste. Dale clic al botón de abajo.', 'LOS LEADS SON TUYOS'),
], tempo=1.12, keywords=['robando', 'control', 'fuera', 'grabadas', 'raro'])

video('08-9-mil-dolares-en-anuncios', 'n08', '9 mil dólares en anuncios y ni un departamento vendido', [
    photo('Una inmobiliaria metió 9 mil dólares en anuncios y no vendió ni un departamento.', 'owner_stressed',
          ['9 MIL DÓLARES.', '[0] VENTAS.'], kicker='Caso real'),
    stack('Le llegaron 700 leads. El dueño culpó a Meta, después a la agencia, después a los leads.',
          [it('Meta', '@Meta', 'amber', k='Culpa de'), it('La agencia', '@agencia', 'amber', k='Culpa de'),
           it('Los leads', '@leads#2', 'red', k='Culpa de')], img='meeting', title='700 LEADS'),
    stat('Pero cuando revisamos los números, el problema estaba en otro lado: para trabajar bien esos 700 leads tocaba hacer unas 9 mil llamadas. El equipo hizo 3 mil.',
         [num(9000, 'llamadas que tocaba hacer', '@9'), num(3000, 'llamadas que hicieron', '@3', 'red')]),
    photo('Dos de cada tres intentos nunca pasaron. Y nadie lo sabía, porque nadie lo estaba midiendo.', 'headset_calls',
          ['2 DE CADA 3', '[NUNCA PASARON]'], [0, '@pasaron']),
    bars('Lead Master mide eso por ti: cuántas llamadas hizo cada asesor, cuántos leads contestaron, a quién nunca se le dio seguimiento y cuántas citas salieron de cada campaña.',
         [{'name': 'Paola Gutiérrez', 'value': 412, 'sub': 'llamadas'}, {'name': 'Valeria Ríos', 'value': 298, 'sub': 'llamadas'},
          {'name': 'Andrés Molina', 'value': 61, 'sub': 'llamadas'}, {'name': 'Diego Herrera', 'value': 23, 'sub': 'llamadas', 'color': 'red'}],
         title='Llamadas por asesor', right='Este mes', at='@llamadas'),
    phonelist('Y a cada asesor le dice todos los días a quién le toca llamar.',
              [it('Te toca llamar hoy', '@llamar', 'red', n=14)], 'advisor_woman', title='Mi trabajo', sub='Hoy'),
    cta('Antes de cambiar de agencia, mide a tu equipo. Dale clic al botón de abajo.', 'MIDE A TU EQUIPO'),
], music='drive', keywords=['culpó', 'midiendo', 'agencia'])

video('09-todavia-llenan-el-crm-a-mano', 'n09', '¿Todavía le pides a tus asesores que llenen el CRM a mano?', [
    photo('¿Tu inmobiliaria todavía le pide a los asesores que llenen el CRM a mano?', 'advisor_notebook',
          ['¿LLENAN EL CRM', '[A MANO]?'], kicker='Inmobiliarias'),
    stack('Ya intentaste todo: bonos para el que lo llene, multas para el que no, juntas diarias, una coordinadora revisando.',
          [it('Bonos', '@bonos', 'green'), it('Multas', '@multas', 'red'), it('Juntas diarias', '@juntas', 'amber'),
           it('Una coordinadora revisando', '@coordinadora', 'purple')], img='meeting'),
    photo('Duró tres días. Porque a tu asesor le pagas por vender, no por capturar datos.', 'coordinator',
          ['DURÓ', '[TRES DÍAS]'], [0, '@días'], stamp={'text': 'VENDER, NO CAPTURAR', 'at': '@capturar', 'color': 'cyan', 'size': 76}),
    quote('«El talón de Aquiles de todos es estar poniendo notas», nos dijo un dueño. Y mientras tanto el CRM se queda vacío y tú no sabes qué pasa con los leads que pagaste.',
          'El talón de Aquiles de todos es estar poniendo notas.', 'excel_night'),
    panel('Con Lead Master nadie llena nada. La IA lee los chats y escucha las llamadas de cada asesor, y escribe la nota, el presupuesto, la zona y las objeciones. Mueve la etapa, crea la tarea de seguimiento y te deja todo listo para tu reporte.',
          [call('Andrés Molina', 'Diana Trejo', 'Nota: busca casa en Mérida · Objeción: tiempo de entrega', 'Nota escrita', 'green', '@nota'),
           wa('Paola Gutiérrez', 'Adriana Solís', 'Tarea: mandar planos el viernes', 'Tarea creada', 'cyan', '@tarea')],
          title='La IA llenó esto'),
    photo('Tu asesor solo habla con el lead, como siempre lo ha hecho.', 'advisor_woman', ['TU ASESOR', 'SOLO [HABLA]'], [0, '@habla']),
    cta('Deja de pelear por el CRM. Dale clic al botón de abajo y te lo instalamos.', 'DEJA DE PELEAR POR EL CRM'),
], tempo=1.12, keywords=['mano', 'multas', 'bonos', 'capturar', 'nadie'])

video('10-asi-le-llegaria-un-lead-a-tus-asesores', 'n10', 'Así le llegaría un lead a tus asesores si usaras Lead Master', [
    photo('Así le llegaría un lead a tus asesores si tu inmobiliaria usara Lead Master.', 'woman_night_phone',
          ['ASÍ LE LLEGA UN', 'LEAD A TU [ASESOR]'], kicker='Si usaras Lead Master', size=112),
    photo('Hoy, cuando alguien deja sus datos a las 11 de la noche, el lead se queda en una bandeja hasta que alguien se acuerde. Para la mañana siguiente, ya le escribió a otra inmobiliaria.',
          'night_building', ['SE QUEDA EN', 'UNA [BANDEJA]'], [0, '@bandeja'], stamp={'text': 'YA ESCRIBIÓ A OTRA', 'at': '@otra', 'size': 76}),
    flow('Con Lead Master, Lucía llena el formulario de un departamento en Tulum a las 11:08 de la noche. El sistema se lo asigna a Valeria según tus reglas y le manda un WhatsApp: nuevo lead, Lucía Hernández, dos recámaras en Tulum.',
         [node('Lucía llena el formulario', '@Lucía', sub='Depa en Tulum · 11:08 pm'), node('Se asigna a Valeria', '@asigna', 'purple', sub='según tus reglas'),
          node('WhatsApp a Valeria', '@WhatsApp', 'cyan', sub='Nuevo lead: Lucía Hernández')]),
    phonelist('A primera hora, Valeria la tiene en su lista como urgente y con un tiempo para llamar. Si no llama, el lead pasa a otro asesor.',
              [it('Lucía Hernández', '@urgente', 'red', n=1, sub='Urgente · llamar antes de las 8:20'),
               it('Si no llamas, pasa a otro asesor', '@pasa', 'amber')], 'advisor_woman', title='Mi trabajo', sub='8:00 am', clock='8:00'),
    panel('Cuando hablan, la IA anota qué busca Lucía y deja la cita lista para confirmar. Y tú lo ves todo en tu reporte.',
          [call('Valeria Ríos', 'Lucía Hernández', 'Busca 2 recámaras en Tulum para vivir · Visita: sábado 11 am', 'Cita para confirmar', 'amber', '@cita')],
          title='CRM · Lucía Hernández'),
    cta('Ningún lead se queda esperando. Dale clic al botón de abajo y te lo instalamos.', 'NINGÚN LEAD ESPERA'),
], voice=ANT, music='drive', keywords=['urgente', 'bandeja', 'Lucía', 'Valeria'])

video('11-que-anuncio-te-vendio-el-ultimo-depa', 'n11', '¿Qué anuncio te vendió el último departamento?', [
    photo('Si tienes una inmobiliaria que invierte en Meta, contéstame esto: ¿qué anuncio te vendió el último departamento?',
          'scrolling_ads', ['¿QUÉ ANUNCIO TE', '[VENDIÓ] EL DEPA?'], kicker='Inmobiliarias en Meta', size=112),
    photo('Casi nadie lo sabe. Ves el costo por lead y apagas los anuncios caros. Pero el lead más barato casi nunca es el que compra.',
          'laptop_dashboard', ['APAGAS LOS', '[CAROS]'], ['@apagas', '@caros'], stamp={'text': 'EL BARATO NO COMPRA', 'at': '@compra', 'size': 76}),
    stack('Un anuncio te puede traer leads a 2 dólares y ninguna cita, y otro, leads a 5 dólares y nueve citas. Si solo miras el costo por lead, apagas el que vendía.',
          [it('Lead a 2 USD · 0 citas', '@2', 'red', k='Anuncio A'), it('Lead a 5 USD · 9 citas', '@5', 'green', k='Anuncio B'),
           it('Apagaste el que vendía', '@vendía', 'amber', k='Resultado')], title='EJEMPLO'),
    flow('Lead Master sigue cada lead desde el anuncio hasta el final: si lo contactaron, si agendó, si asistió, si apartó y si compró.',
         [node('Anuncio', '@anuncio'), node('Contactado', '@contactaron', 'cyan'), node('Agendó y asistió', '@agendó', 'purple'),
          node('Apartó y compró', '@compró', 'green')]),
    bars('Te muestra por campaña y por anuncio cuánto te costó cada cita y cada venta. Y le avisa a Meta quién sí agendó y compró, para que tu publicidad busque más compradores.',
         [{'name': 'Campaña Tulum', 'value': 29, 'sub': 'USD por cita', 'color': 'green'},
          {'name': 'Campaña Mérida', 'value': 50, 'sub': 'USD por cita', 'color': 'cyan'},
          {'name': 'Campaña CDMX', 'value': 265, 'sub': 'USD por cita', 'color': 'red'}], title='Costo por cita', right='Ejemplo', at='@campaña'),
    cta('Deja de medir costo por lead y empieza a medir costo por cita. Dale clic al botón de abajo.', 'MIDE COSTO POR CITA'),
], keywords=['anuncio', 'barato', 'caros', 'vendía', 'costo'])

video('12-dices-con-orgullo-que-pagas-gohighlevel', 'n12', 'Dices con orgullo que pagas GoHighLevel', [
    photo('Si tienes una inmobiliaria y dices con orgullo que pagas GoHighLevel, este video es para ti.', 'owner_relaxed',
          ['DICES CON', '[ORGULLO]…'], kicker='Inmobiliarias'),
    photo('Dices con orgullo que pagas GoHighLevel… y tus asesores siguen anotando en una libreta.', 'advisor_notebook',
          ['PAGAS', '[GOHIGHLEVEL]…'], stamp={'text': 'LIBRETA', 'at': '@libreta'}),
    photo('Dices con orgullo que metes 3 mil dólares al mes en Meta… y no sabes cuántas citas te dieron.', 'scrolling_ads',
          ['3 MIL USD AL MES', 'EN [META]…'], stamp={'text': '¿CUÁNTAS CITAS?', 'at': '@cuántas', 'color': 'amber'}),
    photo('Dices con orgullo que tienes 12 asesores… y no sabes cuántos llamaron hoy.', 'office_agents',
          ['TIENES 12', '[ASESORES]…'], stamp={'text': 'NI IDEA', 'at': '@cuántos', 'size': 120}),
    photo('Dices con orgullo que tu equipo es una familia… y el que renunció se llevó sus leads en su WhatsApp.', 'empty_desk',
          ['TU EQUIPO ES', 'UNA [FAMILIA]…'], stamp={'text': 'SE LLEVÓ TUS LEADS', 'at': '@llevó', 'size': 76}),
    flow('Tener las herramientas no es tener el control. Lead Master conecta tu GoHighLevel con el WhatsApp y las llamadas de tus asesores, llena el CRM solo y te manda todos los días qué pasó con cada lead.',
         [node('GoHighLevel', '@conecta'), node('WhatsApp y llamadas', '@WhatsApp', 'cyan'), node('CRM lleno solo', '@llena', 'green'),
          node('Reporte diario', '@manda', 'purple')], title='EL CONTROL'),
    cta('Orgullo es saberlo. Dale clic al botón de abajo.', 'ORGULLO ES SABERLO'),
], music='drive', keywords=['orgullo', 'libreta', 'familia'])

video('13-pagaste-gohighlevel-y-sigues-en-excel', 'n13', 'Le pagaste a alguien para instalar GoHighLevel y sigues en Excel', [
    photo('Si tienes una inmobiliaria y le pagaste a alguien para que te instalara GoHighLevel, pero tu equipo sigue en Excel, no eres el único.',
          'excel_night', ['PAGASTE GOHIGHLEVEL', 'Y SIGUES EN [EXCEL]'], kicker='Inmobiliarias', size=100),
    stack('Pasa todo el tiempo. Te lo instalan, te cobran y se van.',
          [it('Te lo instalan', '@instalan', 'cyan'), it('Te cobran', '@cobran', 'amber'), it('Y se van', '@van', 'red')], img='meeting'),
    photo('Te dejan un pipeline bonito que nadie usa, automatizaciones que nadie entiende y a tus asesores de vuelta en su WhatsApp personal.',
          'advisor_night', ['PIPELINE BONITO', 'QUE [NADIE USA]'], [0, '@usa']),
    quote('Un dueño nos contó que pagó 500 dólares y no le quedó nada configurado. Otro lo dijo así: «pago y me entregan mal». Y el lunes tú sigues armando el reporte a mano.',
          'Pago y me entregan mal.', 'owner_stressed'),
    stack('Nosotros dejamos tu GoHighLevel funcionando para una inmobiliaria en 7 días y le conectamos Lead Master, para que las notas, las etapas y los reportes se hagan solos.',
          [it('GoHighLevel funcionando en 7 días', '@7', 'cyan'), it('Lead Master conectado', '@conectamos', 'purple'),
           it('Notas, etapas y reportes solos', '@reportes', 'green')], title='CÓMO LO HACEMOS', num=True),
    stat('Después te acompañamos 60 días, con reuniones cada semana, hasta que tu equipo lo use.',
         [num(60, 'días de acompañamiento, con reuniones cada semana', '@60')]),
    cta('Dale clic al botón de abajo y te lo dejamos funcionando.', 'TE LO DEJAMOS FUNCIONANDO'),
], keywords=['Excel', 'cobran', 'mal', 'funcionando'])

video('14-por-que-gohighlevel-no-basta', 'n14', 'Por qué GoHighLevel no le basta a tu inmobiliaria', [
    photo('Te explico por qué GoHighLevel no le basta a tu inmobiliaria.', 'sportscar_rope', ['GOHIGHLEVEL', '[NO BASTA]'],
          kicker='Inmobiliarias'),
    photo('GoHighLevel es como tener un Ferrari y moverlo con una cuerda y tres personas.', 'sportscar_rope',
          ['UN FERRARI', 'CON [CUERDA]'], ['@Ferrari', '@cuerda'], drift='out'),
    compare('Es potente, pero es un lienzo en blanco: guarda contactos, tiene pipeline y manda mensajes. Lo que no sabe es qué pasa en los chats y en las llamadas de tus asesores.',
            [{'t': 'Guarda contactos', 'l': True, 'r': True, 'at': '@contactos'}, {'t': 'Pipeline', 'l': True, 'r': True, 'at': '@pipeline'},
             {'t': 'Manda mensajes', 'l': True, 'r': True, 'at': '@mensajes'},
             {'t': 'Sabe qué pasa en chats y llamadas', 'l': False, 'r': True, 'at': '@sabe'}],
            right='Con Lead Master', title='UN LIENZO EN BLANCO'),
    photo('Así que, si nadie lo llena, el pipeline no dice la verdad. Y tú pagas un Ferrari que no se mueve.', 'owner_stressed',
          ['EL PIPELINE', '[NO DICE] LA VERDAD'], [0, '@verdad'], stamp={'text': 'NO SE MUEVE', 'at': '@mueve'}),
    flow('Lead Master no reemplaza a GoHighLevel: se conecta a él y le pone un cerebro. Lee los WhatsApp, escucha las llamadas, escribe la nota, mueve la etapa y le dice a cada asesor qué hacer hoy.',
         [node('Lee los WhatsApp', '@WhatsApp'), node('Escucha las llamadas', '@llamadas', 'purple'),
          node('Escribe la nota y mueve la etapa', '@nota', 'green'), node('Le dice al asesor qué hacer hoy', '@hoy', 'amber')],
         title='LE PONE UN CEREBRO'),
    stack('GoHighLevel guarda; Lead Master te dice qué pasó. Y si todavía no lo tienes, te lo dejamos funcionando.',
          [it('Guarda', '@guarda', 'purple', k='GoHighLevel'), it('Te dice qué pasó', '@pasó', 'cyan', k='Lead Master'),
           it('Te lo dejamos funcionando', '@funcionando', 'green', k='¿No lo tienes?')]),
    cta('Si ya tienes GoHighLevel en tu inmobiliaria, dale clic al botón de abajo y ponlo a trabajar.', 'PONLO A TRABAJAR'),
], voice=ANT, music='drive', keywords=['Ferrari', 'cuerda', 'cerebro', 'verdad'])

video('15-mi-agente-de-ia-vende-solo-parodia', 'n15', '«¡Mi agente de IA vende departamentos solo!» (parodia)', [
    mock('¡Dueño de inmobiliaria! ¡Mi agente de inteligencia artificial vende departamentos solo! ¡Contesta veinticuatro siete! ¡Despide a tus asesores!',
         [{'t': '¡DUEÑO DE INMOBILIARIA!', 'at': 0}, {'t': '¡VENDE SOLO!', 'at': '@vende'}, {'t': '¡24/7!', 'at': '@veinticuatro'},
          {'t': '¡DESPIDE A TUS ASESORES!', 'at': '@Despide'}]),
    photo('Ajá. A una inmobiliaria le pasó esto: el bot le agendó una cita a un cliente, el cliente llegó a la oficina y ningún asesor sabía nada.',
          'robot_reception', ['AJÁ.', 'Y LUEGO [PASA ESTO]'], [0, '@bot'], stamp={'text': 'NADIE SABÍA', 'at': '@nada'}, voice=ANT,
          extra_sfx=[fx(ST, 0, 0.22)]),
    quote('El dueño lo resumió así: «estábamos mejor antes del sistema».', 'Estábamos mejor antes del sistema.', 'empty_desk', voice=ANT),
    photo('En bienes raíces nadie compra una casa porque un bot le contestó rápido. Compra porque una persona le dio seguimiento.',
          'showing_tour', ['COMPRA POR UNA', '[PERSONA]'], ['@nadie', '@persona'], voice=ANT),
    panel('La IA sí sirve, pero trabajando para tu asesor, no en su lugar. Lead Master lee los chats y las llamadas, llena el CRM, le dice a cada asesor a quién llamar y a ti te dice quién no está llamando.',
          [wa('Valeria Ríos', 'Diana Trejo', 'CRM lleno por la IA.', 'Nota lista', 'green', '@llena'),
           call('Diego Herrera', 'Adriana Solís', 'Llamar hoy antes de las 12.', 'A quién llamar', 'amber', '@llamar'),
           call('Andrés Molina', '4 leads asignados', 'Sin llamadas desde el lunes.', 'No está llamando', 'red', '@está', raw=True)],
          title='La IA trabaja para tu asesor', voice=ANT),
    cta('Y no, no despide a nadie. Dale clic al botón de abajo.', 'NO DESPIDE A NADIE', voice=ANT),
], voice=ANT, music='drive', keywords=['bot', 'persona', 'seguimiento', 'nadie'])

video('16-te-vendieron-un-chatbot-de-botones-parodia', 'n16', 'Te vendieron un chatbot de botones (parodia)', [
    mock('¡Tu inmobiliaria necesita mi chatbot que califica leads con inteligencia artificial de última generación!',
         [{'t': '¡CHATBOT CON IA!', 'at': 0}, {'t': '¡ÚLTIMA GENERACIÓN!', 'at': '@última'}]),
    chat('El lead pregunta: ¿el depa tiene estacionamiento? El bot: elige una opción. El lead: quiero hablar con alguien. El bot: no entendí tu respuesta.',
         [{'from': 'out', 'text': 'Hola, ¿el depa tiene estacionamiento?', 'at': '@pregunta'},
          {'from': 'in', 'text': '¡Hola! Elige una opción: 1. Comprar  2. Rentar  3. Otro', 'at': '@elige'},
          {'from': 'out', 'text': 'Quiero hablar con alguien', 'at': '@quiero'},
          {'from': 'in', 'text': 'No entendí tu respuesta. Elige una opción.', 'at': '@entendí'}],
         'robot_reception', 'Asistente virtual', sub='bot', extra_sfx=[fx(ST, 0, 0.22)]),
    photo('Y el lead se fue. No quería un menú: quería una persona. Nadie compra un departamento de 300 mil dólares con un menú de botones.',
          'woman_night_phone', ['QUERÍA UNA', '[PERSONA]'], ['@menú', '@persona'], stamp={'text': 'SE FUE', 'at': '@fue', 'size': 120}),
    panel('Lo que tu inmobiliaria necesita no es un bot que conteste por tu asesor. Es saber si tu asesor contestó, cuánto tardó y en qué quedó.',
          [wa('Valeria Ríos', 'Diana Trejo', 'Contestó en 3 minutos · Quedó en visita el sábado.', 'Contestó', 'green', '@contestó'),
           wa('Diego Herrera', 'Adriana Solís', 'Tardó 6 horas · Sin siguiente paso.', 'Tarde', 'red', '@tardó')], title='Tu equipo, hoy'),
    phonelist('Lead Master te lo dice con cada lead, el mismo día, y le recuerda al asesor a quién le debe una respuesta.',
              [it('Le debes respuesta a Lucía Hernández', '@recuerda', 'amber', sub='Hace 2 horas')], 'advisor_woman',
              title='Mi trabajo', sub='Pendientes'),
    cta('Dale clic al botón de abajo.', 'QUERÍA UNA PERSONA', tail=1.6),
], voice=ANT, keywords=['bot', 'menú', 'persona', 'botones', 'tardó'])

video('17-contrataste-un-coordinador', 'n17', 'Contrataste un coordinador para vigilar a tus asesores', [
    photo('Si tienes una inmobiliaria y contrataste a alguien para vigilar a tus asesores, mira esto.', 'coordinator',
          ['¿CONTRATASTE A ALGUIEN', 'PARA [VIGILAR]?'], kicker='Inmobiliarias', size=96),
    chat('Primero lo hacías tú: «¿ya le marcaste?», «¿ya mandaste las opciones?», «¿ya llenaste el CRM?». Te volviste la niñera del equipo.',
         [{'from': 'out', 'text': '¿Ya le marcaste?', 'at': '@marcaste'}, {'from': 'out', 'text': '¿Ya mandaste las opciones?', 'at': '@opciones'},
          {'from': 'out', 'text': '¿Ya llenaste el CRM?', 'at': '@llenaste'}],
         'owner_stressed', 'Equipo comercial', sub='grupo'),
    quote('Luego metiste a una coordinadora. Un dueño nos dijo: «metí una coordinadora, pero pues tampoco lo hacen».',
          'Metí una coordinadora, pero pues tampoco lo hacen.', 'coordinator'),
    photo('Y es normal: ¿qué gerente tiene tiempo de escuchar todas las llamadas y leer todos los chats? Ninguno.', 'headset_calls',
          ['¿QUIÉN ESCUCHA', '[TODAS] LAS LLAMADAS?'], ['@escuchar', '@todas'], size=104, stamp={'text': 'NINGUNO', 'at': '@Ninguno', 'size': 120}),
    panel('Lead Master sí lo hace. Lee cada chat, escucha cada llamada que sale del CRM y le arma a cada asesor su lista del día. A ti te dice quién no la cumplió, qué leads se están enfriando y quién lleva días sin dar seguimiento.',
          [wa('Diego Herrera', 'Adriana Solís', 'No cumplió su lista de ayer: 6 pendientes.', 'No cumplió', 'red', '@cumplió'),
           call('Andrés Molina', 'Lucía Hernández', 'Sin contacto en 3 días.', 'Se enfría', 'amber', '@enfriando'),
           wa('Paola Gutiérrez', 'Diana Trejo', '4 días sin seguimiento.', 'Sin seguimiento', 'red', '@seguimiento')],
          title='Lo que no se cumplió'),
    cta('Deja de perseguir a tu equipo. Dale clic al botón de abajo.', 'DEJA DE PERSEGUIRLOS'),
], keywords=['niñera', 'coordinadora', 'vigilar', 'Ninguno'])

video('18-tu-asesor-dice-que-marco-15', 'n18', 'Tu asesor dice que marcó 15. Tu CRM dice 13', [
    photo('Tu asesor inmobiliario dice que marcó 15 veces. Tu CRM dice 13. ¿A quién le crees?', 'headset_calls',
          ['DICE 15.', 'TU CRM DICE [13].'], kicker='Inmobiliarias'),
    quote('Un dueño nos lo dijo así: «si me ponen que llamaron 20, tengo que confiar en que llamaron 20, pero no puedo controlarlo».',
          'Si me ponen que llamaron 20, tengo que confiar en que llamaron 20, pero no puedo controlarlo.', 'owner_stressed'),
    quote('Y otro: «no es que lo hagan a propósito, es que no llevan el hábito de registrar».',
          'No es que lo hagan a propósito, es que no llevan el hábito de registrar.', 'meeting'),
    photo('El resultado es el mismo: decides a quién darle más leads con números que nadie puede comprobar.', 'office_agents',
          ['NÚMEROS QUE NADIE', 'PUEDE [COMPROBAR]'], [0, '@comprobar'], size=104),
    phonelist('Con Lead Master, cada llamada que sale del CRM queda grabada, con hora y duración, y la IA te dice qué se habló y en qué quedaron. Los chats de WhatsApp también quedan. Ya no tienes que creerle a nadie: lo ves.',
              [it('10:42 · Adriana Solís', '@hora', 'red', sub='0:00 · no contestó'), it('11:15 · Diana Trejo', '@duración', 'green', sub='3:48 · quedó en visita'),
               it('Resumen de la IA', '@quedaron', 'purple', sub='Qué se habló y en qué quedaron')],
              'headset_calls', title='Llamadas de Diego', sub='Grabadas desde el CRM'),
    cta('Como dijo un cliente: «mi verdad es lo que dice el sistema». Dale clic al botón de abajo.', '«MI VERDAD ES EL SISTEMA»'),
], music='drive', keywords=['comprobar', 'grabada', 'verdad', 'crees'])

video('19-antes-de-despedir-a-un-asesor', 'n19', 'Antes de despedir a un asesor, mira esto', [
    photo('Si tienes una inmobiliaria y estás por despedir a un asesor, mira esto antes.', 'empty_desk', ['ANTES DE', '[DESPEDIR], MIRA'],
          kicker='Inmobiliarias'),
    bars('En casi todos los equipos pasa lo mismo: unos pocos asesores hacen casi todo el trabajo.',
         [{'name': 'Paola Gutiérrez', 'value': 412, 'sub': 'llamadas'}, {'name': 'Valeria Ríos', 'value': 356, 'sub': 'llamadas'},
          {'name': 'Andrés Molina', 'value': 74, 'sub': 'llamadas'}, {'name': 'Diego Herrera', 'value': 41, 'sub': 'llamadas', 'color': 'red'}],
         title='Llamadas por asesor', right='Ejemplo', at='@pocos'),
    stat('En las inmobiliarias que medimos, 2 de cada 10 asesores hicieron entre el 46 y el 88 por ciento de todas las llamadas.',
         [num(2, 'de cada 10 asesores hicieron entre el 46 y el 88% de las llamadas', '@2')]),
    quote('«De 10, te trabajan bien 3, y el resto, quién sabe», nos dijo un dueño. Sin datos, despides al que te cae mal, no al que no trabaja.',
          'De 10, te trabajan bien 3, y el resto, quién sabe.', 'meeting'),
    panel('Lead Master te arma el ranking real de tu equipo: cuántos leads tiene cada asesor, cuántas llamadas hizo, a cuántos contactó, cuánto tarda en responder y cuántas citas sacó. Así sabes a quién darle más leads, a quién entrenar y a quién no.',
          [call('Paola Gutiérrez', '41 leads', '412 llamadas · responde en 6 min · 9 citas', 'Darle más leads', 'green', '@ranking', raw=True),
           call('Andrés Molina', '38 leads', '74 llamadas · responde en 40 min · 3 citas', 'Entrenar', 'amber', '@entrenar', raw=True),
           call('Diego Herrera', '61 leads', '41 llamadas · responde en 2 h · 1 cita', 'Revisar', 'red', '@citas', raw=True)],
          title='Ranking real del equipo'),
    cta('Medir antes de despedir. Dale clic al botón de abajo.', 'MEDIR ANTES DE DESPEDIR'),
], keywords=['despedir', 'ranking', 'entrenar'])

video('20-renuncio-y-se-llevo-tus-leads', 'n20', 'Tu mejor asesor renunció y se llevó tus leads', [
    photo('Tu mejor asesor renunció el viernes y se llevó tus leads en su WhatsApp.', 'empty_desk', ['RENUNCIÓ Y SE', 'LLEVÓ TUS [LEADS]'],
          kicker='Inmobiliarias'),
    floatchats('Si tienes una inmobiliaria, ya te pasó o te va a pasar. Sus conversaciones, sus seguimientos, las visitas que tenía apalabradas: todo estaba en su celular.',
               'advisor_night', ['TODO EN SU', '[CELULAR]'], ['@todo', '@celular'],
               bubbles=['¿Seguimos con la visita?', 'Te mando la cotización', 'El sábado paso', '¿Ya hay fecha de entrega?']),
    quote('«Cuando se va, no sabemos ni a quiénes les estaba dando seguimiento», nos dijo un dueño. Y el asesor nuevo empieza de cero con leads que tú ya pagaste.',
          'Cuando se va, no sabemos ni a quiénes les estaba dando seguimiento.', 'empty_desk'),
    flow('Con Lead Master, el WhatsApp de cada asesor se conecta al CRM. Solo se guardan las conversaciones con leads; lo personal se queda fuera.',
         [node('WhatsApp del asesor', '@WhatsApp'), node('CRM de tu inmobiliaria', '@CRM', 'green'),
          node('Solo chats con leads', '@personal', 'amber', sub='lo personal se queda fuera')]),
    panel('Si mañana alguien se va, el historial se queda en tu inmobiliaria, con la nota de en qué quedó cada lead, y se lo pasas a otro asesor.',
          [wa('Diego Herrera', 'Adriana Solís', 'Quedó en visita el sábado · le prometió cotización.', 'Pasar a Valeria', 'amber', '@historial'),
           wa('Diego Herrera', 'Lucía Hernández', 'Esperando planos.', 'Pasar a Andrés', 'amber', '@pasas')],
          title='Historial de Diego', right='Se queda contigo'),
    cta('Los leads son de tu inmobiliaria. Dale clic al botón de abajo.', 'LOS LEADS SON TUYOS'),
], music='drive', keywords=['renunció', 'celular', 'historial'])

video('21-el-lead-de-las-11-de-la-noche', 'n21', 'El lead de las 11 de la noche', [
    photo('Casi la mitad de los leads de tu inmobiliaria llega de noche o en fin de semana. ¿Quién los contesta?', 'woman_night_phone',
          ['CASI LA MITAD', 'LLEGA DE [NOCHE]'], kicker='Inmobiliarias'),
    stat('De los 6,497 leads que medimos, el 47% llegó fuera de horario. Y la mitad de esos esperó más de 10 horas por la primera respuesta.',
         [num(47, 'de los leads llegó fuera de horario', '@47%', 'amber', suffix='%'),
          num(10, 'esperó la mitad por la primera respuesta', '@10', 'red', prefix='+', suffix=' h')], foot='6,497 leads medidos en Lead Master'),
    photo('La persona que vio tu desarrollo un domingo en la noche no espera al lunes: le escribe a otras dos inmobiliarias y se queda con la que contesta primero.',
          'night_building', ['NO ESPERA', 'AL [LUNES]'], [0, '@lunes'], stamp={'text': 'SE FUE CON OTRA', 'at': '@primero', 'size': 84}),
    flow('Con Lead Master pones tus reglas: guardia en la noche y los fines de semana, y para lo que llega fuera de horario, recordatorio a primera hora con un tiempo para llamar. Si nadie llama, el lead pasa al siguiente asesor. Y tú ves cuánto tarda cada uno.',
         [node('Guardia de noche y fin de semana', '@guardia', 'purple'), node('Recordatorio a primera hora', '@recordatorio', 'cyan', sub='con tiempo para llamar'),
          node('Si nadie llama, pasa al siguiente', '@siguiente', 'amber'), node('Ves cuánto tarda cada uno', '@tarda', 'green')],
         title='TUS REGLAS'),
    cta('Que ningún lead espere hasta el lunes. Dale clic al botón de abajo.', 'NINGÚN LEAD ESPERA AL LUNES'),
], keywords=['noche', 'lunes', 'guardia', 'horario'])

video('22-el-dia-de-tus-asesores-con-lead-master', 'n22', 'Así sería el día de tus asesores si usaras Lead Master', [
    photo('Así sería el día de tus asesores inmobiliarios si usaras Lead Master.', 'advisor_woman', ['EL DÍA DE TUS', '[ASESORES]'],
          kicker='Si usaras Lead Master'),
    floatchats('Hoy tu asesor llega en la mañana, abre WhatsApp y tiene 40 chats. No sabe por dónde empezar, no se acuerda a quién le prometió llamar y la libreta no ayuda. Así se le pasan los leads que más valen.',
               'advisor_notebook', ['40 CHATS.', '¿POR [DÓNDE] EMPIEZA?'], ['@40', '@dónde']),
    phonelist('Con Lead Master, a las 8 de la mañana le llega por WhatsApp su lista del día: lo urgente, los leads que nunca ha buscado, los que no le han contestado y los que se están enfriando.',
              [it('Lo urgente', '@urgente', 'red', n=3), it('Nunca los has buscado', '@nunca', 'amber', n=5),
               it('No te han contestado', '@contestado', 'purple', n=7), it('Se están enfriando', '@enfriando', 'cyan', n=4)],
              'advisor_woman', title='Mi trabajo', sub='8:00 am', clock='8:00'),
    panel('Habla con sus leads como siempre; la IA anota todo y le deja la cita lista para confirmar.',
          [wa('Valeria Ríos', 'Diana Trejo', 'Busca 3 recámaras · Visita: sábado 11 am', 'Cita para confirmar', 'amber', '@anota')],
          title='Lo anotó la IA'),
    phonelist('La lista se recalcula cada hora con lo que pasa en sus chats y llamadas. Y en la tarde recibe el resumen de lo que hizo.',
              [it('La lista se recalcula cada hora', '@recalcula', 'cyan'), it('Resumen del día.pdf', '@resumen', 'purple', sub='18 llamadas · 7 contactados · 2 citas')],
              'advisor_car', title='Tu día', sub='7:00 pm', clock='7:00'),
    cta('Tu equipo sabe qué hacer y tú dejas de perseguirlo. Dale clic al botón de abajo.', 'TU EQUIPO SABE QUÉ HACER'),
], voice=ANT, music='drive', keywords=['urgente', 'lista', 'resumen'])

video('23-lo-que-quema-tu-inmobiliaria-cada-mes', 'n23', 'Lo que quema tu inmobiliaria cada mes', [
    photo('Haz esta cuenta conmigo si tienes una inmobiliaria que invierte en Meta.', 'scrolling_ads', ['HAZ ESTA', '[CUENTA]'],
          kicker='Inmobiliarias en Meta'),
    stat('Metes 4 mil dólares al mes y te llegan 400 leads. Cada uno te costó 10 dólares.',
         [num(4000, 'al mes en Meta', '@4', prefix='US$'), num(400, 'leads', '@400'), num(10, 'por lead', '@10', 'amber', prefix='US$')],
         stacked=True),
    stat('En las inmobiliarias que medimos, 1 de cada 3 leads nunca habló con una persona. Eso son 133 leads al mes que nadie llamó:',
         [num(1, 'nunca habló con una persona', '@1', 'red', suffix=' de cada 3'), num(133, 'leads al mes que nadie llamó', '@133', 'red')]),
    stat('Más de 1,300 dólares tirados cada mes, casi 16 mil al año. Y nadie te lo dice, porque nadie lo está midiendo.',
         [num(1300, 'tirados cada mes', '@1,300', 'red', prefix='+US$'), num(16000, 'al año', '@16', 'red', prefix='US$')]),
    panel('Lead Master te dice, el mismo día y con nombre, qué leads nadie ha contactado, de qué asesor son y cuánto llevan esperando. Le marca al asesor a quién llamar primero y, si no lo hace, el lead pasa a otro.',
          [wa('Diego Herrera', 'Adriana Solís', 'Esperando desde hace 5 horas.', 'Sin contacto', 'red', '@nadie'),
           call('Andrés Molina', 'Lucía Hernández', 'Esperando desde hace 26 horas.', 'Pasa a otro', 'amber', '@otro')],
          title='Sin contacto hoy'),
    cta('Antes de meterle más dinero a Meta, deja de tirar el que ya pagaste. Dale clic al botón de abajo.', 'DEJA DE TIRAR DINERO'),
], keywords=['cuenta', 'tirados', 'midiendo'])

video('24-ahorita-te-mando-opciones', 'n24', '«Ahorita te mando opciones»', [
    photo('«Ahorita te mando opciones.» Si tienes una inmobiliaria, esa frase te está costando ventas.', 'merida_street',
          ['«AHORITA TE', 'MANDO [OPCIONES]»'], kicker='Inmobiliarias'),
    chat('El lead pide opciones de casas en Mérida. Tu asesor contesta «claro, ahorita te mando». Y nunca las manda. O las manda, el lead no responde y ahí se acaba el seguimiento.',
         [{'from': 'in', 'text': '¿Me mandas opciones de casas en Mérida?', 'at': '@pide'},
          {'from': 'out', 'text': 'Claro, ahorita te mando.', 'at': '@claro'},
          {'from': 'system', 'text': '15 días después', 'at': '@nunca'}],
         'merida_house', 'Adriana Solís', sub='Lead · Mérida'),
    quote('«Te mando opciones, cric, cric, quince días, se perdió», nos dijo un dueño.', 'Te mando opciones, cric, cric, quince días, se perdió.',
          'advisor_notebook'),
    quote('Y otro: «nos están comprando, pero no estamos vendiendo, porque no hacemos seguimiento».',
          'Nos están comprando, pero no estamos vendiendo, porque no hacemos seguimiento.', 'meeting'),
    phonelist('Lead Master lee cada conversación y saca los compromisos. Si el asesor prometió mandar opciones, llamar el martes o confirmar una visita, queda como tarea en su lista del día. Y si no la cumple, tú lo ves en tu reporte.',
              [it('Mandar opciones a Adriana Solís', '@opciones', 'red', sub='Lo prometiste ayer'),
               it('Llamar a Diana Trejo el martes', '@martes', 'amber'), it('Confirmar visita de Lucía', '@visita', 'green')],
              'advisor_woman', title='Compromisos de hoy', sub='Sacados de tus chats'),
    cta('Que ningún «ahorita te mando» se quede en el aire. Dale clic al botón de abajo.', 'NINGÚN «AHORITA» EN EL AIRE'),
], music='drive', keywords=['ahorita', 'opciones', 'seguimiento', 'compromisos'])

video('25-este-video-te-aparecio-porque-tienes-una-inmobiliaria', 'n25', 'Este video te apareció porque tienes una inmobiliaria', [
    photo('Este video te apareció porque tienes una inmobiliaria, o porque viste algo de Lead Master estos días.', 'tulum_pool',
          ['ESTE VIDEO TE', '[APARECIÓ] POR ESTO'], kicker='Tienes una inmobiliaria'),
    photo('Seguramente ya probaste un CRM que tu equipo nunca llenó, o un bot que espantó a tus leads. Y sigues sin saber qué pasa con cada lead que pagas.',
          'robot_reception', ['OTRO CRM.', 'OTRO [BOT].'], ['@CRM', '@bot'], stamp={'text': 'NO FUNCIONÓ', 'at': '@sigues'}),
    stack('Lead Master es un sistema de gestión comercial hecho solo para inmobiliarias. No es un CRM más ni un chatbot de botones.',
          [it('Hecho solo para inmobiliarias', '@inmobiliarias', 'green'), it('No es un CRM más', '@CRM', 'amber'),
           it('No es un chatbot de botones', '@chatbot', 'amber')], title='LEAD MASTER'),
    flow('Se conecta al WhatsApp y a las llamadas de tus asesores, llena el CRM solo, le dice a cada asesor qué hacer cada día y a ti te manda el reporte de tu equipo por WhatsApp.',
         [node('WhatsApp y llamadas', '@WhatsApp'), node('CRM lleno solo', '@llena', 'green'),
          node('Qué hacer cada día', '@día', 'amber', sub='para cada asesor'), node('Reporte por WhatsApp', '@reporte', 'purple', sub='para ti')]),
    stat('Ya lo usan más de 15 inmobiliarias en México, Colombia y Estados Unidos. Lo instalamos en 7 días, te acompañamos 60 y tu equipo no aprende nada nuevo: solo habla con sus leads.',
         [num(15, 'inmobiliarias en México, Colombia y EE. UU.', '@15', prefix='+'), num(7, 'días para instalarlo', '@7', 'green'),
          num(60, 'días de acompañamiento', '@60', 'purple')], stacked=True),
    cta('Si tienes 5 asesores o más e inviertes en anuncios, dale clic al botón de abajo y agenda una llamada.', '+5 ASESORES',
        button='Agenda una llamada'),
], voice=ANT, tempo=1.12, keywords=['apareció', 'inmobiliarias', 'chatbot'])


# ---------------------------------------------------------------------
# Gráficos literales: cuando la voz dice CRM, nota, cita, reporte, llamada o tareas,
# aparece eso en pantalla en esa palabra (src/ui/Inserts.tsx). Clave: (prefijo, número de escena).

def ins(kind, at, to=None, **p):
    d = {'kind': kind, 'at': at}
    if to is not None:
        d['to'] = to
    if p:
        d['p'] = p
    return d


def crm(at, to=None, move=None, stale=False, **p):
    if stale:
        p['stale'] = True
    elif move is False:
        p['move'] = False
    elif move is not None:
        p['move'] = {'card': 0, 'to': 2, 'at': move}
    return ins('crm', at, to, **p)


def note(at, to=None, empty=False, **p):
    if empty:
        p['empty'] = True
    return ins('note', at, to, **p)


def cita(at, to=None, **p):
    return ins('cita', at, to, **p)


def report(at, to=None, **p):
    return ins('report', at, to, **p)


def callrec(at, to=None, **p):
    return ins('call', at, to, **p)


def tasks(at, to=None, **p):
    return ins('tasks', at, to, **p)


def F(k, v, at=None):
    d = {'k': k, 'v': v}
    if at is not None:
        d['at'] = at
    return d


def L(t, at=None, c=None, b=False):
    d = {'t': t}
    if at is not None:
        d['at'] = at
    if c:
        d['c'] = c
    if b:
        d['b'] = True
    return d


def SEP(at=None):
    d = {'t': '', 'sep': True}
    if at is not None:
        d['at'] = at
    return d


def T(t, sub=None, state='new', at=None):
    d = {'t': t, 'state': state}
    if sub:
        d['sub'] = sub
    if at is not None:
        d['at'] = at
    return d


TULUM = [F('Busca', 'Depa 2 recámaras', '@busca'), F('Zona', 'Tulum', '@zona'), F('Presupuesto', '250 mil USD', '@presupuesto'),
         F('Etapa', 'Cita', '@etapa')]
WEEKLY = [L('Leads de la semana: 214', b=True), L('Contactados: 176 · Sin contacto: 38'), L('Citas: 19 · Apartados: 4', c='green'), SEP(),
          L('Paola G. · 61 llamadas · 7 citas'), L('Valeria R. · 48 llamadas · 6 citas'), L('Diego H. · 9 llamadas · 12 leads olvidados', c='red')]
ADVISOR_DAY = [L('Llamadas: 14 · Chats: 22', b=True), L('Contactados: 9 de 12'), L('Citas: 2 (jueves y sábado)', c='green'), SEP(),
               L('Mañana a primera hora: llamar a Diana Trejo', c='amber')]

INSERTS = {
    # 01 Guadalajara
    ('n01', 4): dict(ins=[crm('@CRM', move='@CRM+12', chip='Todo registrado, sin capturar nada', cards=[
        {'name': 'Lucía Hernández', 'sub': 'Depa · Providencia', 'col': 0, 'age': 'hace 4 min'},
        {'name': 'Diana Trejo', 'sub': 'Casa · Zapopan', 'col': 0, 'age': 'hace 12 min'},
        {'name': 'Adriana Solís', 'sub': 'Terreno · Zapopan', 'col': 1, 'age': 'hace 1 h'},
        {'name': 'Carlos Ruiz', 'sub': 'Preventa · Providencia', 'col': 1, 'age': 'ayer'},
        {'name': 'Sofía Méndez', 'sub': 'Depa · Zapopan', 'col': 2, 'age': 'jueves 5 pm'}])]),
    ('n01', 5): dict(ins=[note('@nota', lead='Diana Trejo', tag='Lead · Zapopan', stage='Interesada', typeAt='@nota+3',
                               note='Busca casa con jardín para mudarse en marzo. Pidió planos y forma de pago.',
                               fields=[F('Presupuesto', '330 mil USD', '@presupuesto'), F('Zona', 'Zapopan', '@zona'),
                                       F('Busca', 'Casa con jardín', '@zona+6'), F('Etapa', 'Interesada', '@etapa')])]),
    ('n01', 6): dict(type='ui', ins=[report(0, time='8:00 pm', lines=[
        L('Leads que entraron hoy: 23', '@entraron', b=True), L('Contactados: 18', '@entraron+8'), SEP('@llamó'),
        L('Paola G. llamó a 9 · 2 citas', '@llamó'), L('Valeria R. llamó a 7 · 1 cita', '@llamó+5'), L('Andrés M. llamó a 2', '@llamó+10'),
        SEP('@contacto'), L('Sin contacto: 5 (Diego H. 4, Andrés M. 1)', '@contacto', c='red')],
        alert={'t': 'Ahora: lead nuevo de Meta, Diana Trejo. Valeria R. le escribió en 3 min.', 'c': 'green', 'at': '@Eso'})]),
    # 02 desarrollos
    ('n02', 6): dict(ins=[callrec('@llamadas', '@agendó', advisor='Andrés Molina', lead='Lucía Hernández',
                                  summary=['Le interesa el lanzamiento', 'Pidió precios de preventa', 'Siguiente paso: recorrido']),
                          cita('@agendó', '@descartó', mode='done', what='Recorrido · Lanzamiento', when='Sábado 15 · 11:00 am',
                               dayIdx=5, lead='Diana Trejo', source='Agendó en el chat', doneText='Recorrido agendado')]),
    # 03 este CRM se mueve solo
    ('n03', 1): dict(ins=[crm('@solo', move='@solo+8', chip='Se mueve solo')]),
    ('n03', 2): dict(ins=[note('@segunda', '@mes', empty=True, emptyText='Sin notas desde la semana 2'),
                          crm('@pipeline', stale=True, chip='El pipeline es una mentira')]),
    ('n03', 5): dict(ins=[note('@anota', typeAt='@presupuesto+4', fields=TULUM,
                               note='Quiere ver el proyecto el jueves a las 5 pm. Pidió planos y forma de pago.'),
                          crm('@etapa', move='@etapa+6'),
                          cita('@cita', confirmAt='@confirmar'),
                          crm('@CRM', move=False, chip='Tu CRM dice la verdad')]),
    # 04 curiosos vs compradores
    ('n04', 4): dict(ins=[note('@saca', '@eso', lead='Diana Trejo', tag='Lead · Polanco', stage='Atender primero', right='Sacado del chat',
                               typeAt='@pronto+4', note='Quiere comprar este mes. Ya tiene crédito aprobado. Prioridad alta.',
                               fields=[F('Busca', 'Depa 3 recámaras', '@busca'), F('Zona', 'Polanco', '@zona'),
                                       F('Presupuesto', '450 mil USD', '@presupuesto'), F('Cuándo compra', 'Este mes', '@pronto')])]),
    # 05 depas de +150 mil USD
    ('n05', 5): dict(ins=[report('@aviso', title='Lead nuevo para ti', sub='Avisos para Valeria Ríos', time='11:02 am',
                                 sched='Lead asignado hace 1 min', lines=[
        L('Diana Trejo · Depa en Polanco', b=True), L('Presupuesto: 450 mil USD'), L('Viene de: anuncio de Meta'),
        L('Llámala antes de 10 min', '@llamada', c='amber')],
        alert={'t': 'Sin llamada en 10 min: el lead pasó a Diego H.', 'c': 'red', 'at': '@siguiente'})]),
    # 06 no es la cantidad de leads
    ('n06', 3): dict(ins=[callrec('@nadie', missed=True)]),
    ('n06', 5): dict(ins=[report('@dice', title='Sin contacto hoy', time='1:00 pm', sched='Alerta de leads sin llamar', lines=[
        L('Leads sin llamar hoy: 7', b=True), SEP('@asignados'),
        L('Adriana Solís · Diego H. · espera 26 h', '@asignados', c='red'),
        L('Carlos Ruiz · Diego H. · espera 5 h', '@asignados+6', c='amber'),
        L('Lucía Hernández · Andrés M. · espera 3 h', '@esperando', c='amber')], alert=False),
        tasks('@marca', who='Diego Herrera', right='Ordenadas por la IA', items=[
            T('Llamar primero a Adriana Solís', 'Lleva 26 h esperando'), T('Luego a Carlos Ruiz', 'Lleva 5 h esperando'),
            T('Después a Sofía Méndez', 'Pidió que la buscaran hoy')])]),
    # 07 robando leads
    ('n07', 5): dict(ins=[crm('@CRM', '@llamadas', move='@CRM+12', chip='Solo conversaciones con leads'),
                          callrec('@llamadas', advisor='Diego Herrera', lead='Adriana Solís')]),
    # 08 9 mil dólares
    ('n08', 5): dict(ins=[callrec('@nunca', '@citas', missed=True), cita('@citas', mode='done', doneText='Cita agendada',
                                                                         what='Cita · Campaña Mérida', when='Viernes 14 · 4:00 pm', dayIdx=4)]),
    # 09 llenan el CRM a mano
    ('n09', 4): dict(ins=[crm('@CRM', stale=True, chip='El CRM se queda vacío')]),
    ('n09', 5): dict(ins=[callrec('@escucha'),
                          note('@nota', typeAt='@nota+6', fields=[F('Presupuesto', '180 mil USD', '@presupuesto'), F('Zona', 'Mérida', '@zona'),
                                                                  F('Objeciones', 'Fecha de entrega', '@objeciones'), F('Etapa', 'Cita', '@Mueve')],
                               lead='Adriana Solís', tag='Lead · Mérida', note='Le preocupa la fecha de entrega. Quiere visitar el sábado.'),
                          crm('@Mueve', move='@etapa', chip='Etapa movida y tarea creada'),
                          report('@reporte')]),
    # 10 así le llegaría un lead
    ('n10', 5): dict(ins=[note('@anota', typeAt='@Lucía', fields=[F('Busca', 'Depa 2 recámaras', '@busca'), F('Zona', 'Tulum', '@Lucía'),
                                                                     F('Presupuesto', '250 mil USD', '@Lucía+4'), F('Etapa', 'Cita', '@cita')]),
                          cita('@cita', confirmAt='@confirmar'), report('@reporte')]),
    # 11 qué anuncio te vendió
    ('n11', 4): dict(ins=[crm('@agendó', move='@apartó', cols=['Contactado', 'Cita', 'Apartado'], chip='Del anuncio hasta la venta', cards=[
        {'name': 'Lucía Hernández', 'sub': 'Anuncio B · Tulum', 'col': 1, 'age': 'asistió el sábado'},
        {'name': 'Diana Trejo', 'sub': 'Anuncio B · Mérida', 'col': 0, 'age': 'hace 2 h'},
        {'name': 'Adriana Solís', 'sub': 'Anuncio A · CDMX', 'col': 0, 'age': 'no agendó'},
        {'name': 'Carlos Ruiz', 'sub': 'Anuncio B · Tulum', 'col': 1, 'age': 'jueves 5 pm'},
        {'name': 'Sofía Méndez', 'sub': 'Anuncio B · Cancún', 'col': 2, 'age': 'apartó ayer'}])]),
    # 12 orgullo GoHighLevel
    ('n12', 6): dict(ins=[crm('@llena', move='@CRM+4'), report('@días')]),
    # 13 pagaste GoHighLevel
    ('n13', 3): dict(ins=[crm('@pipeline', '@asesores', stale=True, chip='Bonito, pero nadie lo usa')]),
    ('n13', 5): dict(ins=[note('@conectamos', typeAt='@notas'), report('@reportes')]),
    # 14 GoHighLevel no basta
    ('n14', 3): dict(ins=[crm('@pipeline', '@Lo', move=False, chip='Guarda contactos')]),
    ('n14', 4): dict(ins=[crm('@pipeline', stale=True, chip='No dice la verdad')]),
    ('n14', 5): dict(ins=[callrec('@escucha'), crm('@nota', move='@etapa', chip='Nota escrita y etapa movida por la IA')]),
    # 15 parodia agente de IA
    ('n15', 2): dict(ins=[cita('@agendó', mode='missed', source='Agendada por el bot', missedText='Ningún asesor sabía de la cita',
                               what='Visita · Oficina', advisor='Sin asignar')]),
    ('n15', 5): dict(ins=[crm('@CRM', move='@CRM+10')]),
    # 16 chatbot de botones
    ('n16', 4): dict(ins=[note('@contestó', lead='Lucía Hernández', tag='Lead · Preguntó por estacionamiento', stage='Cita', typeAt='@quedó+4',
                               note='Quiere estacionamiento para 2 autos. Visita el sábado a las 11 am.',
                               fields=[F('Contestó', 'Sí · Valeria R.', '@contestó'), F('Tardó', '4 minutos', '@tardó'),
                                       F('Quedó en', 'Visita el sábado', '@quedó'), F('Etapa', 'Cita', '@quedó+4')])]),
    ('n16', 5): dict(ins=[tasks('@recuerda', items=[T('Responderle a Lucía Hernández', 'Te preguntó por el estacionamiento hace 2 h'),
                                                    T('Mandar precios a Diana Trejo', 'Se los prometiste ayer'),
                                                    T('Confirmar visita del sábado', 'Lucía Hernández · 11 am', 'done')])]),
    # 17 coordinador
    ('n17', 5): dict(ins=[callrec('@escucha'), tasks('@arma', who='Diego Herrera'),
                          report('@ti', title='Tu equipo hoy', lines=[
                              L('Listas cumplidas: 3 de 5 asesores', '@ti+4', b=True), SEP('@cumplió'),
                              L('Diego H. no cumplió: 4 de 9 tareas', '@cumplió', c='red'),
                              L('Leads que se están enfriando: 6', '@enfriando', c='amber'),
                              L('Andrés M.: 3 días sin dar seguimiento', '@seguimiento', c='red')], alert=False)]),
    # 18 marcó 15 veces
    ('n18', 5): dict(ins=[callrec('@llamada', '@chats', when='Hoy 11:42 am · 3 min 42 s',
                                  summary=['Le marcó 1 vez, duró 3:42', 'Quiere visitar el sábado', 'Quedaron en mandar ubicación'])]),
    # 19 antes de despedir
    ('n19', 5): dict(ins=[report('@Así', title='Ranking de tu equipo', time='lunes 8:00 am', sched='Tu ranking llega los lunes a las 8:00 am', lines=[
        L('Paola G. · 61 llamadas · 7 citas', b=True), L('Valeria R. · 48 llamadas · 6 citas'), L('Andrés M. · tarda 3 h en responder', c='amber'),
        L('Diego H. · 9 llamadas · 1 cita', c='red'), SEP('@más'),
        L('Darle más leads: Paola G.', '@más', c='green'), L('Entrenar: Andrés M.', '@entrenar', c='amber'),
        L('Revisar: Diego H.', '@entrenar+12', c='red')], alert=False)]),
    # 20 renunció
    ('n20', 4): dict(ins=[crm('@CRM', move='@CRM+10', chip='Lo personal se queda fuera')]),
    ('n20', 5): dict(ins=[note('@nota', lead='Adriana Solís', tag='Antes con Diego Herrera', stage='Reasignada', typeAt='@nota+4',
                               note='Quedó en mandarle 2 opciones en Mérida el lunes. Reasignada a Paola Gutiérrez.',
                               fields=[F('Busca', 'Casa en Mérida'), F('Presupuesto', '180 mil USD'), F('Último contacto', 'Hace 2 días'),
                                       F('Nuevo asesor', 'Paola G.', '@otro')])]),
    # 21 el lead de las 11 de la noche
    ('n21', 4): dict(ins=[report('@recordatorio', title='Leads de la noche', sub='Avisos para Valeria Ríos', time='8:00 am',
                                 sched='Recordatorio a primera hora', lines=[
        L('Diana Trejo · llegó domingo 11:40 pm', b=True), L('Lucía Hernández · llegó sábado 9:15 pm'),
        L('Llámalos antes de las 9:00 am', '@llamar', c='amber')],
        alert={'t': 'Sin llamada a las 9:00: Diana Trejo pasó a Paola G.', 'c': 'red', 'at': '@siguiente'})]),
    # 22 el día de tus asesores
    ('n22', 4): dict(ins=[note('@IA', typeAt='@IA+6', fields=[F('Busca', 'Depa 2 recámaras'), F('Zona', 'Tulum'), F('Presupuesto', '250 mil USD'),
                                                            F('Etapa', 'Cita', '@cita')]),
                          cita('@cita', confirmAt='@confirmar')]),
    ('n22', 5): dict(ins=[report('@resumen', title='Tu resumen del día', sub='Tu día con Lead Master', sched='Tu resumen llega a las 7:00 pm',
                                 lines=ADVISOR_DAY, alert=False)]),
    # 23 lo que quema tu inmobiliaria
    ('n23', 3): dict(ins=[callrec('@nadie', missed=True)]),
    ('n23', 5): dict(ins=[report('@dice', title='Sin contacto hoy', time='1:00 pm', sched='Alerta de leads sin contactar', lines=[
        L('Leads sin contactar hoy: 6', b=True), SEP('@asesor'),
        L('Adriana Solís · Diego H. · espera 5 h', '@asesor', c='red'),
        L('Lucía Hernández · Andrés M. · espera 26 h', '@esperando', c='red')], alert=False),
        tasks('@marca', who='Diego Herrera', right='Ordenadas por la IA', items=[
            T('Llamar primero a Adriana Solís', 'Lleva 5 h esperando'), T('Luego a Carlos Ruiz', 'Lleva 2 h esperando')]),
        ]),
    # 24 ahorita te mando
    ('n24', 5): dict(type='ui', ins=[tasks(0, '@reporte', who='Diego Herrera', items=[
        T('Mandar opciones a Adriana Solís', 'Lo prometiste ayer en el chat', at='@opciones'),
        T('Llamar a Diana Trejo el martes', 'Ella pidió que la buscaran', at='@martes'),
        T('Confirmar visita de Lucía Hernández', 'Sábado 11:00 am', 'done', at='@visita')]),
        report('@reporte', title='Compromisos del equipo', lines=[
            L('Cumplidos hoy: 7 de 10', b=True), SEP(),
            L('Pendiente: mandar opciones a Adriana Solís (Diego H.)', c='red'), L('Hecho: llamar a Diana Trejo (Valeria R.)', c='green')],
            alert=False)]),
    # 25 te apareció
    ('n25', 2): dict(ins=[crm('@CRM', '@bot', stale=True, chip='Nadie lo llenó')]),
    ('n25', 4): dict(ins=[crm('@CRM', move='@CRM+8'), tasks('@hacer'), report('@reporte')]),
    # A por qué tu CRM no funciona
    ('a', 2): dict(ins=[note('@etapas', '@tareas', empty=True), tasks('@tareas', late=True)]),
    ('a', 3): dict(ins=[crm('@CRM', '@hablan', stale=True, chip='Para ellos es una carga')]),
    ('a', 6): dict(ins=[crm('@intento', move='@etapa'), note('@nota', typeAt='@nota+4')]),
    ('a', 7): dict(type='ui', ins=[report(0, title='Reporte semanal', time='8:00 am', sched='Tu reporte llega los lunes a las 8:00 am', lines=[
        L('Leads de la semana: 214', '@semana', b=True), L('Llamaron a 142', '@llamaron', c='green'),
        L('Nunca contestaron: 38', '@contestó', c='amber'), L('En el olvido: 21 sin seguimiento', '@olvido', c='red'), SEP('@olvido+6'),
        L('Diego H.: 12 leads olvidados', '@olvido+6', c='red'), L('Paola G.: 0 olvidados', '@olvido+10', c='green')], alert=False)]),
    # B marketing vs ventas
    ('b', 6): dict(ins=[cita('@cita', '@llamar', mode='done', doneText='Cita registrada')]),
    # C puros curiosos
    ('c', 4): dict(ins=[callrec('@contestan', missed=True, title='Llamadas del equipo', right='No contesta', when='Lead de formulario de Meta',
                                attempts=['Lunes 10:14 · no contestó', 'Martes 4:30 pm · no contestó', 'Miércoles · no contestó'],
                                chip='Llenó el formulario y desapareció')]),
    ('c', 5): dict(ins=[cita('@agenda', '@avisa', mode='done', doneText='Cita agendada', source='Detectada en el chat por la IA')]),
    # D los CRM murieron
    ('d', 2): dict(ins=[crm('@CRM', '@notas', move=False, chip='Qué pasaba con cada lead'), note('@notas', empty=True)]),
    ('d', 5): dict(ins=[callrec('@Escucha'),
                        note('@registra', typeAt='@etapa', lead='Diana Trejo', tag='Lead · Polanco', stage='Interesada',
                             note='Busca 3 recámaras en Polanco para vivir. Quiere visitar el fin de semana.',
                             fields=[F('Presupuesto', '500 mil USD', '@presupuesto'), F('Zona', 'Polanco', '@zona'),
                                     F('Busca', '3 recámaras', '@busca'), F('Etapa', 'Interesada', '@etapa')])]),
    # E así recibirías tus reportes
    ('e', 5): dict(type='ui', ins=[report(0, title='Tu resumen del día', sub='Tu día con Lead Master', sched='Tu resumen llega a las 7:00 pm',
                                          lines=ADVISOR_DAY, alert=False)]),
    ('e', 6): dict(type='ui', ins=[report(0, lines=[
        L('Leads que entraron hoy: 37', '@entraron', b=True), SEP('@llamó'),
        L('Paola G. llamó a 14 · 2 citas', '@llamó'), L('Valeria R. llamó a 11 · 2 citas', '@llamó+5'),
        L('Diego H. llamó a 3', '@llamó+10', c='amber'), SEP('@contacto'),
        L('Sin contacto: 6 (Diego H. 4, Andrés M. 2)', '@contacto', c='red'), L('Citas del día: 5', '@citas', c='green')],
        alert={'t': 'Ahora: Adriana Solís lleva 26 h sin llamada (Diego H.)', 'c': 'amber', 'at': '@citas+20'})]),
    # F en un minuto
    ('f', 5): dict(type='ui', ins=[report(0, title='Reporte semanal', time='8:00 am', sched='Tu reporte llega los lunes a las 8:00 am',
                                          lines=WEEKLY, alert=False)]),
    # G1..G5
    ('g1', 4): dict(ins=[callrec('@habla', summary=['Habló de precios y entrega', 'Quiere visitar el sábado', 'Siguiente paso: confirmar'])]),
    ('g2', 4): dict(ins=[callrec('@llamada', '@sin')]),
    ('g3', 3): dict(ins=[crm('@CRM', move='@CRM+8', chip='Solo conversaciones con leads')]),
    ('g3', 4): dict(ins=[callrec('@grabadas')]),
    ('g4', 4): dict(ins=[report('@llegue', title='Lead nuevo para ti', sub='Avisos para Valeria Ríos', time='10:15 am',
                                sched='Lead asignado hace 1 min', lines=[
        L('Diana Trejo · Desarrollo en Mérida', b=True), L('Viene de: anuncio de Meta'), L('Llámala antes de 10 min', '@llamada', c='amber')],
        alert={'t': 'Sin llamada en 10 min: el lead pasó a Diego H.', 'c': 'red', 'at': '@otro'})]),
    ('g4', 5): dict(ins=[cita('@agenda', '@avise', mode='done', what='Recorrido · Desarrollo', doneText='Recorrido agendado',
                              when='Sábado 15 · 11:00 am', dayIdx=5)]),
    ('g6', 4): dict(ins=[report('@guardia', title='Lead nuevo · guardia', sub='Avisos para Paola Gutiérrez', time='11:40 pm',
                                sched='Estás de guardia esta noche', lines=[
        L('Diana Trejo · Depa en Tulum', b=True), L('Llegó hace 1 min por Meta'), L('Asignado a ti: llámala ahora', '@asignados', c='amber')],
        alert={'t': 'Paola G. le escribió en 3 min.', 'c': 'green', 'at': '@asignados+20'})]),
    ('g5', 3): dict(ins=[crm('@vacío', stale=True, chip='Sin notas, sin etapas')]),
    ('g5', 5): dict(ins=[crm('@CRM', move='@solo'), callrec('@escucha'),
                         note('@nota', typeAt='@nota+4', fields=[F('Presupuesto', '180 mil USD', '@presupuesto'), F('Zona', 'Mérida', '@zona'),
                                                               F('Objeciones', 'Fecha de entrega', '@objeciones'), F('Etapa', 'Cita', '@etapa')],
                              lead='Adriana Solís', tag='Lead · Mérida', note='Le preocupa la fecha de entrega. Quiere visitar el sábado.'),
                         tasks('@tarea', items=[T('Confirmar visita de Adriana Solís', 'Siguiente paso, creado por la IA', at='@tarea')])]),
    ('g5', 6): dict(ins=[report('@recibes')]),
}


# ---------------------------------------------------------------------
# Idea 1 con el gancho en otras ciudades: solo cambia la primera escena (voz, foto y ciudad);
# el resto reutiliza las voces del 01 de Guadalajara. Las zonas de los ejemplos se adaptan.
CITIES = [
    ('jalisco', 'jal', 'Jalisco', 'gdl_development', 'Jalisco', ('Zapopan', 'Providencia')),
    ('monterrey', 'mty', 'Monterrey', 'monterrey_tower', 'Monterrey', ('San Pedro', 'Cumbres')),
    ('merida', 'mid', 'Mérida', 'merida_house', 'Mérida', ('Temozón Norte', 'Altabrisa')),
    ('puebla', 'pue', 'Puebla', 'aerial_community', 'Puebla', ('Angelópolis', 'Cholula')),
    ('queretaro', 'qro', 'Querétaro', 'queretaro_house', 'Querétaro', ('Juriquilla', 'El Refugio')),
    ('cdmx', 'cdmx', 'la Ciudad de México', 'polanco_building', 'CDMX', ('Polanco', 'Del Valle')),
    ('cancun', 'cun', 'Cancún', 'cancun_tower', 'Cancún', ('Puerto Cancún', 'Zona Hotelera')),
]


def city_variants():
    import copy
    base = next(v for v in VIDEOS if v['prefix'] == 'n01')

    def zones(obj, z1, z2):
        return json.loads(json.dumps(obj, ensure_ascii=False).replace('Zapopan', z1).replace('Providencia', z2))

    for slug, code, name, img, short, (z1, z2) in CITIES:
        prefix = f'n01{code}'
        v = zones(copy.deepcopy(base), z1, z2)
        v['vid'] = f'01-si-yo-tuviera-una-inmobiliaria-en-{slug}'
        v['prefix'] = prefix
        v['title'] = f'Si yo tuviera una inmobiliaria en {name}'
        v['keywords'] = [k for k in v['keywords'] if k != 'Guadalajara'] + [name.split()[-1]]
        first = v['scenes'][0]
        first['text'] = first['text'].replace('en Guadalajara', f'en {name}')
        first['p']['img'] = img
        first['p']['kicker'] = f'{short} · +5 asesores'
        for i, sc in enumerate(v['scenes'][1:], start=2):
            sc['key'] = f'n01_s{i}'
        for (pre, n), extra in list(INSERTS.items()):
            if pre == 'n01':
                INSERTS[(prefix, n)] = zones(extra, z1, z2)
        VIDEOS.append(v)


city_variants()


# ---------------------------------------------------------------------

def build_all():
    out = []
    for v in VIDEOS:
        scenes = []
        for i, sc in enumerate(v['scenes']):
            sc = dict(sc)
            sfx = list(sc.pop('sfx', []))
            sfx += sc.pop('extra_sfx', [])
            sfx.insert(0, fx(I, 0, 0.2) if i == 0 else fx(W, 0, 0.08))
            sc['sfx'] = sfx
            sc['key'] = sc.get('key') or f"{v['prefix']}_s{i + 1}"
            extra = INSERTS.get((v['prefix'], i + 1))
            if extra:
                sc.update(extra)
            sc.setdefault('voice', v['voice'])
            if sc['type'] == 'cta':
                sc.setdefault('captions', True)
            scenes.append(sc)
        spec = {'id': v['vid'], 'title': v['title'], 'voice': v['voice'], 'music': f"music/{v['music']}.mp3",
                'tempo': v['tempo'], 'keywords': v['keywords'], 'scenes': scenes}
        path = os.path.join(ROOT, 'videos', f"{v['vid']}.json")
        json.dump(spec, open(path, 'w'), ensure_ascii=False, indent=1)
        out.append(path)
    return out


if __name__ == '__main__':
    paths = build_all()
    words = sum(len(sc['text'].split()) for v in VIDEOS for sc in v['scenes'])
    chars = sum(len(sc['text']) for v in VIDEOS for sc in v['scenes'])
    print(f'{len(paths)} videos, {words} palabras, {chars} caracteres')
