#!/usr/bin/env bash
set -euo pipefail

# Wrapper around the Python pull scripts.
# Usage:
#   ./scripts/pull_period.sh 2026Q1 2026-01-01T00:00:00 2026-04-01T00:00:00

PERIOD=${1:?PERIOD required (e.g., 2026Q1)}
START=${2:?START required (e.g., 2026-01-01T00:00:00)}
END=${3:?END required (e.g., 2026-04-01T00:00:00)}

if [[ ! -d .venv ]]; then
  echo ".venv not found. Run: make install"
  exit 1
fi

source .venv/bin/activate
python -m src.pull_dataminer --period "$PERIOD" --start "$START" --end "$END"
python -m src.pull_imm --period "$PERIOD" --start "$START" --end "$END"

echo "Pull complete. Raw data in raw/"
