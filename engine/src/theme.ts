// Marca Lead Master (tema oscuro de la app) y reglas de zona segura IG/TikTok.
export const C = {
  bg: '#060B12',
  panel: '#0D1219',
  panel2: '#111A24',
  line: '#1E2A3A',
  cyan: '#00F0FF',
  purple: '#B24BF3',
  green: '#00E676',
  amber: '#FFB020',
  red: '#FF4D5E',
  white: '#FFFFFF',
  gray: '#9AA7B8',
  gray2: '#5E6B7D',
  wa: '#25D366',
  waDark: '#0B141A',
  waBubbleIn: '#202C33',
  waBubbleOut: '#005C4B',
  meta: '#0866FF',
};

export const GRAD = `linear-gradient(135deg, ${C.purple}, ${C.cyan})`;

// 1080x1920. Instagram Reels y TikTok tapan arriba (~250 px), abajo (~500 px)
// y la columna de botones a la derecha (~140 px en la mitad de abajo).
export const W = 1080;
export const H = 1920;
export const SAFE = {
  top: 250,
  bottom: 1420, // nada importante por debajo de esta línea
  left: 70,
  right: 930, // borde derecho para contenido en la mitad de abajo
  rightTop: 1010, // borde derecho arriba (y < 900)
};

export const FONT = {
  title: 'Bebas Neue, Impact, sans-serif',
  body: 'Poppins, Inter, sans-serif',
  ui: 'Inter, Poppins, sans-serif',
};
