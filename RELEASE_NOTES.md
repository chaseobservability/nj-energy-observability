# NJ Energy Observability -- Release Notes

## Version
**v0.1.0 -- Structure-Only Release**

## Date
2026-01-20

## Overview
This release establishes the public observability structure for NJ Energy Observability.

It provides schemas, templates, governance rules, and tracking artifacts that define how public electricity system data is processed, classified, and synthesized. It intentionally does not include populated datasets, forecasts, or recommendations.

## Versioning
This project follows Semantic Versioning (SemVer). While pre-1.0, version increments may include breaking changes to structure and naming.

## What's included
- Core code for data pulls and scorecard generation in `src/`, with utility helpers and one-pager rendering
- Config scaffolding for capacity pricing, customers, pnodes, and zones in `config/`
- Templates for scorecards and public one-pagers in `templates/`
- Metric catalog and metric design rules in `metrics/` and `governance/`
- Scope guardrails in `governance/not-in-scope.md`
- Baseline registry skeleton and snapshot index in `baseline/`
- EO1 milestones tracker and public artifacts index in `eo/`
- Weekly brief template for periodic reporting in `reports/weekly/`
- Example outputs and manifests in `out/EXAMPLE_2026Q1/`
- Documentation set for GitHub Pages in `docs/` (architecture, format/nulls, index)
- Open-source hygiene files: LICENSE, code of conduct, disclaimer, and contributing guide

## What's explicitly out of scope
- Nonpublic or confidential data
- Market forecasts or nowcasts
- Policy recommendations
- Utility or program performance evaluations
- Incentive mechanisms or enforcement logic

## Intended use
Transparency and verification of public information, and open collaboration on observability structure and methods. Not an official regulatory instrument.

## Next planned increments
- Wire weekly brief generation to the metric catalog
- Public-data ingestion once API access is live
- Signals-to-questions engine (descriptive only)
