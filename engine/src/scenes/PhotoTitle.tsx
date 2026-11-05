import React from 'react';
import {AbsoluteFill} from 'remotion';
import {SAFE} from '../theme';
import {Bg} from '../ui/Bg';
import {BigTitle} from '../ui/Text';

// Foto realista + frases grandes que entran en el momento que las dice la voz.
export const PhotoTitle: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const pos = p.pos ?? 'top';
  const top = pos === 'top' ? SAFE.top + 20 : pos === 'middle' ? 640 : 820;
  return (
    <AbsoluteFill>
      <Bg img={p.img} dur={dur} dim={p.dim ?? 0.3} drift={p.drift ?? 'in'} />
      <div style={{position: 'absolute', left: SAFE.left, right: 1080 - SAFE.right, top}}>
        <BigTitle
          lines={p.lines ?? []}
          lineAts={p.lineAts}
          size={p.size ?? 130}
          accent={p.accent}
          align={p.align ?? 'left'}
        />
      </div>
    </AbsoluteFill>
  );
};
