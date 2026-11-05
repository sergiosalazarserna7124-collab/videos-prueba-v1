import React from 'react';
import {C, FONT} from '../theme';

// Logo Lead Master: cuadro redondeado morado→cian con el ícono de panel.
export const LogoMark: React.FC<{size?: number}> = ({size = 120}) => (
  <svg width={size} height={size} viewBox="0 0 100 100">
    <defs>
      <linearGradient id="lmg" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stopColor={C.purple} />
        <stop offset="1" stopColor={C.cyan} />
      </linearGradient>
    </defs>
    <rect x="0" y="0" width="100" height="100" rx="24" fill="url(#lmg)" />
    <g fill="none" stroke="#fff" strokeWidth="6.5" strokeLinejoin="round">
      <rect x="22" y="22" width="22" height="28" rx="4" />
      <rect x="56" y="22" width="22" height="16" rx="4" />
      <rect x="56" y="50" width="22" height="28" rx="4" />
      <rect x="22" y="62" width="22" height="16" rx="4" />
    </g>
  </svg>
);

export const Logo: React.FC<{size?: number; color?: string}> = ({size = 90, color = C.white}) => (
  <div style={{display: 'flex', alignItems: 'center', gap: size * 0.28}}>
    <LogoMark size={size} />
    <div
      style={{
        fontFamily: FONT.body,
        fontWeight: 800,
        fontSize: size * 0.62,
        color,
        letterSpacing: -1,
        lineHeight: 1,
      }}
    >
      Lead Master
    </div>
  </div>
);
