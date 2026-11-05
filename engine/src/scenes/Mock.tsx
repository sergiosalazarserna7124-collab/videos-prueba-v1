import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {Pill} from '../ui/Text';
import {pop} from '../ui/anim';

// Parodia del "gurú": foto que tiembla y se deforma, colores saturados, texto tipo meme y etiqueta PARODIA.
export const Mock: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const shake = 6 * Math.sin(f * 1.7) + 4 * Math.sin(f * 2.9);
  const wob = 1.12 + 0.04 * Math.sin(f / 3);
  const hue = 25 * Math.sin(f / 6);
  const lines: {t: string; at: number}[] = p.lines ?? [];
  const cur = [...lines].reverse().find((l) => f >= l.at);
  const s = cur ? pop(f, cur.at, 30, 9, 0.6) : 0;
  return (
    <AbsoluteFill style={{background: '#000', overflow: 'hidden'}}>
      <Img
        src={staticFile(`img/${p.img ?? 'guru'}.jpg`)}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transform: `translate(${shake}px, ${-shake / 2}px) scale(${wob}, ${wob * (1 + 0.03 * Math.sin(f / 2))})`,
          filter: `saturate(1.8) contrast(1.15) hue-rotate(${hue}deg)`,
        }}
      />
      <AbsoluteFill style={{background: 'radial-gradient(circle at 50% 45%, transparent 35%, rgba(0,0,0,0.65) 100%)'}} />
      <div style={{position: 'absolute', left: 0, right: 0, top: 262, display: 'flex', justifyContent: 'center'}}>
        <Pill text="Parodia" bg={C.amber} color={C.bg} size={26} />
      </div>
      {cur ? (
        <div style={{position: 'absolute', left: 60, right: 60, top: 360, display: 'flex', justifyContent: 'center'}}>
          <div
            style={{
              fontFamily: FONT.title,
              fontSize: p.size ?? 112,
              lineHeight: 0.95,
              color: C.white,
              textAlign: 'center',
              WebkitTextStroke: '6px #000',
              paintOrder: 'stroke fill',
              textShadow: '0 8px 0 #000',
              transform: `rotate(${-3 + 2 * Math.sin(f / 4)}deg) scale(${interpolate(s, [0, 1], [1.6, 1])})`,
              opacity: Math.min(1, s * 2),
            }}
          >
            {cur.t}
          </div>
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
