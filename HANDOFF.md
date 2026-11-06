# Videos UGC de la modelo (6 nov 2026)

Listos y enviados a Sergio: U1 reportes, U2 CRA, U3 curiosos, U4 Lead Master en 5 pasos
(`videos/U*-celular.mp4`, specs en `engine/videos/U*.json`). Estilo de "Un mensaje. Una demanda" y siempre
con casa o desarrollo detrás al inicio (`engine/tools/ugc_bg.py`).
Originales: carpeta de Drive 1n0KyNDilNbQGyMV1GX1TdivMY9aWwAHr (se bajan con GOOGLEDRIVE_DOWNLOAD_FILE por Composio;
drive.usercontent.google.com está bloqueado). Para rehacerlos: `tools/ugc_prep.py`, Scribe para las palabras,
`tools/ugc_bg.py` y `tools/build.py` (ver README). Pendiente: que Sergio los revise; no están en la cola de Instagram.

UGC anteriores re-editados con el mismo formato (6 nov): 6 ganchos (H1 Jalisco, H2 Monterrey, H3 Mérida, H4 robando
leads, H5 claridad en 7 días, H6 monitorear asesores) x 2 cuerpos (C1 el CRM que nadie usa, C2 juntas de marketing y
ventas) = 12 videos `videos/UH*-C*-celular.mp4`. Originales en Drive 1q-rkfY2oC3OlxRROjeswqORj9aPJOQLE (sueltos = cuerpos,
carpeta Hooks = ganchos, carpeta editados = la edición vieja). Specs `engine/videos/UH*.json`, `UC*.json` ("part": true) y
`engine/videos/_ugc_combos.json`; se renderiza cada parte una vez y `tools/ugc_combo.py` arma las combinaciones.
Subidos en HD (los 16: U1-U4 + los 12) a Drive "ads laura/editados formato nuevo" (1bUHexL7mICjbiMi4wz5XS2Kl9rewvuit).
Para subir a Drive desde aquí: URL de subida firmada del workbench de Composio (tool_router/internal/presigned_url),
curl PUT local, y GOOGLEDRIVE_RESUMABLE_UPLOAD con el s3key (GOOGLEDRIVE_UPLOAD_FILE solo acepta 5 MB).

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

## Instagram
Las tareas programadas publican la cola `videos/ig_queue.json`. Sergio autorizó publicar Jalisco
(ya publicado). Para los siguientes, preguntarle si quiere que se publiquen solos al llegar cada aviso.
