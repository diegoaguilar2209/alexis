#!/usr/bin/env bash
# Runs a plugin Python script with the available interpreter (python3 or python).
# Usage: run-py.sh <script.py>  (the hook JSON arrives on stdin)
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if command -v python3 >/dev/null 2>&1; then
  PY=python3
elif command -v python >/dev/null 2>&1; then
  PY=python
else
  # Without Python nothing is blocked; warn on stderr.
  echo "alexis: Python not found; safety hooks disabled." >&2
  exit 0
fi
exec "$PY" "$DIR/$1"
