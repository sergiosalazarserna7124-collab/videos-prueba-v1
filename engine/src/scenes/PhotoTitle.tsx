import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, SAFE} from '../theme';
import {Bg} from '../ui/Bg';
import {BigTitle, Pill} from '../ui/Text';
import {pop} from '../ui/anim';
import {colorOf} from './Stack';

// Sello que cae de golpe (MANUAL, NI IDEA, LIBRETA...).
export const Stamp: React.FC<{text: string; at: number; top?: number; color?: string; size?: number; rot?: number}> = ({
  text,
  at,
  top = 900,
  color = C.red,
  size = 96,
  rot = -8,
}) => {
  const f = useCurrentFrame();
  const s = pop(f, at, 30, 9, 0.9);
  if (f < at) return null;
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top, display: 'flex', justifyContent: 'center'}}>
      <div
        style={{
          transform: `rotate(${rot}deg) scale(${interpolate(s, [0, 1], [2.2, 1])})`,
          opacity: Math.min(1, s * 2),
          border: `8px solid ${color}`,
          color,
          fontFamily: FONT.title,
          fontSize: size,
          padding: '4px 30px 0',
          borderRadius: 18,
          background: 'rgba(6,11,18,0.78)',
          letterSpacing: 3,
          whiteSpace: 'nowrap',
        }}
      >
        {text}
      </div>
    </div>
  );
};

// Foto realista + frases grandes que entran en el momento que las dice la voz.
// Opcionales: kicker (píldora arriba del título), stamp {text, at, color}.
export const PhotoTitle: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const pos = p.pos ?? 'top';
  const top = pos === 'top' ? SAFE.top + 20 : pos === 'middle' ? 600 : 820;
  return (
    <AbsoluteFill>
      <Bg img={p.img} dur={dur} dim={p.dim ?? 0.3} drift={p.drift ?? 'in'} />
      <div style={{position: 'absolute', left: 70, right: 70, top, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        {p.kicker ? (
          <div style={{marginBottom: 22, opacity: pop(f, 0)}}>
            <Pill text={p.kicker} bg={colorOf(p.kickerColor ?? 'cyan')} color={C.bg} size={28} />
          </div>
        ) : null}
        <BigTitle lines={p.lines ?? []} lineAts={p.lineAts} size={p.size ?? 130} accent={colorOf(p.accent ?? 'cyan')} align={p.align ?? 'center'} />
      </div>
      {p.stamp ? <Stamp text={p.stamp.text} at={p.stamp.at ?? 0} top={p.stamp.top ?? 900} color={colorOf(p.stamp.color ?? 'red')} size={p.stamp.size ?? 96} /> : null}
    </AbsoluteFill>
  );
};
