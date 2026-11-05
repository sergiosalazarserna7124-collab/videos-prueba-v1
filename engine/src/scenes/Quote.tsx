import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {Bg} from '../ui/Bg';
import {pop} from '../ui/anim';

// Frase real de un dueño (sin nombre) sobre foto oscura.
export const Quote: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const s = pop(f, 0, 30, 15, 0.7);
  const words: string[] = (p.text ?? '').split(' ');
  const per = Math.max(1, Math.min(3, Math.floor((dur * 0.55) / Math.max(1, words.length))));
  return (
    <AbsoluteFill>
      <Bg img={p.img} dur={dur} dim={0.7} blur={3} drift="left" />
      <div
        style={{
          position: 'absolute',
          left: 100,
          right: 100,
          top: p.top ?? 330,
          background: 'rgba(13,18,25,0.88)',
          border: `1px solid ${C.line}`,
          borderRadius: 36,
          padding: '56px 56px 46px',
          boxShadow: '0 30px 90px rgba(0,0,0,0.55)',
          opacity: s,
          transform: `translateY(${interpolate(s, [0, 1], [60, 0])}px)`,
        }}
      >
        <div style={{fontFamily: FONT.title, fontSize: 200, lineHeight: 0.6, color: C.cyan, height: 90}}>“</div>
        <div style={{fontFamily: FONT.body, fontWeight: 700, fontSize: p.size ?? 50, lineHeight: 1.25, color: C.white}}>
          {words.map((w, i) => (
            <span key={i} style={{opacity: f >= 6 + i * per ? 1 : 0.15}}>
              {w}{' '}
            </span>
          ))}
        </div>
        <div style={{marginTop: 30, fontFamily: FONT.ui, fontWeight: 600, fontSize: 28, color: C.gray}}>— {p.who ?? 'Dueño de inmobiliaria'}</div>
      </div>
    </AbsoluteFill>
  );
};
