import React, {useMemo} from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {C, FONT, SAFE} from '../theme';

export type Word = {w: string; s: number; e: number; hl?: boolean}; // tiempos absolutos en segundos

type Chunk = {words: Word[]; s: number; e: number};

const chunkWords = (words: Word[], maxWords = 3, maxChars = 18): Chunk[] => {
  const out: Chunk[] = [];
  let cur: Word[] = [];
  const flush = () => {
    if (cur.length) out.push({words: cur, s: cur[0].s, e: cur[cur.length - 1].e});
    cur = [];
  };
  words.forEach((w, i) => {
    const prev = cur[cur.length - 1];
    const gap = prev ? w.s - prev.e : 0;
    const chars = cur.reduce((a, x) => a + x.w.length + 1, 0) + w.w.length;
    if (cur.length && (cur.length >= maxWords || gap > 0.35 || chars > maxChars)) flush();
    cur.push(w);
    if (/[.!?…:;]$|[»"]$/.test(w.w)) flush();
    void i;
  });
  flush();
  // cada bloque dura hasta que empieza el siguiente (máx +0.6 s)
  for (let i = 0; i < out.length; i++) {
    const next = out[i + 1];
    out[i].e = next ? Math.min(next.s, out[i].e + 0.6) : out[i].e + 0.6;
  }
  return out;
};

// Subtítulos: 1-3 palabras, Poppins 800, contorno oscuro, palabras clave en cian.
export const Captions: React.FC<{words: Word[]; y?: number; hidden?: [number, number][]}> = ({
  words,
  y = 1210,
  hidden = [],
}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = f / fps;
  const chunks = useMemo(() => chunkWords(words), [words]);
  if (hidden.some(([a, b]) => t >= a && t < b)) return null;
  const c = chunks.find((x) => t >= x.s && t < x.e);
  if (!c) return null;
  const local = f - Math.round(c.s * fps);
  const s = spring({frame: local, fps, config: {damping: 13, mass: 0.5, stiffness: 220}});
  return (
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      <div
        style={{
          position: 'absolute',
          left: SAFE.left + 40,
          right: 1080 - SAFE.right + 40,
          top: y,
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
          gap: '0 18px',
          transform: `scale(${interpolate(s, [0, 1], [0.86, 1])})`,
          opacity: Math.min(1, s * 2),
        }}
      >
        {c.words.map((w, i) => {
          const active = t >= w.s - 0.02;
          const color = w.hl ? C.cyan : C.white;
          return (
            <span
              key={i}
              style={{
                fontFamily: FONT.body,
                fontWeight: 800,
                fontSize: 68,
                lineHeight: 1.12,
                color,
                opacity: active ? 1 : 0.55,
                WebkitTextStroke: '10px rgba(0,0,0,0.9)',
                paintOrder: 'stroke fill',
                textShadow: '0 6px 18px rgba(0,0,0,0.55)',
              }}
            >
              {w.w}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
