import React from 'react';
import {AbsoluteFill, Easing, interpolate, OffthreadVideo, staticFile, useCurrentFrame} from 'remotion';
import {C, GRAD} from '../theme';
import {BrandBg, NoBgCtx} from '../ui/Bg';

// Videos UGC: la persona habla todo el video (su audio nunca se corta) y encima va el motor.
// Cada tramo tiene un modo:
//   face  -> ella a pantalla completa (con títulos, píldoras, sellos encima)
//   split -> el sistema arriba y ella abajo
//   full  -> gráfico a pantalla completa (ella se sigue oyendo)

export const SPLIT_Y = 960; // alto del panel de arriba en pantalla dividida
export const SPLIT_CAP_Y = 925; // subtítulos sobre la línea divisoria
const HEAD_FACE = 500; // dónde queda la coronilla cuando habla a cámara (deja aire para el título)
const K = 0.72; // escala del contenido del motor dentro del panel de arriba
const TY = 40;
const IN = 9; // cuadros de la transición a pantalla dividida

export type Seg = {from: number; to: number; mode: 'face' | 'split' | 'full'; zoom?: number};
// faceX/faceY: centro de la cara (nariz) y faceTop: coronilla, en coordenadas de 1080x1920 del video.
export type UgcBase = {src: string; faceX: number; faceY: number; faceTop: number; zoom?: number; splitZoom?: number; splitHead?: number; segs: Seg[]; vol?: number};

type Geo = {top: number; x0: number; y0: number; z: number};

const ease = (t: number) => Easing.out(Easing.cubic)(Math.max(0, Math.min(1, t)));
const clamp = (v: number, a: number, b: number) => Math.max(a, Math.min(b, v));

const geoOf = (seg: Seg | undefined, b: UgcBase): Geo => {
  const split = seg?.mode === 'split';
  const z = split ? b.splitZoom ?? 1 : (b.zoom ?? 1.2) * (seg?.zoom ?? 1);
  const top = split ? SPLIT_Y : 0;
  // y de la cara en pantalla: la coronilla queda en HEAD_*; el video siempre cubre su recuadro.
  let ty = (split ? SPLIT_Y + (b.splitHead ?? 40) : HEAD_FACE) + (b.faceY - b.faceTop) * z;
  ty = clamp(ty, 1920 - (1920 - b.faceY) * z, top + b.faceY * z);
  const x0 = clamp(540 - b.faceX * z, 1080 - 1080 * z, 0);
  return {top, x0, y0: ty - b.faceY * z, z};
};

const mix = (a: Geo, b: Geo, t: number): Geo => ({
  top: a.top + (b.top - a.top) * t,
  x0: a.x0 + (b.x0 - a.x0) * t,
  y0: a.y0 + (b.y0 - a.y0) * t,
  z: a.z + (b.z - a.z) * t,
});

export const BaseVideo: React.FC<{base: UgcBase}> = ({base}) => {
  const f = useCurrentFrame();
  const i = Math.max(0, base.segs.findIndex((s) => f >= s.from && f < s.to));
  const seg = base.segs[i];
  const prev = base.segs[i - 1];
  let g = geoOf(seg, base);
  // De cara a pantalla dividida: el video baja mientras el panel del sistema entra desde arriba.
  if (seg && prev && seg.mode === 'split' && prev.mode === 'face') g = mix(geoOf(prev, base), g, ease((f - seg.from) / IN));
  // Empuje lento mientras habla a cámara.
  const push = seg && seg.mode === 'face' ? 1 + 0.035 * ((f - seg.from) / Math.max(1, seg.to - seg.from)) : 1;
  return (
    <AbsoluteFill style={{backgroundColor: C.bg}}>
      <div style={{position: 'absolute', left: 0, right: 0, top: g.top, bottom: 0, overflow: 'hidden'}}>
        <div
          style={{
            position: 'absolute',
            left: 0,
            top: -g.top,
            width: 1080,
            height: 1920,
            transform: `translate(${g.x0}px, ${g.y0}px) scale(${g.z})`,
            transformOrigin: '0 0',
          }}
        >
          <div style={{width: 1080, height: 1920, transform: `scale(${push})`, transformOrigin: `${base.faceX}px ${base.faceY}px`}}>
            <OffthreadVideo src={staticFile(base.src)} volume={base.vol ?? 1} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// Panel de arriba en pantalla dividida. El contenido es una escena del motor (o insertos) a escala,
// sin su fondo: el fondo de marca lo pone el panel.
export const SplitTop: React.FC<{dur: number; enter: boolean; k?: number; ty?: number; children: React.ReactNode}> = ({dur, enter, k = K, ty = TY, children}) => {
  const f = useCurrentFrame();
  const t = enter ? ease(f / IN) : 1;
  const glow = 0.6 + 0.4 * Math.sin(f / 9);
  return (
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: SPLIT_Y, overflow: 'hidden', transform: `translateY(${-(1 - t) * SPLIT_Y}px)`}}>
        <BrandBg dur={dur} force />
        <NoBgCtx.Provider value={true}>
          <div
            style={{
              position: 'absolute',
              left: 0,
              top: 0,
              width: 1080,
              height: 1920,
              transform: `translateY(${ty}px) scale(${k})`,
              transformOrigin: '540px 0px',
              opacity: interpolate(f, [enter ? 4 : 0, enter ? 10 : 1], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
            }}
          >
            {children}
          </div>
        </NoBgCtx.Provider>
        <div style={{position: 'absolute', left: 0, right: 0, bottom: 0, height: 6, background: GRAD, boxShadow: `0 0 ${30 * glow}px ${C.cyan}`}} />
      </div>
      {/* sombra suave sobre ella, debajo de la línea */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: SPLIT_Y,
          height: 120,
          background: 'linear-gradient(180deg, rgba(6,11,18,0.55), rgba(6,11,18,0))',
          opacity: t,
        }}
      />
    </AbsoluteFill>
  );
};
