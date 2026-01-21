# Weekly NJ Electricity System Brief (Public Data Only)
**Week Ending:** {{week_ending_date}}  
**Prepared Using:** Public PJM, IMM, EIA, and NJ public sources  
**Definition Version:** {{definition_version}}  
**Baseline Reference:** {{baseline_id}}

---

## Executive Snapshot (Read Time: ~2 minutes)

- **System posture:** {{reliability_posture | upper}} (contextual, non-forecast)
- **Peak pressure:** {{peak_pressure_trend | upper}} vs prior period
- **Affordability exposure (capacity component):** {{capacity_exposure_summary}}
- **Gas-set exposure in risk hours:** {{gas_marginal_share_top_n | pct}}

> This brief is descriptive and diagnostic.  
> It does not forecast market outcomes or recommend policy actions.

---

## EO1 Implementation Status (Public Milestones)

| Item | Owner | Status | Latest Public Artifact |
|---|---|---|---|
| Residential Universal Bill Credits (RUBCs) | BPU | {{eo1_rubc_status}} | {{eo1_rubc_link}} |
| RGGI Public Statement (30-day) | BPU/DEP/EDA | {{eo1_rggi_status}} | {{eo1_rggi_link}} |
| SBC Review | BPU | {{eo1_sbc_status}} | {{eo1_sbc_link}} |
| NJCEP FY26 True-Up | NJCEP/BPU | {{eo1_njcep_status}} | {{eo1_njcep_link}} |
| Utility Business Model Study (180-day) | BPU | {{eo1_study_status}} | {{eo1_study_link}} |

*Status reflects public documents only; no internal deliberations included.*

---

## Scorecard Highlights (Zone-first, Descriptive)

### Load & Peak (Scorecarded vs Baseline)
- Zones with peak intensity outliers vs baseline: {{zones_peak_outliers}}
- Peak coincidence summary: {{peak_coincidence_summary}}

### Emissions in Risk Hours (Scorecarded)
- Median marginal CO₂ (top-N hours): {{emissions_summary}}
- Dispersion (P25–P75): {{emissions_dispersion_summary}}

### Affordability (Descriptive Exposure)
- Capacity price anchor: {{capacity_price_anchor}}
- Exposure band: {{capacity_exposure_band}}
- Volatility context: {{affordability_volatility_context}}

---

## Signals → Questions (No Decisions)

Each signal is labeled as Outcome or Program per `metrics/metric-catalog.yml`.

- **Outcome:** {{signal_1}}
  - Question: {{question_1}}
- **Outcome:** {{signal_2}}
  - Question: {{question_2}}
- **Program (public proxy):** {{signal_3}}
  - Question: {{question_3}}

*Questions are intended to sharpen inquiry, not to assert conclusions.*

---

## Public Docket / Filings Delta (Since Last Brief)

- PJM postings: {{pjm_updates}}
- FERC dockets: {{ferc_updates}}
- NJ BPU agenda/orders: {{bpu_updates}}

---

## Data & Traceability

- Run manifest: `out/{{period}}/run_manifest.json`
- Metric definitions: `metrics/metric-catalog.yml`
- Baseline registry: `baseline/data-snapshots.yml`
- EO1 milestones: `eo/EO1/eo1-milestones.yml`

---

## Guardrails (Repeat, Explicit)

This brief does not:
- forecast prices or reliability outcomes,
- recommend regulatory actions,
- evaluate utility performance,
- or use nonpublic data.

It is a public-data-based monitoring and synthesis artifact.
