// Hoja de contacto: un cuadro por escena (al 75% de cada escena) de uno o varios videos.
// Uso: node tools/sheet.mjs build/<id>.props.json [...más props]  -> build/<id>.sheet/<n>.png
import {bundle} from '@remotion/bundler';
import {renderStill, selectComposition} from '@remotion/renderer';
import fs from 'node:fs';
import path from 'node:path';

const CHROME = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell';
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const serveUrl = await bundle({entryPoint: path.join(root, 'src/index.ts'), publicDir: path.join(root, 'public')});

for (const propsPath of process.argv.slice(2)) {
  const props = JSON.parse(fs.readFileSync(propsPath, 'utf8'));
  const comp = await selectComposition({serveUrl, id: 'Reel', inputProps: props, browserExecutable: CHROME});
  const outDir = path.join(root, 'build', `${props.id}.sheet`);
  fs.mkdirSync(outDir, {recursive: true});
  for (const [i, s] of props.scenes.entries()) {
    const frame = Math.min(props.totalFrames - 1, s.from + Math.floor(s.dur * 0.75));
    await renderStill({composition: comp, serveUrl, output: path.join(outDir, `${String(i).padStart(2, '0')}.png`), frame, inputProps: props, browserExecutable: CHROME, scale: 0.5});
  }
  console.log(`${props.id}: ${props.scenes.length} cuadros`);
}
