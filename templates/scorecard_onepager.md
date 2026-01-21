# NJ Quarterly Capacity Exposure Scorecard (Internal)
**Period:** {{period}} (ET)  
**Definition Version:** {{definition_version}} (frozen for this cycle)  
**Data Vintage:** {{data_vintage}}  
**Code Version:** {{code_version}}  

**Purpose:** Situational awareness of capacity-driven affordability exposure, reliability posture, and peak-hour emissions risk.  
**Not a forecast. Not a policy recommendation.**

---

## 1) Executive Snapshot (60 seconds)

### A) Capacity Exposure (Affordability Lens)
- **Capacity price anchor:** {{capacity_price_usd_per_mw_day}} $/MW-day ({{capacity_price_source}}, effective {{capacity_price_effective_date}})
- **Statewide capacity exposure (diagnostic):** **${{nj_statewide.capacity_exposure_usd_per_customer_month_point}}/customer-month**
  - Range: **${{nj_statewide.capacity_exposure_usd_per_customer_month_low}}–${{nj_statewide.capacity_exposure_usd_per_customer_month_high}}**
  - Confidence: **{{nj_statewide.capacity_exposure_confidence}}**

### B) Reliability Context (Risk Lens)
- **System posture (proxy):** **{{nj_statewide.reliability_posture | upper}}**
- **Peak pressure trend:** **{{nj_statewide.peak_pressure_trend | upper}}** (vs prior quarter)

### C) Emissions During Peak-Risk Hours
- **Gas marginal exposure (top {{top_hours_n}} hours, statewide):** **{{pct(nj_statewide.gas_marginal_share_top_n_hours)}}**
- **Marginal CO₂ (top {{top_hours_n}} hours, statewide P50):** **{{nj_statewide.marginal_co2_tons_per_mwh_top_n_hours_p50}} tons/MWh**
  - P25–P75: {{nj_statewide.marginal_co2_tons_per_mwh_top_n_hours_p25}} – {{nj_statewide.marginal_co2_tons_per_mwh_top_n_hours_p75}}

---

## 2) Zone Scoreboard (Operational view — no rankings implied)

**Top-hours definition:** Top {{top_hours_n}} hours by **zone metered load** within the quarter (ET).  
**Coincidence metrics:** Compare each zone’s load behavior to PJM RTO load for situational awareness.

| Zone | Qtr Load (MWh) | Peak (MW) | Coincidence (Corr) | Top-N overlap w/ RTO | Gas marginal share (Top-N) | Marginal CO₂ (Top-N P50) | Capacity exposure ($/cust-mo) | Confidence |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| AECO | {{aeco.total_load_mwh}} | {{aeco.peak_load_mw}} | {{aeco.coincidence_corr_with_pjm_rto}} | {{pct(aeco.coincident_top_n_share)}} | {{pct(aeco.gas_marginal_share_top_n_hours)}} | {{aeco.marginal_co2_tons_per_mwh_top_n_hours_p50}} | ${{aeco.capacity_exposure_usd_per_customer_month_point}} | {{aeco.capacity_exposure_confidence}} |
| JCPL | {{jcpl.total_load_mwh}} | {{jcpl.peak_load_mw}} | {{jcpl.coincidence_corr_with_pjm_rto}} | {{pct(jcpl.coincident_top_n_share)}} | {{pct(jcpl.gas_marginal_share_top_n_hours)}} | {{jcpl.marginal_co2_tons_per_mwh_top_n_hours_p50}} | ${{jcpl.capacity_exposure_usd_per_customer_month_point}} | {{jcpl.capacity_exposure_confidence}} |
| PSEG | {{pseg.total_load_mwh}} | {{pseg.peak_load_mw}} | {{pseg.coincidence_corr_with_pjm_rto}} | {{pct(pseg.coincident_top_n_share)}} | {{pct(pseg.gas_marginal_share_top_n_hours)}} | {{pseg.marginal_co2_tons_per_mwh_top_n_hours_p50}} | ${{pseg.capacity_exposure_usd_per_customer_month_point}} | {{pseg.capacity_exposure_confidence}} |
| RECO | {{reco.total_load_mwh}} | {{reco.peak_load_mw}} | {{reco.coincidence_corr_with_pjm_rto}} | {{pct(reco.coincident_top_n_share)}} | {{pct(reco.gas_marginal_share_top_n_hours)}} | {{reco.marginal_co2_tons_per_mwh_top_n_hours_p50}} | ${{reco.capacity_exposure_usd_per_customer_month_point}} | {{reco.capacity_exposure_confidence}} |
| **NJ (Rollup)** | **{{nj_statewide.total_load_mwh}}** | **{{nj_statewide.peak_load_mw}}** | **{{nj_statewide.coincidence_corr_with_pjm_rto}}** | **{{pct(nj_statewide.coincident_top_n_share)}}** | **{{pct(nj_statewide.gas_marginal_share_top_n_hours)}}** | **{{nj_statewide.marginal_co2_tons_per_mwh_top_n_hours_p50}}** | **${{nj_statewide.capacity_exposure_usd_per_customer_month_point}}** | **{{nj_statewide.capacity_exposure_confidence}}** |

**Rollup method:** {{nj_statewide.rollup_method}} across {{nj_statewide.rollup_member_zones}}  
**Rollup weights:** {{nj_statewide.rollup_weights}}  
**Rollup integrity check:** {{nj_statewide.rollup_integrity_check_passed}} {{nj_statewide.rollup_integrity_notes}}

---

## 3) What Changed Since Last Quarter (Max 3 bullets)

- **Peak contribution / load shape:** {{what_changed_1}}
- **Accreditation / effective supply:** {{what_changed_2}}
- **Constraint / price environment:** {{what_changed_3}}

**Guardrail sentence (always):**  
Observed movements in capacity exposure cannot be explained by demand growth alone; peak contribution, accreditation treatment, and constraint sensitivity materially affect outcomes.

---

## 4) Data Provenance (Public Sources)

- **Load:** PJM Data Miner 2 — `hrl_load_metered`
- **Marginal emissions:** PJM Data Miner 2 — `hourly_marginal_emissions`
- **Marginal fuel (gas as marginal):** Monitoring Analytics / PJM IMM — marginal fuel postings
- **Capacity price anchor:** PJM RPM auction results (BRA/IA as specified above)
- **Customer normalization:** EIA (vintage noted above)

---

## 5) Confidence & Limitations

- This scorecard is an **exposure diagnostic**. It does **not** forecast PJM auctions or customer bills.
- Zone-level customer counts may be approximated; confidence reflects allocation fidelity.
- Marginal fuel data may have reporting lag; lag days shown above.
- Emissions metrics focus on **risk-relevant hours** (top {{top_hours_n}} hours) and should not be interpreted as annual inventory averages.
