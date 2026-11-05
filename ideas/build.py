#!/usr/bin/env python3
"""Arma el banco de ideas: une data/*.json y genera la página (banco-de-ideas.html) y el README.

Uso:  python3 ideas/build.py
"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')

# Videos ya hechos (para "Variación de ...").
BASE = {
    '01': 'Si yo tuviera una inmobiliaria en [ciudad]', '01-demanda': 'Un mensaje, una demanda',
    '02': 'Vendes desarrollos y tienes este problema', '03': 'Este CRM se mueve solo',
    '04': 'Separa curiosos de compradores', '05': 'Departamentos de más de 150 mil dólares',
    '06': 'El problema no es la cantidad de leads', '07': 'Tus asesores se pueden estar robando tus leads',
    '08': '9 mil dólares en anuncios', '09': '¿Todavía llenan el CRM a mano?',
    '10': 'Así le llegaría un lead a tus asesores', '11': '¿Qué anuncio te vendió el último depa?',
    '12': 'Dices con orgullo que pagas GoHighLevel', '13': 'Pagaste GoHighLevel y sigues en Excel',
    '14': 'Por qué GoHighLevel no basta', '15': 'Mi agente de IA vende solo (parodia)',
    '16': 'Te vendieron un chatbot de botones (parodia)', '17': 'Contrataste un coordinador',
    '18': 'Tu asesor dice que marcó 15', '19': 'Antes de despedir a un asesor',
    '20': 'Renunció y se llevó tus leads', '21': 'El lead de las 11 de la noche',
    '22': 'El día de tus asesores con Lead Master', '23': 'Lo que quema tu inmobiliaria cada mes',
    '24': '«Ahorita te mando opciones»', '25': 'Este video te apareció porque tienes una inmobiliaria',
    'A': 'Por qué tu CRM no funciona', 'B': 'Marketing y ventas siempre pelean',
    'C': 'Por qué te llegan puros curiosos', 'D': 'Los CRM murieron, llegaron los CRA',
    'E': 'Así recibirías tus reportes', 'F': 'Qué es Lead Master en un minuto',
    'G1': 'Si yo tuviera una inmobiliaria', 'G2': 'No puedo creer que todavía confíes',
    'G3': 'Si crees que se roban los leads', 'G4': 'Si yo vendiera desarrollos',
    'G5': 'No puedo creer que pagues un CRM que nadie llena', 'G6': 'Si la mitad de mis leads llegara de noche',
}


def load():
    meta = json.load(open(os.path.join(DATA, 'meta.json'), encoding='utf-8'))
    ideas = []
    for f in sorted(glob.glob(os.path.join(DATA, 'ideas-*.json'))):
        ideas += json.load(open(f, encoding='utf-8'))
    ideas.sort(key=lambda d: d['id'])
    angs = {k for p in meta['pilares'] for k in p['angulos']}
    ids = [d['id'] for d in ideas]
    assert len(ids) == len(set(ids)), 'ids repetidos'
    for d in ideas:
        assert d['angulo'] in angs and d['angulo'].startswith(d['pilar']), d['id']
        assert d['formato'] in meta['formatos'], d['id']
        assert not d.get('base') or d['base'] in BASE, (d['id'], d.get('base'))
    return meta, ideas


def build_html(meta, ideas):
    tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    sala = []
    for f in sorted(glob.glob(os.path.join(HERE, '..', 'guiones', 'sala-de-juntas', 's*.json'))):
        sala += json.load(open(f, encoding='utf-8'))
    payload = json.dumps({'meta': meta, 'ideas': ideas, 'base': BASE, 'sala': sala}, ensure_ascii=False)
    payload = payload.replace('</', '<\\/')
    out = tpl.replace('/*__DATA__*/', payload)
    path = os.path.join(HERE, 'banco-de-ideas.html')
    open(path, 'w', encoding='utf-8').write(out)
    return path


def build_md(meta, ideas):
    F = meta['formatos']
    L = ['# Mapa de contenido Lead Master', '',
         'Generado con `python3 ideas/build.py` a partir de `ideas/data/`. La versión interactiva (con botones para aprobar) es `banco-de-ideas.html`, publicada como Artifact.', '',
         f'**{len(ideas)} ideas · {len(meta["pilares"])} pilares · {sum(len(p["angulos"]) for p in meta["pilares"])} ángulos · {len(F)} formatos**', '']
    L += ['## Formatos', '', '| Formato | Cómo se hace | Costo aprox. |', '|---|---|---|']
    for k, f in F.items():
        L.append(f'| {f["nombre"]}{" (nuevo)" if f["nuevo"] else ""} | {f["como"]} | {f["costo"]} |')
    L += ['', '## Pilares y ángulos (los círculos y sus flechas)', '']
    fam = meta['familias']
    for p in meta['pilares']:
        L.append(f'- **{p["id"]} · {p["nombre"]}** ({fam[p["familia"]]["nombre"]}). {p["porque"]}')
        for k, v in p['angulos'].items():
            L.append(f'  - {k[-1]}) {v}')
    L += ['', '## Lo que pediste, uno por uno', '']
    for i, a in enumerate(meta['pedidos'], 1):
        L.append(f'{i}. **{a["titulo"]}.** {a["entendi"]}')
    L += ['', '## Banco de ideas', '']
    by = {}
    for d in ideas:
        by.setdefault(d['pilar'], []).append(d)
    for p in meta['pilares']:
        L += [f'### {p["id"]} · {p["nombre"]}', '']
        for d in by.get(p['id'], []):
            base = f' · variación de {d["base"]} ({BASE[d["base"]]})' if d.get('base') else ''
            L.append(f'- **{d["id"]} · {d["titulo"]}** _{F[d["formato"]]["nombre"]} · {p["angulos"][d["angulo"]]} · Comenta {d["cta"]}{base}_  ')
            L.append(f'  Gancho: {d["gancho"]}  ')
            L.append(f'  {d["idea"]}')
        L.append('')
    L += ['## Guiones de prueba', '']
    for g in meta['guiones']:
        L += [f'### {g["id"]} · {g["titulo"]} ({F[g["formato"]]["nombre"]}, {g["dur"]})', '', f'Elenco: {g["elenco"]}', '',
              '| # | Quién | Dice | Se ve |', '|---|---|---|---|']
        for i, pl in enumerate(g['planos'], 1):
            L.append(f'| {i} | {pl["quien"]} | {pl["dice"]} | {pl["ve"]} |')
        L += ['', f'**Cierre en el motor:** {g["cierre"]}', '']
    L += ['## Historias de asesores', '']
    for h in meta['historias']:
        L.append(f'- **{h["titulo"]}** ({F[h["formato"]]["nombre"]}). {h["historia"]} _{h["leccion"]}_')
    P = meta['produccion']
    L += ['', '## Cómo producir sin que salga caro', '', P['resumen'], '',
          '| Herramienta | Dónde | Precio | Qué hace bien | Para qué |', '|---|---|---|---|---|']
    for h in P['herramientas']:
        L.append(f'| {h["nombre"]} | {h["donde"]} | {h["precio"]} | {h["bien"]} | {h["uso"]} |')
    L += ['', '**Proceso**', '']
    for i, s in enumerate(P['pasos'], 1):
        L.append(f'{i}. **{s["t"]}.** {s["d"]}')
    L += ['', '**Costos**', '']
    for c in P['costos']:
        L.append(f'- {c["concepto"]}: {c["valor"]}')
    L += ['', '**Primera prueba**', '']
    for s in P['pruebas']:
        L.append(f'- {s["t"]}: {s["d"]}')
    L += ['', f'Qué vamos a revisar: {P["criterios"]}', '', f'**Lo que necesito:** {P["necesito"]}', '', f'_{P["avisos"]}_', '']
    V = meta['variaciones']
    L += ['## Variaciones', '', V['intro'], '']
    for a in V['ejes']:
        L.append(f'- **{a["eje"]}:** {", ".join(a["valores"])}')
    L += ['', V['cuenta'], '', f'**{V["ejemplo_titulo"]}**', '']
    for i, x in enumerate(V['ejemplo'], 1):
        L.append(f'{i}. {x}')
    path = os.path.join(HERE, 'README.md')
    open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    return path


if __name__ == '__main__':
    meta, ideas = load()
    print(build_html(meta, ideas))
    print(build_md(meta, ideas))
    print(len(ideas), 'ideas')
