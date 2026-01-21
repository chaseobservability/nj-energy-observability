---
title: First Live Weekly Brief -- Readiness Checklist (v0.1.1)
---

This checklist should be completed **before** publishing the first live
Weekly Brief based on real public data.

---

## A. Data Access & Ingestion

- [ ] PJM API key active
- [ ] `hrl_load_metered` ingestion working
- [ ] `hourly_marginal_emissions` ingestion working
- [ ] Pagination and rate limits respected
- [ ] Raw data stored privately (not in Git)

---

## B. Traceability

- [ ] `run_manifest.json` generated for the run
- [ ] Source URLs, timestamps, and query parameters recorded
- [ ] Missing data handling documented (if applicable)

---

## C. Metric Governance

- [ ] All rendered metrics are registered in `metrics/metric-catalog.yml`
- [ ] Taxonomy respected:
  - reported vs scorecarded
- [ ] No incentive-linked metrics rendered
- [ ] Baseline id specified if scorecarded metrics are shown

---

## D. Weekly Brief Content

- [ ] Executive Snapshot is factual and short
- [ ] EO1 section references only public artifacts
- [ ] Scorecard Highlights are descriptive (no ranking language)
- [ ] Signals -> Questions contain questions only
- [ ] No "should", "likely", "expect", or "recommend" language

---

## E. Review & Publication

- [ ] Weekly Brief submitted via PR
- [ ] Reviewer confirms guardrails
- [ ] Any warnings or caveats included explicitly
- [ ] File named correctly (`YYYY-MM-DD.md`)

---

## Go / No-Go

- [ ] All checks passed -> Publish
- [ ] Any check failed -> Fix before publishing

The first live weekly brief sets precedent.
Take the extra hour.
