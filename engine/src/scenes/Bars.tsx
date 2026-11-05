import React from 'react';
import {AbsoluteFill, Easing, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {BrandBg} from '../ui/Bg';
import {LogoMark} from '../ui/Logo';
import {pop} from '../ui/anim';
import {colorOf} from './Stack';

type BarRow = {name: string; value: number; sub?: string; color?: string};

// Ranking por asesor con barras que crecen (datos de ejemplo).
export const Bars: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const rows: BarRow[] = p.rows ?? [];
  const max = Math.max(...rows.map((r) => r.value), 1);
  const at: number = p.at ?? 6;
  const card = pop(f, 0, 30, 15, 0.7);
  return (
    <AbsoluteFill>
      <BrandBg dur={dur} />
      <div
        style={{
          position: 'absolute',
          left: 90,
          right: 90,
          top: 290,
          background: 'rgba(13,18,25,0.95)',
          border: `1px solid ${C.line}`,
          borderRadius: 32,
          padding: '30px 34px 36px',
          boxShadow: '0 40px 120px rgba(0,0,0,0.6)',
          opacity: card,
          transform: `translateY(${interpolate(card, [0, 1], [60, 0])}px)`,
        }}
      >
        <div style={{display: 'flex', alignItems: 'center', gap: 16, marginBottom: 26}}>
          <LogoMark size={52} />
          <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 34, color: C.white}}>{p.title ?? 'Llamadas por asesor'}</div>
          <div style={{marginLeft: 'auto', fontFamily: FONT.ui, fontSize: 22, color: C.gray}}>{p.right ?? 'Esta semana'}</div>
        </div>
        {rows.map((r, i) => {
          const t = interpolate(f, [at + i * 5, at + i * 5 + 22], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
          const col = colorOf(r.color ?? (i < 2 ? 'cyan' : i === rows.length - 1 ? 'red' : 'purple'));
          return (
            <div key={i} style={{marginBottom: 22}}>
              <div style={{display: 'flex', justifyContent: 'space-between', fontFamily: FONT.ui, fontSize: 28, color: C.white, fontWeight: 700, marginBottom: 8}}>
                <span>{r.name}</span>
                <span style={{color: col}}>{Math.round(r.value * t)}{r.sub ? <span style={{color: C.gray, fontWeight: 500, fontSize: 22}}> {r.sub}</span> : null}</span>
              </div>
              <div style={{height: 22, borderRadius: 11, background: C.line, overflow: 'hidden'}}>
                <div style={{width: `${(r.value / max) * 100 * t}%`, height: '100%', borderRadius: 11, background: col}} />
              </div>
            </div>
          );
        })}
        {p.foot ? <div style={{fontFamily: FONT.ui, fontSize: 22, color: C.gray, marginTop: 6}}>{p.foot}</div> : null}
      </div>
    </AbsoluteFill>
  );
};
