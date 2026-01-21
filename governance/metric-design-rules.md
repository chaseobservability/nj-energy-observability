# Metric Design Rules (Public-Only Observability OS)

**Applies to:** NJ Energy Observability  
**Scope:** Public-data-only, artifact-first, descriptive analytics  
**Explicit exclusions:** Forecasting/nowcasting, recommendations, internal deliberations, incentive design

---

## Purpose

This doctrine prevents the system from becoming:
- a metric graveyard (too many numbers, no meaning),
- a narrative machine (interpretation outruns facts),
- or an accidental incentive mechanism (metrics start being used as targets).

---

## The three-bucket taxonomy (non-negotiable)

Every metric must be classified as one of:
- Reported (visibility only)
- Scorecarded (contextual benchmark to a baseline registry)
- Incentive-linked (deferred; out of scope)

Any metric not in `metrics/metric-catalog.yml` is non-existent for institutional use.

---

## Outcome vs Program

Each metric is tagged as Outcome (system signal) or Program (initiative proxy).  
Default posture: emphasize Outcome metrics. Program metrics require stable public proxies and clear caveats.

---

## Metric admissibility tests

A metric may be included only if it passes:

1) **Definition clarity**: unit, boundary conditions, grain, method, source fields  
2) **Auditability**: reproducible from public sources with recorded query params and versions  
3) **Controllability**: state who can influence it and what exogenous drivers dominate  
4) **Non-perverse incentives**: identify gaming vectors and mitigations  
5) **Customer relevance**: link to affordability, reliability risk hours, or transparency

---

## Baseline discipline

Scorecarded metrics require baseline registry entries.  
Baselines are frozen per cycle; changes require version bump and restatement.

---

## Traceability by design

Every run must emit:
- `out/<PERIOD>/run_manifest.json`

Manifests must include:
- source references
- retrieval timestamps
- query parameters
- pagination details (where applicable)
- row counts and missingness
- code and definition versions

---

## Allowed vs disallowed claims

Every metric must define allowed and disallowed claims.  
Examples of disallowed claims:
- forecasts
- implied causality
- recommendations
- performance judgments

---

## Non-scope fence

This system must not include:
- nonpublic data
- forecasts/nowcasts
- recommended actions
- incentive targets/payouts
- real-time market alerts
- internal deliberations

It is a monitoring + synthesis OS, not a decision engine.
