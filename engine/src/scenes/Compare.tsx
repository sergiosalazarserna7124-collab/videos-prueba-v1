import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {BrandBg} from '../ui/Bg';
import {LogoMark} from '../ui/Logo';
import {IconCheck, IconX} from '../ui/Icons';
import {pop} from '../ui/anim';

type Row = {t: string; l: boolean; r: boolean; at: number};

// Comparación en dos columnas: izquierda (ej. GoHighLevel solo) vs derecha (con Lead Master).
export const Compare: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const rows: Row[] = p.rows ?? [];
  const head = pop(f, 0, 30, 15, 0.7);
  const merge = p.mergeAt != null ? pop(f, p.mergeAt, 30, 13, 0.8) : 0;
  return (
    <AbsoluteFill>
      <BrandBg dur={dur} />
      <div style={{position: 'absolute', left: 80, right: 80, top: 270, opacity: head}}>
        {p.title ? <div style={{fontFamily: FONT.title, fontSize: 78, color: C.white, textAlign: 'center', lineHeight: 1, marginBottom: 26}}>{p.title}</div> : null}
        <div style={{display: 'grid', gridTemplateColumns: '1fr 150px 150px', alignItems: 'center', padding: '0 24px 14px', borderBottom: `1px solid ${C.line}`}}>
          <div />
          <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 24, color: C.gray, textAlign: 'center', lineHeight: 1.1}}>{p.left ?? 'GoHighLevel'}</div>
          <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6}}>
            <LogoMark size={44} />
            <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 22, color: C.cyan, textAlign: 'center'}}>{p.right ?? 'Lead Master'}</div>
          </div>
        </div>
        {rows.map((r, i) => {
          const s = pop(f, r.at, 30, 15, 0.6);
          return (
            <div
              key={i}
              style={{
                display: 'grid',
                gridTemplateColumns: '1fr 150px 150px',
                alignItems: 'center',
                padding: '20px 24px',
                borderBottom: `1px solid ${C.line}`,
                opacity: Math.min(1, s * 1.4),
                transform: `translateX(${interpolate(s, [0, 1], [-50, 0])}px)`,
                background: i % 2 ? 'transparent' : 'rgba(255,255,255,0.025)',
              }}
            >
              <div style={{fontFamily: FONT.body, fontWeight: 700, fontSize: 36, color: C.white, lineHeight: 1.15}}>{r.t}</div>
              <div style={{display: 'flex', justifyContent: 'center'}}>{r.l ? <IconCheck size={46} /> : <IconX size={46} />}</div>
              <div style={{display: 'flex', justifyContent: 'center'}}>{r.r ? <IconCheck size={46} /> : <IconX size={46} />}</div>
            </div>
          );
        })}
      </div>
      {p.mergeText && f >= (p.mergeAt ?? 1e9) ? (
        <div style={{position: 'absolute', left: 0, right: 0, top: 1040, display: 'flex', justifyContent: 'center'}}>
          <div
            style={{
              fontFamily: FONT.title,
              fontSize: 80,
              color: C.bg,
              background: C.cyan,
              padding: '10px 40px 0',
              borderRadius: 24,
              transform: `scale(${interpolate(merge, [0, 1], [0.5, 1])})`,
              opacity: merge,
              boxShadow: `0 0 60px ${C.cyan}66`,
            }}
          >
            {p.mergeText}
          </div>
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
