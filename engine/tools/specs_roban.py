"""Serie Sala de Juntas: 5 variaciones de J03 (el asesor que se roba los leads). J07 a J11.

Uso: python3 tools/specs_roban.py  -> escribe videos/J07..J11*.json
Planos de IA: 3 por video (un personaje hablando por plano), mismo estilo caricatura 3D que J03.
"""
import copy
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
J03 = json.load(open(os.path.join(ROOT, 'videos', 'J03-se-lo-ofrezco-a-mi-compadre.json')))
AUTO = json.load(open(os.path.join(ROOT, 'videos', '_auto_std.json')))
J03_STACK = copy.deepcopy(next(s for s in J03['scenes'] if s.get('key') == 'j03_s4'))
J03_CTA = copy.deepcopy(next(s for s in J03['scenes'] if s.get('key') == 'j03_s5'))

STYLE = ('Vertical 9:16 video. Stylized 3D animated cartoon with exaggerated caricature proportions, '
         'like a modern animated comedy film.')
RODRIGO = ('Rodrigo, a tall thin Mexican real estate agent in his thirties with slicked-back shiny hair, a thin pencil '
           'mustache, a shiny grey suit with an open collar and a gold chain, sly smile')
RAMIRO = ('Don Ramiro, the owner of a real estate agency, a short chubby Mexican man in his fifties with a thick black '
          'mustache, receding hairline, white shirt with rolled-up sleeves and a loose red tie')
PAOLA = ('Paola, a confident Mexican real estate agent in her thirties with big curly hair, a pink blouse and gold '
         'hoop earrings')
FABIAN = ('Fabián, the sales director of a real estate agency, a Mexican man in his forties with a neatly trimmed '
          'beard, square black glasses and a fitted navy blazer over a black turtleneck')
CAR = 'Daytime, inside a parked car right outside a real estate agency office with a big "AGENCIA INMOBILIARIA" sign.'
MEETING = ('Warm office lighting, a modern real estate agency meeting room with a glass wall, a long white table '
           'with laptops, coffee mugs and printed charts.')


def ia(clip, who, dice, setting, action, voice_style, shot='Medium close-up, static camera.', amb='',
       pronoun='his'):
    return {
        'clip': clip,
        'dice': dice,
        'prompt': (f'{STYLE} {setting} {who}, {action} and says in Mexican Spanish, {voice_style}: "{dice}" '
                   f'{shot} Audio: only {pronoun} voice in Spanish{amb}. No music. No subtitles, no on-screen text.'),
    }


def fx(src, at, vol):
    return {'src': src, 'at': at, 'vol': vol}


def clip(name, first=None):
    sc = {'type': 'clip', 'p': {'src': f'clips/{name}.mp4', 'words': f'clips/{name}.words.json'}}
    if first:
        sc['p'].update(first)
        sc['sfx'] = [fx('sfx/notif.wav', 0, 0.16)]
    return sc


def photo(key, text, img, lines, lineAts, stamp, stamp_at, size=124, stamp_size=100):
    return {
        'type': 'photo', 'key': key, 'voice': 'antonio', 'tail': 0.1, 'text': text,
        'p': {'img': img, 'lines': lines, 'lineAts': lineAts, 'size': size,
              'stamp': {'text': stamp, 'at': stamp_at, 'size': stamp_size}},
        'sfx': [fx('sfx/whoosh.wav', 0, 0.08), fx('sfx/pop.wav', lineAts[1], 0.1), fx('sfx/stamp.wav', stamp_at, 0.26)],
    }


def panel(key, text, ok, bad, aviso_at='@aviso', title='Conversaciones de hoy'):
    """ok / bad: (asesor, lead, resumen, estado, palabra)"""
    rows = [
        {'ch': 'wa', 'advisor': ok[0], 'lead': ok[1], 'summary': ok[2], 'status': ok[3], 'color': 'green', 'at': ok[4]},
        {'ch': 'wa', 'advisor': bad[0], 'lead': bad[1], 'summary': bad[2], 'status': bad[3], 'color': 'red', 'at': bad[4]},
    ]
    sfx = [fx('sfx/whoosh.wav', 0, 0.08), fx('sfx/ding.wav', ok[4], 0.08), fx('sfx/impact.wav', bad[4], 0.12)]
    if aviso_at:
        sfx.append(fx('sfx/notif.wav', aviso_at, 0.14))
    return {'type': 'panel', 'key': key, 'voice': 'antonio', 'text': text,
            'p': {'title': title, 'right': 'Avisos de la IA', 'rows': rows}, 'sfx': sfx}


KEYWORDS = ['WhatsApp', 'asesor', 'asesores', 'automático', 'aviso', 'avisa', 'compadre', 'comisión', 'competencia',
            'dólares', 'fuera', 'grabadas', 'inmobiliaria', 'inmobiliarios', 'lead', 'leads', 'reporte', 'robando',
            'probar', 'contestó', 'celular', 'saber', 'venta']


def spec(vid, title, ias, scenes):
    return {'id': vid, 'title': title, 'voice': 'antonio', 'music': 'music/pulse.mp3', 'tempo': 1.15,
            'keywords': KEYWORDS, 'ia': ias, 'scenes': scenes}


V = []

# ---------- J07 · ¿Mis asesores me roban leads? (no lo puedes saber) ----------
V.append(spec(
    'J07-me-estan-robando-los-leads',
    '¿Me están robando los leads?: el dueño que no lo puede saber (Serie Sala de Juntas, video 7)',
    [
        ia('j07_a', RAMIRO, '¿Y si mis asesores inmobiliarios me están robando los leads? ¿Cómo lo voy a saber?',
           'Night, the owner\'s office of a real estate agency, dark, lit only by the glow of his phone and a desk lamp; '
           'through the glass wall you can see the empty desks of his real estate agents.',
           'paranoid and scared, peeks between the window blinds toward the agents\' desks, then looks at the camera '
           'with wide worried eyes, sweating',
           'anxious, whispering and fast', amb=', quiet night office ambience'),
        ia('j07_b', RODRIGO, 'Ese proyecto aquí no lo tenemos, señora… pero no se preocupe: conozco a alguien que sí.',
           CAR, 'sits in the driver seat holding the phone to his ear, smiling',
           'in a sweet, overly friendly voice', amb=', quiet street ambience'),
        ia('j07_c', RODRIGO, 'Lo vendo por fuera… y mi director comercial ni cuenta se va a dar.',
           CAR, 'lowers the phone, covers it with his hand, turns to the camera, winks',
           'whispering like a mockumentary confession, sly', shot='Close-up, static camera.'),
    ],
    [
        clip('j07_a', {'lines': ['¿ME ROBAN', 'LOS [LEADS]?'], 'kicker': 'Dueño de inmobiliaria',
                       'kickerColor': 'red', 'titleOut': 66, 'size': 130}),
        clip('j07_b'),
        clip('j07_c'),
        photo('j07_s2', 'Si tus asesores atienden los leads desde su WhatsApp personal, no tienes cómo saber qué les '
                        'dicen, ni a quién se los pasan.',
              'owner_stressed', ['NO LO', 'PUEDES [SABER]'], ['@leads', '@saber'], 'SIN CONTROL', '@pasan'),
        copy.deepcopy(AUTO),
        panel('j07_s3', 'Con Lead Master, la IA lee los chats de cada asesor. Y si alguien manda un lead a otro lado, '
                        'te llega un aviso.',
              ('Valeria Ríos', 'Diana Trejo', 'Le mandó 3 opciones de la inmobiliaria · visita el sábado', 'Normal',
               '@chats'),
              ('Rodrigo (asesor)', 'Lucía Hernández', '«Ese proyecto no lo tenemos, pero conozco a alguien que sí»',
               'Lead por fuera', '@lado')),
        copy.deepcopy(J03_STACK),
        copy.deepcopy(J03_CTA),
    ]))

# ---------- J08 · Un lead de 200 mil dólares (la comisión) ----------
V.append(spec(
    'J08-un-lead-de-200-mil-dolares',
    'Un lead de 200 mil dólares: la comisión que se va por fuera (Serie Sala de Juntas, video 8)',
    [
        ia('j08_a', RODRIGO, 'Asesores inmobiliarios: ¿saben cuánto vale uno de estos leads? Un depa de doscientos mil '
                             'dólares.',
           CAR, 'shows his phone screen with a luxury apartment listing to the camera, greedy grin, rubs his thumb '
                'and fingers together in a money gesture',
           'fast and confident, like a mockumentary confession', amb=', quiet street ambience'),
        ia('j08_b', RODRIGO, 'Compadre, te paso el lead. Tú lo cierras allá y la comisión nos la partimos.',
           CAR, 'holds the phone to his ear, looks left and right to make sure nobody is watching, leans in',
           'whispering, conspiratorial', shot='Close-up, static camera.'),
        ia('j08_c', RAMIRO, '¿Doscientos leads este mes… y ni una venta? Yo no entiendo qué pasa.',
           'Daytime, a real estate agency owner\'s office with a big whiteboard that says "VENTAS: 0".',
           'stands in front of the whiteboard holding a printed leads report, confused, scratches his head and '
           'looks at the camera', 'confused and frustrated', shot='Medium shot, static camera.',
           amb=', office ambience'),
    ],
    [
        clip('j08_a', {'lines': ['UN [LEAD] DE', 'US$200,000'], 'kicker': 'Asesores inmobiliarios',
                       'kickerColor': 'red', 'titleOut': 66, 'size': 118}),
        clip('j08_b'),
        clip('j08_c'),
        {
            'type': 'stat', 'key': 'j08_s2', 'voice': 'antonio', 'tail': 0.1,
            'text': 'Haz la cuenta: cada lead que se va por fuera puede ser una venta de cincuenta, cien o doscientos '
                    'mil dólares. Y esa comisión ya no es para tu inmobiliaria.',
            'p': {'title': 'LO QUE SE VA POR FUERA', 'img': 'advisor_car', 'stacked': True,
                  'items': [
                      {'value': 50000, 'prefix': 'US$', 'label': 'un depa', 'at': '@cincuenta', 'color': 'amber'},
                      {'value': 100000, 'prefix': 'US$', 'label': 'una casa', 'at': '@cien', 'color': 'amber'},
                      {'value': 200000, 'prefix': 'US$', 'label': 'un penthouse', 'at': '@doscientos',
                       'color': 'red'},
                  ]},
            'sfx': [fx('sfx/whoosh.wav', 0, 0.08), fx('sfx/ding.wav', '@cincuenta', 0.09),
                    fx('sfx/ding.wav', '@cien', 0.09), fx('sfx/impact.wav', '@doscientos', 0.12)],
        },
        copy.deepcopy(AUTO),
        panel('j08_s3', 'Con Lead Master ves cada conversación. Y si un asesor manda un lead a otra inmobiliaria, te '
                        'llega un aviso antes de que se cierre la venta.',
              ('Valeria Ríos', 'Diana Trejo', 'Depa de 2 recámaras · visita el sábado 11 am', 'Normal',
               '@conversación'),
              ('Rodrigo (asesor)', 'Adriana Solís', '«Te paso con mi compadre, allá te lo dejan mejor»',
               'Lead por fuera', '@otra')),
        copy.deepcopy(J03_CTA),
    ]))

# ---------- J09 · «Ese lead nunca contestó» (el director comercial le cree) ----------
V.append(spec(
    'J09-ese-lead-nunca-contesto',
    'Ese lead nunca contestó: lo que tu director comercial no ve (Serie Sala de Juntas, video 9)',
    [
        ia('j09_a', FABIAN, 'A ver, asesores inmobiliarios: de los leads de ayer, ¿qué pasó con el del penthouse?',
           MEETING, 'stands at the head of the table holding a tablet, serious, looks over his glasses at the real '
                    'estate agents sitting around the table',
           'firm and direct', shot='Medium shot, slow push-in.', amb=', office ambience'),
        ia('j09_b', RODRIGO, 'Ese lead nunca contestó, jefe. Ya lo di por perdido.',
           MEETING, 'sits at the table leaning back in his chair, totally relaxed, shrugs and spins a pen',
           'casual and convincing', amb=', office ambience'),
        ia('j09_c', RODRIGO, '¡Felicidades por su penthouse, señora! Mañana firmamos… pero en la otra oficina.',
           CAR, 'holds the phone to his ear, very happy, then winks at the camera',
           'cheerful and overly friendly, the last words whispered', amb=', quiet street ambience'),
    ],
    [
        clip('j09_a', {'lines': ['¿Y EL [LEAD]', 'DEL PENTHOUSE?'], 'kicker': 'Junta de asesores · inmobiliaria',
                       'kickerColor': 'red', 'titleOut': 66, 'size': 118}),
        clip('j09_b'),
        clip('j09_c'),
        photo('j09_s2', 'Tu director comercial no puede leer el WhatsApp de cada asesor. Si le dicen «no contestó», '
                        'tiene que creerles. Aunque el lead sí contestó… y compró en otro lado.',
              'meeting', ['«NO', '[CONTESTÓ]»'], ['@director', '@creerles'], '¿SEGURO?', '@compró', size=140,
              stamp_size=120),
        copy.deepcopy(AUTO),
        panel('j09_s3', 'Con Lead Master, si un asesor dice que el lead no contestó, pero en su WhatsApp hay mensajes '
                        'con él, la IA te avisa.',
              ('Paola Gutiérrez', 'Diana Trejo', 'Contestó · cita el sábado 11 am', 'Normal', '@asesor'),
              ('Rodrigo (asesor)', 'Adriana Solís', 'Dijo «no contestó» · 14 mensajes con ella ayer', 'No cuadra',
               '@mensajes'), aviso_at='@avisa'),
        copy.deepcopy(J03_CTA),
    ]))

# ---------- J10 · Dos celulares (el lead se va a la competencia) ----------
V.append(spec(
    'J10-dos-celulares',
    'Dos celulares: el asesor que le pasa tus leads a la competencia (Serie Sala de Juntas, video 10)',
    [
        ia('j10_a', RODRIGO, 'Asesores inmobiliarios: dos celulares. Uno para los leads de la inmobiliaria… y otro '
                             'para los míos.',
           'Daytime, a busy modern real estate agency office with desks and property posters.',
           'sits at his desk holding two phones, one in each hand, lifts each one when he mentions it, smug grin, '
           'talking to the camera', 'fast and confident, like a mockumentary confession', amb=', office ambience'),
        ia('j10_b', PAOLA, 'Rodrigo, ¿otra vez le estás pasando leads a la competencia?',
           'Daytime, a busy modern real estate agency office with desks and property posters.',
           'stands behind a desk with her arms crossed, catching a colleague red-handed, raises one eyebrow, angry',
           'firm and accusing', amb=', office ambience', pronoun='her'),
        ia('j10_c', RODRIGO, '¿Yo? No, no, no… es mi primo. Bueno, mi primo trabaja ahí.',
           'Daytime, a busy modern real estate agency office with desks and property posters.',
           'sitting at his desk, startled, quickly hides one of his two phones inside his jacket, nervous laugh, '
           'sweating', 'nervous and fast', amb=', office ambience'),
    ],
    [
        clip('j10_a', {'lines': ['¿EL [LEAD] ES', 'TUYO O SUYO?'], 'kicker': 'Inmobiliarias',
                       'kickerColor': 'red', 'titleOut': 66, 'size': 122}),
        clip('j10_b'),
        clip('j10_c'),
        photo('j10_s2', 'Si tus leads viven en el celular personal de cada asesor, son más de él que de tu '
                        'inmobiliaria. Y nadie ve a quién se los pasa.',
              'advisor_night', ['SU CELULAR,', 'SUS [LEADS]'], ['@celular', '@inmobiliaria'],
              'A LA COMPETENCIA', '@pasa', stamp_size=80),
        copy.deepcopy(AUTO),
        panel('j10_s3', 'Con Lead Master, el WhatsApp de cada asesor está conectado: ves lo que le dice a cada lead. '
                        'Y si manda uno a la competencia, te avisa.',
              ('Valeria Ríos', 'Diana Trejo', 'Le mandó 3 opciones de la inmobiliaria · visita el sábado', 'Normal',
               '@conectado'),
              ('Rodrigo (asesor)', 'Lucía Hernández', '«Mejor te atiende mi primo, en la otra inmobiliaria»',
               'A la competencia', '@competencia'), aviso_at='@avisa'),
        copy.deepcopy(J03_STACK),
        copy.deepcopy(J03_CTA),
    ]))

# ---------- J11 · ¿Quién se robó el lead? (la junta, sin pruebas) ----------
V.append(spec(
    'J11-quien-se-robo-el-lead',
    '¿Quién se robó el lead?: la junta sin pruebas (Serie Sala de Juntas, video 11)',
    [
        ia('j11_a', RAMIRO, '¡Asesores inmobiliarios! De todos mis leads, el de la casa en Zapopan compró… ¡con otra '
                            'inmobiliaria!',
           MEETING, 'stands at the head of the table, his face turns red with anger, slams both fists on the table so '
                    'the mugs jump, shouting at his real estate agents',
           'furious, shouting', shot='Medium shot, slow push-in.', amb=', fists on the table, mugs rattling'),
        ia('j11_b', PAOLA, '¡Fue Rodrigo, jefe! Yo vi cuando le pasó el lead a su compadre.',
           MEETING, 'sits at the table, stands up and points her finger accusingly across the table',
           'indignant and fast', amb=', office ambience', pronoun='her'),
        ia('j11_c', RODRIGO, '¿Yo? Qué acusación tan fuerte… A ver, ¡pruébalo!',
           MEETING, 'sits at the table, raises both hands pretending to be offended, then leans back with a smug '
                    'smile and crosses his arms', 'dramatic, then cocky', amb=', a dramatic silence'),
    ],
    [
        clip('j11_a', {'lines': ['¿QUIÉN SE ROBÓ', 'EL [LEAD]?'], 'kicker': 'Junta de asesores · inmobiliaria',
                       'kickerColor': 'red', 'titleOut': 66, 'size': 124}),
        clip('j11_b'),
        clip('j11_c'),
        photo('j11_s2', 'Y ese es el problema: si todo pasa en el WhatsApp personal de cada asesor, no puedes probar '
                        'quién se llevó el lead.',
              'meeting', ['SIN', '[PRUEBAS]'], ['@problema', '@probar'], 'NO SE PUEDE PROBAR', '@llevó', size=150,
              stamp_size=76),
        copy.deepcopy(AUTO),
        panel('j11_s3', 'Con Lead Master queda todo: qué le dijo cada asesor a cada lead y cuándo. Y si alguien lo '
                        'manda a otro lado, la IA te avisa.',
              ('Paola Gutiérrez', 'Diana Trejo', 'Le mandó 2 casas en Zapopan · visita el sábado', 'Normal', '@dijo'),
              ('Rodrigo (asesor)', 'Lucía Hernández', '«Te paso el número de mi compadre, él te lo deja más barato»',
               'Lead por fuera', '@lado'), aviso_at='@avisa'),
        copy.deepcopy(J03_STACK),
        copy.deepcopy(J03_CTA),
    ]))


def main():
    for s in V:
        out = os.path.join(ROOT, 'videos', s['id'] + '.json')
        json.dump(s, open(out, 'w'), ensure_ascii=False, indent=1)
        print(out)


if __name__ == '__main__':
    main()
