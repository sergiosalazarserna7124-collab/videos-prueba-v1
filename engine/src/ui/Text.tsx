import React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {pop} from './anim';

// "UN MENSAJE. UNA [DEMANDA]." -> la parte entre corchetes va en color de acento.
export const Rich: React.FC<{text: string; accent?: string}> = ({text, accent = C.cyan}) => {
  const parts = text.split(/(\[[^\]]+\])/g).filter(Boolean);
  return (
    <>
      {parts.map((p, i) =>
        p.startsWith('[') ? (
          <span key={i} style={{color: accent}}>
            {p.slice(1, -1)}
          </span>
        ) : (
          <span key={i}>{p}</span>
        ),
      )}
    </>
  );
};

// Título grande estilo gancho: cada línea entra con un resorte.
export const BigTitle: React.FC<{
  lines: string[];
  at?: number; // frame de entrada
  stagger?: number;
  size?: number;
  accent?: string;
  align?: 'left' | 'center';
  shadow?: boolean;
  lineAts?: number[]; // frames por línea (opcional)
}> = ({lines, at = 0, stagger = 5, size = 128, accent = C.cyan, align = 'left', shadow = true, lineAts}) => {
  const f = useCurrentFrame();
  return (
    <div style={{display: 'flex', flexDirection: 'column', alignItems: align === 'center' ? 'center' : 'flex-start'}}>
      {lines.map((l, i) => {
        const a = lineAts?.[i] ?? at + i * stagger;
        const s = pop(f, a);
        const y = interpolate(s, [0, 1], [40, 0]);
        return (
          <div
            key={i}
            style={{
              fontFamily: FONT.title,
              fontSize: size,
              lineHeight: 0.95,
              color: C.white,
              letterSpacing: 1,
              opacity: Math.min(1, s * 1.4),
              transform: `translateY(${y}px) scale(${0.92 + 0.08 * s})`,
              transformOrigin: align === 'center' ? 'center' : 'left center',
              textShadow: shadow ? '0 6px 30px rgba(0,0,0,0.65)' : undefined,
              textAlign: align,
            }}
          >
            <Rich text={l} accent={accent} />
          </div>
        );
      })}
    </div>
  );
};

// Etiqueta tipo píldora.
export const Pill: React.FC<{text: string; bg?: string; color?: string; size?: number; style?: React.CSSProperties}> = ({
  text,
  bg = C.red,
  color = C.white,
  size = 30,
  style,
}) => (
  <div
    style={{
      display: 'inline-flex',
      alignItems: 'center',
      gap: 10,
      background: bg,
      color,
      fontFamily: FONT.body,
      fontWeight: 800,
      fontSize: size,
      letterSpacing: 2,
      padding: `${size * 0.32}px ${size * 0.7}px`,
      borderRadius: 999,
      textTransform: 'uppercase',
      ...style,
    }}
  >
    {text}
  </div>
);
