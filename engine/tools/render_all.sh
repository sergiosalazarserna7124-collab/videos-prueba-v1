#!/usr/bin/env bash
# Renderiza todos los videos cuyas voces ya estén en public/tts/ y que todavía no existan en ../videos/.
# Uso: bash tools/render_all.sh   (deja una línea OK/FALTA/FALLO por video)
cd "$(dirname "$0")/.." || exit 1
for spec in videos/*.json; do
  id=$(basename "$spec" .json)
  case "$id" in _*|v01) continue ;; esac
  out=../videos/$id.mp4
  [ -f "$out" ] && [ -f "../videos/$id-celular.mp4" ] && continue
  missing=$(python3 - "$spec" <<'EOF'
import json, os, sys
s = json.load(open(sys.argv[1]))
if 'ugc' in s:  # UGC: la voz es la del video de ella
    print(0 if os.path.exists(os.path.join('public', s['ugc']['src'])) else 1)
else:
    print(sum(1 for sc in s['scenes'] if not os.path.exists(f"public/tts/{sc['key']}.json")))
EOF
)
  if [ "$missing" != "0" ]; then echo "FALTA_VOZ $id ($missing escenas)"; continue; fi
  if python3 tools/build.py "$spec" > "build/render_$id.log" 2>&1; then
    ffmpeg -v error -y -i "$out" -c:v libx264 -crf 25 -preset slow -maxrate 3M -bufsize 6M \
      -c:a aac -b:a 160k -movflags +faststart "../videos/$id-celular.mp4"
    echo "OK $id $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out")"
  else
    echo "FALLO $id"
  fi
done
echo "RENDER_ALL_TERMINADO"
