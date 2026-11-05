import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, SAFE} from '../theme';
import {BrandBg} from '../ui/Bg';
import {LogoMark} from '../ui/Logo';
import {IconPhone, IconWhatsApp} from '../ui/Icons';
import {pop} from '../ui/anim';

type Row = {ch: 'wa' | 'call'; advisor: string; lead: string; summary: string; status: string; color?: string; at: number};

const colorOf = (c?: string) => (c && (C as any)[c]) || c || C.green;

// Panel de Lead Master: conversaciones de hoy con resumen de la IA por asesor.
export const Panel: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const head = pop(f, 0, 30, 16, 0.7);
  const rows: Row[] = p.rows ?? [];
  return (
    <AbsoluteFill>
      <BrandBg dur={dur} />
      <div
        style={{
          position: 'absolute',
          left: 90,
          width: 900,
          top: 280,
          background: 'rgba(13,18,25,0.96)',
          border: `1px solid ${C.line}`,
          borderRadius: 36,
          overflow: 'hidden',
          boxShadow: `0 40px 120px rgba(0,0,0,0.6), 0 0 80px ${C.purple}22`,
          opacity: head,
          transform: `translateY(${interpolate(head, [0, 1], [80, 0])}px)`,
        }}
      >
        <div style={{display: 'flex', alignItems: 'center', gap: 18, padding: '28px 34px', borderBottom: `1px solid ${C.line}`}}>
          <LogoMark size={58} />
          <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 36, color: C.white}}>{p.title ?? 'Conversaciones de hoy'}</div>
          <div style={{marginLeft: 'auto', fontFamily: FONT.ui, fontSize: 24, color: C.gray}}>{p.right ?? 'Resumen de la IA'}</div>
        </div>
        <div style={{display: 'flex', gap: 12, padding: '18px 34px 6px'}}>
          {(p.tabs ?? ['Chats', 'Llamadas', 'Por asesor']).map((t: string, i: number) => (
            <div
              key={i}
              style={{
                fontFamily: FONT.ui,
                fontWeight: 700,
                fontSize: 22,
                color: i === 0 ? C.bg : C.gray,
                background: i === 0 ? C.cyan : 'transparent',
                border: i === 0 ? 'none' : `1px solid ${C.line}`,
                borderRadius: 999,
                padding: '8px 18px',
              }}
            >
              {t}
            </div>
          ))}
        </div>
        <div style={{padding: '12px 22px 26px', display: 'flex', flexDirection: 'column', gap: 14}}>
          {rows.map((r, i) => {
            const s = pop(f, r.at, 30, 15, 0.6);
            const col = colorOf(r.color);
            return (
              <div
                key={i}
                style={{
                  background: C.panel2,
                  border: `1px solid ${C.line}`,
                  borderRadius: 22,
                  padding: '20px 22px',
                  opacity: Math.min(1, s * 1.4),
                  transform: `translateY(${interpolate(s, [0, 1], [40, 0])}px)`,
                }}
              >
                <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
                  {r.ch === 'wa' ? <IconWhatsApp size={40} /> : (
                    <div style={{width: 40, height: 40, borderRadius: 20, background: C.purple, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                      <IconPhone size={22} />
                    </div>
                  )}
                  <div style={{fontFamily: FONT.ui, fontWeight: 700, fontSize: 31, color: C.white}}>{r.advisor}</div>
                  <div style={{fontFamily: FONT.ui, fontSize: 26, color: C.gray}}>{(r as any).raw ? r.lead : `con ${r.lead}`}</div>
                  <div
                    style={{
                      marginLeft: 'auto',
                      fontFamily: FONT.ui,
                      fontWeight: 800,
                      fontSize: 22,
                      color: col,
                      background: `${col}1F`,
                      border: `1px solid ${col}66`,
                      borderRadius: 999,
                      padding: '6px 14px',
                      whiteSpace: 'nowrap',
                    }}
                  >
                    {r.status}
                  </div>
                </div>
                <div style={{fontFamily: FONT.ui, fontSize: 31, color: '#D6DEE8', marginTop: 12, lineHeight: 1.35}}>{r.summary}</div>
              </div>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};
