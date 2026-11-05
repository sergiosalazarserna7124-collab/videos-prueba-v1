import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {BrandBg} from '../ui/Bg';
import {Logo} from '../ui/Logo';
import {pop} from '../ui/anim';

// Cierre: logo + "Comenta PALABRA" dentro de la zona segura.
export const Cta: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const a = pop(f, 0, 30, 15, 0.7);
  const b = pop(f, 6, 30, 10, 0.8);
  const c = pop(f, 12);
  const pulse = 1 + 0.03 * Math.sin(f / 5);
  return (
    <AbsoluteFill>
      <BrandBg dur={dur} />
      <div style={{position: 'absolute', left: 0, right: 140, top: 330, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <div style={{opacity: a, transform: `translateY(${interpolate(a, [0, 1], [40, 0])}px)`}}>
          <Logo size={96} />
        </div>
        <div style={{marginTop: 110, fontFamily: FONT.body, fontWeight: 700, fontSize: 56, color: C.gray, opacity: b}}>Comenta</div>
        <div
          style={{
            marginTop: 22,
            fontFamily: FONT.title,
            fontSize: 190,
            lineHeight: 1,
            color: C.bg,
            background: C.cyan,
            padding: '18px 56px 6px',
            borderRadius: 32,
            transform: `scale(${interpolate(b, [0, 1], [0.5, 1]) * pulse})`,
            opacity: b,
            boxShadow: `0 0 80px ${C.cyan}66`,
            letterSpacing: 4,
          }}
        >
          {p.word}
        </div>
        <div style={{marginTop: 40, fontFamily: FONT.body, fontWeight: 700, fontSize: 48, color: C.white, opacity: c, textAlign: 'center', maxWidth: 780}}>
          {p.sub ?? 'y te mando cómo funciona'}
        </div>
      </div>
    </AbsoluteFill>
  );
};
