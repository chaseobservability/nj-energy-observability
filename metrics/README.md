# Metrics Overview & Taxonomy

This directory defines what metrics exist, what they mean, and how they may be used within NJ Energy Observability.

Authoritative sources:
- Metric definitions: `metrics/metric-catalog.yml`
- Design doctrine: `governance/metric-design-rules.md`

If a metric is not registered in the catalog, it does not exist for institutional use.

---

## Metric taxonomy (three buckets)

### 1) Reported (visibility only)
Descriptive; no benchmark implied; no judgment implied.

### 2) Scorecarded (context to baseline)
Compared to a locked historical reference distribution. Still descriptive — not a target.

### 3) Incentive-linked (deferred)
Explicitly out of scope. Placeholder only.

---

## Outcome vs Program signals

Each metric is tagged as:
- Outcome: system-level signals (load shape, peaks, emissions in risk hours, etc.)
- Program: initiative-level proxies (EE/DR, interconnection timelines, etc.)

This distinction prevents metric sprawl and accidental program evaluation.

---

## Allowed vs disallowed claims

Every metric must declare:
- Allowed claims: what can safely be said
- Disallowed claims: what must never be implied (forecasts, causality, recommendations)

---

## Adding or modifying metrics

To add a metric:
1. Register it in `metrics/metric-catalog.yml`
2. Define unit, cadence, source, and computation
3. Assign taxonomy and signal type
4. Declare allowed and disallowed claims
5. Specify baseline requirements (if scorecarded)

Metrics should not be added ad hoc in code or reports.
