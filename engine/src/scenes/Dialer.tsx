import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, GRAD} from '../theme';
import {BrandBg} from '../ui/Bg';
import {LogoMark} from '../ui/Logo';
import {IconPhone} from '../ui/Icons';
import {clamp01, pop} from '../ui/anim';

// Llamadas en cola: un botón y el sistema marca a toda la lista, uno tras otro.
// p.pressAt: cuadro en que se aprieta el botón. p.rows: [{name, sub, at, ring?, outcome}]
// outcome: 'buzon' | 'nocontesta' | 'contesto'. Al contestar, la fila queda "En llamada" con reloj.
// p.total: cuántos hay en la lista (para el contador). p.advisor: quién llama.
type Row = {name: string; sub?: string; at: number; ring?: number; outcome?: 'buzon' | 'nocontesta' | 'contesto'};

const initials = (n: string) => n.split(' ').slice(0, 2).map((w) => w[0]).join('').toUpperCase();

const Status: React.FC<{text: string; color: string; pulse?: boolean}> = ({text, color, pulse}) => {
  const f = useCurrentFrame();
  const o = pulse ? 0.55 + 0.45 * Math.abs(Math.sin(f / 5)) : 1;
  return (
    <div
      style={{
        marginLeft: 'auto',
        fontFamily: FONT.ui,
        fontWeight: 800,
        fontSize: 23,
        color,
        background: `${color}1F`,
        border: `1px solid ${color}66`,
        borderRadius: 999,
        padding: '7px 16px',
        whiteSpace: 'nowrap',
        opacity: o,
      }}
    >
      {text}
    </div>
  );
};

export const Dialer: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const head = pop(f, 0, 30, 16, 0.7);
  const rows: Row[] = p.rows ?? [];
  const pressAt = p.pressAt ?? 12;
  const pressed = f >= pressAt;
  const press = pop(f, pressAt, 30, 10, 0.5);
  const total = p.total ?? 40;
  // Filas ya resueltas (no contestó / buzón) bajan el contador.
  const done = rows.filter((r) => r.outcome !== 'contesto' && f >= r.at + (r.ring ?? 22)).length;
  const live = rows.find((r) => r.outcome === 'contesto' && f >= r.at + (r.ring ?? 22));
  const left = Math.max(0, total - done - (live ? 1 : 0));
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
          boxShadow: `0 40px 120px rgba(0,0,0,0.6), 0 0 80px ${C.cyan}22`,
          opacity: head,
          transform: `translateY(${interpolate(head, [0, 1], [80, 0])}px)`,
        }}
      >
        <div style={{display: 'flex', alignItems: 'center', gap: 18, padding: '26px 34px', borderBottom: `1px solid ${C.line}`}}>
          <LogoMark size={56} />
          <div>
            <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 34, color: C.white}}>{p.title ?? 'Seguimientos de hoy'}</div>
            <div style={{fontFamily: FONT.ui, fontSize: 23, color: C.gray}}>{p.advisor ?? 'Paola Gutiérrez'}</div>
          </div>
          <div style={{marginLeft: 'auto', textAlign: 'right'}}>
            <div style={{fontFamily: FONT.title, fontSize: 64, lineHeight: 0.9, color: pressed ? C.cyan : C.white}}>{left}</div>
            <div style={{fontFamily: FONT.ui, fontSize: 20, color: C.gray}}>en la lista</div>
          </div>
        </div>
        <div style={{display: 'flex', justifyContent: 'center', padding: '22px 34px 8px'}}>
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 14,
              background: pressed ? C.green : GRAD,
              color: pressed ? C.bg : C.white,
              fontFamily: FONT.ui,
              fontWeight: 800,
              fontSize: 32,
              padding: '18px 40px',
              borderRadius: 999,
              transform: `scale(${pressed ? interpolate(press, [0, 1], [0.86, 1]) : 1 + 0.03 * Math.sin(f / 4)})`,
              boxShadow: pressed ? `0 0 40px ${C.green}55` : `0 0 40px ${C.purple}55`,
            }}
          >
            <IconPhone size={30} color={pressed ? C.bg : C.white} />
            {pressed ? p.running ?? 'Llamando a la lista…' : p.button ?? `Llamar a los ${total}`}
          </div>
        </div>
        <div style={{padding: '14px 22px 26px', display: 'flex', flexDirection: 'column', gap: 12}}>
          {rows.map((r, i) => {
            const ring = r.ring ?? 22;
            const s = pop(f, Math.max(0, pressAt - 6 + i * 3), 30, 15, 0.6);
            const dialing = f >= r.at && f < r.at + ring;
            const resolved = f >= r.at + ring;
            let st: React.ReactNode = <Status text="En cola" color={C.gray2} />;
            if (dialing) st = <Status text="Marcando…" color={C.cyan} pulse />;
            else if (resolved && r.outcome === 'buzon') st = <Status text="Buzón · siguiente" color={C.amber} />;
            else if (resolved && r.outcome === 'nocontesta') st = <Status text="No contestó · siguiente" color={C.gray} />;
            else if (resolved && r.outcome === 'contesto') {
              const secs = Math.floor((f - r.at - ring) / 30);
              st = <Status text={`En llamada 0:${String(secs).padStart(2, '0')}`} color={C.green} pulse={secs < 1} />;
            }
            const activeRow = dialing || (resolved && r.outcome === 'contesto');
            const doneRow = resolved && r.outcome !== 'contesto';
            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 16,
                  background: activeRow ? '#0A1A22' : C.panel2,
                  border: `${activeRow ? 2 : 1}px solid ${activeRow ? (resolved ? C.green : C.cyan) : C.line}`,
                  borderRadius: 22,
                  padding: '18px 20px',
                  opacity: Math.min(1, s * 1.4) * (doneRow ? 0.55 : 1),
                  transform: `translateY(${interpolate(s, [0, 1], [30, 0])}px)`,
                }}
              >
                <div
                  style={{
                    width: 58,
                    height: 58,
                    borderRadius: 29,
                    background: GRAD,
                    color: C.white,
                    fontFamily: FONT.ui,
                    fontWeight: 800,
                    fontSize: 22,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexShrink: 0,
                  }}
                >
                  {initials(r.name)}
                </div>
                <div style={{minWidth: 0}}>
                  <div style={{fontFamily: FONT.ui, fontWeight: 700, fontSize: 30, color: C.white}}>{r.name}</div>
                  {r.sub ? <div style={{fontFamily: FONT.ui, fontSize: 23, color: C.gray}}>{r.sub}</div> : null}
                </div>
                {st}
              </div>
            );
          })}
        </div>
        {p.foot ? (
          <div style={{padding: '0 34px 26px', fontFamily: FONT.ui, fontSize: 23, color: C.gray, opacity: clamp01((f - (p.footAt ?? 0)) / 8)}}>{p.foot}</div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
