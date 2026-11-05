import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {C} from '../theme';

// Foto de fondo con movimiento lento (sin zooms bruscos) y degradados para que el texto se lea.
export const Bg: React.FC<{
  img?: string;
  dur: number;
  dim?: number; // 0..1 oscurecer
  blur?: number;
  drift?: 'in' | 'out' | 'left' | 'right' | 'up';
  topShade?: boolean;
  bottomShade?: boolean;
  tint?: string;
}> = ({img, dur, dim = 0.35, blur = 0, drift = 'in', topShade = true, bottomShade = true, tint}) => {
  const f = useCurrentFrame();
  const t = interpolate(f, [0, Math.max(1, dur)], [0, 1], {extrapolateRight: 'clamp'});
  let scale = 1.06 + 0.06 * t;
  let tx = 0;
  let ty = 0;
  if (drift === 'out') scale = 1.12 - 0.06 * t;
  if (drift === 'left') tx = 20 - 40 * t;
  if (drift === 'right') tx = -20 + 40 * t;
  if (drift === 'up') ty = 20 - 40 * t;
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, overflow: 'hidden'}}>
      {img ? (
        <Img
          src={staticFile(`img/${img}.jpg`)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transform: `scale(${scale}) translate(${tx}px, ${ty}px)`,
            filter: `blur(${blur}px) saturate(1.05) contrast(1.05)`,
          }}
        />
      ) : null}
      <AbsoluteFill style={{backgroundColor: `rgba(6,11,18,${dim})`}} />
      {tint ? <AbsoluteFill style={{background: tint, mixBlendMode: 'soft-light'}} /> : null}
      {topShade ? (
        <AbsoluteFill
          style={{background: 'linear-gradient(180deg, rgba(6,11,18,0.85) 0%, rgba(6,11,18,0) 32%)'}}
        />
      ) : null}
      {bottomShade ? (
        <AbsoluteFill
          style={{background: 'linear-gradient(0deg, rgba(6,11,18,0.92) 0%, rgba(6,11,18,0.55) 30%, rgba(6,11,18,0) 55%)'}}
        />
      ) : null}
    </AbsoluteFill>
  );
};

// Fondo oscuro de marca con rejilla sutil y brillo morado/cian.
export const BrandBg: React.FC<{dur: number}> = ({dur}) => {
  const f = useCurrentFrame();
  const t = f / Math.max(1, dur);
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, overflow: 'hidden'}}>
      <AbsoluteFill
        style={{
          backgroundImage:
            'linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px)',
          backgroundSize: '60px 60px',
          transform: `translateY(${-30 * t}px)`,
        }}
      />
      <div
        style={{
          position: 'absolute',
          width: 900,
          height: 900,
          left: -300 + 80 * t,
          top: 200,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${C.purple}55, transparent 65%)`,
          filter: 'blur(40px)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          width: 900,
          height: 900,
          right: -350 + 60 * t,
          top: 900,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${C.cyan}40, transparent 65%)`,
          filter: 'blur(40px)',
        }}
      />
    </AbsoluteFill>
  );
};
