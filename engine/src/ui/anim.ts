import {Easing, interpolate, spring} from 'remotion';

export const FPS = 30;
export const sec = (s: number) => Math.round(s * FPS);

// Entrada con resorte que arranca en el frame `at`.
export const pop = (frame: number, at: number, fps = FPS, damping = 14, mass = 0.6) =>
  spring({frame: frame - at, fps, config: {damping, mass, stiffness: 180}});

export const fadeIn = (frame: number, at: number, len = 8) =>
  interpolate(frame, [at, at + len], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

export const slide = (frame: number, at: number, dist = 60, len = 12) =>
  interpolate(frame, [at, at + len], [dist, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

export const clamp01 = (v: number) => Math.max(0, Math.min(1, v));
