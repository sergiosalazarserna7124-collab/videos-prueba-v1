import React from 'react';
import {C} from '../theme';

type P = {size?: number; color?: string};

export const IconWhatsApp: React.FC<P> = ({size = 64}) => (
  <svg width={size} height={size} viewBox="0 0 64 64">
    <circle cx="32" cy="32" r="30" fill={C.wa} />
    <path
      d="M32 14c-9.9 0-18 7.6-18 17.1 0 3.3 1 6.4 2.7 9L14.6 49l9.2-2.4c2.5 1.3 5.3 2 8.2 2 9.9 0 18-7.6 18-17.1S41.9 14 32 14z"
      fill="#fff"
    />
    <path
      d="M25.5 24.5c.5-1 1-1 1.5-1h1.2c.4 0 .9.1 1.2.9l1.6 3.8c.1.4.1.8-.2 1.1l-1.2 1.4c-.3.3-.3.6-.1 1 1.4 2.4 3.3 4 5.7 5.1.4.2.7.1 1-.2l1.5-1.8c.3-.4.7-.4 1.1-.2l3.6 1.7c.4.2.7.4.7.8 0 1.4-.6 2.9-2 3.6-1.3.7-3.4.9-6.6-.6-3.7-1.7-6.6-5-8.1-7.6-1.3-2.4-1.4-4.6-.9-6z"
      fill={C.wa}
    />
  </svg>
);

export const IconPhone: React.FC<P> = ({size = 48, color = C.white}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z" />
  </svg>
);

export const IconCheck: React.FC<P> = ({size = 40, color = C.green}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
    <polyline points="20 6 9 17 4 12" />
  </svg>
);

export const IconX: React.FC<P> = ({size = 40, color = C.red}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="3" strokeLinecap="round">
    <line x1="18" y1="6" x2="6" y2="18" />
    <line x1="6" y1="6" x2="18" y2="18" />
  </svg>
);

export const IconAlert: React.FC<P> = ({size = 40, color = C.amber}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round">
    <path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z" />
    <line x1="12" y1="9" x2="12" y2="13" />
    <line x1="12" y1="17" x2="12.01" y2="17" />
  </svg>
);

export const IconDoc: React.FC<P> = ({size = 40, color = C.white}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
    <polyline points="14 2 14 8 20 8" />
    <line x1="8" y1="13" x2="16" y2="13" />
    <line x1="8" y1="17" x2="14" y2="17" />
  </svg>
);

export const IconScale: React.FC<P> = ({size = 40, color = C.white}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M12 3v18" />
    <path d="M5 21h14" />
    <path d="M3 7h18" />
    <path d="M6 7l-3 7a3 3 0 0 0 6 0z" />
    <path d="M18 7l-3 7a3 3 0 0 0 6 0z" />
  </svg>
);

export const IconChat: React.FC<P> = ({size = 40, color = C.white}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.6 8.6 0 0 1-3.8-.9L3 21l1.9-5.2A8.4 8.4 0 0 1 12 3a8.5 8.5 0 0 1 9 8.5z" />
  </svg>
);
