# Architecture Overview

NJ Energy Observability is designed as a **layered observability system**.
Each layer has a distinct purpose and a strict boundary.

This separation is intentional.

---

## High-level structure

```
Public Data Sources
        |
        v
Ingestion & Traceability
        |
        v
Scorecard Kernel
        |
        v
Governance & Meaning
        |
        v
Synthesis & Cadence
```

---

## Layer 1 — Public Data Sources

**Purpose:** Define the authoritative sources of truth.

Examples:
- PJM Data Miner public feeds
- Monitoring Analytics (PJM IMM) public postings
- U.S. EIA public datasets
- New Jersey public orders, notices, and filings

**Rules**
- Public sources only
- No scraping where prohibited
- No enrichment with nonpublic data

This layer answers:  
**“Where does the data come from?”**

---

## Layer 2 — Ingestion & Traceability

**Purpose:** Preserve provenance and prevent silent data loss.

Artifacts:
- Raw data pulls (stored privately, not committed)
- Normalized staging tables
- Per-run manifests capturing:
  - source URLs
  - retrieval timestamps
  - query parameters
  - pagination details
  - row counts
  - code and definition versions

This layer answers:  
**“What exactly was pulled, and when?”**

---

## Layer 3 — Scorecard Kernel

**Purpose:** Produce stable, reproducible descriptive outputs.

Artifacts:
- Quarterly zone-first scorecards
- Statewide rollups
- Onepager templates
- Exposure and risk-hour diagnostics

Characteristics:
- Deterministic
- Reproducible
- Public-data-based
- Non-prescriptive

This layer answers:  
**“What happened, in a structured way?”**

---

## Layer 4 — Governance & Meaning

**Purpose:** Constrain interpretation and prevent misuse.

Artifacts:
- Metric catalog
- Metric design rules
- Baseline registry
- Explicit “not in scope” doctrine

This layer answers:  
**“How should these numbers be interpreted — and how should they not?”**

---

## Layer 5 — Synthesis & Cadence

**Purpose:** Maintain awareness without reactivity.

Artifacts:
- Weekly briefs (PR-based)
- Executive Order trackers
- Public docket and filings watchlists

Characteristics:
- Reviewable
- Non-real-time
- Question-oriented (not decision-oriented)

This layer answers:  
**“What deserves attention next?”**

---

## Public vs private boundary

| Public (this repository) | Private (outside this repository) |
|--------------------------|-----------------------------------|
| Public data              | Nonpublic information             |
| Reproducible metrics     | Internal deliberations            |
| Questions                | Decisions                         |
| Artifacts                | Opinions                          |

This boundary is strict and intentional.

---

## Why this architecture works

- It scales without central authority
- It invites scrutiny rather than resisting it
- It separates observation from action
- It survives leadership and political change

**Observability precedes accountability.**
