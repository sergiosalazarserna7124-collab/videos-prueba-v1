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
- `videos/ig_queue.json` queda como historial (status `programado_metricool`); ya no se usa para publicar.
- Composio ya no publica en Instagram; los avisos programados de Claude para Instagram están apagados.
- Nunca subir a Instagram los videos que Sergio editó al inicio (status `no_instagram`): ya están en @sergio_salazaar.
- Ya publicados en @leaad_master por Composio: El mayor error, Un mensaje. Una demanda., Le pregunto a mi CRM,
  Idea 1 Jalisco, G3, F e Idea 4.
- Videos UGC con modelo (16, de la rama `claude/modest-euler-0k49k2`): del 13 al 15 nov, también en GoHighLevel.
