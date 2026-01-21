#!/usr/bin/env bash
set -euo pipefail

# Render docs pages for all EO trackers found under eo/EO*
#
# Assumes:
# - eo/<EO>/eoN-milestones.yml
# - eo/<EO>/eoN-public-artifacts-index.yml
# and writes:
# - docs/eo/<EO>.md
#
# Usage:
#   bash scripts/render_all_eos.sh
#
# Optional env:
#   VENV_ACTIVATE=".venv/bin/activate"  (default)
#   PYTHON_MODULE="src.render.render_eo_table" (default)

VENV_ACTIVATE="${VENV_ACTIVATE:-.venv/bin/activate}"
PYTHON_MODULE="${PYTHON_MODULE:-src.render.render_eo_table}"

if [[ ! -f "${VENV_ACTIVATE}" ]]; then
  echo "ERROR: venv activate script not found at ${VENV_ACTIVATE}"
  echo "Run: make install"
  exit 1
fi

# shellcheck disable=SC1090
source "${VENV_ACTIVATE}"

rendered=0
skipped=0

shopt -s nullglob
for d in eo/EO*; do
  [[ -d "$d" ]] || continue
  eo_code="$(basename "$d")"
  eo_lower="$(echo "$eo_code" | tr '[:upper:]' '[:lower:]')"

  milestones="${d}/${eo_lower}-milestones.yml"
  artifacts="${d}/${eo_lower}-public-artifacts-index.yml"

  if [[ ! -f "${milestones}" || ! -f "${artifacts}" ]]; then
    echo "SKIP ${eo_code}: missing ${milestones} or ${artifacts}"
    skipped=$((skipped+1))
    continue
  fi

  echo "RENDER ${eo_code}"
  python -m "${PYTHON_MODULE}" --eo "${eo_code}"
  rendered=$((rendered+1))
done

echo "Done. Rendered=${rendered} Skipped=${skipped}"

if [[ "${rendered}" -eq 0 ]]; then
  echo "ERROR: No EO docs rendered. Check eo/EO*/eoN-*.yml files."
  exit 2
fi
