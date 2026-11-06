import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, GRAD} from '../theme';
import {BrandBg} from '../ui/Bg';
import {LogoMark} from '../ui/Logo';
import {IconPhone, IconWhatsApp} from '../ui/Icons';
import {clamp01, pop} from '../ui/anim';

// Lead Master al centro conectado al WhatsApp y a las llamadas de cada asesor.
// p.nodes: [{name, at}] (hasta 4) · p.title · p.centerAt · p.foot / p.footAt: chip abajo.
type Node = {name: string; at: number; sub?: string};

const POS = [
  [230, 500],
  [850, 500],
  [230, 950],
  [850, 950],
];
const CX = 540;
const CY = 725;

const initials = (n: string) =>
  n
    .split(' ')
    .slice(0, 2)
    .map((w) => w[0])
    .join('')
    .toUpperCase();

export const Hub: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const nodes: Node[] = (p.nodes ?? []).slice(0, 4);
  const cS = pop(f, p.centerAt ?? 0, 30, 12, 0.7);
  const ring = (f % 40) / 40;
  const footS = p.foot != null ? pop(f, p.footAt ?? 30, 30, 14, 0.6) : 0;
  return (
    <AbsoluteFill>
      <BrandBg dur={dur} />
      {p.title ? (
        <div style={{position: 'absolute', left: 60, right: 60, top: 280, textAlign: 'center', fontFamily: FONT.title, fontSize: 84, color: C.white, lineHeight: 1, opacity: pop(f, 0)}}>
          {p.title}
        </div>
      ) : null}
      <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        <defs>
          <linearGradient id="hubl" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" stopColor={C.purple} />
            <stop offset="1" stopColor={C.cyan} />
          </linearGradient>
        </defs>
        {nodes.map((n, i) => {
          const [x, y] = POS[i];
          const t = clamp01((f - n.at - 4) / 12);
          const len = Math.hypot(CX - x, CY - y);
          const dots = [0, 0.5].map((o, k) => {
            const u = ((f - n.at) / 34 + o) % 1;
            const toC = k === 0;
            const uu = toC ? u : 1 - u;
            return f > n.at + 16 ? (
              <circle key={k} cx={x + (CX - x) * uu} cy={y + (CY - y) * uu} r={9} fill={toC ? C.wa : C.cyan} opacity={0.95} />
            ) : null;
          });
          return (
            <g key={i}>
              <line x1={x} y1={y} x2={CX} y2={CY} stroke="url(#hubl)" strokeWidth={6} strokeLinecap="round" strokeDasharray={len} strokeDashoffset={len * (1 - t)} opacity={0.85} />
              {dots}
            </g>
          );
        })}
      </svg>
      {/* centro */}
      <div style={{position: 'absolute', left: CX - 120, top: CY - 120, width: 240, height: 240, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        <div
          style={{
            position: 'absolute',
            inset: 0,
            borderRadius: 70,
            border: `4px solid ${C.cyan}`,
            opacity: (1 - ring) * 0.7 * cS,
            transform: `scale(${1 + ring * 0.5})`,
          }}
        />
        <div style={{transform: `scale(${interpolate(cS, [0, 1], [0.4, 1])})`, opacity: Math.min(1, cS * 1.4), filter: `drop-shadow(0 0 40px ${C.cyan}88)`}}>
          <LogoMark size={210} />
        </div>
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, top: CY + 135, textAlign: 'center', fontFamily: FONT.body, fontWeight: 800, fontSize: 44, color: C.white, opacity: cS}}>Lead Master</div>
      {nodes.map((n, i) => {
        const [x, y] = POS[i];
        const s = pop(f, n.at, 30, 13, 0.6);
        if (f < n.at) return null;
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: x - 130,
              top: y - 80,
              width: 260,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              opacity: Math.min(1, s * 1.5),
              transform: `scale(${interpolate(s, [0, 1], [0.5, 1])})`,
            }}
          >
            <div style={{position: 'relative'}}>
              <div
                style={{
                  width: 130,
                  height: 130,
                  borderRadius: 65,
                  background: GRAD,
                  border: `4px solid ${C.bg}`,
                  boxShadow: `0 0 0 3px ${C.line}, 0 20px 40px rgba(0,0,0,0.5)`,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontFamily: FONT.ui,
                  fontWeight: 800,
                  fontSize: 46,
                  color: C.white,
                }}
              >
                {initials(n.name)}
              </div>
              <div style={{position: 'absolute', right: -18, top: -10}}>
                <IconWhatsApp size={56} />
              </div>
              <div style={{position: 'absolute', left: -18, top: -10, width: 56, height: 56, borderRadius: 28, background: C.purple, display: 'flex', alignItems: 'center', justifyContent: 'center', border: `3px solid ${C.bg}`}}>
                <IconPhone size={28} />
              </div>
            </div>
            <div style={{marginTop: 14, fontFamily: FONT.ui, fontWeight: 800, fontSize: 32, color: C.white, textAlign: 'center', lineHeight: 1.1, textShadow: '0 4px 14px rgba(0,0,0,0.7)'}}>{n.name}</div>
            <div style={{fontFamily: FONT.ui, fontWeight: 600, fontSize: 24, color: C.gray, marginTop: 4}}>{n.sub ?? 'Asesor'}</div>
          </div>
        );
      })}
      {p.foot ? (
        <div style={{position: 'absolute', left: 0, right: 0, top: 1105, display: 'flex', justifyContent: 'center', opacity: Math.min(1, footS * 1.4), transform: `translateY(${interpolate(footS, [0, 1], [30, 0])}px)`}}>
          <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 34, color: C.bg, background: C.cyan, borderRadius: 999, padding: '14px 32px'}}>{p.foot}</div>
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
