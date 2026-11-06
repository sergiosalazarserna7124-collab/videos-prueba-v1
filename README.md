# Reels Lead Master

Fábrica de reels verticales (1080x1920) para Lead Master: fotos realistas, motion graphics, voz de ElevenLabs y subtítulos sincronizados palabra por palabra.

- Guiones (25): documento "Guiones LeadMaster: 25 reels" en Claude (ver `guiones/README.md`).
- Videos terminados: `videos/`.
- Ideas de contenido (210, con mapa de pilares, guiones de prueba y plan de producción con IA): `ideas/` y la página para aprobarlas: https://claude.ai/artifact/P3VF9fWuQsvozsJ2Apkz7c
- Motor: `engine/` (Remotion + Python).

## Cómo se arma un video

1. **Guion → spec.** Cada video es un JSON en `engine/videos/` con sus escenas: tipo de escena, texto que dice la voz, foto, y en qué palabra entra cada elemento (`"@palabra"`, `"@palabra#2"`, `"@palabra+5"` en frames).
2. **Voz.** Cada escena se genera en ElevenLabs con alineación por carácter y queda en `engine/public/tts/<key>.mp3` + `<key>.json`. El mapa `TTS_MAP` de `tools/build.py` corrige la pronunciación (Lead Master → "Lid Máster").
3. **Render.**
   ```bash
   cd engine
   npm install
   python3 tools/synth.py                    # efectos y música (una vez)
   python3 tools/build.py videos/v01.json     # props + render + -14 LUFS
   python3 tools/build.py videos/v01.json --still 30,400   # cuadros de prueba
   python3 tools/build.py videos/v01.json --safe --still 30 # con guías de zona segura
   ```

## Reglas que sigue el motor

- **Zona segura IG y TikTok:** nada importante arriba de 250 px ni debajo de 1420 px; la columna derecha (x > 930) libre en la mitad de abajo. Subtítulos en y≈1210.
- Gancho en pantalla desde el primer cuadro. Algo nuevo cada 3–6 s. Sin emojis, pocos zooms.
- Música 20 dB debajo de la voz, efectos bajos, entrega a -14 LUFS.
- Solo nombres de demo (leads: Adriana Solís, Diana Trejo, Lucía Hernández; asesores: Paola Gutiérrez, Valeria Ríos, Diego Herrera, Andrés Molina). Ningún cliente real.

## Videos UGC (la modelo hablando a cámara)

Su voz manda: el video de ella corre de principio a fin con su audio y el motor pone todo encima.
Spec con `"ugc": {"src", "words", "face": [x, y nariz, y coronilla], "zoom", "splitZoom"}` y escenas con:

- `"at": "@palabra"`: la escena empieza cuando ella dice esa palabra (se busca después de la escena anterior).
- `"layout"`: `face` (ella completa, con `over` encima: título, píldoras, sello, paso, CTA), `split` (el sistema
  arriba y ella abajo) o `full` (gráfico a pantalla completa, ella se sigue oyendo).

```bash
cd engine
python3 tools/ugc_prep.py <original.mov> u1      # public/ugc/u1.mp4 (1440x2560, audio limpio a -16 LUFS)
# subtítulos: ElevenLabs Scribe (Composio) -> public/ugc/u1.words.json
python3 tools/build.py videos/U1-asi-reciben-su-reporte-tus-asesores.json
```
Los .mp4 de `public/ugc/` no se suben (pesan); los originales están en Drive (carpeta de la modelo UGC).

## Escenas disponibles

`news` (titular), `chat` (WhatsApp / SMS en un celular), `photo` (foto + frases), `case` (expediente con sello), `floatchats` (burbujas subiendo + pregunta), `stack` (tarjetas), `panel` (panel de Lead Master), `hub` (Lead Master conectado al WhatsApp y llamadas de cada asesor), `over` (encima de la persona en los UGC), `cta` (cierre "Comenta PALABRA").
