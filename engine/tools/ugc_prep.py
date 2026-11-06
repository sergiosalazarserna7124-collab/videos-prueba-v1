"""Prepara un video UGC (la modelo hablando a cámara) para el motor.

- Video: 1440x2560 H.264 a 30 fps (deja margen para acercamientos sin perder nitidez).
- Audio: quita graves, baja el ruido de fondo y lo deja en -16 LUFS (la entrega final va a -14).

Uso: python3 tools/ugc_prep.py <video original .mov/.mp4> <nombre>   -> public/ugc/<nombre>.mp4

Los subtítulos (public/ugc/<nombre>.words.json, lista de {"w","s","e"} en segundos) salen de
ElevenLabs Scribe (ELEVENLABS_TRANSCRIBE_AUDIO por Composio, modelo scribe_v2, idioma es).
"""
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'public', 'ugc')

AF = 'highpass=f=75,afftdn=nf=-45,loudnorm=I=-16:TP=-1.5:LRA=9'


def prep(src, name):
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, f'{name}.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src,
                    '-vf', 'scale=1440:2560:flags=lanczos,fps=30', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17',
                    '-pix_fmt', 'yuv420p', '-af', AF, '-ar', '48000', '-c:a', 'aac', '-b:a', '256k',
                    '-movflags', '+faststart', dst], check=True)
    print(dst)


if __name__ == '__main__':
    prep(sys.argv[1], sys.argv[2])
