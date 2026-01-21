# Formatting + Null Handling Spec

## pct(x)
- Input: float in [0,1] or null
- Output: percentage string with <= 1 decimal, drop trailing .0
- Null -> "—"

## Null handling
- Never silently impute.
- Any null renders as "—".
- Confidence downgrades when key inputs missing.

## Rounding
- $/customer-month: 1 decimal
- MW/MWh: whole number unless <100 -> 1 decimal
- tons CO2/MWh: 2 decimals
- correlation: 2 decimals
