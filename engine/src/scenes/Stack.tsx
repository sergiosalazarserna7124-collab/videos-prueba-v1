import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {Bg, BrandBg} from '../ui/Bg';
import {pop} from '../ui/anim';

export const colorOf = (c?: string) => (c && (C as any)[c]) || c || C.white;

// Tarjetas que entran una por una (consecuencias, pasos, puntos).
// p.num = true -> cada tarjeta lleva su número (1, 2, 3) en un círculo de color.
export const Stack: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const items: {t: string; k?: string; color?: string; at: number}[] = p.items ?? [];
  const big = items.length <= 3;
  return (
    <AbsoluteFill>
      {p.img ? <Bg img={p.img} dur={dur} dim={0.6} blur={p.blur ?? 0} drift="up" /> : <BrandBg dur={dur} />}
      <div style={{position: 'absolute', left: 100, width: 880, top: p.top ?? 300, display: 'flex', flexDirection: 'column', gap: big ? 26 : 18}}>
        {p.title ? (
          <div style={{fontFamily: FONT.title, fontSize: p.titleSize ?? 84, color: C.white, lineHeight: 1, marginBottom: 8, textAlign: 'center', opacity: pop(f, 0)}}>
            {p.title}
          </div>
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
                background: 'rgba(13,18,25,0.92)',
                border: `1px solid ${C.line}`,
                borderRadius: 28,
                overflow: 'hidden',
                opacity: Math.min(1, s * 1.4),
                transform: `translateY(${interpolate(s, [0, 1], [60, 0])}px) scale(${interpolate(s, [0, 1], [0.94, 1])})`,
                boxShadow: '0 20px 60px rgba(0,0,0,0.45)',
              }}
            >
              {p.num ? (
                <div style={{width: 110, display: 'flex', alignItems: 'center', justifyContent: 'center', background: `${col}22`}}>
                  <div
                    style={{
                      width: 70,
                      height: 70,
                      borderRadius: 35,
                      background: col,
                      color: C.bg,
                      fontFamily: FONT.title,
                      fontSize: 52,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      paddingTop: 4,
                    }}
                  >
                    {i + 1}
                  </div>
                </div>
              ) : (
                <div style={{width: 14, background: col}} />
              )}
              <div style={{padding: big ? '28px 34px' : '20px 28px'}}>
                {it.k ? (
                  <div style={{fontFamily: FONT.body, fontWeight: 700, fontSize: big ? 30 : 26, color: col, letterSpacing: 1, textTransform: 'uppercase'}}>
                    {it.k}
                  </div>
                ) : null}
                <div style={{fontFamily: FONT.body, fontWeight: 800, fontSize: big ? 48 : 40, color: C.white, lineHeight: 1.12, marginTop: it.k ? 6 : 0}}>
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
