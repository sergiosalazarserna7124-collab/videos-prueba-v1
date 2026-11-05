import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, SAFE} from '../theme';
import {Bg} from '../ui/Bg';
import {IconScale} from '../ui/Icons';
import {Pill} from '../ui/Text';
import {pop} from '../ui/anim';

// Tarjeta de expediente: a quién demandan (aparecen uno por uno) y un sello final.
export const Case: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const card = pop(f, 0, 30, 16, 0.7);
  const items: {t: string; at: number}[] = p.items ?? [];
  const stamp = p.stamp ? pop(f, p.stamp.at, 30, 9, 0.9) : 0;
  return (
    <AbsoluteFill>
      <Bg img={p.img} dur={dur} dim={0.55} drift="left" />
      <div
        style={{
          position: 'absolute',
          left: SAFE.left,
          width: 820,
          top: 300,
          background: 'rgba(13,18,25,0.92)',
          border: `1px solid ${C.line}`,
          borderRadius: 36,
          padding: '44px 48px',
          boxShadow: '0 30px 90px rgba(0,0,0,0.6)',
          transform: `translateY(${interpolate(card, [0, 1], [80, 0])}px)`,
          opacity: card,
        }}
      >
        <div style={{display: 'flex', alignItems: 'center', gap: 18}}>
          <IconScale size={54} color={C.white} />
          <Pill text={p.label ?? 'Demanda'} bg={C.red} size={28} />
        </div>
        <div style={{fontFamily: FONT.title, fontSize: 92, color: C.white, marginTop: 26, lineHeight: 0.95}}>{p.title}</div>
        <div style={{marginTop: 26, display: 'flex', flexDirection: 'column', gap: 18}}>
          {items.map((it, i) => {
            const s = pop(f, it.at);
            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 22,
                  fontFamily: FONT.body,
                  fontWeight: 700,
                  fontSize: 46,
                  color: C.white,
                  opacity: s,
                  transform: `translateX(${interpolate(s, [0, 1], [-40, 0])}px)`,
                }}
              >
                <span
                  style={{
                    width: 50,
                    height: 50,
                    borderRadius: 14,
                    background: `${C.red}26`,
                    border: `2px solid ${C.red}`,
                    color: C.red,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontSize: 30,
                    fontWeight: 900,
                  }}
                >
                  {i + 1}
                </span>
                {it.t}
              </div>
            );
          })}
        </div>
        {p.foot ? (
          <div style={{marginTop: 30, fontFamily: FONT.ui, fontSize: 25, color: C.gray, lineHeight: 1.35}}>{p.foot}</div>
        ) : null}
      </div>
      {p.stamp ? (
        <div
          style={{
            position: 'absolute',
            left: SAFE.left + 40,
            top: 960,
            transform: `rotate(-8deg) scale(${interpolate(stamp, [0, 1], [2.2, 1])})`,
            opacity: Math.min(1, stamp * 2),
            border: `8px solid ${C.red}`,
            color: C.red,
            fontFamily: FONT.title,
            fontSize: 80,
            padding: '6px 30px',
            borderRadius: 18,
            background: 'rgba(6,11,18,0.75)',
            letterSpacing: 3,
          }}
        >
          {p.stamp.text}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
