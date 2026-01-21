#!/usr/bin/env bash
set -euo pipefail

# Small one-day pull to quickly inspect real field names.
# Usage:
#   ./scripts/pull_samples_1day.sh 2026-01-01

DAY=${1:?Provide YYYY-MM-DD}
START="${DAY}T00:00:00"
NEXT_DAY=$(
DAY="$DAY" python3 - <<'PY'
import datetime as dt
import os

day = os.environ["DAY"]
next_day = dt.datetime.strptime(day, "%Y-%m-%d").date() + dt.timedelta(days=1)
print(next_day.isoformat())
PY
)
END="${NEXT_DAY}T00:00:00"
PERIOD="SAMPLE_${DAY}"

./scripts/pull_period.sh "$PERIOD" "$START" "$END"

echo "Now inspect raw/dataminer/${PERIOD}/hrl_load_metered_ALL.json"
echo "and raw/dataminer/${PERIOD}/hourly_marginal_emissions_ALL.json"
