import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {C, FONT} from '../theme';
import {Bg} from '../ui/Bg';
import {Phone, StatusBar} from '../ui/Phone';
import {BigTitle, Pill} from '../ui/Text';
import {pop} from '../ui/anim';
import {SAFE} from '../theme';

type Msg = {
  from: 'in' | 'out' | 'system';
  text: string;
  at: number;
  time?: string;
  alert?: boolean;
  translation?: string;
  voice?: string; // duración de nota de voz, ej. "4:12"
};

const Typing: React.FC<{show: boolean}> = ({show}) => {
  const f = useCurrentFrame();
  if (!show) return null;
  return (
    <div style={{alignSelf: 'flex-start', background: C.waBubbleIn, borderRadius: 24, padding: '18px 24px', display: 'flex', gap: 8}}>
      {[0, 1, 2].map((i) => (
        <span
          key={i}
          style={{
            width: 12,
            height: 12,
            borderRadius: 6,
            background: '#8696A0',
            opacity: 0.4 + 0.6 * Math.abs(Math.sin((f / 6) + i)),
          }}
        />
      ))}
    </div>
  );
};

// Chat tipo WhatsApp dentro de un celular. Mensajes con tiempo de entrada en frames.
export const Chat: React.FC<{dur: number; p: any}> = ({dur, p}) => {
  const f = useCurrentFrame();
  const msgs: Msg[] = p.messages ?? [];
  const visible = msgs.filter((m) => f >= m.at);
  const next = msgs.find((m) => f < m.at);
  const typing = next && next.from === 'in' && f >= next.at - 24 && f < next.at;
  const sms = p.style === 'sms';
  const phoneAt: number = p.phoneAt ?? 0;
  const intro = f < phoneAt;
  const blurT = interpolate(f, [phoneAt, phoneAt + 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill>
      <Bg img={p.bg} dur={dur} dim={0.25 + 0.35 * blurT} blur={(p.blur ?? 6) * blurT} drift="in" />
      {p.introLines ? (
        <div style={{position: 'absolute', left: SAFE.left, right: 1080 - SAFE.right, top: SAFE.top + 20, opacity: 1 - blurT}}>
          <BigTitle lines={p.introLines} lineAts={p.introAts} size={p.introSize ?? 120} accent={p.accent ?? C.cyan} />
        </div>
      ) : null}
      {p.label && !intro ? (
        <div style={{position: 'absolute', left: 70, top: 262}}>
          <Pill text={p.label} bg="rgba(255,255,255,0.14)" size={24} />
        </div>
      ) : null}
      {intro ? null : (
      <Phone at={phoneAt} top={p.top ?? 330} height={p.height ?? 860} screenBg={sms ? '#000' : C.waDark}>
        <StatusBar time={p.clock ?? '6:42'} />
        <div
          style={{
            height: 96,
            display: 'flex',
            alignItems: 'center',
            gap: 18,
            padding: '0 26px',
            background: sms ? '#111' : '#1F2C34',
            borderBottom: '1px solid rgba(255,255,255,0.06)',
          }}
        >
          <div style={{width: 62, height: 62, borderRadius: 31, background: p.avatarColor ?? '#6B7C93', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 800, fontSize: 28}}>
            {(p.contact ?? '?').slice(0, 1)}
          </div>
          <div>
            <div style={{color: '#E9EDEF', fontWeight: 700, fontSize: 30}}>{p.contact}</div>
            <div style={{color: '#8696A0', fontSize: 22, marginTop: 2}}>{typing ? 'escribiendo…' : p.sub ?? 'en línea'}</div>
          </div>
        </div>
        <div
          style={{
            position: 'absolute',
            top: 166,
            left: 0,
            right: 0,
            bottom: 0,
            padding: '24px 22px',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'flex-end',
            gap: 14,
            background: sms ? '#000' : '#0B141A',
          }}
        >
          {visible.map((m, i) => {
            const s = pop(f, m.at, 30, 13, 0.5);
            const isIn = m.from === 'in';
            if (m.from === 'system') {
              return (
                <div key={i} style={{alignSelf: 'center', background: '#182229', color: '#8696A0', fontSize: 22, padding: '8px 18px', borderRadius: 12, opacity: s}}>
                  {m.text}
                </div>
              );
            }
            const bubbleBg = sms ? (isIn ? '#26252A' : '#0A84FF') : isIn ? C.waBubbleIn : C.waBubbleOut;
            return (
              <div
                key={i}
                style={{
                  alignSelf: isIn ? 'flex-start' : 'flex-end',
                  maxWidth: '82%',
                  transform: `scale(${interpolate(s, [0, 1], [0.6, 1])})`,
                  transformOrigin: isIn ? 'left bottom' : 'right bottom',
                  opacity: Math.min(1, s * 1.5),
                }}
              >
                <div
                  style={{
                    background: bubbleBg,
                    color: '#E9EDEF',
                    fontSize: m.alert ? 40 : 30,
                    fontWeight: m.alert ? 700 : 500,
                    lineHeight: 1.3,
                    padding: m.alert ? '22px 28px' : '16px 22px',
                    borderRadius: 26,
                    boxShadow: m.alert ? `0 0 0 4px ${C.red}, 0 0 60px ${C.red}AA` : undefined,
                  }}
                >
                  {m.voice ? (
                    <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
                      <div style={{width: 0, height: 0, borderTop: '14px solid transparent', borderBottom: '14px solid transparent', borderLeft: '22px solid #E9EDEF'}} />
                      <div style={{display: 'flex', gap: 4, alignItems: 'center'}}>
                        {Array.from({length: 26}).map((_, k) => (
                          <span key={k} style={{width: 5, height: 8 + ((k * 37) % 30), background: '#8696A0', borderRadius: 3}} />
                        ))}
                      </div>
                      <span style={{fontSize: 24, color: '#8696A0'}}>{m.voice}</span>
                    </div>
                  ) : (
                    m.text
                  )}
                  {m.time ? <div style={{fontSize: 20, color: '#8696A0', textAlign: 'right', marginTop: 6}}>{m.time}</div> : null}
                </div>
                {m.translation ? (
                  <div
                    style={{
                      marginTop: 14,
                      fontFamily: FONT.body,
                      fontWeight: 700,
                      fontSize: 30,
                      color: C.white,
                      background: 'rgba(255,77,94,0.18)',
                      border: `2px solid ${C.red}`,
                      padding: '10px 18px',
                      borderRadius: 16,
                      opacity: Math.min(1, Math.max(0, (f - m.at - 10) / 8)),
                    }}
                  >
                    {m.translation}
                  </div>
                ) : null}
              </div>
            );
          })}
          <Typing show={!!typing} />
        </div>
      </Phone>
      )}
    </AbsoluteFill>
  );
};
