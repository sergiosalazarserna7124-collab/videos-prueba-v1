import {loadFont} from '@remotion/fonts';
import {staticFile} from 'remotion';

const faces: [string, string, string][] = [
  ['Bebas Neue', 'fonts/BebasNeue.woff2', '400'],
  ['Poppins', 'fonts/Poppins-500.woff2', '500'],
  ['Poppins', 'fonts/Poppins-600.woff2', '600'],
  ['Poppins', 'fonts/Poppins-700.woff2', '700'],
  ['Poppins', 'fonts/Poppins-800.woff2', '800'],
  ['Poppins', 'fonts/Poppins-900.woff2', '900'],
  ['Inter', 'fonts/Inter-400.woff2', '400'],
  ['Inter', 'fonts/Inter-500.woff2', '500'],
  ['Inter', 'fonts/Inter-600.woff2', '600'],
  ['Inter', 'fonts/Inter-700.woff2', '700'],
  ['Inter', 'fonts/Inter-800.woff2', '800'],
];

let started = false;
export const loadFonts = () => {
  if (started) return;
  started = true;
  for (const [family, file, weight] of faces) {
    loadFont({family, url: staticFile(file), weight, format: 'woff2'}).catch((e) => console.error(e));
  }
};
