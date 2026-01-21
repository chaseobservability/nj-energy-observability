# NJ Energy Observability -- Roadmap

This roadmap describes the planned evolution of NJ Energy Observability following
the **v0.1.0 structure-only release**.

All future work will continue to respect the project's core guardrails:
- public data only
- descriptive, not prescriptive
- no forecasts or recommendations
- artifact-first, reviewable outputs

---

## v0.1.0 -- Structure-Only (Released)

**Status:** Released  
**Tag:** v0.1.0

Established the foundational observability system:
- zone-first scorecard kernel
- metric taxonomy and design rules
- baseline registry scaffolding
- weekly brief templates
- EO1 public-artifact tracker
- traceability and open-source governance

This release intentionally contains **no populated datasets**.

---

## v0.1.1 -- First Live Signals (Planned)

**Goal:**  
Move from static structure to **live, reproducible observability** using public data,
without introducing forecasting or recommendations.

The first live weekly brief will be published only after
the First Live Weekly Brief Readiness Checklist is satisfied.

EO tracker docs are auto-rendered from YAML and enforced by CI.

### Scope

#### 1. Metric-Governed Weekly Brief Generation
- Wire the weekly brief renderer to `metrics/metric-catalog.yml`
- Rendering behavior determined entirely by metric taxonomy:
  - `reported` -> value + trend
  - `scorecarded` -> value + baseline context
  - `incentive_linked_deferred` -> excluded
- Baseline context pulled from `baseline/data-snapshots.yml`

#### 2. Signals-to-Questions Engine (Minimal)
- Generate structured **questions**, not conclusions
- Tag each question as:
  - outcome-level
  - program-level (public proxy only)
- No thresholds implying action

#### 3. Public Data Ingestion (When API Access Is Live)
- Enable PJM Data Miner ingestion for:
  - `hrl_load_metered`
  - `hourly_marginal_emissions`
- Enforce pagination, rate limits, and manifests
- Raw data stored privately; manifests and derived artifacts public

#### 4. First Live Weekly Brief
- Produced entirely from public data
- Includes EO1 status, scorecard highlights, and signals->questions
- Fully traceable via run manifests

---

## v0.1.2 -- Expanded Context (Optional)

Potential additions (subject to guardrails):
- Hourly LMP feeds for descriptive congestion/volatility context
- Expanded EO tracking (if new executive actions issued)
- Additional public watchlists (PJM/FERC/NJBPU)

Explicitly excluded:
- dashboards as primary output
- alerts
- forecasting models
- incentive logic

---

## v0.2.0 -- Multi-State / Fork-Ready (Exploratory)

If adopted or forked by others:
- support for additional states or zones
- shared observability conventions
- cross-repo comparison via common metric catalog patterns

This phase will require additional governance discussion.

---

## Change Control

All roadmap changes:
- must preserve public-only posture
- must not weaken metric governance
- must not imply official endorsement or authority
