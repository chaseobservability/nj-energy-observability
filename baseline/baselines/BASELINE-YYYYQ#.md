# Baseline Definition: BASELINE-YYYYQ#
**Status:** Active  
**Registry Version:** v1.0  
**Applies To:** Scorecarded metrics only (see metric-catalog.yml)

---

## Purpose
This baseline defines the historical reference distribution used to contextualize scorecarded metrics.

It exists to prevent baseline drift and preserve comparability across quarters.
It does not imply targets, incentives, or performance judgments.

---

## Baseline Period
- Quarters included: YYYYQ# → YYYYQ#
- Total periods: N

---

## Zones Covered
- AECO
- JCPL
- PSEG
- RECO
- NJ_STATEWIDE

---

## Metrics Covered
(As defined in `metrics/metric-catalog.yml`)

---

## Method Summary
- Metrics computed using frozen definitions for the baseline construction cycle.
- Top-N hour definitions frozen per `config/zones.json`.
- No imputation of missing hours; exclusions documented.

---

## Change Control
- This baseline may not be modified mid-cycle.
- If superseded, create a new baseline file and restate historical comparisons.

---

## Non-Scope
This baseline does not define performance targets or incentive mechanisms.
