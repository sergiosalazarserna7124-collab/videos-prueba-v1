import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {Bg, BrandBg} from '../ui/Bg';
import {pop} from '../ui/anim';
import {colorOf} from './Stack';

type Node = {t: string; sub?: string; color?: string; at: number};

// Flujo vertical: cada paso aparece cuando la voz lo dice; la línea se dibuja y un punto viaja.
export const Flow: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const nodes: Node[] = p.nodes ?? [];
  const gap = nodes.length > 4 ? 168 : 200;
  const top = p.top ?? 290;
  return (
    <AbsoluteFill>
      {p.img ? <Bg img={p.img} dur={dur} dim={0.75} blur={6} drift="in" /> : <BrandBg dur={dur} />}
      {p.title ? (
        <div style={{position: 'absolute', left: 60, right: 60, top: top - 10, textAlign: 'center', fontFamily: FONT.title, fontSize: 70, color: C.white, opacity: pop(f, 0)}}>{p.title}</div>
      ) : null}
      {nodes.map((n, i) => {
        const y = top + (p.title ? 100 : 0) + i * gap;
        const s = pop(f, n.at, 30, 15, 0.6);
        const col = colorOf(n.color ?? 'cyan');
        const next = nodes[i + 1];
        const lineT = next ? interpolate(f, [next.at - 10, next.at], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
        return (
          <React.Fragment key={i}>
            {next ? (
              <div style={{position: 'absolute', left: 539, top: y + 120, width: 4, height: (gap - 120) * lineT, background: `linear-gradient(${col}, ${colorOf(next.color ?? 'cyan')})`, borderRadius: 2}} />
            ) : null}
            {next && lineT > 0 && lineT < 1 ? (
              <div style={{position: 'absolute', left: 531, top: y + 120 + (gap - 120) * lineT - 10, width: 20, height: 20, borderRadius: 10, background: C.white, boxShadow: `0 0 20px ${C.cyan}`}} />
            ) : null}
            <div
              style={{
                position: 'absolute',
                left: 150,
                right: 150,
                top: y,
                height: 120,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                background: 'rgba(13,18,25,0.94)',
                border: `2px solid ${col}`,
                borderRadius: 26,
                boxShadow: `0 0 40px ${col}33`,
                opacity: Math.min(1, s * 1.4),
                transform: `scale(${interpolate(s, [0, 1], [0.85, 1])})`,
              }}
            >
              <div style={{fontFamily: FONT.body, fontWeight: 800, fontSize: 40, color: C.white, lineHeight: 1.1, textAlign: 'center'}}>{n.t}</div>
              {n.sub ? <div style={{fontFamily: FONT.ui, fontWeight: 500, fontSize: 25, color: C.gray, marginTop: 4, textAlign: 'center'}}>{n.sub}</div> : null}
            </div>
          </React.Fragment>
        );
      })}
    </AbsoluteFill>
  );
};
