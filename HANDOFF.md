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
Instagram NO está en Metricool (Metricool solo tiene TikTok, Facebook y YouTube). Los reels de @leaad_master los
publica Claude con Composio cuando llega cada aviso programado, siguiendo la cola `videos/ig_queue.json`.
- Desde el 6 nov los avisos llegan a la sesión «Videos no subidos a Instagram» (rama `claude/dazzling-lovelace-todckv`).
  Los avisos viejos de la sesión de videos quedaron apagados, para no publicar dos veces.
- Sergio ya autorizó que salgan solos a su hora, sin pedirle permiso cada vez.
- Solo van los videos nuevos de IA. Los que Sergio editó al inicio (status `no_instagram`) ya están en Instagram: no se suben.
- Siempre como colaboración con @sergio_salazaar (no etiqueta).
- Para meter un video nuevo a Instagram: agregarlo a `videos/ig_queue.json` como `pendiente` con su hora (`when`, Bogotá).
- Videos UGC con modelo (16: U1-U4 y UH1..UH6 x C1/C2, de la rama `claude/modest-euler-0k49k2`): programados el 6 nov
  en Metricool (TikTok, Facebook, YouTube) del 13 al 15 nov, y en la cola de Instagram a la misma hora. Metricool tomó
  cada video del link público de GitHub (raw, fijado al commit 717d253) y la cola usa la copia de static.metricool.com.
