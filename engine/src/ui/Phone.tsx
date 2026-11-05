import React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {pop} from './anim';

// Marco de celular. Centrado en la zona segura (x 150..930, y 270..1170 por defecto).
export const Phone: React.FC<{
  children: React.ReactNode;
  at?: number;
  top?: number;
  width?: number;
  height?: number;
  left?: number;
  screenBg?: string;
}> = ({children, at = 0, top = 260, width = 640, height = 920, left, screenBg = C.waDark}) => {
  const f = useCurrentFrame();
  const s = pop(f, at, 30, 16, 0.7);
  const x = left ?? (1080 - width) / 2 - 40; // corrido a la izquierda: libre la columna de botones
  return (
    <div
      style={{
        position: 'absolute',
        left: x,
        top,
        width,
        height,
        borderRadius: 64,
        background: '#05070A',
        padding: 16,
        boxShadow: '0 40px 120px rgba(0,0,0,0.65), 0 0 0 2px rgba(255,255,255,0.08) inset',
        transform: `translateY(${interpolate(s, [0, 1], [120, 0])}px) scale(${0.94 + 0.06 * s})`,
        opacity: Math.min(1, s * 1.5),
      }}
    >
      <div
        style={{
          width: '100%',
          height: '100%',
          borderRadius: 50,
          overflow: 'hidden',
          background: screenBg,
          position: 'relative',
          fontFamily: FONT.ui,
        }}
      >
        {children}
        <div
          style={{
            position: 'absolute',
            top: 14,
            left: '50%',
            width: 150,
            height: 38,
            marginLeft: -75,
            borderRadius: 20,
            background: '#000',
          }}
        />
      </div>
    </div>
  );
};

export const StatusBar: React.FC<{time?: string; dark?: boolean}> = ({time = '9:41', dark = true}) => (
  <div
    style={{
      height: 70,
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: '10px 44px 0',
      color: dark ? '#fff' : '#000',
      fontWeight: 700,
      fontSize: 26,
    }}
  >
    <span>{time}</span>
    <span style={{display: 'flex', gap: 8, alignItems: 'center'}}>
      <span style={{width: 34, height: 16, border: `2px solid ${dark ? '#fff' : '#000'}`, borderRadius: 5, display: 'inline-block', position: 'relative'}}>
        <span style={{position: 'absolute', left: 2, top: 2, bottom: 2, width: 22, background: dark ? '#fff' : '#000', borderRadius: 2}} />
      </span>
    </span>
  </div>
);
