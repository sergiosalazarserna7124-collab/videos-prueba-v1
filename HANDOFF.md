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
  CBO de US$80/día a nivel campaña (Meta reparte entre países); conjuntos Colombia, Chile y USA (gente con Facebook en
  español); 25-65 años, Advantage+ audiencia. 16 anuncios por país, 48 en total: 10 UGC (U1-U4, UH4-UH6 C1/C2) y los 6 de
  Sala de Juntas (J01-J06, Gemini). Los UH1-UH3 (ganchos Jalisco/Monterrey/Mérida) no están. Ids en `videos/meta_ads_9nov.json`.
  Nadie la ha prendido.
- Las campañas viejas de Laura (web + evento Schedule del píxel) gastaron ~US$2.400 sin citas atribuidas.
