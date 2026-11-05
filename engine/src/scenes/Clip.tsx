import React from 'react';
import {AbsoluteFill, interpolate, OffthreadVideo, staticFile, useCurrentFrame} from 'remotion';
import {C, SAFE} from '../theme';
import {BigTitle, Pill} from '../ui/Text';
import {pop} from '../ui/anim';
import {colorOf} from './Stack';

// Clip hecho con IA (sala de juntas, frutinovela...) a pantalla completa, con su propio audio.
// p.src: ruta en public/ · p.lines: gancho en pantalla · p.titleOut: cuadro en que se va el gancho
// p.kicker: píldora arriba del gancho · p.startFrom: cuadros a recortar al inicio · p.vol: volumen del clip
export const Clip: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const out = p.titleOut ?? 75;
  const titleOp = p.lines ? interpolate(f, [out, out + 8], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
  const zoom = 1 + (p.zoom ?? 0.035) * (f / Math.max(1, dur));
  return (
    <AbsoluteFill style={{backgroundColor: C.bg}}>
      <AbsoluteFill style={{transform: `scale(${zoom})`}}>
        <OffthreadVideo
          src={staticFile(p.src)}
          startFrom={p.startFrom ?? 0}
          volume={p.vol ?? 1}
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
        />
      </AbsoluteFill>
      {p.lines && titleOp > 0 ? (
        <>
          <AbsoluteFill
            style={{
              background: 'linear-gradient(180deg, rgba(6,11,18,0.78) 0%, rgba(6,11,18,0.35) 30%, rgba(6,11,18,0) 45%)',
              opacity: titleOp,
            }}
          />
          <div
            style={{
              position: 'absolute',
              left: 70,
              right: 70,
              top: SAFE.top + 10,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              opacity: titleOp,
            }}
          >
            {p.kicker ? (
              <div style={{marginBottom: 18, opacity: pop(f, 0)}}>
                <Pill text={p.kicker} bg={colorOf(p.kickerColor ?? 'red')} color={C.white} size={26} />
              </div>
            ) : null}
            <BigTitle lines={p.lines} size={p.size ?? 112} accent={colorOf(p.accent ?? 'cyan')} />
          </div>
        </>
      ) : null}
    </AbsoluteFill>
  );
};
