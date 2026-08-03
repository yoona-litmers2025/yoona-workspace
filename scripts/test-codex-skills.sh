#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

python3 -m unittest discover \
  -s "$ROOT_DIR/tests/codex-skills" \
  -p 'test_*.py' \
  -v

python3 "$ROOT_DIR/scripts/sync-codex-skills.py" --check
