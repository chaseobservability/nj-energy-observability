# Weekly Brief Renderer

**Project:** NJ Energy Observability  
**Status:** Spec (v0.1.1 target)  
**Guardrails:** Public data only; descriptive only; no forecasts; no recommendations.

This document defines how the Weekly Brief is generated from:
- scorecard outputs,
- the metric catalog taxonomy,
- the baseline registry,
- and EO trackers.

The key principle:

> **The renderer does not decide what to show. The metric catalog decides.**

---

## 1) Purpose

The Weekly Brief Renderer produces a reviewable markdown artifact:

- `reports/weekly/YYYY-MM-DD.md`

It converts public signals into:
- descriptive summaries, and
- structured questions (not conclusions),

with full traceability.

---

## 2) Inputs (required)

### A) Metric Catalog
- `metrics/metric-catalog.yml`

Used for:
- taxonomy (reported vs scorecarded)
- output field mapping
- allowed/disallowed claims

### B) Baseline Registry
- `baseline/data-snapshots.yml`
- (and a referenced baseline definition file in `baseline/baselines/`)

Used only for:
- scorecarded metric contextualization (percentiles/bands)

### C) Scorecard Output
- `out/<PERIOD>/scorecard_all.json`

The renderer must be able to operate on:
- zone rows (AECO, JCPL, PSEG, RECO)
- statewide row (NJ_STATEWIDE)

### D) EO1 Trackers
- `eo/EO1/eo1-milestones.yml`
- `eo/EO1/eo1-public-artifacts-index.yml`

Used for:
- factual status table
- links only (no interpretation)

---

## 3) Output (required)

### Weekly Brief Artifact
- `reports/weekly/YYYY-MM-DD.md`

Required sections:
1. Executive Snapshot (short)
2. EO1 Implementation Status (public artifacts only)
3. Scorecard Highlights (zone-first, descriptive)
4. Signals -> Questions (no decisions)
5. Public Docket Delta (optional; placeholder OK)
6. Data & Traceability (explicit references)

---

## 4) Taxonomy-driven rendering rules (non-negotiable)

Each metric in `metrics/metric-catalog.yml` has a `taxonomy`:

### A) reported
Render:
- value (current)
- optional directional trend vs prior period (if available)

Do NOT render:
- baseline percentiles
- implicit benchmarking language

### B) scorecarded
Render:
- value (current)
- baseline context:
  - percentile band (preferred): p50 / p90 / p95 or p25/p50/p75
  - or rank-within-baseline (optional)

Baseline must be:
- explicitly referenced by baseline id (e.g., BASELINE-2025Q4)

### C) incentive_linked_deferred
Do NOT render.
This repo does not publish incentive-linked logic.

---

## 5) Baseline behavior

A metric may only be rendered as scorecarded if:
- its catalog entry indicates baseline use is required, and
- a baseline snapshot exists in `baseline/data-snapshots.yml`.

If missing:
- downgrade to "reported" behavior for that run (value only), and
- add a brief note in the Traceability section:
  - "Baseline missing for metric X; rendered as reported."

No baseline changes mid-cycle:
- baseline id used must be recorded in the brief header.

---

## 6) Zone-first behavior

The Weekly Brief must be zone-first:

- Render AECO, JCPL, PSEG, RECO first
- NJ_STATEWIDE is a rollup summary second

Avoid "ranking" tone:
- do not label zones as best/worst
- use "outlier vs baseline" language only, and only for scorecarded metrics

---

## 7) Signals -> Questions engine (safe mode)

Signals -> Questions is generated from **scorecarded** metrics only.

### Trigger condition (descriptive)
A metric is a "signal" if the current value is:
- above the baseline p90, or
- below the baseline p10,
or comparable extreme rule defined in the catalog.

### Output requirement
Each signal must be translated into a **question**, never a conclusion.

Template:
- **Signal (Outcome/Program):** <factual statement>
- **Question:** <clarifying inquiry>

Examples:
- Signal: "PSEG coincident top-N share is in the top decile of baseline."
  Question: "Is this change driven by weather anomalies, or by persistent constraint patterns visible in public PJM data?"

### Hard exclusions
Signals -> Questions must not include:
- "should"
- "recommend"
- "likely"
- "will"
- "forecast"
- "action"

---

## 8) Traceability requirements

Every Weekly Brief must include:

- Period and definition_version
- Baseline id (if used)
- Link/path to:
  - `out/<PERIOD>/run_manifest.json`
  - metric catalog file
  - EO tracker files

If the renderer transforms data:
- it must log the transformation at a high level in the brief footer.

---

## 9) Suggested minimal module layout (implementation target)

This spec anticipates a python module like:

- `src/render/render_weekly_brief.py`

with functions:
- `load_metric_catalog(path) -> catalog`
- `load_baseline_registry(path) -> registry`
- `load_scorecard(path) -> records`
- `render_weekly_brief(context) -> markdown`
- `emit_signals_to_questions(context) -> list[questions]`

The renderer should be deterministic given inputs.

---

## 10) Non-scope fence (repeat)

This renderer must not:
- forecast prices or reliability outcomes
- recommend actions
- evaluate utilities or programs
- ingest nonpublic data
- send real-time alerts

It produces a **reviewable descriptive artifact** only.
