#!/bin/bash
# Экспорт презентации в PDF через системный Google Chrome.
# Запуск: ./export.sh  (или: bash export.sh)
# Ничего устанавливать не нужно — использует установленный Chrome.
cd "$(dirname "$0")"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --virtual-time-budget=6000 \
  --print-to-pdf="Медиацентр_презентация+кейсы.pdf" \
  "file://$(pwd)/index.html" 2>/dev/null
echo "✅ PDF готов: Медиацентр_презентация+кейсы.pdf"
