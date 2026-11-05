import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, SAFE} from '../theme';
import {Bg} from '../ui/Bg';
import {pop} from '../ui/anim';

const colorOf = (c?: string) => (c && (C as any)[c]) || c || C.white;

// Tarjetas que entran una por una (consecuencias, pasos, puntos).
export const Stack: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const items: {t: string; k?: string; color?: string; at: number}[] = p.items ?? [];
  return (
    <AbsoluteFill>
      <Bg img={p.img} dur={dur} dim={0.6} blur={p.blur ?? 0} drift="up" />
      <div style={{position: 'absolute', left: SAFE.left, width: 840, top: p.top ?? 320, display: 'flex', flexDirection: 'column', gap: 26}}>
        {p.title ? (
          <div style={{fontFamily: FONT.title, fontSize: 84, color: C.white, lineHeight: 1, marginBottom: 8}}>{p.title}</div>
        ) : null}
        {items.map((it, i) => {
          const s = pop(f, it.at, 30, 15, 0.6);
          const col = colorOf(it.color);
          return (
            <div
              key={i}
              style={{
                display: 'flex',
                alignItems: 'stretch',
                background: 'rgba(13,18,25,0.9)',
                border: `1px solid ${C.line}`,
                borderRadius: 28,
                overflow: 'hidden',
                opacity: Math.min(1, s * 1.4),
                transform: `translateX(${interpolate(s, [0, 1], [-120, 0])}px)`,
                boxShadow: '0 20px 60px rgba(0,0,0,0.45)',
              }}
            >
              <div style={{width: 14, background: col}} />
              <div style={{padding: '28px 34px'}}>
                {it.k ? (
                  <div style={{fontFamily: FONT.body, fontWeight: 700, fontSize: 30, color: col, letterSpacing: 1, textTransform: 'uppercase'}}>
                    {it.k}
                  </div>
                ) : null}
                <div style={{fontFamily: FONT.body, fontWeight: 800, fontSize: 52, color: C.white, lineHeight: 1.12, marginTop: it.k ? 6 : 0}}>
                  {it.t}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
