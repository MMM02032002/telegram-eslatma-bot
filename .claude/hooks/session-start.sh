#!/bin/bash
set -euo pipefail

# Faqat Claude Code on the web (bulut) sessiyalarida ishlaydi
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# Tizim paketlaridan ajratilgan virtual muhit (tizimdagi cryptography buzilgan bo'lishi mumkin)
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
fi
.venv/bin/pip install --quiet --disable-pip-version-check -r requirements.txt pyflakes

if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"$CLAUDE_PROJECT_DIR/.venv/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi
