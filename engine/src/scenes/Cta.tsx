import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {BrandBg} from '../ui/Bg';
import {Logo} from '../ui/Logo';
import {pop} from '../ui/anim';

// Cierre. mode 'comment' (default): "Comenta PALABRA". mode 'ad': botón "DALE CLIC ABAJO" con flecha.
export const Cta: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const a = pop(f, 0, 30, 15, 0.7);
  const b = pop(f, 6, 30, 10, 0.8);
  const c = pop(f, 12);
  const pulse = 1 + 0.03 * Math.sin(f / 5);
  const bob = 14 * Math.sin(f / 4);
  if (p.mode === 'ad') {
    return (
      <AbsoluteFill>
        <BrandBg dur={dur} />
        <div style={{position: 'absolute', left: 60, right: 60, top: 300, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
          <div style={{opacity: a, transform: `translateY(${interpolate(a, [0, 1], [40, 0])}px)`}}>
            <Logo size={92} />
          </div>
          {p.top ? (
            <div style={{marginTop: 70, fontFamily: FONT.title, fontSize: 96, lineHeight: 1, color: C.white, textAlign: 'center', opacity: b}}>
              {p.top}
            </div>
          ) : null}
          <div
            style={{
              marginTop: 50,
              fontFamily: FONT.body,
              fontWeight: 800,
              fontSize: 58,
              color: C.bg,
              background: C.cyan,
              padding: '26px 52px',
              borderRadius: 999,
              transform: `scale(${interpolate(b, [0, 1], [0.5, 1]) * pulse})`,
              opacity: b,
              boxShadow: `0 0 80px ${C.cyan}66`,
              textAlign: 'center',
            }}
          >
            {p.button ?? 'Dale clic abajo'}
          </div>
          <svg width="90" height="90" viewBox="0 0 24 24" style={{marginTop: 34, opacity: c, transform: `translateY(${bob}px)`}}>
            <path d="M12 4v14M5 11l7 7 7-7" fill="none" stroke={C.cyan} strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          {p.sub ? (
            <div style={{marginTop: 20, fontFamily: FONT.body, fontWeight: 700, fontSize: 40, color: C.white, opacity: c, textAlign: 'center', maxWidth: 860}}>
              {p.sub}
            </div>
          ) : null}
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill>
      <BrandBg dur={dur} />
      <div style={{position: 'absolute', left: 0, right: 0, top: 330, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
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
