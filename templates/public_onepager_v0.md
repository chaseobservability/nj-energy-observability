# New Jersey Electricity Capacity Exposure — Quarterly Snapshot
**Period:** {{period}} (ET)  
**Purpose:** Informational snapshot of capacity-related cost exposure, reliability posture, and peak-hour emissions context.

---

## What this snapshot shows (at a glance)

### Affordability (Capacity Component Only)
- **Capacity price anchor:** {{capacity_price_usd_per_mw_day}} $/MW-day (PJM auction result)
- **Estimated capacity exposure:** **${{nj_statewide.capacity_exposure_usd_per_customer_month_point}} per customer per month**
  - Range: ${{nj_statewide.capacity_exposure_usd_per_customer_month_low}}–${{nj_statewide.capacity_exposure_usd_per_customer_month_high}}

> This reflects exposure to capacity market outcomes under current assumptions. It is not a full customer bill and not a forecast.

---

### Reliability Context
- **System posture (proxy):** **{{nj_statewide.reliability_posture | upper}}**
- **Peak pressure trend:** **{{nj_statewide.peak_pressure_trend | upper}}** relative to the prior quarter

> Reliability posture reflects publicly reported system adequacy signals and planning context.

---

### Emissions During Peak-Risk Hours
- **Gas as marginal resource (peak hours):** **{{pct(nj_statewide.gas_marginal_share_top_n_hours)}}**
- **Marginal CO₂ emissions (peak hours):** **{{nj_statewide.marginal_co2_tons_per_mwh_top_n_hours_p50}} tons/MWh**

> These values describe emissions during the hours most relevant to system stress and costs, not annual averages.

---

## Data Sources
- PJM Interconnection — market and operational data
- PJM Monitoring Analytics (IMM) — marginal fuel information
- U.S. Energy Information Administration — customer and sales statistics

## Important limitations
- This snapshot does **not** predict future auction results or customer bills.
- Zone-level diagnostics inform internal analysis; statewide values are shown here for clarity.
- Emissions metrics focus on peak-risk hours and should not be compared directly to annual inventory totals.
