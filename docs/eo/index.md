# Executive Order Tracking

Executive Order Tracking is a public-artifact-first view of major New Jersey energy directives.

This section is designed to make implementation **observable and verifiable** using:
- official Executive Order PDFs,
- publicly posted agency orders, notices, agendas, and reports,
- dated links with retrieval timestamps.

It is intentionally **descriptive**, not prescriptive.

---

## What this section is

- A structured index of Executive Orders relevant to New Jersey electricity system conditions
- A milestones tracker tied to **public artifacts**
- A way to answer: **"What has been published, when, and where can I verify it?"**

---

## What this section is not

This section does not:
- assess effectiveness,
- recommend actions,
- interpret internal intent or strategy,
- include nonpublic or confidential information.

It only tracks what can be verified publicly.

---

## Active Trackers

### EO1 -- Executive Order No. 1
- Official EO PDF: https://www.nj.gov/infobank/eo/057sherrill/pdf/EO-1.pdf
- Human-readable tracker: `/eo/EO1/`
- Generated milestones table: `/eo/EO1.md`

Canonical tracker sources:
- `eo/EO1/eo1-milestones.yml`
- `eo/EO1/eo1-public-artifacts-index.yml`

---

## Adding a new EO tracker

To add EO2/EO3 later:
1. Scaffold the tracker folder and YAML files using the generator:
   - `make new_eo EO=EO2`
2. Fill `meta.source_url` in the new milestones YAML with the official EO PDF link.
3. Render the docs table:
   - `make render_eo EO=EO2`
4. Add the new EO link under "Active Trackers" above.

---

## Integrity & update discipline

- Updates are append-only where possible.
- Links include both:
  - posted date (if known),
  - retrieval date (when captured).
- If an artifact is superseded, the prior link is retained and marked superseded.

This ensures the tracker remains auditable over time.

---

EO Tracking exists to support **clarity over time**, not reaction in the moment.
