import React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, GRAD} from '../theme';
import {LogoMark} from './Logo';
import {IconCheck, IconPhone, IconWhatsApp} from './Icons';
import {Phone, StatusBar} from './Phone';
import {clamp01, pop} from './anim';

// Gráficos "literales": cuando la voz dice CRM, nota, cita, reporte, llamada o tareas,
// aparece eso en pantalla. Todo dentro de la zona segura (x 90..990, y 280..1170).
// Los tiempos (at, to, move.at, confirmAt...) vienen en cuadros de la escena.

export type Ins = {kind: string; at: number; to?: number; p?: any};

const col = (c?: string) => (c && (C as any)[c]) || c || C.cyan;

const short = (name: string) => {
  const w = name.split(' ');
  return w.length > 1 ? `${w[0]} ${w[1][0]}.` : name;
};

const initials = (name: string) =>
  name
    .split(' ')
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0])
    .join('')
    .toUpperCase();

const Avatar: React.FC<{name: string; size?: number; color?: string}> = ({name, size = 56, color}) => (
  <div
    style={{
      width: size,
      height: size,
      borderRadius: size / 2,
      background: color ?? GRAD,
      color: C.white,
      fontFamily: FONT.ui,
      fontWeight: 800,
      fontSize: size * 0.38,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      flexShrink: 0,
    }}
  >
    {initials(name)}
  </div>
);

const Sparkle: React.FC<{size?: number; color?: string}> = ({size = 26, color = C.cyan}) => (
  <svg width={size} height={size} viewBox="0 0 24 24">
    <path d="M12 2l2.2 6.6L21 11l-6.8 2.4L12 20l-2.2-6.6L3 11l6.8-2.4z" fill={color} />
  </svg>
);

const Chip: React.FC<{text: string; color?: string; solid?: boolean; size?: number; icon?: React.ReactNode}> = ({
  text,
  color = C.cyan,
  solid,
  size = 22,
  icon,
}) => (
  <div
    style={{
      display: 'inline-flex',
      alignItems: 'center',
      gap: 8,
      fontFamily: FONT.ui,
      fontWeight: 800,
      fontSize: size,
      color: solid ? C.bg : color,
      background: solid ? color : `${color}1F`,
      border: `2px solid ${color}`,
      borderRadius: 999,
      padding: '6px 16px',
      whiteSpace: 'nowrap',
    }}
  >
    {icon}
    {text}
  </div>
);

// Tarjeta base de la app (encabezado con logo).
const Shell: React.FC<{title: string; right?: string; top?: number; children: React.ReactNode; accent?: string}> = ({
  title,
  right,
  top = 290,
  children,
  accent = C.purple,
}) => (
  <div
    style={{
      position: 'absolute',
      left: 90,
      width: 900,
      top,
      background: 'rgba(13,18,25,0.98)',
      border: `1px solid ${C.line}`,
      borderRadius: 36,
      overflow: 'hidden',
      boxShadow: `0 40px 120px rgba(0,0,0,0.7), 0 0 90px ${accent}26`,
    }}
  >
    <div style={{display: 'flex', alignItems: 'center', gap: 16, padding: '24px 30px', borderBottom: `1px solid ${C.line}`}}>
      <LogoMark size={60} />
      <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 40, color: C.white}}>{title}</div>
      {right ? <div style={{marginLeft: 'auto', fontFamily: FONT.ui, fontSize: 26, maxWidth: 380, color: C.gray, textAlign: 'right'}}>{right}</div> : null}
    </div>
    {children}
  </div>
);

// ---------------------------------------------------------------- CRM (pipeline)
type Card = {name: string; sub?: string; col: number; age?: string; warn?: boolean};

const DEF_CARDS: Card[] = [
  {name: 'Lucía Hernández', sub: 'Depa 2 rec · Tulum', col: 0, age: 'hace 4 min'},
  {name: 'Diana Trejo', sub: 'Casa · Zapopan', col: 0, age: 'hace 12 min'},
  {name: 'Adriana Solís', sub: 'Terreno · Mérida', col: 1, age: 'hace 1 h'},
  {name: 'Carlos Ruiz', sub: 'Preventa · Polanco', col: 1, age: 'ayer'},
  {name: 'Sofía Méndez', sub: 'Depa · Cancún', col: 2, age: 'jueves 5 pm'},
];

const STALE_CARDS: Card[] = [
  {name: 'Lucía Hernández', sub: 'Sin notas', col: 0, age: 'Sin actividad 92 días', warn: true},
  {name: 'Diana Trejo', sub: 'Sin notas', col: 0, age: 'Sin actividad 64 días', warn: true},
  {name: 'Adriana Solís', sub: 'Etapa sin mover', col: 0, age: 'Sin actividad 47 días', warn: true},
  {name: 'Carlos Ruiz', sub: 'Sin notas', col: 1, age: 'Sin actividad 81 días', warn: true},
  {name: 'Sofía Méndez', sub: '¿En qué quedó?', col: 2, age: 'Sin actividad 39 días', warn: true},
];

const COL_COLORS = [C.gray, C.purple, C.green, C.amber];

const Crm: React.FC<{ins: Ins}> = ({ins}) => {
  const f = useCurrentFrame();
  const p = ins.p ?? {};
  const stale = !!p.stale;
  const cols: string[] = p.cols ?? ['Nuevo', 'Contactado', 'Cita'];
  const cards: Card[] = p.cards ?? (stale ? STALE_CARDS : DEF_CARDS);
  const move = p.move ?? (stale ? null : {card: 0, to: Math.min(2, cols.length - 1), at: ins.at + 26});
  const mp = move ? clamp01(pop(f, move.at, 30, 18, 0.8)) : 0;
  const colW = 274;
  const gap = 14;
  const x0 = 22;
  const cardH = 176;
  const top0 = 96;
  // posición en la columna antes y después de mover
  const slot = (moved: boolean) => {
    const out: {c: number; i: number}[] = [];
    const counts = cols.map(() => 0);
    if (moved && move) counts[move.to] = 1; // la tarjeta movida entra arriba
    cards.forEach((cd, k) => {
      if (moved && move && k === move.card) {
        out.push({c: move.to, i: 0});
        return;
      }
      out.push({c: cd.col, i: counts[cd.col]++});
    });
    return out;
  };
  const before = slot(false);
  const after = slot(true);
  const counts = (s: {c: number}[]) => cols.map((_, c) => s.filter((x) => x.c === c).length);
  const cb = counts(before);
  const ca = counts(after);
  const chipS = move ? pop(f, move.at + 14, 30, 14, 0.6) : 0;
  return (
    <Shell title={p.title ?? 'CRM · Pipeline'} right={p.right ?? (stale ? 'Última actualización: hace 3 meses' : 'Se mueve solo')} accent={stale ? C.red : C.purple}>
      <div style={{position: 'relative', height: top0 + 3 * cardH + 110}}>
        {cols.map((c, i) => {
          const n = Math.round(interpolate(mp, [0, 1], [cb[i], ca[i]]));
          return (
            <div key={i} style={{position: 'absolute', left: x0 + i * (colW + gap), top: 22, width: colW}}>
              <div style={{height: 6, borderRadius: 3, background: COL_COLORS[i % 4], marginBottom: 12}} />
              <div style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between'}}>
                <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 30, color: C.white}}>{c}</div>
                <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 24, color: C.gray, background: C.panel2, borderRadius: 999, padding: '2px 12px'}}>
                  {stale ? [148, 63, 21, 4][i] : n}
                </div>
              </div>
            </div>
          );
        })}
        {cards.map((cd, k) => {
          const s = pop(f, ins.at + 3 + k * 3, 30, 15, 0.6);
          const isMoving = move && k === move.card;
          const b = before[k];
          const a = after[k];
          const x = interpolate(mp, [0, 1], [x0 + b.c * (colW + gap), x0 + a.c * (colW + gap)]);
          const y = interpolate(mp, [0, 1], [top0 + b.i * cardH, top0 + a.i * cardH]) + (isMoving ? -26 * Math.sin(mp * Math.PI) : 0);
          const glow = isMoving ? Math.sin(clamp01(mp) * Math.PI) : 0;
          const done = isMoving && mp > 0.6;
          return (
            <div
              key={k}
              style={{
                position: 'absolute',
                left: x,
                top: y + 30,
                width: colW,
                height: cardH - 16,
                boxSizing: 'border-box',
                background: C.panel2,
                border: `2px solid ${isMoving ? (done ? C.green : C.cyan) : cd.warn ? `${C.red}88` : C.line}`,
                borderRadius: 20,
                padding: '14px 16px',
                opacity: Math.min(1, s * 1.4),
                transform: `scale(${(0.9 + 0.1 * s) * (1 + 0.06 * glow)})`,
                boxShadow: isMoving ? `0 18px 50px rgba(0,0,0,0.6), 0 0 ${40 * glow + 10}px ${C.cyan}66` : 'none',
                zIndex: isMoving ? 5 : 1,
              }}
            >
              <div style={{display: 'flex', alignItems: 'center', gap: 10}}>
                <Avatar name={cd.name} size={46} color={cd.warn ? C.gray2 : undefined} />
                <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 27, color: C.white, lineHeight: 1.1}}>{short(cd.name)}</div>
              </div>
              <div style={{fontFamily: FONT.ui, fontSize: 22, color: cd.warn ? C.amber : C.gray, marginTop: 10, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis'}}>{cd.sub}</div>
              <div style={{fontFamily: FONT.ui, fontWeight: 700, fontSize: 21, color: cd.warn ? C.red : C.gray2, marginTop: 4}}>
                {done ? 'Movido por la IA' : cd.age}
              </div>
            </div>
          );
        })}
        {move ? (
          <div
            style={{
              position: 'absolute',
              left: 0,
              right: 0,
              bottom: 26,
              display: 'flex',
              justifyContent: 'center',
              opacity: Math.min(1, chipS * 1.3),
              transform: `translateY(${interpolate(chipS, [0, 1], [30, 0])}px)`,
            }}
          >
            <Chip text={p.chip ?? `Etapa actualizada: ${cols[move.to]}`} color={C.green} icon={<Sparkle size={26} color={C.green} />} size={28} />
          </div>
        ) : stale || p.chip ? (
          <div style={{position: 'absolute', left: 0, right: 0, bottom: 18, display: 'flex', justifyContent: 'center', opacity: clamp01((f - ins.at - 20) / 8)}}>
            <Chip text={p.chip ?? 'Nadie lo actualiza'} color={stale ? C.red : C.green} size={28} />
          </div>
        ) : null}
      </div>
    </Shell>
  );
};

// ---------------------------------------------------------------- Nota en la ficha del lead
const Note: React.FC<{ins: Ins}> = ({ins}) => {
  const f = useCurrentFrame();
  const p = ins.p ?? {};
  const empty = !!p.empty;
  const lead = p.lead ?? 'Lucía Hernández';
  const fields: {k: string; v: string; at?: number}[] = p.fields ?? [
    {k: 'Busca', v: 'Depa 2 recámaras'},
    {k: 'Zona', v: 'Tulum'},
    {k: 'Presupuesto', v: '250 mil USD'},
    {k: 'Etapa', v: 'Cita'},
  ];
  const note: string = p.note ?? 'Quiere ver el proyecto el jueves a las 5 pm. Pidió planos y forma de pago. Seguimiento: confirmar visita.';
  const typeAt = p.typeAt ?? ins.at + 14;
  const speed = p.speed ?? 2.2; // caracteres por cuadro
  const shown = Math.max(0, Math.floor((f - typeAt) * speed));
  const txt = note.slice(0, shown);
  const doneAt = typeAt + Math.ceil(note.length / speed);
  const saved = pop(f, doneAt + 4, 30, 14, 0.6);
  const cursor = f < doneAt && Math.floor(f / 8) % 2 === 0;
  return (
    <Shell title={p.title ?? 'CRM · Ficha del lead'} right={p.right ?? (empty ? 'Nadie la llenó' : 'Se llena sola')} accent={empty ? C.red : C.cyan}>
      <div style={{padding: '24px 30px 30px'}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 18}}>
          <Avatar name={lead} size={84} color={empty ? C.gray2 : undefined} />
          <div>
            <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 42, color: C.white}}>{lead}</div>
            <div style={{fontFamily: FONT.ui, fontSize: 27, color: C.gray, marginTop: 2}}>{p.tag ?? 'Lead · Formulario de Meta'}</div>
          </div>
          <div style={{marginLeft: 'auto'}}>
            <Chip text={empty ? 'Nuevo' : (p.stage ?? 'Cita')} color={empty ? C.gray : C.green} size={26} />
          </div>
        </div>
        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14, marginTop: 24}}>
          {fields.map((fl, i) => {
            const s = pop(f, fl.at ?? ins.at + 6 + i * 4, 30, 15, 0.6);
            return (
              <div key={i} style={{background: C.panel2, border: `1px solid ${C.line}`, borderRadius: 18, padding: '14px 18px', opacity: Math.min(1, s * 1.4)}}>
                <div style={{fontFamily: FONT.ui, fontWeight: 700, fontSize: 22, color: C.gray, textTransform: 'uppercase', letterSpacing: 1}}>{fl.k}</div>
                <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 33, color: empty ? C.gray2 : C.white, marginTop: 4}}>{empty ? '—' : fl.v}</div>
              </div>
            );
          })}
        </div>
        <div
          style={{
            marginTop: 20,
            background: '#0A1018',
            border: `2px solid ${empty ? `${C.red}99` : f >= typeAt ? C.cyan : C.line}`,
            borderRadius: 22,
            padding: '18px 22px',
            minHeight: 210,
          }}
        >
          <div style={{display: 'flex', alignItems: 'center', gap: 10, marginBottom: 10}}>
            <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 24, color: C.gray, letterSpacing: 1}}>NOTA</div>
            {!empty ? <Chip text="Escrita por la IA" color={C.cyan} size={23} icon={<Sparkle size={22} />} /> : null}
          </div>
          {empty ? (
            <div style={{fontFamily: FONT.ui, fontWeight: 700, fontSize: 34, color: C.red}}>{p.emptyText ?? 'Sin notas · última hace 47 días'}</div>
          ) : (
            <div style={{fontFamily: FONT.ui, fontWeight: 600, fontSize: 34, color: C.white, lineHeight: 1.35}}>
              {txt}
              <span style={{display: 'inline-block', width: 3, height: 36, background: cursor ? C.cyan : 'transparent', marginLeft: 3, verticalAlign: 'middle'}} />
            </div>
          )}
        </div>
        {!empty ? (
          <div style={{display: 'flex', justifyContent: 'center', marginTop: 18, opacity: Math.min(1, saved * 1.3), transform: `scale(${0.8 + 0.2 * saved})`}}>
            <Chip text="Nota guardada sola" color={C.green} solid icon={<IconCheck size={28} color={C.bg} />} size={28} />
          </div>
        ) : null}
      </div>
    </Shell>
  );
};

// ---------------------------------------------------------------- Cita en la agenda
const Cita: React.FC<{ins: Ins}> = ({ins}) => {
  const f = useCurrentFrame();
  const p = ins.p ?? {};
  const days = ['L', 'M', 'M', 'J', 'V', 'S', 'D'];
  const dayIdx = p.dayIdx ?? 3;
  const nums = [10, 11, 12, 13, 14, 15, 16];
  const evS = pop(f, ins.at + 10, 30, 15, 0.7);
  const mode: string = p.mode ?? 'confirm'; // confirm | done | missed
  const confirmAt = p.confirmAt ?? ins.at + 42;
  const tap = mode === 'confirm' ? clamp01((f - (confirmAt - 10)) / 10) : 0;
  const confirmed = mode === 'done' || (mode === 'confirm' && f >= confirmAt);
  const cS = pop(f, confirmAt, 30, 12, 0.5);
  const hours = ['3:00 pm', '4:00 pm', '5:00 pm', '6:00 pm'];
  const slot = p.slot ?? 2;
  const evColor = mode === 'missed' ? C.red : confirmed ? C.green : C.purple;
  return (
    <Shell title={p.title ?? 'Agenda'} right={p.right ?? 'Noviembre'} accent={evColor}>
      <div style={{padding: '20px 30px 28px'}}>
        <div style={{display: 'flex', justifyContent: 'space-between'}}>
          {days.map((d, i) => {
            const on = i === dayIdx;
            const s = on ? pop(f, ins.at + 4, 30, 12, 0.5) : 1;
            return (
              <div key={i} style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6, width: 110}}>
                <div style={{fontFamily: FONT.ui, fontWeight: 700, fontSize: 25, color: C.gray}}>{d}</div>
                <div
                  style={{
                    width: 76,
                    height: 76,
                    borderRadius: 38,
                    background: on ? C.cyan : 'transparent',
                    color: on ? C.bg : C.white,
                    fontFamily: FONT.ui,
                    fontWeight: 800,
                    fontSize: 33,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    transform: `scale(${on ? 0.7 + 0.3 * s : 1})`,
                  }}
                >
                  {nums[i]}
                </div>
              </div>
            );
          })}
        </div>
        <div style={{position: 'relative', marginTop: 18, height: 4 * 104}}>
          {hours.map((h, i) => (
            <div key={i} style={{position: 'absolute', top: i * 104, left: 0, right: 0, display: 'flex', alignItems: 'flex-start', gap: 16}}>
              <div style={{width: 120, fontFamily: FONT.ui, fontSize: 24, color: C.gray2, marginTop: -14}}>{h}</div>
              <div style={{flex: 1, height: 1, background: C.line}} />
            </div>
          ))}
          <div
            style={{
              position: 'absolute',
              left: 136,
              right: 0,
              top: slot * 104 + 6,
              height: 92 + 104,
              boxSizing: 'border-box',
              background: `${evColor}24`,
              borderLeft: `8px solid ${evColor}`,
              borderRadius: 18,
              padding: '16px 22px',
              opacity: Math.min(1, evS * 1.4),
              transform: `translateX(${interpolate(evS, [0, 1], [120, 0])}px)`,
            }}
          >
            <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 36, color: C.white}}>{p.what ?? 'Recorrido · Torre Mar'}</div>
            <div style={{fontFamily: FONT.ui, fontSize: 27, color: C.gray, marginTop: 6}}>
              {(p.when ?? 'Jueves 13 · 5:00 pm') + ' · ' + (p.lead ?? 'Lucía Hernández')}
            </div>
            <div style={{fontFamily: FONT.ui, fontSize: 26, color: C.gray, marginTop: 4}}>{'Asesor: ' + (p.advisor ?? 'Valeria Ríos')}</div>
          </div>
        </div>
        <div style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 8, opacity: clamp01((f - ins.at - 16) / 8)}}>
          <Chip
            text={mode === 'missed' ? (p.missedText ?? 'Nadie le dio seguimiento') : p.source ?? 'Detectada en el chat por la IA'}
            color={mode === 'missed' ? C.red : C.cyan}
            size={23}
            icon={mode === 'missed' ? undefined : <Sparkle size={18} />}
          />
          {mode !== 'missed' ? (
            <div style={{position: 'relative'}}>
              <div
                style={{
                  fontFamily: FONT.ui,
                  fontWeight: 800,
                  fontSize: 28,
                  color: C.bg,
                  background: confirmed ? C.green : C.cyan,
                  borderRadius: 16,
                  padding: '14px 24px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 10,
                  transform: `scale(${confirmed ? 1 + 0.08 * (1 - cS) * Math.sin(cS * Math.PI) : 1 - 0.05 * tap})`,
                }}
              >
                {confirmed ? <IconCheck size={26} color={C.bg} /> : null}
                {confirmed ? (p.doneText ?? 'Cita confirmada') : 'Confirmar cita'}
              </div>
              {mode === 'confirm' && f < confirmAt + 12 ? (
                <div
                  style={{
                    position: 'absolute',
                    width: 54,
                    height: 54,
                    borderRadius: 27,
                    border: `4px solid ${C.white}`,
                    background: 'rgba(255,255,255,0.25)',
                    left: interpolate(tap, [0, 1], [190, 90]),
                    top: interpolate(tap, [0, 1], [90, 10]),
                    opacity: tap * (f < confirmAt ? 1 : 1 - (f - confirmAt) / 12),
                    transform: `scale(${f >= confirmAt ? 1 + (f - confirmAt) / 10 : 1})`,
                  }}
                />
              ) : null}
            </div>
          ) : null}
        </div>
      </div>
    </Shell>
  );
};

// ---------------------------------------------------------------- Reporte por WhatsApp (en el celular)
type RLine = {t: string; c?: string; b?: boolean; at?: number; sep?: boolean};

const DEF_REPORT: RLine[] = [
  {t: 'Leads que entraron hoy: 23', b: true},
  {t: 'Contactados: 18 · Sin contacto: 5'},
  {t: 'Citas agendadas: 4', c: 'green'},
  {t: '', sep: true},
  {t: 'Paola G. · 14 llamadas · 2 citas'},
  {t: 'Valeria R. · 11 llamadas · 1 cita'},
  {t: 'Diego H. · 2 llamadas · 4 sin contactar', c: 'red'},
  {t: '', sep: true},
  {t: 'Atención: Adriana Solís lleva 26 h sin llamada (Diego H.)', c: 'amber'},
];

const Report: React.FC<{ins: Ins}> = ({ins}) => {
  const f = useCurrentFrame();
  const p = ins.p ?? {};
  const time: string = p.time ?? '7:00 pm';
  const lines: RLine[] = p.lines ?? DEF_REPORT;
  const bubbleS = pop(f, ins.at + 10, 30, 15, 0.6);
  const alert = p.alert === false ? null : p.alert ?? {t: 'Ahora: lead nuevo de Meta, Diana Trejo. Valeria R. le escribió en 3 min.', c: 'green'};
  const alertAt = alert?.at ?? ins.at + 16 + lines.length * 5 + 20;
  const aS = pop(f, alertAt, 30, 14, 0.6);
  return (
    <Phone at={ins.at} top={268} width={720} height={904} screenBg={C.waDark}>
      <StatusBar time={time.replace(/ ?(am|pm)/, '')} />
      <div style={{display: 'flex', alignItems: 'center', gap: 14, padding: '6px 22px 14px', background: '#1F2C34'}}>
        <div style={{fontSize: 34, color: C.white, marginRight: 4}}>‹</div>
        <LogoMark size={56} />
        <div>
          <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 30, color: C.white}}>Lead Master</div>
          <div style={{fontFamily: FONT.ui, fontSize: 22, color: C.gray}}>{p.sub ?? 'Reportes de tu inmobiliaria'}</div>
        </div>
        <div style={{marginLeft: 'auto'}}>
          <IconWhatsApp size={40} />
        </div>
      </div>
      <div style={{padding: '14px 18px', display: 'flex', flexDirection: 'column', gap: 12}}>
        <div style={{alignSelf: 'center', fontFamily: FONT.ui, fontSize: 22, color: '#FFD279', background: '#1C2A21', borderRadius: 12, padding: '8px 16px', textAlign: 'center'}}>
          {p.sched ?? `Tu reporte diario llega a las ${time}`}
        </div>
        <div
          style={{
            alignSelf: 'flex-start',
            maxWidth: 650,
            background: C.waBubbleIn,
            borderRadius: '6px 22px 22px 22px',
            padding: '16px 22px 10px',
            opacity: Math.min(1, bubbleS * 1.4),
            transform: `translateY(${interpolate(bubbleS, [0, 1], [40, 0])}px)`,
          }}
        >
          <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 30, color: C.white, marginBottom: 8}}>{p.title ?? 'Reporte de tu equipo'}</div>
          {lines.map((l, i) => {
            const at = l.at ?? ins.at + 16 + i * 5;
            const s = clamp01((f - at) / 6);
            if (l.sep) return <div key={i} style={{height: 1, background: '#33424C', margin: '8px 0', opacity: s}} />;
            return (
              <div
                key={i}
                style={{
                  fontFamily: FONT.ui,
                  fontWeight: l.b ? 800 : 500,
                  fontSize: 27,
                  lineHeight: 1.36,
                  color: l.c ? col(l.c) : '#E9EDEF',
                  opacity: s,
                  transform: `translateX(${(1 - s) * 18}px)`,
                }}
              >
                {l.t}
              </div>
            );
          })}
          <div style={{fontFamily: FONT.ui, fontSize: 20, color: C.gray, textAlign: 'right', marginTop: 6}}>{time}</div>
        </div>
        {alert ? (
          <div
            style={{
              alignSelf: 'flex-start',
              maxWidth: 650,
              background: C.waBubbleIn,
              borderLeft: `6px solid ${col(alert.c ?? 'green')}`,
              borderRadius: '6px 22px 22px 22px',
              padding: '14px 18px',
              opacity: Math.min(1, aS * 1.4),
              transform: `translateY(${interpolate(aS, [0, 1], [40, 0])}px)`,
            }}
          >
            <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 22, color: col(alert.c ?? 'green'), marginBottom: 4}}>EN TIEMPO REAL</div>
            <div style={{fontFamily: FONT.ui, fontWeight: 600, fontSize: 26, color: '#E9EDEF', lineHeight: 1.35}}>{alert.t}</div>
          </div>
        ) : null}
      </div>
    </Phone>
  );
};

// ---------------------------------------------------------------- Llamada grabada
const BARS = Array.from({length: 46}, (_, i) => 0.25 + 0.75 * Math.abs(Math.sin(i * 1.7) * Math.cos(i * 0.6 + 1)));

const Call: React.FC<{ins: Ins}> = ({ins}) => {
  const f = useCurrentFrame();
  const p = ins.p ?? {};
  const missed = !!p.missed;
  const advisor = p.advisor ?? 'Diego Herrera';
  const lead = p.lead ?? 'Adriana Solís';
  const prog = clamp01((f - ins.at - 10) / (p.playLen ?? 70));
  const summary: string[] = p.summary ?? ['Quiere visitar el sábado a las 11', 'Presupuesto: 180 mil USD', 'Siguiente paso: mandar ubicación'];
  const attempts: string[] = p.attempts ?? ['Lunes 10:14 · sin llamada', 'Martes · sin llamada', 'Miércoles · sin llamada'];
  return (
    <Shell title={p.title ?? 'Llamadas del equipo'} right={p.right ?? (missed ? 'Nadie le llamó' : 'Grabada desde el CRM')} accent={missed ? C.red : C.purple}>
      <div style={{padding: '24px 30px 30px'}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 18}}>
          <div style={{width: 72, height: 72, borderRadius: 36, background: missed ? C.red : C.purple, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
            <IconPhone size={38} />
          </div>
          <div>
            <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 36, color: C.white}}>{`${advisor.split(' ')[0]} → ${lead}`}</div>
            <div style={{fontFamily: FONT.ui, fontSize: 26, color: C.gray, marginTop: 2}}>{p.when ?? (missed ? 'Lead de hace 3 días' : 'Hoy 11:42 am · 3 min 42 s')}</div>
          </div>
          {!missed ? (
            <div style={{marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: 8}}>
              <div style={{width: 16, height: 16, borderRadius: 8, background: C.red, opacity: Math.floor(f / 12) % 2 ? 0.4 : 1}} />
              <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 24, color: C.red}}>GRABADA</div>
            </div>
          ) : null}
        </div>
        {missed ? (
          <div style={{display: 'flex', flexDirection: 'column', gap: 12, marginTop: 26}}>
            {attempts.map((a, i) => {
              const s = pop(f, ins.at + 8 + i * 6, 30, 15, 0.6);
              return (
                <div key={i} style={{display: 'flex', alignItems: 'center', gap: 14, background: C.panel2, border: `1px solid ${C.line}`, borderRadius: 18, padding: '16px 20px', opacity: Math.min(1, s * 1.4)}}>
                  <div style={{width: 14, height: 14, borderRadius: 7, background: C.red}} />
                  <div style={{fontFamily: FONT.ui, fontWeight: 700, fontSize: 31, color: C.white}}>{a}</div>
                </div>
              );
            })}
            <div style={{display: 'flex', justifyContent: 'center', marginTop: 10, opacity: clamp01((f - ins.at - 30) / 8)}}>
              <Chip text={p.chip ?? 'Lead sin contactar · tú lo ves hoy'} color={C.red} size={28} />
            </div>
          </div>
        ) : (
          <>
            <div style={{display: 'flex', alignItems: 'center', gap: 5, height: 150, marginTop: 26, padding: '0 6px'}}>
              {BARS.map((h, i) => {
                const played = i / BARS.length < prog;
                return <div key={i} style={{flex: 1, height: `${h * 100}%`, borderRadius: 4, background: played ? C.cyan : C.gray2, opacity: played ? 1 : 0.55}} />;
              })}
            </div>
            <div style={{display: 'flex', justifyContent: 'space-between', fontFamily: FONT.ui, fontSize: 23, color: C.gray, marginTop: 6}}>
              <span>{`${Math.floor(prog * 3)}:${String(Math.floor((prog * 222) % 60)).padStart(2, '0')}`}</span>
              <span>3:42</span>
            </div>
            <div style={{marginTop: 20, background: '#0A1018', border: `2px solid ${C.cyan}`, borderRadius: 22, padding: '18px 22px'}}>
              <div style={{display: 'flex', alignItems: 'center', gap: 10, marginBottom: 10}}>
                <Sparkle size={22} />
                <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 25, color: C.cyan, letterSpacing: 1}}>RESUMEN DE LA IA</div>
              </div>
              {summary.map((s, i) => {
                const at = ins.at + 24 + i * 10;
                const o = clamp01((f - at) / 6);
                return (
                  <div key={i} style={{fontFamily: FONT.ui, fontWeight: 600, fontSize: 32, color: C.white, lineHeight: 1.4, opacity: o, transform: `translateX(${(1 - o) * 18}px)`}}>
                    {'• ' + s}
                  </div>
                );
              })}
            </div>
          </>
        )}
      </div>
    </Shell>
  );
};

// ---------------------------------------------------------------- Tareas del asesor
type Task = {t: string; sub?: string; state?: 'new' | 'done' | 'late'; at?: number};

const DEF_TASKS: Task[] = [
  {t: 'Mandar opciones a Lucía Hernández', sub: 'Lo prometió ayer en el chat', state: 'new'},
  {t: 'Llamar a Diana Trejo el martes', sub: 'Ella pidió que la buscaran', state: 'new'},
  {t: 'Confirmar visita de Adriana Solís', sub: 'Sábado 11:00 am', state: 'done'},
];

const LATE_TASKS: Task[] = [
  {t: 'Llamar a Diana Trejo', sub: 'Vencida hace 6 días', state: 'late'},
  {t: 'Mandar opciones a Lucía', sub: 'Vencida hace 9 días', state: 'late'},
  {t: 'Seguimiento a Adriana Solís', sub: 'Nunca se creó', state: 'late'},
];

const Tasks: React.FC<{ins: Ins}> = ({ins}) => {
  const f = useCurrentFrame();
  const p = ins.p ?? {};
  const late = !!p.late;
  const items: Task[] = p.items ?? (late ? LATE_TASKS : DEF_TASKS);
  return (
    <Shell title={p.title ?? `Tareas · ${p.who ?? 'Valeria Ríos'}`} right={p.right ?? (late ? 'Nadie las hace' : 'Creadas por la IA')} accent={late ? C.red : C.green}>
      <div style={{padding: '22px 26px 30px', display: 'flex', flexDirection: 'column', gap: 14}}>
        {items.map((t, i) => {
          const at = t.at ?? ins.at + 6 + i * 7;
          const s = pop(f, at, 30, 15, 0.6);
          const st = t.state ?? 'new';
          const checkAt = at + 22;
          const checked = st === 'done' && f >= checkAt;
          const ck = st === 'done' ? pop(f, checkAt, 30, 12, 0.5) : 0;
          const c = st === 'late' ? C.red : checked ? C.green : C.cyan;
          return (
            <div
              key={i}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 18,
                background: C.panel2,
                border: `1px solid ${C.line}`,
                borderLeft: `8px solid ${c}`,
                borderRadius: 20,
                padding: '18px 20px',
                opacity: Math.min(1, s * 1.4),
                transform: `translateX(${interpolate(s, [0, 1], [60, 0])}px)`,
              }}
            >
              <div
                style={{
                  width: 54,
                  height: 54,
                  borderRadius: 14,
                  border: `3px solid ${c}`,
                  background: checked ? C.green : 'transparent',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  flexShrink: 0,
                  transform: `scale(${checked ? 0.8 + 0.2 * ck : 1})`,
                }}
              >
                {checked ? <IconCheck size={36} color={C.bg} /> : null}
              </div>
              <div style={{flex: 1}}>
                <div style={{fontFamily: FONT.ui, fontWeight: 800, fontSize: 32, color: C.white, textDecoration: checked ? 'line-through' : 'none', lineHeight: 1.2}}>{t.t}</div>
                {t.sub ? <div style={{fontFamily: FONT.ui, fontSize: 25, color: st === 'late' ? C.red : C.gray, marginTop: 4}}>{t.sub}</div> : null}
              </div>
              <Chip text={st === 'late' ? 'Vencida' : checked ? 'Hecha' : 'Nueva'} color={c} size={22} />
            </div>
          );
        })}
      </div>
    </Shell>
  );
};

const KINDS: Record<string, React.FC<{ins: Ins}>> = {crm: Crm, note: Note, cita: Cita, report: Report, call: Call, tasks: Tasks};

// Cuánto tapa un inserto a la escena de fondo (0..1) en el cuadro f.
export const coverOf = (ins: Ins[] | undefined, f: number, dur: number) => {
  let v = 0;
  for (const x of ins ?? []) {
    const to = x.to ?? dur;
    if (f < x.at || f >= to) continue;
    const a = clamp01((f - x.at) / 6);
    const b = to >= dur ? 1 : clamp01((to - f) / 5);
    v = Math.max(v, Math.min(a, b));
  }
  return v;
};

export const InsertLayer: React.FC<{ins: Ins[]; dur: number}> = ({ins, dur}) => {
  const f = useCurrentFrame();
  return (
    <>
      {ins.map((x, i) => {
        const to = x.to ?? dur;
        if (f < x.at || f >= to) return null;
        const Comp = KINDS[x.kind];
        if (!Comp) return null;
        const s = pop(f, x.at, 30, 16, 0.7);
        const out = to >= dur ? 1 : clamp01((to - f) / 5);
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              inset: 0,
              opacity: Math.min(1, s * 1.5) * out,
              transform: `translateY(${interpolate(s, [0, 1], [70, 0])}px) scale(${0.95 + 0.05 * s})`,
            }}
          >
            <Comp ins={x} />
          </div>
        );
      })}
    </>
  );
};
