# Ahora (20 nov 2026): Serie Sala de Juntas J13 a J21 (9 videos nuevos)

- Guiones: `guiones/sala-de-juntas/J13-J21.md`. Specs: `engine/videos/J13..J21*.json`, salen de `engine/tools/specs_sala2.py`
  (editar ahí y correrlo). 3 planos de IA por video; 1 línea nueva de narrador (`jXX_s2`, ya generadas para los 9 con
  ElevenLabs por Composio, ruta with-timestamps); se reusan `auto_std`, `j03_s3` y/o `j03_s4` y el cierre `j03_s5`.
- Elenco nuevo: Karla (asesora, J14), Brayan (asesor tiktoker, J16), Doña Mónica (dueña, J17), Kevin (asesor, J19),
  Señora Lupita (clienta, J15), Daniela (podcast) y el asesor anónimo (J20), Don Arturo (desarrollador, J21).
- **HECHOS** (copias para celular en `videos/`): J13 49,5 s · J14 50,4 s · J15 56,7 s · J16 50,3 s · J17 44,4 s · J18 45,7 s.
  18 planos, ninguno regenerado. j13_b dice «Cero, cero» (subtítulo ajustado). No se pudo verificar con transcripción
  qué dicen j16_a y j17_c (Gemini texto también dio 402); el audio tiene voz en el tramo esperado.
- **FALTAN J19, J20 y J21**: el prepago de Gemini se agotó (402 «prepayment credits are depleted») al lanzar la tanda 3.
  Los 9 planos (j19_a..j21_c) fallaron sin cobro. Cuando Sergio recargue en AI Studio: desde `engine/`,
  `python3 tools/ia_clip.py spec videos/J19-....json` (igual J20, J21), revisar cuadros, `tools/words_energia.py` por plano,
  y render con build.py + copia para celular (ver `tools/render_all.sh`).
- Gasto Gemini en esta tanda: 18 × 8 s × US$0,07 ≈ US$10,1 (faltan ≈ US$5,0).
- Meta Ads (20 nov): Sergio quería los 12 anuncios nuevos (J07–J11, J13–J18 y HF1 de Higgsfield) SOLO en México, dentro de
  la campaña que ya corría: «LeadMaster | MX por estados | Landing · Llamada agendada | 16 nov» (conjunto 120253260374290351).
  Ahí están creados EN PAUSA, con el mismo formato que los J de esa campaña (landing leadmaster.com.co, «Más información», utm).
  Falta que Sergio confirme para prenderlos. ERROR de esta sesión: primero se metieron en la campaña de formulario CO-CL-USA y se
  lanzó; se volvió a pausar (gastó US$4,42, 1 lead). Ahí quedaron los mismos 12 anuncios en PAUSED y la campaña en pausa.
  HF1 es 480p y no tiene el bloque TODO EN AUTOMÁTICO ni cierre (test). Ids en `videos/meta_ads_20nov.json` (clave «mexico»).
- Ojo, reglas automáticas creadas el 18 nov por otra sesión en la cuenta: «Fin de semana · JUEVES bajar presupuesto 80% (auto)»
  y «Fin de semana · DOMINGO 6am restaurar presupuesto x5 (auto)», para TODAS las campañas activas o pausadas. Por eso el 19 nov
  esta campaña quedó en US$16/día (antes US$80). La única campaña activa es «MX por estados | Landing · Llamada agendada | 16 nov».
- Drive: J13–J18 subidos (20 nov) a la carpeta privada «Lead Master · Sala de Juntas J13-J21»
  (https://drive.google.com/drive/folders/15dEzhmpk_Y1kIMoQtTetZmutOdmgGRu3) con GOOGLEDRIVE_UPLOAD_FROM_URL de Composio
  (cuenta de Sergio) desde el raw de GitHub de esta rama; el conector de Drive de la sesión no acepta más de ~3 MB por llamada.

# Ahora (19 nov 2026): 5 variaciones de J03 «se roban los leads» (J07 a J11)

Sergio pidió 5 variaciones del J03 (el que mejor funciona) con 2 o 3 muñecos peleando y más narrativa.
- Guiones: `guiones/sala-de-juntas/J07-J11-se-roban-los-leads.md`. Specs: `engine/videos/J07..J11*.json`, salen de
  `engine/tools/specs_roban.py` (editar ahí y correrlo). 3 planos de IA por video (un personaje por plano).
- Voces del narrador ya generadas (ElevenLabs por Composio, ruta with-timestamps): `engine/public/tts/j07_s2..j11_s3`.
  Reusan `auto_std`, `j03_s4` (stack) y `j03_s5` (cierre «Comenta LEADS»).
- FALTA: los 15 planos de muñecos (`python3 tools/ia_clip.py spec videos/J07-....json`, luego `tools/clip_words.py`
  por plano) y el render. Necesita la key de Gemini: en el entorno leadmaster-tracker hay que agregar un secreto de red
  para generativelanguage.googleapis.com con encabezado `x-goog-api-key` (el formulario automático no acepta ese encabezado).
  Si la key llega por secreto de red, poner `GEMINI_API_KEY=proxy` (valor de relleno, el proxy lo cambia).
- Alternativa que Sergio está viendo: Higgsfield por MCP (prueba 3 días gratis; luego US$79 el 1er mes y US$129/mes).
  Los conectores solo se cargan en una sesión nueva.
- **HECHO (19 nov, 5:30 pm):** los 15 planos generados y los 5 videos renderizados; copias para celular en `videos/`:
  J07 58,2 s · J08 52,1 s · J09 51,4 s · J10 60,0 s · J11 58,3 s. j09_a se regeneró una vez (la 1ª versión salió realista);
  j10_c y j11_c se relanzaron porque fallaron por RESOURCE_EXHAUSTED (15 a la vez es demasiado; lanzar de a 10 o menos).
  j08_c tiene «VENTAS: 0» en el tablero porque así lo pide el prompt. Falta que Sergio los revise.
- Subtítulos de los planos: la transcripción de Gemini (`clip_words.py`) dio tiempos amontonados; se rehicieron con
  `tools/words_energia.py <clip> "<dice>"` (texto del guion alineado por la energía del audio).
- Arreglado `tools/ia_clip.py`: google-genai 3.x usa la API v1 por defecto y ahí Omni da 404; ahora fuerza `v1beta`.
- Después de cada plano, ajustar `range` de los clips con los tiempos de `*.words.json` para cortar tiempo muerto.

# Siguiente paso: video demo J01 (Serie Sala de Juntas)

Estado al 5 nov 2026, 4:15 pm Bogotá.

## Qué falta
Solo generar los 2 planos de personas con IA (8 s cada uno) y renderizar.
Todo lo demás de `engine/videos/J01-por-que-carajo-no-pasan-los-reportes.json` ya está:
voces del narrador (`engine/public/tts/j01_s2..s4`), escenas del motor, reporte y cierre "Comenta SISTEMA".
Sergio pidió hacer SOLO este video y revisarlo antes de hacer los otros 9 aprobados
(P08-01, P08-02, P08-04, P08-05, P08-11, P08-13, P13-01, P13-03, P13-08, P13-12 en la página de ideas).

## Cómo generar los planos
- Modelo: `gemini-omni-1.2-flash` (US$0.07/s, 720p, audio y diálogo con labios). Solo funciona por la
  **Interactions API** nativa de Gemini (`https://generativelanguage.googleapis.com/v1beta/interactions`),
  con la key en `x-goog-api-key` o `?key=`. La key está en la variable de entorno `GEMINI_API_KEY`
  del entorno `videos-prueba-v1`. (El secreto de red del mismo host va en `Authorization: Bearer`
  y solo sirve para la ruta compatible con OpenAI: texto/imágenes, no para Omni ni Veo.)
- La cuenta ya tiene saldo prepago activo.
- Prompts exactos: campo `ia` del spec J01 (`j01_a`: Don Ramiro grita; `j01_b`: Diego y Paola se excusan).
  Vertical 9:16 (720x1280), 8 s, con audio.
- Guardar como `engine/public/clips/j01_a.mp4` y `j01_b.mp4`.
- Subtítulos de los planos: `engine/public/clips/j01_a.words.json` y `j01_b.words.json`, lista de
  `{"w","s","e"}` (segundos dentro del clip). Sacar tiempos reales con ElevenLabs Scribe vía Composio
  (`ELEVENLABS_TRANSCRIBE_AUDIO`, cuenta de Sergio) o alinear el texto conocido con
  `ELEVENLABS_ALIGN_AUDIO_AND_TRANSCRIPT`. Archivos de Composio se bajan con `curl -L` desde
  `backend.composio.dev` (permitido en el entorno).
- `engine/tools/ia_clip.py` tiene un intento con la ruta compatible con OpenAI que NO sirve para Omni:
  actualizarlo a la Interactions API.

## Ojo con la autenticación
El entorno tiene DOS cosas para Gemini: la variable `GEMINI_API_KEY` (ya guardada, 5 nov) y un secreto de red
que el proxy mete como `Authorization: Bearer` en todo lo que va a generativelanguage.googleapis.com.
Si la llamada nativa con `x-goog-api-key: $GEMINI_API_KEY` devuelve 401 por ese Bearer, prueba `?key=$GEMINI_API_KEY`;
si sigue fallando, pídele a Sergio que borre el secreto de red "Gemini API key (Google AI Studio)" en el ⚙ del entorno
(la variable basta para todo). Nunca imprimas la key.

## Render
```bash
cd engine
python3 tools/build.py videos/J01-por-que-carajo-no-pasan-los-reportes.json --still 20,300,560,800
python3 tools/build.py videos/J01-por-que-carajo-no-pasan-los-reportes.json
# copia para celular como las demás (videos/*-celular.mp4) y mandarla a Sergio para revisar
```
La escena `clip` (engine/src/scenes/Clip.tsx) pone el gancho "¿Y LOS REPORTES?" encima del primer plano;
la música entra después de los clips. Probado con un clip de relleno: funciona.

## Publicaciones (desde el 7 nov: GoHighLevel)
El 7 nov Metricool empezó a fallar con «You have reached your Metricool account limit» (desde las 8 am ya no publicó nada).
La sesión de videos (rama `claude/keen-cerf-e6nqma`) programó todo el calendario del 7 al 15 nov en el **Social Planner de
GoHighLevel**: Instagram @leaad_master y @sergio_salazaar por separado, Facebook, TikTok y YouTube (69 publicaciones; plan e
ids en `publicar/plan_ghl.json` y `publicar/ghl_programado.json` de esa rama). Esa es ahora la fuente de verdad.
- Metricool está apagado: el 8 nov se pasaron a borrador los 99 posts pendientes del 7 al 15 nov (nada borrado; del 16 al
  30 no había nada). Así no se publica nada doble con GoHighLevel aunque Metricool vuelva a tener cupo. Queda uno sin pasar
  porque Sergio negó ese cambio: 11 nov 14:00, «Este video lo editó una IA» (Facebook, TikTok, YouTube; id 417939290).
  Los 14 posts del 7 y 8 nov que fallaron por el límite quedaron en ERROR, sin tocar. No programar nada nuevo en Metricool.
- Instagram en GoHighLevel: una sola publicación por video, desde @sergio_salazaar con @leaad_master de colaborador
  (`instagramPostDetails = {"collaborators": {"<accountId de @sergio_salazaar>": ["leaad_master"]}}`). Nunca programar
  el mismo video en los dos Instagram por separado: Meta lo toma como contenido duplicado. El 7 y 8 nov salieron 13 videos
  dobles así; el 8 nov en la noche se corrigieron los 46 pendientes (9 al 15 nov). Lista de los 13 dobles con links y ids:
  `videos/ig_dobles_publicados.json`. @leaad_master tiene que aceptar la invitación de colaboración en la app.
- `videos/ig_queue.json` queda como historial (status `programado_metricool`); ya no se usa para publicar.
- Composio ya no publica en Instagram; los avisos programados de Claude para Instagram están apagados.
- Nunca subir a Instagram los videos que Sergio editó al inicio (status `no_instagram`): ya están en @sergio_salazaar.
- Ya publicados en @leaad_master por Composio: El mayor error, Un mensaje. Una demanda., Le pregunto a mi CRM,
  Idea 1 Jalisco, G3, F e Idea 4.
- Videos UGC con modelo (16, de la rama `claude/modest-euler-0k49k2`): el 9 nov Sergio pidió sacarlos ese mismo día.
  Se movieron en GoHighLevel a 9 nov de 11:00 a 22:15 (cada 45 min: U1-U4 primero, luego los 12 UH). Los 6 que estaban
  el 9 nov desde las 12:00 pasaron a los huecos del 13 al 15 (Mérida 13 nov 12:00, Si no llama 13 nov 16:00, Idea 14
  14 nov 12:00, J02 14 nov 19:15, B 15 nov 12:00, E 15 nov 18:00). Antes/después con ids: `videos/ghl_movidos_9nov.json`.
  `plan_ghl.json` y `ghl_programado.json` de la otra rama tienen las horas viejas de esos 22.
  Reporte con todo el calendario: https://claude.ai/artifact/AJ81oJxGM6Z2eoGHHUSp2W

## Meta Ads (9 nov)
Token de Meta (usuario del sistema "Conversions API System User") guardado como secreto de red de graph.facebook.com en el entorno
lead-master-video: se usa con `Authorization: Bearer proxy-injected`. Ojo con curl y las llaves `{}` en los fields: usar `curl -g`.
- Campaña EN PAUSA "LeadMaster | UGC formato nuevo | Formulario | CO-CL-USA | 9 nov" (formulario 4563633850580091, optimiza leads):
  CBO de US$80/día a nivel campaña y UN SOLO conjunto (Sergio lo pidió así) con Colombia, Chile y USA; gente con Facebook en
  español, 25-65 años, Advantage+ audiencia. 16 anuncios: 10 UGC (U1-U4, UH4-UH6 C1/C2) y los 6 de Sala de Juntas (J01-J06,
  Gemini). Los UH1-UH3 (ganchos Jalisco/Monterrey/Mérida) no están. Los 3 conjuntos por país que se armaron antes se borraron
  (nunca gastaron). Ids en `videos/meta_ads_9nov.json`.
  Se prendió el 9 nov y se volvió a pausar a los minutos (gastó US$0,34, sin leads): Sergio quiere un formulario nuevo antes.
  Formulario nuevo APROBADO por Sergio (9 nov), falta crearlo: Meta exige link de política de privacidad («Falta contenido legal»).
  es_LA. Preguntas: asesores (Solo yo / Entre 2 y 5 / Entre 6 y 10 / Más de 10), leads al mes (Menos de 50 / Entre 50 y 200 /
  Entre 200 y 500 / Más de 500), nombre o Instagram de la inmobiliaria (libre), nombre, teléfono, correo; botón final WhatsApp.
  Se crea con el token de página (GET /348238158383886?fields=access_token, mandarlo como access_token, nunca imprimirlo).
  Después: pasar los 16 anuncios al formulario nuevo y revisar que llegue a GoHighLevel (Integraciones → Facebook).
- WhatsApp de GoHighLevel (proveedor custom «Whatsapp», id 67fb7921ff76fb73c232c866) DESCONECTADO el 9 nov: todo envío falla con
  «Error 101: No connected instances found!». Los 2 leads del 9 nov (contactos Rd2QuF0AghiTONZ4bmfm y NbHWk5exNL8Q6GEJdYnl)
  no han recibido nada; reenviarles el primer mensaje de Lead Master (está en las instrucciones del bot) cuando se reconecte.
  Bot «Lead Master · Calificación inmobiliarias» (PcY06YwRZVuqw0Wvyvoe) en modo off: falta que Sergio diga si va para toda la
  subcuenta o solo para esos contactos. El workflow que dispara al llegar el lead todavía manda el texto viejo de AutoKPI.
  El formulario actual (4563633850580091) sí mandó leads a GoHighLevel en junio (6 contactos con fuente «Facebook», 2 jun).
- Las campañas viejas de Laura (web + evento Schedule del píxel) gastaron ~US$2.400 sin citas atribuidas.
