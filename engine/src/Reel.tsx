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
import {Stat} from './scenes/Stat';
import {Quote} from './scenes/Quote';
import {Compare} from './scenes/Compare';
import {Events} from './scenes/Events';
import {Flow} from './scenes/Flow';
import {Bars} from './scenes/Bars';
import {PhoneList} from './scenes/PhoneList';
import {Mock} from './scenes/Mock';
import {Clip} from './scenes/Clip';
import {Dialer} from './scenes/Dialer';
import {BrandBg} from './ui/Bg';
import {coverOf, Ins, InsertLayer} from './ui/Inserts';

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
  stat: Stat,
  quote: Quote,
  compare: Compare,
  events: Events,
  flow: Flow,
  bars: Bars,
  phonelist: PhoneList,
  mock: Mock,
  clip: Clip,
  dialer: Dialer,
  ui: ({dur}) => <BrandBg dur={dur} />, // fondo de marca; el contenido lo ponen los insertos
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
  ins?: Ins[]; // gráficos literales (CRM, nota, cita, reporte...) que entran en la palabra
};

export type ReelProps = {
  id: string;
  totalFrames: number;
  scenes: SceneSpec[];
  words: Word[];
  music?: {src: string; vol: number; from?: number};
  safeDebug?: boolean;
};

// La escena de fondo se apaga y desenfoca mientras un inserto está en pantalla.
const Covered: React.FC<{ins?: Ins[]; dur: number; children: React.ReactNode}> = ({ins, dur, children}) => {
  const f = useCurrentFrame();
  const c = coverOf(ins, f, dur);
  if (c <= 0) return <AbsoluteFill>{children}</AbsoluteFill>;
  return (
    <AbsoluteFill style={{opacity: 1 - 0.78 * c, filter: `blur(${(10 * c).toFixed(1)}px)`, transform: `scale(${1 - 0.04 * c})`}}>{children}</AbsoluteFill>
  );
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
            <Enter>
              <Covered ins={s.ins} dur={s.dur}>{Comp ? <Comp dur={s.dur} p={s.p} /> : null}</Covered>
              {s.ins?.length ? <InsertLayer ins={s.ins} dur={s.dur} /> : null}
            </Enter>
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
      {music ? (
        <Sequence from={music.from ?? 0}>
          <Audio src={staticFile(music.src)} volume={music.vol} loop />
        </Sequence>
      ) : null}
      {safeDebug ? <SafeGuide /> : null}
    </AbsoluteFill>
  );
};
