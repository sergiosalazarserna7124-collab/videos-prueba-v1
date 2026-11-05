import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, SAFE} from '../theme';
import {Bg} from '../ui/Bg';
import {BigTitle} from '../ui/Text';
import {IconWhatsApp} from '../ui/Icons';

// Muchas burbujas de chat subiendo sobre una foto de oficina + pregunta grande.
export const FloatChats: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const texts: string[] = p.bubbles ?? ['Hola, ¿sigue disponible?', 'Te mando info', '¿Para cuándo?'];
  const n = 18;
  return (
    <AbsoluteFill>
      <Bg img={p.img} dur={dur} dim={0.35} drift="right" />
      {Array.from({length: n}).map((_, i) => {
        const start = (i * 7) % Math.max(20, dur - 20);
        const life = 70;
        const t = (f - start) / life;
        if (t < 0 || t > 1) return null;
        const x = 70 + ((i * 263) % 700);
        const y = interpolate(t, [0, 1], [1250, 330]);
        const op = interpolate(t, [0, 0.12, 0.8, 1], [0, 1, 1, 0]);
        const isIn = i % 3 !== 0;
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: x,
              top: y,
              opacity: op * 0.95,
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              background: isIn ? 'rgba(32,44,51,0.92)' : 'rgba(0,92,75,0.92)',
              color: '#E9EDEF',
              fontFamily: FONT.ui,
              fontSize: 26,
              fontWeight: 500,
              padding: '12px 18px',
              borderRadius: 20,
              boxShadow: '0 10px 30px rgba(0,0,0,0.4)',
              transform: `scale(${0.85 + (i % 4) * 0.06})`,
            }}
          >
            {i % 4 === 0 ? <IconWhatsApp size={30} /> : null}
            {texts[i % texts.length]}
          </div>
        );
      })}
      <div style={{position: 'absolute', left: SAFE.left, right: 1080 - SAFE.right, top: p.titleTop ?? 760}}>
        <BigTitle lines={p.lines ?? []} lineAts={p.lineAts} size={p.size ?? 140} accent={p.accent ?? C.cyan} />
      </div>
      {p.counter ? (
        <div
          style={{
            position: 'absolute',
            left: SAFE.left,
            top: SAFE.top + 10,
            fontFamily: FONT.body,
            fontWeight: 800,
            fontSize: 40,
            color: C.white,
            background: 'rgba(6,11,18,0.7)',
            padding: '12px 22px',
            borderRadius: 16,
            border: `1px solid ${C.line}`,
          }}
        >
          {p.counter}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
