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

## Bloque obligatorio: TODO EN AUTOMÁTICO (en todos los videos)
- Todo video tiene que DECIR y MOSTRAR que Lead Master trabaja solo: se conecta al WhatsApp y a las llamadas
  de los asesores y vendedores, y en automático dice qué pasó con cada lead y manda el reporte, sin que nadie llene nada.
- Usa la escena fija `engine/videos/_auto_std.json` (voz `auto_std`, ya generada): flujo «WhatsApp de tus asesores
  → Sus llamadas → Lead Master (IA) en automático» con título «TODO EN AUTOMÁTICO» y el reporte lead por lead
  llegando solo por WhatsApp. Va justo después de plantear el problema. Si el guion ya explica pasos, la escena
  puede cambiar el título (p. ej. «2 · TODO EN AUTOMÁTICO») pero tiene que estar.

## Videos con personas de IA (Serie Sala de Juntas)
- La IA solo hace el gancho (8 a 16 s, 1 o 2 planos de 8 s, un personaje hablando por plano de preferencia).
  El resto es el motor (`engine/`) con la voz del narrador.
- Planos: Gemini Omni 1.2 Flash por la Interactions API (`engine/tools/ia_clip.py`), key en `GEMINI_API_KEY`.
  Subtítulos de los planos: `engine/tools/clip_words.py`.
- Guiones: `guiones/sala-de-juntas/`. Página de aprobación: https://claude.ai/artifact/P3VF9fWuQsvozsJ2Apkz7c
