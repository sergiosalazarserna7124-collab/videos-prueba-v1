# Reels Lead Master

Fábrica de reels verticales (1080x1920) para Lead Master: fotos realistas, motion graphics, voz de ElevenLabs y subtítulos sincronizados palabra por palabra.

- Guiones (25): documento "Guiones LeadMaster: 25 reels" en Claude (ver `guiones/README.md`).
- Videos terminados: `videos/`.
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

## Escenas disponibles

`news` (titular), `chat` (WhatsApp / SMS en un celular), `photo` (foto + frases), `case` (expediente con sello), `floatchats` (burbujas subiendo + pregunta), `stack` (tarjetas), `panel` (panel de Lead Master), `cta` (cierre "Comenta PALABRA").
