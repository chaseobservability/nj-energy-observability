# Pull Request: NJ Energy Observability

Thank you for contributing to **NJ Energy Observability**.

This project is an **independent, public-data-based observability system**.
All contributions must respect the project's guardrails.

Please complete the sections below.

---

## Summary

**What does this PR change or add?**  
(1-3 sentences, factual description only.)

---

## Type of Contribution
(Check all that apply.)

- [ ] Documentation / clarification
- [ ] Metric definition or refinement
- [ ] Governance / baseline / methodology
- [ ] Template or artifact structure
- [ ] Bug fix
- [ ] Other (explain below)

---

## Data Sources Used

- [ ] Public PJM data
- [ ] Public federal or state data (EIA, EPA, NJ public filings)
- [ ] No data (structure / documentation only)

**List sources and links (if applicable):**

---

## Metric Governance (Required if metrics are involved)

- [ ] I have registered or updated the metric in `metrics/metric-catalog.yml`
- [ ] The metric taxonomy is explicitly defined:
  - [ ] reported
  - [ ] scorecarded
  - [ ] incentive_linked_deferred
- [ ] Allowed and disallowed claims are specified
- [ ] Baseline requirements are defined (if scorecarded)

---

## Guardrails Checklist (Required)

Please confirm all of the following:

- [ ] This PR uses **public data only**
- [ ] This PR introduces **no forecasts or predictions**
- [ ] This PR introduces **no recommendations or prescribed actions**
- [ ] This PR does **not** evaluate or rank utilities or programs
- [ ] This PR does **not** include nonpublic or confidential information
- [ ] This PR respects the `governance/not-in-scope.md` boundaries

---

## Repo Integrity (Required)

- [ ] I did NOT commit `raw/`, `stage/`, `.env*`, API keys, or parquet files
- [ ] If I changed any `eo/**` YAML, I ran `make render_all_eos` and committed `docs/eo/*.md`
- [ ] If I changed `docs/**`, I confirmed the docs build should succeed

---

## Traceability & Reproducibility

- [ ] Any derived artifacts include clear source references
- [ ] Any new transformations are described at a high level
- [ ] No raw datasets or API keys are included

---

## Rationale (Optional)

If helpful, explain:
- why this change improves observability,
- what ambiguity it reduces,
- or what misuse it prevents.

Avoid policy arguments.

---

## Reviewer Notes

Anything you want reviewers to pay special attention to?

---

## Acknowledgement

By submitting this PR, I acknowledge that:
- NJ Energy Observability is independent and non-official
- Contributions may be accepted, modified, or declined to preserve project guardrails
