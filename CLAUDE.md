# Reglas de contenido Lead Master (pedidas por Sergio)

## Ganchos (siempre)
- La primera frase que se dice en el video (el personaje de IA o el narrador) tiene que mencionar
  **leads** y **asesores inmobiliarios**, y el video tiene que decir **inmobiliaria** en los primeros segundos
  (en la voz o en el gancho en pantalla). Ejemplo aprobado: «¡Asesores inmobiliarios! Les di doscientos leads
  esta semana. ¿Por qué carajo nadie me pasa el reporte?»
- Tiene que tener sentido: lo que contestan los demás personajes responde al gancho (si el dueño pregunta por
  los leads, las excusas son sobre los leads).
- El gancho en pantalla (2 líneas, palabra clave entre [ ]) nombra los leads o los asesores, y la píldora dice
  "Inmobiliarias" o similar.
- No usar "manual action". Nombres solo de demo (ver README).

## Videos con personas de IA (Serie Sala de Juntas)
- La IA solo hace el gancho (8 a 16 s, 1 o 2 planos de 8 s, un personaje hablando por plano de preferencia).
  El resto es el motor (`engine/`) con la voz del narrador.
- Planos: Gemini Omni 1.2 Flash por la Interactions API (`engine/tools/ia_clip.py`), key en `GEMINI_API_KEY`.
  Subtítulos de los planos: `engine/tools/clip_words.py`.
- Guiones: `guiones/sala-de-juntas/`. Página de aprobación: https://claude.ai/artifact/P3VF9fWuQsvozsJ2Apkz7c

## Videos UGC (la modelo hablando a cámara)
- Mismo estilo que "Un mensaje. Una demanda": títulos con palabra en color, subtítulos palabra por palabra, sellos,
  tarjetas del sistema. Mostrar lo que ella dice: el sistema arriba y ella abajo, o gráfico a pantalla completa.
- **Al inicio siempre una casa o un desarrollo detrás de ella** (`intro` en el spec + `engine/tools/ugc_bg.py`).
- Specs: `engine/videos/U*.json`. Ver README.
