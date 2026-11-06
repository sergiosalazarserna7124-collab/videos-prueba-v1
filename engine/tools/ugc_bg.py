"""Gancho de los UGC con una casa o desarrollo detrás: recorta a la persona (Robust Video Matting)
en los primeros cuadros y pone la foto de fondo. El resto del video queda igual.

En el spec: "ugc": {..., "intro": {"img": "queretaro_house", "frames": 149, "fade": [980, 1180]}}
"fade": de qué y a qué y (en coordenadas 1080x1920 del video) baja a oscuro: tapa donde el recorte
corta el cuerpo (portátil, sofá) y deja aire para los subtítulos.
Uso: python3 tools/ugc_bg.py videos/U1-....json [--test 40]   (--test: solo un cuadro de prueba)

- Lee public/ugc/<n>.orig.mp4 (la primera vez renombra public/ugc/<n>.mp4) y escribe public/ugc/<n>.mp4,
  así los props no cambian y en el render solo hay que rehacer el primer tramo.
- Modelo: rvm_mobilenetv3_fp32.onnx (github.com/PeterL1n/RobustVideoMatting, release v1.0.0) en build/models/.
"""
import json
import os
import subprocess
import sys

import numpy as np
import onnxruntime as ort

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PUB = os.path.join(ROOT, 'public')
MODEL = os.path.join(ROOT, 'build', 'models', 'rvm_mobilenetv3_fp32.onnx')
MODEL_URL = 'https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3_fp32.onnx'
W, H = 1440, 2560
PAN = 0.06  # la foto entra un poco más grande y se desliza despacio


def background(img, n):
    """Foto a pantalla completa, un poco desenfocada (como fondo de cámara), más ancha para deslizarla."""
    bw, bh = int(W * (1 + PAN)) // 2 * 2, int(H * (1 + PAN)) // 2 * 2
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(PUB, 'img', f'{img}.jpg'),
                          '-vf', f'scale={bw}:{bh}:force_original_aspect_ratio=increase,crop={bw}:{bh},gblur=sigma=4',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    big = np.frombuffer(raw, np.uint8).reshape(bh, bw, 3).astype(np.float32) / 255
    dy = (bh - H) // 2

    def at(i):
        dx = int((bw - W) * (i / max(1, n - 1)))
        return big[dy:dy + H, dx:dx + W]
    return at


def main(spec_path, test=None):
    spec = json.load(open(spec_path))
    u = spec['ugc']
    intro = u['intro']
    src = os.path.join(PUB, u['src'])
    orig = src.replace('.mp4', '.orig.mp4')
    if not os.path.exists(orig):
        os.rename(src, orig)
    if not os.path.exists(MODEL):
        os.makedirs(os.path.dirname(MODEL), exist_ok=True)
        subprocess.run(['curl', '-sSL', '-o', MODEL, MODEL_URL], check=True)
    sess = ort.InferenceSession(MODEL, providers=['CPUExecutionProvider'])
    n = intro['frames']
    bg = background(intro['img'], n)
    ya, yb = [v * H / 1920 for v in intro.get('fade', [1500, 1700])]
    t = np.clip((np.arange(H, dtype=np.float32) - ya) / max(1, yb - ya), 0, 1)
    shade = (0.94 * t * t * (3 - 2 * t))[:, None, None]
    dark = np.array([6, 11, 18], np.float32) / 255
    rec = [np.zeros((1, 1, 1, 1), np.float32)] * 4
    ratio = np.array([intro.get('ratio', 0.3)], np.float32)
    frame_bytes = W * H * 3
    reader = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', orig, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                              stdout=subprocess.PIPE)
    if test is None:
        writer = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                                   '-r', '30', '-i', '-', '-i', orig, '-map', '0:v', '-map', '1:a',
                                   '-c:v', 'libx264', '-preset', 'fast', '-crf', '17', '-pix_fmt', 'yuv420p',
                                   '-c:a', 'copy', '-movflags', '+faststart', src], stdin=subprocess.PIPE)
    i = 0
    while True:
        buf = reader.stdout.read(frame_bytes)
        if len(buf) < frame_bytes:
            break
        if i < n:
            img = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32) / 255
            x = img.transpose(2, 0, 1)[None]
            fgr, pha, *rec = sess.run(None, {'src': x, 'r1i': rec[0], 'r2i': rec[1], 'r3i': rec[2], 'r4i': rec[3],
                                             'downsample_ratio': ratio})
            a = pha[0].transpose(1, 2, 0)
            f = fgr[0].transpose(1, 2, 0)
            out = f * a + bg(i) * (1 - a)
            out = np.clip(out * (1 - shade) + dark * shade, 0, 1)
            buf = (out * 255 + 0.5).astype(np.uint8).tobytes()
            if test is not None and i == test:
                path = os.path.join(ROOT, 'build', f"{spec['id']}-intro-{i}.png")
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                                '-i', '-', path], input=buf, check=True)
                print(path)
                reader.kill()
                return
            if i % 30 == 0:
                print(f'  intro {i}/{n}', flush=True)
        if test is None:
            writer.stdin.write(buf)
        i += 1
    reader.wait()
    writer.stdin.close()
    writer.wait()
    print(src, f'({i} cuadros, {n} con fondo)')


if __name__ == '__main__':
    t = int(sys.argv[sys.argv.index('--test') + 1]) if '--test' in sys.argv else None
    main(sys.argv[1], t)
