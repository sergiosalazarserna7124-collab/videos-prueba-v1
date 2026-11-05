import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, SAFE} from '../theme';
import {Bg} from '../ui/Bg';
import {BigTitle, Pill} from '../ui/Text';
import {fadeIn, pop} from '../ui/anim';

// Titular de noticia sobre una foto: etiqueta roja, fecha, titular grande y fuente.
export const News: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const bar = pop(f, 0);
  const blink = Math.floor(f / 15) % 2 === 0 ? 1 : 0.35;
  return (
    <AbsoluteFill>
      <Bg img={p.img} dur={dur} dim={0.4} drift="in" />
      <div style={{position: 'absolute', left: SAFE.left, top: SAFE.top + 10, right: 1080 - SAFE.rightTop}}>
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 18,
            transform: `translateX(${interpolate(bar, [0, 1], [-200, 0])}px)`,
            opacity: bar,
          }}
        >
          <Pill
            text={p.label ?? 'Noticia'}
            bg={C.red}
            size={30}
            style={{boxShadow: `0 0 30px ${C.red}88`}}
          />
          <span style={{width: 16, height: 16, borderRadius: 8, background: C.red, opacity: blink}} />
          <span style={{fontFamily: FONT.body, fontWeight: 600, fontSize: 30, color: C.white, opacity: 0.9}}>
            {p.meta}
          </span>
        </div>
        <div style={{marginTop: 34}}>
          <BigTitle lines={p.lines} at={0} stagger={4} size={p.size ?? 150} accent={p.accent ?? C.red} />
        </div>
        {p.sub ? (
          <div
            style={{
              marginTop: 26,
              fontFamily: FONT.body,
              fontWeight: 600,
              fontSize: 38,
              color: C.white,
              maxWidth: 820,
              opacity: fadeIn(f, 14),
              textShadow: '0 4px 20px rgba(0,0,0,0.7)',
            }}
          >
            {p.sub}
          </div>
        ) : null}
      </div>
      {p.source ? (
        <div
          style={{
            position: 'absolute',
            left: SAFE.left,
            top: 1080,
            fontFamily: FONT.ui,
            fontSize: 26,
            fontWeight: 500,
            color: 'rgba(255,255,255,0.75)',
            opacity: fadeIn(f, 20),
          }}
        >
          {p.source}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
