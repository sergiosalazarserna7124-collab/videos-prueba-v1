import React from 'react';
import {AbsoluteFill, Audio, interpolate, Sequence, staticFile, useCurrentFrame} from 'remotion';
import {loadFonts} from './fonts';
import {C, SAFE} from './theme';
import {Captions, Word} from './ui/Captions';
import {News} from './scenes/News';
import {Chat} from './scenes/Chat';
import {PhotoTitle} from './scenes/PhotoTitle';
import {Case} from './scenes/Case';
import {FloatChats} from './scenes/FloatChats';
import {Stack} from './scenes/Stack';
import {Panel} from './scenes/Panel';
import {Cta} from './scenes/Cta';

loadFonts();

const SCENES: Record<string, React.FC<{dur: number; p: any}>> = {
  news: News,
  chat: Chat,
  photo: PhotoTitle,
  case: Case,
  floatchats: FloatChats,
  stack: Stack,
  panel: Panel,
  cta: Cta,
};

export type SceneSpec = {
  type: string;
  from: number;
  dur: number;
  p: any;
  audio?: string;
  audioFrom?: number; // frames de retraso del audio dentro de la escena
  sfx?: {src: string; at: number; vol?: number}[];
  captions?: boolean;
};

export type ReelProps = {
  id: string;
  totalFrames: number;
  scenes: SceneSpec[];
  words: Word[];
  music?: {src: string; vol: number};
  safeDebug?: boolean;
};

// Entrada corta de cada escena: corte con un poco de desenfoque (sin zoom fuerte).
const Enter: React.FC<{children: React.ReactNode}> = ({children}) => {
  const f = useCurrentFrame();
  const blur = interpolate(f, [0, 5], [10, 0], {extrapolateRight: 'clamp'});
  const op = interpolate(f, [0, 4], [0.3, 1], {extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{filter: blur > 0.1 ? `blur(${blur}px)` : undefined, opacity: op}}>{children}</AbsoluteFill>;
};

const SafeGuide: React.FC = () => (
  <AbsoluteFill style={{pointerEvents: 'none'}}>
    <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: SAFE.top, background: 'rgba(255,0,0,0.25)'}} />
    <div style={{position: 'absolute', left: 0, right: 0, top: SAFE.bottom, bottom: 0, background: 'rgba(255,0,0,0.25)'}} />
    <div style={{position: 'absolute', left: SAFE.right, right: 0, top: 900, bottom: 0, background: 'rgba(255,160,0,0.25)'}} />
    <div style={{position: 'absolute', left: 0, width: SAFE.left, top: 0, bottom: 0, background: 'rgba(255,160,0,0.18)'}} />
  </AbsoluteFill>
);

export const Reel: React.FC<ReelProps> = ({scenes, words, music, safeDebug}) => {
  const hidden: [number, number][] = scenes
    .filter((s) => s.captions === false)
    .map((s) => [s.from / 30, (s.from + s.dur) / 30]);
  return (
    <AbsoluteFill style={{backgroundColor: C.bg}}>
      {scenes.map((s, i) => {
        const Comp = SCENES[s.type];
        return (
          <Sequence key={i} from={s.from} durationInFrames={s.dur} name={`${i + 1}-${s.type}`}>
            <Enter>{Comp ? <Comp dur={s.dur} p={s.p} /> : null}</Enter>
            {s.audio ? (
              <Sequence from={s.audioFrom ?? 0}>
                <Audio src={staticFile(s.audio)} volume={1} />
              </Sequence>
            ) : null}
            {(s.sfx ?? []).map((x, k) => (
              <Sequence key={k} from={Math.max(0, x.at)}>
                <Audio src={staticFile(x.src)} volume={x.vol ?? 0.18} />
              </Sequence>
            ))}
          </Sequence>
        );
      })}
      <Captions words={words} hidden={hidden} />
      {music ? <Audio src={staticFile(music.src)} volume={music.vol} loop /> : null}
      {safeDebug ? <SafeGuide /> : null}
    </AbsoluteFill>
  );
};
