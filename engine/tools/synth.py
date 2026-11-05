"""Genera efectos de sonido y una cama musical sin licencias (síntesis con numpy).

Uso: python3 tools/synth.py  -> public/sfx/*.wav y public/music/*.wav
"""
import os
import wave

import numpy as np

SR = 44100
ROOT = os.path.join(os.path.dirname(__file__), '..', 'public')
rng = np.random.default_rng(7)


def save(path, x, stereo=True):
    x = np.asarray(x, dtype=np.float64)
    peak = np.max(np.abs(x)) or 1.0
    x = x / peak * 0.89
    if stereo and x.ndim == 1:
        x = np.stack([x, x], axis=1)
    data = (x * 32767).astype(np.int16)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with wave.open(path, 'wb') as w:
        w.setnchannels(2 if data.ndim == 2 else 1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())


def t(sec):
    return np.arange(int(SR * sec)) / SR


def lowpass(x, cutoff):
    """Filtro de un polo; cutoff puede ser escalar o arreglo por muestra."""
    cutoff = np.broadcast_to(np.asarray(cutoff, dtype=np.float64), x.shape)
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.zeros_like(x)
    prev = 0.0
    for i in range(len(x)):
        prev = (1 - a[i]) * x[i] + a[i] * prev
        y[i] = prev
    return y


def lp_fast(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    from scipy.signal import lfilter  # noqa

    return lfilter([1 - a], [1, -a], x)


def highpass(x, cutoff):
    return x - lp(x, cutoff)


def lp(x, cutoff):
    try:
        return lp_fast(x, cutoff)
    except Exception:
        return lowpass(x, cutoff)


def env(n, a=0.005, r=0.2, sustain=0.0):
    e = np.ones(n)
    na = max(1, int(a * SR))
    e[:na] = np.linspace(0, 1, na)
    tail = np.arange(n - na) / SR
    e[na:] = sustain + (1 - sustain) * np.exp(-tail / max(1e-3, r))
    return e


def sfx():
    out = os.path.join(ROOT, 'sfx')
    # whoosh
    n = t(0.55)
    noise = rng.standard_normal(len(n))
    sweep = 300 + 5000 * np.sin(np.pi * n / n[-1]) ** 2
    w = lowpass(noise, sweep) * np.sin(np.pi * n / n[-1]) ** 1.5
    save(f'{out}/whoosh.wav', w)
    # pop
    n = t(0.12)
    f = 900 * np.exp(-n * 18) + 380
    ph = 2 * np.pi * np.cumsum(f) / SR
    save(f'{out}/pop.wav', np.sin(ph) * env(len(n), 0.001, 0.035))
    # ding (campana suave)
    n = t(1.4)
    base = 1318.5
    d = sum(a * np.sin(2 * np.pi * base * k * n) * np.exp(-n * dk) for a, k, dk in [(1, 1, 3.2), (0.45, 2.76, 5), (0.2, 5.4, 8)])
    save(f'{out}/ding.wav', d * env(len(n), 0.002, 2))
    # notificación (dos tonos)
    n1 = t(0.16)
    n2 = t(0.3)
    a1 = np.sin(2 * np.pi * 880 * n1) * env(len(n1), 0.002, 0.06)
    a2 = np.sin(2 * np.pi * 1318.5 * n2) * env(len(n2), 0.002, 0.1)
    save(f'{out}/notif.wav', np.concatenate([a1, a2]))
    # impacto grave
    n = t(1.0)
    f = 70 * np.exp(-n * 3) + 32
    ph = 2 * np.pi * np.cumsum(f) / SR
    boom = np.sin(ph) * env(len(n), 0.002, 0.35)
    crack = lowpass(rng.standard_normal(len(n)), 2500) * env(len(n), 0.001, 0.05)
    save(f'{out}/impact.wav', boom + 0.6 * crack)
    # sello (golpe seco)
    n = t(0.35)
    thud = np.sin(2 * np.pi * (110 * np.exp(-n * 10) + 50) * n) * env(len(n), 0.001, 0.08)
    click = lowpass(rng.standard_normal(len(n)), 3500) * env(len(n), 0.0005, 0.02)
    save(f'{out}/stamp.wav', thud + 0.8 * click)
    # riser
    n = t(1.4)
    f = 200 * (6 ** (n / n[-1]))
    ph = 2 * np.pi * np.cumsum(f) / SR
    r = (0.4 * np.sin(ph) + lowpass(rng.standard_normal(len(n)), 1000 + 6000 * n / n[-1])) * (n / n[-1]) ** 2
    save(f'{out}/riser.wav', r)
    # tecleo
    n = t(0.6)
    k = np.zeros(len(n))
    for s in np.arange(0.0, 0.55, 0.075):
        i = int(s * SR)
        m = int(0.012 * SR)
        k[i:i + m] += lowpass(rng.standard_normal(m), 4000) * np.exp(-np.arange(m) / (0.003 * SR))
    save(f'{out}/type.wav', k)
    # disco rayado
    n = t(0.7)
    f = 900 * np.sin(2 * np.pi * 7 * n) ** 2 + 120
    ph = 2 * np.pi * np.cumsum(f) / SR
    sc = (np.sin(ph) * 0.5 + lowpass(rng.standard_normal(len(n)), f * 3) * 0.8) * env(len(n), 0.003, 0.3)
    save(f'{out}/scratch.wav', sc)


def note(freq, dur, kind='saw', detune=0.0):
    n = t(dur)
    if kind == 'sine':
        return np.sin(2 * np.pi * freq * n)
    out = np.zeros(len(n))
    for d in (-detune, 0, detune):
        ph = (freq * (1 + d) * n) % 1.0
        out += 2 * ph - 1
    return out / 3


def music_pulse(seconds=80, bpm=96, name='pulse'):
    """Cama tensa y moderna: pad + bajo en corcheas + bombo suave + hats."""
    beat = 60 / bpm
    total = int(SR * seconds)
    L = np.zeros(total)
    R = np.zeros(total)
    midi = lambda m: 440 * 2 ** ((m - 69) / 12)
    prog = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]  # Am F C G
    bar = beat * 4
    i_bar = 0
    pos = 0.0
    while pos < seconds:
        chord = prog[(i_bar // 2) % 4]
        dur = bar
        n0 = int(pos * SR)
        seg = np.zeros(int(dur * SR))
        for m in chord:
            seg += note(midi(m), dur, 'saw', 0.004)
        seg = lp(seg, 900) * env(len(seg), 0.4, 3.0, 0.7) * 0.35
        end = min(total, n0 + len(seg))
        L[n0:end] += seg[: end - n0]
        R[n0:end] += seg[: end - n0]
        # bajo en corcheas
        root = midi(chord[0] - 24)
        for k in range(8):
            s = pos + k * beat / 2
            b = note(root, beat / 2 * 0.9, 'saw', 0.002)
            b = lp(b, 400) * env(len(b), 0.003, 0.12) * (0.55 if k % 2 == 0 else 0.4)
            a = int(s * SR)
            e = min(total, a + len(b))
            if a < total:
                L[a:e] += b[: e - a]
                R[a:e] += b[: e - a]
        # bombo en 1 y 3, hats a contratiempo
        for k in range(4):
            s = pos + k * beat
            a = int(s * SR)
            if k % 2 == 0:
                n = t(0.35)
                kick = np.sin(2 * np.pi * np.cumsum(55 + 90 * np.exp(-n * 30)) / SR) * env(len(n), 0.001, 0.12)
                e = min(total, a + len(kick))
                if a < total:
                    L[a:e] += 0.9 * kick[: e - a]
                    R[a:e] += 0.9 * kick[: e - a]
            h0 = int((s + beat / 2) * SR)
            n = t(0.05)
            hat = highpass(rng.standard_normal(len(n)), 7000) * env(len(n), 0.001, 0.015) * 0.18
            e = min(total, h0 + len(hat))
            if h0 < total:
                L[h0:e] += hat[: e - h0] * 0.8
                R[h0:e] += hat[: e - h0]
        # pluck arpegiado suave cada 2 compases
        if i_bar % 2 == 1:
            for k, m in enumerate(chord + [chord[0] + 12]):
                s = pos + k * beat / 2
                p = note(midi(m + 12), 0.4, 'sine') * env(int(0.4 * SR), 0.002, 0.12) * 0.12
                a = int(s * SR)
                e = min(total, a + len(p))
                if a < total:
                    L[a:e] += p[: e - a] * 0.6
                    R[a:e] += p[: e - a]
        pos += dur
        i_bar += 1
    fade = int(SR * 2)
    L[-fade:] *= np.linspace(1, 0, fade)
    R[-fade:] *= np.linspace(1, 0, fade)
    save(os.path.join(ROOT, 'music', f'{name}.wav'), np.stack([L, R], axis=1))


if __name__ == '__main__':
    sfx()
    music_pulse()
    print('ok')
