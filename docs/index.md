---
title: NJ Energy Observability
---

**Independent, public-data-based observability of New Jersey's electricity system.**

NJ Energy Observability is an open-source project that makes New Jersey's electricity system more observable using
**publicly available data** and **reproducible methods**.

This project is **not** an official product of:
- the State of New Jersey,
- the New Jersey Board of Public Utilities,
- PJM Interconnection,
- or any electric utility or market participant.

---

This site reflects the latest published artifacts as of 2026-02-02.

---

## Source Code

This project is fully open source.

- **GitHub Repository:**  
  [https://github.com/chaseobservability/nj-energy-observability](https://github.com/chaseobservability/nj-energy-observability)

Issues and pull requests are welcome, subject to the project's public-data
and non-prescriptive guardrails.

---

## What this project is

- A **descriptive observability system**, not a forecasting or optimization model
- A collection of **verifiable artifacts** (scorecards, briefs, trackers)
- A **public reference implementation** for monitoring complex energy systems transparently
- A place where engineers, analysts, and stakeholders can **inspect, challenge, and improve the structure** of how information is processed

All outputs are derived from **public sources only** and can be independently reproduced.

---

## What this project is not

- Not a market forecast
- Not a policy recommendation engine
- Not an official regulatory scorecard
- Not a performance evaluation of any utility, program, or actor
- Not a repository of nonpublic or confidential data

Interpretation and use of the outputs are the responsibility of the reader.

---

## Core artifacts

- **Quarterly Scorecard**  
  Zone-first (`AECO`, `JCPL`, `PSEG`, `RECO`) with a statewide rollup, focused on exposure and risk-relevant hours.

- **Metric Catalog & Design Rules**  
  A formal taxonomy that governs what metrics mean, how they can be used, and what claims are explicitly disallowed.

- **Baseline Registry**  
  Locked historical reference sets to prevent baseline drift and post-hoc reinterpretation.

- **Weekly Briefs**  
  PR-based, reviewable synthesis artifacts that turn public signals into structured questions -- not conclusions.

- **EO1 Tracker**  
  A public-artifact-first tracker for Executive Order No. 1 implementation milestones.

---

## Transparency & traceability

Every generated artifact is accompanied by:
- source references
- retrieval timestamps
- query parameters
- transformation summaries
- version identifiers

The goal is **trust through inspectability**, not authority.

---

## Contributions

Issues and pull requests are welcome via GitHub. The maintainer reserves the right to decline contributions that:
- introduce nonpublic data,
- embed forecasts or recommendations,
- or violate the project's observability guardrails.

See `CONTRIBUTING.md` and `governance/not-in-scope.md`.
