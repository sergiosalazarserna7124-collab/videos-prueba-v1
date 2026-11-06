"""Une un gancho y un cuerpo UGC ya renderizados (specs con "part": true) en un video final.

Los ganchos y los cuerpos se renderizan una sola vez (tools/build.py) y aquí se combinan: video sin
recomprimir, música corrida por encima de los dos (20 dB debajo de la voz) y entrega a -14 LUFS.

Uso: python3 tools/ugc_combo.py videos/_ugc_combos.json            # todas las que falten
     python3 tools/ugc_combo.py videos/_ugc_combos.json UH1-C1     # una
Archivo de combinaciones: {"music": {...}, "combos": [{"id", "hook": <id spec gancho>, "body": <id spec cuerpo>, "music"}]}
"""
import json
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BUILD = os.path.join(ROOT, 'build')
OUT = os.path.join(ROOT, '..', 'videos')


def dur(path):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                                capture_output=True, text=True).stdout)


def combo(c, vol):
    hook = os.path.join(BUILD, f"{c['hook']}.raw.mp4")
    body = os.path.join(BUILD, f"{c['body']}.raw.mp4")
    for p in (hook, body):
        if not os.path.exists(p):
            raise SystemExit(f'falta renderizar {p}')
    lst = os.path.join(BUILD, f"{c['id']}.concat.txt")
    open(lst, 'w').write(f"file '{hook}'\nfile '{body}'\n")
    joined = os.path.join(BUILD, f"{c['id']}.joined.mp4")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', joined], check=True)
    total = dur(joined)
    music = os.path.join(ROOT, 'public', c['music'])
    final = os.path.join(OUT, f"{c['id']}.mp4")
    fx = (f"[1:a]volume={vol},afade=t=out:st={max(0, total - 1.5):.2f}:d=1.5[m];"
          f"[0:a][m]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1:LRA=11[a]")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', joined, '-stream_loop', '-1', '-i', music,
                    '-filter_complex', fx, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-ar', '48000',
                    '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', final], check=True)
    cel = os.path.join(OUT, f"{c['id']}-celular.mp4")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', final, '-c:v', 'libx264', '-crf', '25', '-preset', 'slow',
                    '-maxrate', '3M', '-bufsize', '6M', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', cel], check=True)
    os.remove(joined)
    print(f"{c['id']}: {total:.1f} s -> {cel}")


if __name__ == '__main__':
    cfg = json.load(open(sys.argv[1]))
    only = set(sys.argv[2:])
    for c in cfg['combos']:
        if only and c['id'] not in only:
            continue
        if not only and os.path.exists(os.path.join(OUT, f"{c['id']}-celular.mp4")):
            continue
        combo(c, cfg.get('musicVol', 0.08))
