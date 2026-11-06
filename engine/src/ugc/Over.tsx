import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT, GRAD, SAFE} from '../theme';
import {BigTitle, Pill} from '../ui/Text';
import {Logo, LogoMark} from '../ui/Logo';
import {IconCheck, IconX} from '../ui/Icons';
import {pop} from '../ui/anim';
import {colorOf} from '../scenes/Stack';
import {Stamp} from '../scenes/PhotoTitle';

// Lo que va encima de ella cuando habla a cámara (modo face). Todo opcional:
//   lines/lineAts/kicker -> gancho o frase grande arriba (2 líneas, palabra clave entre [ ])
//   pills   -> lista de píldoras arriba a la izquierda: [{t, at, icon: 'x'|'check'|'q'|'dot'|'num', color}]
//   row     -> píldoras en fila (países, etiquetas): [{t, at, color}]
//   stamp   -> sello {text, at, top, color}
//   logo    -> {at, top}: logo de Lead Master
//   step    -> {n, t, at}: número de paso grande + título
//   big     -> {text, sub, at, top}: número o palabra enorme
//   cta     -> {top, button, at}: cierre de anuncio con botón y flecha

type PillT = {t: string; at: number; icon?: 'x' | 'check' | 'q' | 'dot' | 'num'; color?: string};

const Shade: React.FC<{h?: number; o?: number}> = ({h = 900, o = 0.85}) => (
  <div
    style={{
      position: 'absolute',
      left: 0,
      right: 0,
      top: 0,
      height: h,
      background: `linear-gradient(180deg, rgba(6,11,18,${o}) 0%, rgba(6,11,18,${o * 0.55}) 45%, rgba(6,11,18,0) 100%)`,
    }}
  />
);

const IconQ: React.FC<{size?: number; color?: string}> = ({size = 34, color = C.amber}) => (
  <div style={{fontFamily: FONT.title, fontSize: size * 1.25, color, lineHeight: 1, paddingTop: 4}}>?</div>
);

const PillRow: React.FC<{p: PillT; i: number; f: number}> = ({p, i, f}) => {
  const s = pop(f, p.at, 30, 14, 0.6);
  if (f < p.at) return null;
  const icon = p.icon ?? 'x';
  const col = colorOf(p.color ?? (icon === 'check' ? 'green' : icon === 'q' ? 'amber' : icon === 'dot' ? 'cyan' : icon === 'num' ? 'cyan' : 'red'));
  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: 18,
        alignSelf: 'flex-start',
        background: 'rgba(13,18,25,0.93)',
        border: `2px solid ${col}66`,
        borderRadius: 22,
        padding: '12px 26px 12px 12px',
        boxShadow: `0 18px 50px rgba(0,0,0,0.5), 0 0 30px ${col}22`,
        opacity: Math.min(1, s * 1.5),
        transform: `translateX(${interpolate(s, [0, 1], [-90, 0])}px) scale(${0.9 + 0.1 * s})`,
        transformOrigin: 'left center',
      }}
    >
      <div
        style={{
          width: 52,
          height: 52,
          borderRadius: 14,
          background: `${col}26`,
          border: `2px solid ${col}`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          flexShrink: 0,
        }}
      >
        {icon === 'check' ? (
          <IconCheck size={32} color={col} />
        ) : icon === 'q' ? (
          <IconQ color={col} />
        ) : icon === 'num' ? (
          <div style={{fontFamily: FONT.title, fontSize: 44, color: col, paddingTop: 4}}>{i + 1}</div>
        ) : icon === 'dot' ? (
          <div style={{width: 20, height: 20, borderRadius: 10, background: col}} />
        ) : (
          <IconX size={30} color={col} />
        )}
      </div>
      <div style={{fontFamily: FONT.body, fontWeight: 700, fontSize: 38, color: C.white, lineHeight: 1.15, whiteSpace: 'nowrap'}}>{p.t}</div>
    </div>
  );
};

export const Over: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const out = interpolate(f, [dur - 4, dur], [1, 0.85], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const pills: PillT[] = p.pills ?? [];
  const row: PillT[] = p.row ?? [];
  const hasTop = !!(p.lines || pills.length || p.step || p.logo || p.cta || p.big);
  const titleTop = p.titleTop ?? SAFE.top + 20;
  return (
    <AbsoluteFill style={{opacity: out}}>
      {hasTop && p.shade !== false ? <Shade h={p.shadeH ?? (p.cta ? 1150 : 860)} o={p.shadeO ?? 0.82} /> : null}

      {p.lines ? (
        <div style={{position: 'absolute', left: 60, right: 60, top: titleTop, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
          {p.kicker ? (
            <div style={{marginBottom: 20, opacity: Math.min(1, pop(f, p.kickerAt ?? 0) * 1.4)}}>
              <Pill text={p.kicker} bg={colorOf(p.kickerColor ?? 'cyan')} color={C.bg} size={28} />
            </div>
          ) : null}
          <BigTitle lines={p.lines} lineAts={p.lineAts} at={p.at ?? 0} size={p.size ?? 118} accent={colorOf(p.accent ?? 'cyan')} />
        </div>
      ) : null}

      {pills.length ? (
        <div style={{position: 'absolute', left: SAFE.left, right: 60, top: p.pillsTop ?? (p.lines ? 560 : SAFE.top + 30), display: 'flex', flexDirection: 'column', gap: 14}}>
          {pills.map((x, i) => (
            <PillRow key={i} p={x} i={i} f={f} />
          ))}
        </div>
      ) : null}

      {row.length ? (
        <div style={{position: 'absolute', left: 50, right: 50, top: p.rowTop ?? 560, display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: 16}}>
          {row.map((x, i) => {
            const s = pop(f, x.at, 30, 13, 0.6);
            if (f < x.at) return null;
            const col = colorOf(x.color ?? 'cyan');
            return (
              <div
                key={i}
                style={{
                  fontFamily: FONT.body,
                  fontWeight: 800,
                  fontSize: 38,
                  color: C.white,
                  background: 'rgba(13,18,25,0.93)',
                  border: `2px solid ${col}`,
                  borderRadius: 999,
                  padding: '12px 30px',
                  boxShadow: `0 0 30px ${col}33`,
                  opacity: Math.min(1, s * 1.5),
                  transform: `translateY(${interpolate(s, [0, 1], [40, 0])}px) scale(${0.85 + 0.15 * s})`,
                }}
              >
                {x.t}
              </div>
            );
          })}
        </div>
      ) : null}

      {p.big ? (() => {
        const s = pop(f, p.big.at ?? 0, 30, 11, 0.7);
        if (f < (p.big.at ?? 0)) return null;
        return (
          <div style={{position: 'absolute', left: 0, right: 0, top: p.big.top ?? 300, display: 'flex', flexDirection: 'column', alignItems: 'center', opacity: Math.min(1, s * 1.5), transform: `scale(${interpolate(s, [0, 1], [0.6, 1])})`}}>
            <div style={{fontFamily: FONT.title, fontSize: p.big.size ?? 230, lineHeight: 0.9, color: colorOf(p.big.color ?? 'cyan'), textShadow: `0 0 60px ${colorOf(p.big.color ?? 'cyan')}55, 0 8px 30px rgba(0,0,0,0.6)`}}>{p.big.text}</div>
            {p.big.sub ? <div style={{fontFamily: FONT.title, fontSize: p.big.subSize ?? 84, color: C.white, lineHeight: 1, marginTop: 6, textShadow: '0 6px 24px rgba(0,0,0,0.6)'}}>{p.big.sub}</div> : null}
          </div>
        );
      })() : null}

      {p.logo ? (() => {
        const at = p.logo.at ?? 0;
        const s = pop(f, at, 30, 13, 0.6);
        if (f < at) return null;
        return (
          <div style={{position: 'absolute', left: 0, right: 0, top: p.logo.top ?? SAFE.top + 20, display: 'flex', justifyContent: 'center'}}>
            <div
              style={{
                background: 'rgba(13,18,25,0.93)',
                border: `1px solid ${C.line}`,
                borderRadius: 36,
                padding: '22px 40px',
                boxShadow: `0 20px 60px rgba(0,0,0,0.55), 0 0 60px ${C.purple}33`,
                opacity: Math.min(1, s * 1.5),
                transform: `translateY(${interpolate(s, [0, 1], [-40, 0])}px) scale(${0.85 + 0.15 * s})`,
              }}
            >
              <Logo size={p.logo.size ?? 84} />
            </div>
          </div>
        );
      })() : null}

      {p.step ? (() => {
        const at = p.step.at ?? 0;
        const s = pop(f, at, 30, 12, 0.7);
        const s2 = pop(f, at + 5, 30, 14, 0.6);
        return (
          <div style={{position: 'absolute', left: 60, right: 60, top: p.step.top ?? SAFE.top + 10, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
            <div
              style={{
                width: 190,
                height: 190,
                borderRadius: 95,
                background: GRAD,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontFamily: FONT.title,
                fontSize: 150,
                color: C.white,
                paddingTop: 12,
                boxShadow: `0 0 80px ${C.cyan}66, 0 20px 50px rgba(0,0,0,0.5)`,
                opacity: Math.min(1, s * 1.5),
                transform: `scale(${interpolate(s, [0, 1], [0.3, 1])}) rotate(${interpolate(s, [0, 1], [-30, 0])}deg)`,
              }}
            >
              {p.step.n}
            </div>
            <div style={{marginTop: 26, opacity: Math.min(1, s2 * 1.4), transform: `translateY(${interpolate(s2, [0, 1], [30, 0])}px)`}}>
              <BigTitle lines={p.step.lines ?? [p.step.t]} at={at + 5} size={p.step.size ?? 104} accent={C.cyan} />
            </div>
          </div>
        );
      })() : null}

      {p.cta ? (() => {
        const at = p.cta.at ?? 0;
        const a = pop(f, at, 30, 15, 0.7);
        const b = pop(f, at + 6, 30, 10, 0.8);
        const c = pop(f, at + 12);
        const pulse = 1 + 0.035 * Math.sin(f / 5);
        const bob = 14 * Math.sin(f / 4);
        return (
          <>
            <div style={{position: 'absolute', left: 60, right: 60, top: p.cta.top ?? SAFE.top + 10, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
              <div
                style={{
                  background: 'rgba(13,18,25,0.93)',
                  border: `1px solid ${C.line}`,
                  borderRadius: 30,
                  padding: '16px 32px',
                  opacity: Math.min(1, a * 1.4),
                  transform: `translateY(${interpolate(a, [0, 1], [-30, 0])}px)`,
                }}
              >
                <Logo size={64} />
              </div>
              {p.cta.lines ? (
                <div style={{marginTop: 26}}>
                  <BigTitle lines={p.cta.lines} at={at + 4} size={p.cta.size ?? 104} accent={C.cyan} />
                </div>
              ) : null}
            </div>
            <div style={{position: 'absolute', left: 0, right: 0, top: p.cta.buttonTop ?? 990, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
              <div
                style={{
                  fontFamily: FONT.body,
                  fontWeight: 800,
                  fontSize: 54,
                  color: C.bg,
                  background: C.cyan,
                  padding: '22px 50px',
                  borderRadius: 999,
                  transform: `scale(${interpolate(b, [0, 1], [0.5, 1]) * pulse})`,
                  opacity: Math.min(1, b * 1.4),
                  boxShadow: `0 0 80px ${C.cyan}88, 0 20px 50px rgba(0,0,0,0.5)`,
                  textAlign: 'center',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 16,
                }}
              >
                <LogoMark size={52} />
                {p.cta.button ?? 'Dale clic abajo'}
              </div>
              <svg width="84" height="84" viewBox="0 0 24 24" style={{marginTop: 18, opacity: c, transform: `translateY(${bob}px)`, filter: 'drop-shadow(0 4px 12px rgba(0,0,0,0.6))'}}>
                <path d="M12 4v14M5 11l7 7 7-7" fill="none" stroke={C.cyan} strokeWidth="2.8" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </div>
          </>
        );
      })() : null}

      {p.stamp ? <Stamp text={p.stamp.text} at={p.stamp.at ?? 0} top={p.stamp.top ?? 860} color={colorOf(p.stamp.color ?? 'red')} size={p.stamp.size ?? 96} rot={p.stamp.rot ?? -8} /> : null}
    </AbsoluteFill>
  );
};
