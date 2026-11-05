import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {Bg} from '../ui/Bg';
import {Phone, StatusBar} from '../ui/Phone';
import {LogoMark} from '../ui/Logo';
import {IconDoc} from '../ui/Icons';
import {pop} from '../ui/anim';
import {colorOf} from './Stack';

type Item = {t: string; n?: string | number; sub?: string; color?: string; at: number};

// Celular con una lista de Lead Master ("Mi trabajo", notificaciones, reporte con PDF).
export const PhoneList: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const items: Item[] = p.items ?? [];
  return (
    <AbsoluteFill>
      <Bg img={p.bg} dur={dur} dim={0.6} blur={8} drift="in" />
      <Phone at={0} top={p.top ?? 270} height={p.height ?? 900} screenBg={C.bg}>
        <StatusBar time={p.clock ?? '8:00'} />
        <div style={{display: 'flex', alignItems: 'center', gap: 16, padding: '14px 28px 18px', borderBottom: `1px solid ${C.line}`}}>
          <LogoMark size={52} />
          <div>
            <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 30, color: C.white}}>{p.title ?? 'Mi trabajo'}</div>
            <div style={{fontFamily: FONT.ui, fontSize: 22, color: C.gray}}>{p.sub ?? 'Qué debo hacer hoy'}</div>
          </div>
        </div>
        <div style={{padding: '18px 20px', display: 'flex', flexDirection: 'column', gap: 14}}>
          {items.map((it, i) => {
            const s = pop(f, it.at, 30, 15, 0.6);
            const col = colorOf(it.color ?? 'cyan');
            const isDoc = it.t.toLowerCase().endsWith('.pdf');
            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 16,
                  background: C.panel2,
                  border: `1px solid ${C.line}`,
                  borderLeft: `8px solid ${col}`,
                  borderRadius: 20,
                  padding: '18px 20px',
                  opacity: Math.min(1, s * 1.4),
                  transform: `translateX(${interpolate(s, [0, 1], [60, 0])}px)`,
                }}
              >
                {isDoc ? <IconDoc size={44} color={C.red} /> : null}
                <div style={{flex: 1}}>
                  <div style={{fontFamily: FONT.ui, fontWeight: 700, fontSize: 28, color: C.white, lineHeight: 1.2}}>{it.t}</div>
                  {it.sub ? <div style={{fontFamily: FONT.ui, fontSize: 22, color: C.gray, marginTop: 4, lineHeight: 1.3}}>{it.sub}</div> : null}
                </div>
                {it.n != null ? (
                  <div style={{minWidth: 58, height: 58, borderRadius: 29, background: col, color: C.bg, fontFamily: FONT.ui, fontWeight: 900, fontSize: 28, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '0 10px'}}>
                    {it.n}
                  </div>
                ) : null}
              </div>
            );
          })}
        </div>
      </Phone>
    </AbsoluteFill>
  );
};
