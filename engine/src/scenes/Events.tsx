import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {BrandBg} from '../ui/Bg';
import {pop} from '../ui/anim';

type Ev = {name: string; count: number; at: number; hot?: boolean};

// Administrador de eventos de Meta (recreado, sin datos de clientes) + aviso de evento recibido.
export const Events: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const evs: Ev[] = p.events ?? [];
  const card = pop(f, 0, 30, 15, 0.7);
  const toastAt: number | undefined = p.toastAt;
  const toast = toastAt != null ? pop(f, toastAt, 30, 13, 0.7) : 0;
  return (
    <AbsoluteFill>
      <BrandBg dur={dur} />
      <div
        style={{
          position: 'absolute',
          left: 90,
          right: 90,
          top: 300,
          background: '#FFFFFF',
          borderRadius: 28,
          overflow: 'hidden',
          boxShadow: '0 40px 120px rgba(0,0,0,0.6)',
          opacity: card,
          transform: `translateY(${interpolate(card, [0, 1], [70, 0])}px)`,
          fontFamily: FONT.ui,
        }}
      >
        <div style={{display: 'flex', alignItems: 'center', gap: 16, padding: '24px 30px', borderBottom: '1px solid #E4E6EB'}}>
          <svg width="46" height="46" viewBox="0 0 40 40">
            <path d="M8 26c0-6 3-12 7-12 3 0 5 4 7 8 2 4 4 8 7 8 2 0 3-2 3-5 0-6-3-11-6-11-3 0-5 4-7 7" fill="none" stroke={C.meta} strokeWidth="3.4" strokeLinecap="round" />
          </svg>
          <div style={{fontWeight: 800, fontSize: 32, color: '#1C2B33'}}>{p.title ?? 'Administrador de eventos'}</div>
        </div>
        <div style={{display: 'grid', gridTemplateColumns: '1fr 160px 150px', padding: '14px 30px', fontSize: 22, fontWeight: 700, color: '#65676B', background: '#F5F6F7'}}>
          <div>Evento</div>
          <div style={{textAlign: 'right'}}>Recibidos</div>
          <div style={{textAlign: 'right'}}>Estado</div>
        </div>
        {evs.map((e, i) => {
          const s = pop(f, e.at, 30, 15, 0.6);
          const live = toastAt != null && e.hot && f >= toastAt;
          const n = Math.round(e.count * interpolate(f, [e.at, e.at + 20], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})) + (live ? 1 : 0);
          return (
            <div
              key={i}
              style={{
                display: 'grid',
                gridTemplateColumns: '1fr 160px 150px',
                alignItems: 'center',
                padding: '22px 30px',
                borderTop: '1px solid #E4E6EB',
                opacity: Math.min(1, s * 1.4),
                background: live ? '#E7F3FF' : '#FFF',
              }}
            >
              <div style={{fontWeight: 700, fontSize: 31, color: '#1C2B33'}}>{e.name}</div>
              <div style={{fontWeight: 800, fontSize: 31, color: '#1C2B33', textAlign: 'right'}}>{n}</div>
              <div style={{display: 'flex', alignItems: 'center', justifyContent: 'flex-end', gap: 10, fontSize: 24, fontWeight: 700, color: '#31A24C'}}>
                <span style={{width: 14, height: 14, borderRadius: 7, background: '#31A24C'}} /> Activo
              </div>
            </div>
          );
        })}
        <div style={{padding: '16px 30px', fontSize: 22, color: '#65676B', borderTop: '1px solid #E4E6EB'}}>Fuente: API de conversiones · Lead Master</div>
      </div>
      {toastAt != null && f >= toastAt ? (
        <div style={{position: 'absolute', left: 0, right: 0, top: 1000, display: 'flex', justifyContent: 'center'}}>
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 18,
              background: C.panel,
              border: `2px solid ${C.green}`,
              borderRadius: 24,
              padding: '20px 30px',
              boxShadow: `0 0 50px ${C.green}55`,
              opacity: toast,
              transform: `translateY(${interpolate(toast, [0, 1], [40, 0])}px)`,
            }}
          >
            <span style={{width: 18, height: 18, borderRadius: 9, background: C.green}} />
            <div>
              <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 30, color: C.white}}>{p.toast ?? 'Evento recibido: Zoom agendado'}</div>
              <div style={{fontFamily: FONT.ui, fontSize: 24, color: C.gray}}>{p.toastSub ?? 'Campaña Tulum · hace 2 min'}</div>
            </div>
          </div>
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
