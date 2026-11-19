"""Serie Sala de Juntas: J13 a J21 (mismo método que J07-J11).

Uso: python3 tools/specs_sala2.py  -> escribe videos/J13..J21*.json
3 planos de IA por video (un personaje por plano), 1 línea nueva de narrador (jXX_s2, photo) y se reusan
auto_std, j03_s3 (panel) y/o j03_s4 (stack) y el cierre j03_s5 («Comenta LEADS»).
"""
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from specs_roban import (AUTO, CAR, FABIAN, J03, J03_CTA, J03_STACK, MEETING, RAMIRO, RODRIGO, ROOT,  # noqa: E402
                         clip, ia, photo, spec)

J03_PANEL = copy.deepcopy(next(s for s in J03['scenes'] if s.get('key') == 'j03_s3'))

KARLA = ('Karla, a Mexican real estate agent in her late twenties with a very tight high ponytail, huge fake eyelashes, '
         'a leopard print blouse and long pink nails')
BRAYAN = ('Brayan, a young Mexican real estate agent in his twenties who acts like a TikTok influencer, with a trendy '
          'fade haircut, a tight white t-shirt under a slim beige blazer, a small gold earring, sunglasses on top of his head and white sneakers')
MONICA = ('Doña Mónica, the owner of a real estate agency, an elegant Mexican woman in her fifties with short silver '
          'hair, red-framed glasses, a cream blazer and pearl earrings')
ARTURO = ('Don Arturo, a Mexican real estate developer in his sixties, tall and broad with grey hair and a grey '
          'mustache, wearing a white hard hat, a white shirt and a reflective orange safety vest')
CLIENTA = ('Señora Lupita, a cheerful Mexican woman in her fifties with a short curly brown bob, big sunglasses on her '
           'head and a colorful blouse')
KEVIN = ('Kevin, a chubby young Mexican real estate agent in his twenties with spiky gelled hair, a wrinkled light blue '
         'shirt and a crooked tie')
ANON = ('an anonymous real estate agent shown only as a dark silhouette against a bright backlit window, face '
        'completely hidden in shadow, wearing a suit')
HOST = ('Daniela, a Mexican podcast host in her thirties with a short black bob, big headphones around her neck and a '
        'black t-shirt')
PODCAST = ('A small podcast studio with acoustic foam panels, a neon sign that says "PODCAST", and big professional '
           'microphones on boom arms.')
OFFICE = 'Daytime, a busy modern real estate agency office with desks and property posters.'
NIGHT_OFFICE = ('Night, the owner\'s office of a real estate agency, dark, lit only by the glow of a big computer '
                'monitor showing a Facebook Ads dashboard with charts and the word "LEADS".')


def hook(lines, kicker, size=118):
    return {'lines': lines, 'kicker': kicker, 'kickerColor': 'red', 'titleOut': 66, 'size': size}


def tail(*extra):
    """Escenas que se reusan después de la línea nueva del narrador."""
    return [copy.deepcopy(AUTO)] + [copy.deepcopy(x) for x in extra] + [copy.deepcopy(J03_CTA)]


V = []

# ---------- J13 · El dueño que paga la pauta y no vende ----------
V.append(spec(
    'J13-pago-la-pauta-y-no-vendo',
    'Pago la pauta y no vendo: los leads que sí compraron, por fuera (Serie Sala de Juntas, video 13)',
    [
        ia('j13_a', RAMIRO, 'Cien mil pesos al mes en Facebook… trescientos leads para mis asesores inmobiliarios.',
           NIGHT_OFFICE, 'sits in front of the monitor, exhausted, loosened tie, looks at the screen and then at the '
                         'camera with tired eyes', 'tired and bitter, slow', amb=', quiet night office ambience'),
        ia('j13_b', RAMIRO, '¿Y ventas? Cero. ¿Dónde están esos clientes?',
           NIGHT_OFFICE, 'rubs his face with both hands in desperation, then throws his arms up and looks at the camera',
           'desperate, almost shouting', shot='Close-up, static camera.', amb=', quiet night office ambience'),
        ia('j13_c', RODRIGO, 'Firme aquí, señora. Y tranquila: la inmobiliaria no tiene por qué enterarse.',
           'Daytime, a coffee shop table with two coffee cups and a contract with a pen.',
           'sits at the table sliding a contract and a pen to a smiling client off-screen, then winks at the camera',
           'sweet and overly friendly, the last words whispered', amb=', coffee shop ambience'),
    ],
    [
        clip('j13_a', hook(['$100 MIL EN [LEADS]', '¿Y LAS VENTAS?'], 'Dueño de inmobiliaria', 104)),
        clip('j13_b'),
        clip('j13_c'),
        photo('j13_s2', 'Pagas la pauta y los leads sí llegan. Pero si tus asesores los atienden en su WhatsApp '
                        'personal, algunas de esas ventas se cierran por fuera.',
              'scrolling_ads', ['LOS LEADS', 'SÍ [LLEGAN]'], ['@pauta', '@WhatsApp'], 'POR FUERA', '@fuera'),
    ] + tail(J03_PANEL)))

# ---------- J14 · «Escríbame a mi número personal» ----------
V.append(spec(
    'J14-escribame-a-mi-numero-personal',
    'Escríbame a mi número personal: la nota de voz que no era para el grupo (Serie Sala de Juntas, video 14)',
    [
        ia('j14_a', KARLA, 'Asesores inmobiliarios: así me quedo con los leads de la inmobiliaria.',
           'Daytime, a narrow office hallway of a real estate agency next to the restrooms, a fire extinguisher on '
           'the wall.', 'hides in the hallway, looks left and right, then leans toward the camera with a sly smile',
           'whispering, like a mockumentary confession', amb=', muffled office ambience', pronoun='her'),
        ia('j14_b', KARLA, 'Señora, escríbame a mi número personal, ¿sí? Yo le consigo uno igualito… y no le comente '
                           'a nadie.',
           'Daytime, a narrow office hallway of a real estate agency next to the restrooms.',
           'holds her phone close to her mouth recording a WhatsApp voice note, covering it with her other hand',
           'whispering fast, conspiratorial', shot='Close-up, static camera.', pronoun='her'),
        ia('j14_c', KARLA, '¿Qué? No, no, no… ¿lo mandé al grupo de la inmobiliaria?',
           'Daytime, a narrow office hallway of a real estate agency next to the restrooms.',
           'looks at her phone screen, her eyes go huge with horror, she covers her mouth',
           'panicking, high pitched', amb=', a phone notification sound', pronoun='her'),
    ],
    [
        clip('j14_a', hook(['¿A QUÉ NÚMERO', 'VA TU [LEAD]?'], 'Inmobiliarias', 112)),
        clip('j14_b'),
        clip('j14_c'),
        photo('j14_s2', 'Esta vez la cacharon por error. Pero casi siempre pasa en el WhatsApp personal del asesor, '
                        'y en tu inmobiliaria nadie se entera.',
              'advisor_woman', ['«A MI NÚMERO', '[PERSONAL]»'], ['@error', '@WhatsApp'], 'NADIE SE ENTERA',
              '@entera', stamp_size=80),
    ] + tail(J03_PANEL)))

# ---------- J15 · El gerente se da cuenta ----------
V.append(spec(
    'J15-el-muchacho-que-me-escribio-de-ustedes',
    'El muchacho que me escribió de ustedes: el gerente que se dio cuenta (Serie Sala de Juntas, video 15)',
    [
        ia('j15_a', FABIAN, 'Hoy yo mismo voy a llamar a los leads que mis asesores inmobiliarios dieron por perdidos.',
           'Daytime, the sales manager\'s office of a real estate agency with a glass wall.',
           'sits at his desk with a printed list of leads, dials on his phone and puts it to his ear, determined',
           'determined, firm', amb=', office ambience'),
        ia('j15_b', CLIENTA, 'No, ya compré, gracias. El muchacho que me escribió de ustedes me consiguió otro '
                             'departamento.',
           'Daytime, a bright cozy living room.', 'sits on her sofa talking on the phone, happy and friendly',
           'cheerful and chatty', amb=', quiet home ambience', pronoun='her'),
        ia('j15_c', FABIAN, '¿Otro departamento? ¿Con quién…? ¡Rodrigo!',
           'Daytime, the sales manager\'s office of a real estate agency with a glass wall.',
           'holds the phone, confused, then realizes, his face turns red with fury, he stands up and looks through the '
           'glass wall toward the agents\' desks', 'confused, then furious shouting', shot='Close-up, slow push-in.',
           amb=', office ambience'),
    ],
    [
        clip('j15_a', hook(['¿Y ESE [LEAD]', 'CON QUIÉN COMPRÓ?'], 'Gerente de inmobiliaria', 108)),
        clip('j15_b'),
        clip('j15_c'),
        photo('j15_s2', 'Ese gerente se enteró de suerte. Si cada asesor atiende los leads en su WhatsApp personal, '
                        'casi nunca te vas a enterar.',
              'owner_phone_report', ['SE ENTERÓ', 'DE [SUERTE]'], ['@gerente', '@asesor'], 'CASI NUNCA',
              '@enterar'),
    ] + tail(J03_PANEL, J03_STACK)))

# ---------- J16 · Regla número uno del asesor vivo ----------
V.append(spec(
    'J16-regla-numero-uno-del-asesor-vivo',
    'Regla número uno del asesor vivo: los clientes se van con él (Serie Sala de Juntas, video 16)',
    [
        ia('j16_a', BRAYAN, 'Regla número uno del asesor inmobiliario vivo: los leads entran por el WhatsApp de la '
                            'empresa… y yo me los paso a mi WhatsApp.',
           'Daytime, his desk in a real estate agency office, a ring light and a phone on a tripod in front of him.',
           'talks to the camera like a TikTok tutorial, counting with one finger, moving his hands a lot',
           'fast and cocky, like an influencer', amb=', office ambience'),
        ia('j16_b', BRAYAN, 'Regla número dos: si me corren… los clientes se van conmigo.',
           'Daytime, his desk in a real estate agency office, a ring light in front of him.',
           'leans toward the camera, lowers his sunglasses and winks, then points at himself with both thumbs',
           'cocky, slow and smug', shot='Close-up, static camera.', amb=', office ambience'),
        ia('j16_c', RAMIRO, '¿Ese no es… mi asesor?',
           'Daytime, the owner\'s office of a real estate agency.',
           'sits at his desk watching a video on his phone, his jaw drops and his eyes pop out, he looks at the camera '
           'in shock', 'shocked, slow', shot='Close-up, static camera.', amb=', faint phone video audio'),
    ],
    [
        clip('j16_a', hook(['REGLA DEL', '[ASESOR] VIVO'], 'Inmobiliarias', 124)),
        clip('j16_b'),
        clip('j16_c'),
        photo('j16_s2', 'Y tiene razón: si el lead vive en el WhatsApp personal del asesor, el día que se va, se lleva '
                        'tus clientes. Y tú pagaste cada uno.',
              'advisor_night', ['TÚ LOS PAGAS,', 'ÉL SE LOS [LLEVA]'], ['@razón', '@lleva'], 'TUS CLIENTES',
              '@pagaste', size=112, stamp_size=90),
    ] + tail(J03_STACK)))

# ---------- J17 · La dueña que perdió su base de datos ----------
V.append(spec(
    'J17-le-di-los-leads-y-se-fue',
    'Le di los leads y se fue: la dueña que perdió sus clientes (Serie Sala de Juntas, video 17)',
    [
        ia('j17_a', MONICA, 'A mi mejor asesor inmobiliario le pagué la pauta, le pagué el sueldo, le di los leads…',
           'Night, an empty real estate agency office, rows of empty desks, only one desk lamp on.',
           'stands next to an empty desk with an open folder in her hands, voice breaking, counts with her fingers',
           'hurt and angry, slow', amb=', quiet night office ambience', pronoun='her'),
        ia('j17_b', MONICA, '…y se fue con la competencia. ¡Con todos mis clientes!',
           'Night, an empty real estate agency office, rows of empty desks, only one desk lamp on.',
           'slams the folder on the desk so papers fly everywhere, furious, looks at the camera',
           'furious, shouting', shot='Medium close-up, static camera.', amb=', papers flying', pronoun='her'),
        ia('j17_c', RODRIGO, 'Nueva oficina… mismos clientes.',
           'Daytime, a brand new office of a competing real estate agency with a sign that says "INMOBILIARIA NUEVA".',
           'puts a cardboard box with his things on a new desk, takes out his phone full of WhatsApp chats, smiles '
           'smugly at the camera', 'smug and relaxed', amb=', office ambience'),
    ],
    [
        clip('j17_a', hook(['LE DI LOS [LEADS]', 'Y SE FUE'], 'Dueña de inmobiliaria', 112)),
        clip('j17_b'),
        clip('j17_c'),
        photo('j17_s2', 'Le pasa a muchos dueños de inmobiliaria: el asesor se va, y los leads que pagaste se van con '
                        'él, en su celular.',
              'empty_desk', ['SE FUE CON', 'TUS [CLIENTES]'], ['@dueños', '@leads'], 'EN SU CELULAR', '@celular',
              stamp_size=86),
    ] + tail(J03_STACK)))

# ---------- J18 · La junta del lunes ----------
V.append(spec(
    'J18-la-junta-del-lunes',
    'La junta del lunes: «llamamos a todos, jefe» (Serie Sala de Juntas, video 18)',
    [
        ia('j18_a', FABIAN, 'A ver, asesores inmobiliarios: ¿a cuántos leads llamaron esta semana?',
           MEETING, 'stands at the head of the table with his arms crossed, looks over his glasses at the real estate '
                    'agents sitting around the table', 'firm and direct', shot='Medium shot, slow push-in.',
           amb=', office ambience'),
        ia('j18_b', RODRIGO, '¡A todos, jefe! Uno por uno. Yo personalmente.',
           MEETING, 'sits at the table, puts his hand on his chest, very proud, nods with total confidence',
           'confident and exaggerated', amb=', office ambience'),
        ia('j18_c', FABIAN, '¿Ah, sí? ¿Y por qué tengo cuarenta sin respuesta?',
           MEETING, 'slowly turns his laptop around toward the agents, the screen shows a list in red, raises one '
                    'eyebrow', 'calm and ironic', shot='Medium close-up, static camera.',
           amb=', then an awkward silence'),
    ],
    [
        clip('j18_a', hook(['¿LLAMARON A', 'TODOS LOS [LEADS]?'], 'Junta del lunes · inmobiliaria', 112)),
        clip('j18_b'),
        clip('j18_c'),
        photo('j18_s2', 'Todos dicen que llamaron. Pero si no ves los chats ni las llamadas de cada asesor, no sabes '
                        'cuántos leads se quedaron sin respuesta.',
              'meeting', ['«LLAMAMOS', 'A [TODOS]»'], ['@llamaron', '@asesor'], 'SIN RESPUESTA', '@respuesta',
              size=132, stamp_size=90),
    ] + tail(J03_PANEL)))

# ---------- J19 · «Esos leads no sirven, jefe» ----------
V.append(spec(
    'J19-esos-leads-no-sirven-jefe',
    'Esos leads no sirven, jefe: el dueño que apagó la pauta (Serie Sala de Juntas, video 19)',
    [
        ia('j19_a', KEVIN, 'Jefe, como asesor inmobiliario se lo digo: esos leads de Facebook no sirven. Pura gente que '
                           'no compra.', OFFICE,
           'slouches bored at his desk, spinning in his chair, talks to his boss off-screen with a yawn',
           'bored and lazy', amb=', office ambience'),
        ia('j19_b', RAMIRO, 'Ya ni modo. Si mis asesores dicen que no sirven… apaguen la pauta.',
           'Daytime, the owner\'s office of a real estate agency.',
           'sits at his desk talking on the phone, sighs, defeated, rubs his forehead',
           'tired and resigned', amb=', office ambience'),
        ia('j19_c', KEVIN, 'Don Carlos, ¿cómo va? Le tengo el departamento que me pidió… sí, por fuera, tranquilo.',
           CAR, 'sits in the driver seat holding the phone to his ear, super happy and energetic, then winks at the '
                'camera', 'cheerful and friendly, the last words whispered', amb=', quiet street ambience'),
    ],
    [
        clip('j19_a', hook(['«ESOS [LEADS]', 'NO SIRVEN»'], 'Inmobiliarias', 122)),
        clip('j19_b'),
        clip('j19_c'),
        photo('j19_s2', 'Si tu asesor dice que los leads no sirven, no tienes cómo comprobarlo. Y a lo mejor sí '
                        'sirven… pero para él.',
              'advisor_car', ['«NO', '[SIRVEN]»'], ['@asesor', '@comprobarlo'], 'PARA ÉL', '@él', size=140,
              stamp_size=120),
    ] + tail(J03_PANEL)))

# ---------- J20 · Confesión anónima ----------
V.append(spec(
    'J20-confesion-de-un-asesor',
    'Confesión de un asesor: la mitad lo vendo por fuera (Serie Sala de Juntas, video 20)',
    [
        ia('j20_a', ANON, 'Llevo tres años como asesor inmobiliario. La mitad de los leads que me llegan… los vendo '
                          'por fuera.', PODCAST,
           'sits in front of a podcast microphone, leaning toward it, speaking slowly',
           'low, deep and mysterious, voice slightly distorted like an anonymous interview',
           amb=', soft room tone'),
        ia('j20_b', HOST, '¿Y tu jefe nunca se ha dado cuenta?', PODCAST,
           'sits across the table in front of her own microphone, leans in with wide eyes, shocked and curious',
           'shocked, almost whispering', shot='Medium close-up, static camera.', amb=', soft room tone',
           pronoun='her'),
        ia('j20_c', ANON, 'Mi jefe cree que la publicidad no funciona.', PODCAST,
           'sits in front of a podcast microphone, the silhouette leans back and lets out a short laugh',
           'low, deep and mysterious, voice slightly distorted like an anonymous interview, a short laugh at the end',
           amb=', soft room tone'),
    ],
    [
        clip('j20_a', hook(['CONFESIÓN DE', 'UN [ASESOR]'], 'Inmobiliarias · confesión anónima', 124)),
        clip('j20_b'),
        clip('j20_c'),
        photo('j20_s2', 'Cuando los leads se trabajan en el WhatsApp personal de cada asesor, el dueño culpa a la '
                        'publicidad. Y el problema está adentro.',
              'owner_stressed', ['NO ES LA', '[PUBLICIDAD]'], ['@leads', '@publicidad'], 'ESTÁ ADENTRO',
              '@adentro', size=118, stamp_size=90),
    ] + tail(J03_PANEL, J03_STACK)))

# ---------- J21 · Pregunta directa al dueño ----------
V.append(spec(
    'J21-te-estan-robando-y-no-te-has-dado-cuenta',
    'Te están robando y no te has dado cuenta: pregunta directa al dueño (Serie Sala de Juntas, video 21)',
    [
        ia('j21_a', ARTURO, 'Si tienes una inmobiliaria y no sabes qué le dijo cada asesor inmobiliario a cada uno de '
                            'tus leads…',
           'Daytime, in front of a big apartment building under construction with cranes and scaffolding.',
           'stands in front of the construction site, looks straight at the camera, serious, points at the camera',
           'serious and direct', amb=', distant construction ambience'),
        ia('j21_b', ARTURO, '…te están robando. Y todavía no te has dado cuenta.',
           'Daytime, in front of a big apartment building under construction with cranes and scaffolding.',
           'takes two steps toward the camera, lowers his voice, very serious, raises one eyebrow',
           'low and grave', shot='Close-up, slow push-in.', amb=', distant construction ambience'),
        ia('j21_c', RODRIGO, 'Borrar chat… borrar chat… borrar chat.',
           'Daytime, his desk in a real estate agency office.',
           'sits hunched at his desk, sweating and nervous, quickly tapping on his phone to delete WhatsApp chats, '
           'glancing over his shoulder', 'nervous whisper, fast', amb=', office ambience'),
    ],
    [
        clip('j21_a', hook(['¿QUÉ LE DIJO', 'A TUS [LEADS]?'], 'Dueños de inmobiliaria', 116)),
        clip('j21_b'),
        clip('j21_c'),
        photo('j21_s2', 'Si todo pasa en el WhatsApp personal de tus asesores, no sabes qué le prometieron a cada '
                        'cliente, ni a quién le pasaron tus leads.',
              'construction', ['¿QUÉ LE', '[DIJERON]?'], ['@WhatsApp', '@prometieron'], 'NO LO SABES', '@leads'),
    ] + tail(J03_PANEL, J03_STACK)))


def main():
    for s in V:
        out = os.path.join(ROOT, 'videos', s['id'] + '.json')
        json.dump(s, open(out, 'w'), ensure_ascii=False, indent=1)
        print(out)


if __name__ == '__main__':
    main()
