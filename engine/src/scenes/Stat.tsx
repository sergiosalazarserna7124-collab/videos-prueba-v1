import React from 'react';
import {AbsoluteFill, Easing, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {Bg, BrandBg} from '../ui/Bg';
import {pop} from '../ui/anim';
import {colorOf} from './Stack';

type StatItem = {value: number; prefix?: string; suffix?: string; decimals?: number; label: string; color?: string; at: number; sep?: boolean};

const fmt = (v: number, d = 0) => {
  const s = v.toFixed(d);
  const [i, dec] = s.split('.');
  const withSep = i.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  return dec ? `${withSep}.${dec}` : withSep;
};

// Números grandes que cuentan hacia arriba. Uno o varios (se reemplazan o se apilan).
export const Stat: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const items: StatItem[] = p.items ?? [];
  const stacked = p.stacked ?? items.length <= 3;
  const visible = stacked ? items.filter((it) => f >= it.at) : items.filter((it, i) => f >= it.at && (i === items.length - 1 || f < items[i + 1].at));
  return (
    <AbsoluteFill>
      {p.img ? <Bg img={p.img} dur={dur} dim={0.72} blur={p.blur ?? 4} drift="in" /> : <BrandBg dur={dur} />}
      <div style={{position: 'absolute', left: 60, right: 60, top: p.top ?? 280, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 34}}>
        {p.title ? (
          <div style={{fontFamily: FONT.body, fontWeight: 700, fontSize: 40, color: C.gray, textAlign: 'center', opacity: pop(f, 0), letterSpacing: 1}}>{p.title}</div>
        ) : null}
        {visible.map((it, i) => {
          const s = pop(f, it.at, 30, 14, 0.7);
          const t = interpolate(f, [it.at, it.at + 24], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
          const col = colorOf(it.color ?? 'cyan');
          return (
            <div key={i} style={{display: 'flex', flexDirection: 'column', alignItems: 'center', opacity: Math.min(1, s * 1.4), transform: `scale(${interpolate(s, [0, 1], [0.8, 1])})`}}>
              <div style={{fontFamily: FONT.title, fontSize: stacked && items.length > 1 ? 170 : 260, lineHeight: 0.9, color: col, textShadow: `0 0 60px ${col}55`}}>
                {it.prefix ?? ''}
                {fmt(it.value * t, it.decimals ?? 0)}
                {it.suffix ?? ''}
              </div>
              <div style={{fontFamily: FONT.body, fontWeight: 800, fontSize: 44, color: C.white, textAlign: 'center', maxWidth: 880, lineHeight: 1.15, marginTop: 8}}>
                {it.label}
              </div>
            </div>
          );
        })}
      </div>
      {p.foot ? (
        <div style={{position: 'absolute', left: 0, right: 0, top: 1110, textAlign: 'center', fontFamily: FONT.ui, fontSize: 24, color: 'rgba(255,255,255,0.6)'}}>{p.foot}</div>
      ) : null}
    </AbsoluteFill>
  );
};
