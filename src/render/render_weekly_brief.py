"""
Weekly Brief Renderer (Scaffold)
NJ Energy Observability

Public-only, descriptive-only renderer that wires the weekly brief to:
- metrics/metric-catalog.yml (taxonomy)
- baseline/data-snapshots.yml (baseline registry)
- out/<PERIOD>/scorecard_all.json (scorecard outputs)
- eo/EO1/* (EO1 tracker files)

Guardrails:
- No forecasts/nowcasts
- No recommendations
- No nonpublic data
- Signals -> Questions only (no conclusions)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import yaml
from jinja2 import Environment, FileSystemLoader

# -----------------------------
# Helpers
# -----------------------------


def _load_yaml(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def _load_json(path: str) -> Any:
    with open(path, "r") as f:
        return json.load(f)


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _pct(x: Optional[float]) -> str:
    if x is None:
        return "--"
    val = round(float(x) * 100.0, 1)
    if val.is_integer():
        return f"{int(val)}%"
    return f"{val}%"


def _to_float(x: Any) -> Optional[float]:
    try:
        if x is None:
            return None
        return float(x)
    except Exception:
        return None


def _iso_today() -> str:
    return dt.date.today().isoformat()


# -----------------------------
# Catalog structures
# -----------------------------


@dataclass(frozen=True)
class MetricDef:
    id: str
    name: str
    taxonomy: str  # reported | scorecarded | incentive_linked_deferred
    signal_type: str  # outcome | program
    domain: str
    output_field: Optional[str] = None
    output_fields: Optional[List[str]] = None
    baseline_required: bool = False


@dataclass
class RenderedMetric:
    metric_id: str
    name: str
    taxonomy: str
    domain: str
    value: Any
    value_str: str
    baseline_context: Optional[str] = None


# -----------------------------
# Loading + normalization
# -----------------------------


def load_metric_catalog(path: str) -> List[MetricDef]:
    cat = _load_yaml(path)
    raw_metrics = cat.get("metrics", [])
    out: List[MetricDef] = []

    for m in raw_metrics:
        taxonomy = m.get("taxonomy")
        metric_id = m.get("id")
        name = m.get("name", metric_id)
        signal_type = m.get("signal_type", "outcome")
        domain = m.get("domain", "misc")

        output_field = m.get("output_field")
        output_fields = m.get("output_fields")
        baseline_required = bool(m.get("baseline_use", {}).get("required", False))

        out.append(
            MetricDef(
                id=metric_id,
                name=name,
                taxonomy=taxonomy,
                signal_type=signal_type,
                domain=domain,
                output_field=output_field,
                output_fields=output_fields,
                baseline_required=baseline_required,
            )
        )

    return out


def load_baseline_registry(path: str, baseline_id: str) -> dict:
    reg = _load_yaml(path)
    snaps = reg.get("snapshots", [])
    for s in snaps:
        if s.get("id") == baseline_id:
            return s
    return {"id": baseline_id, "missing": True}


def load_scorecard_all(path: str) -> List[dict]:
    data = _load_json(path)
    if isinstance(data, dict) and "records" in data:
        return data["records"]
    if isinstance(data, dict):
        return []
    if isinstance(data, list):
        return data
    raise ValueError("Unexpected scorecard_all.json shape; expected list or {records: [...]}")


def index_scorecard_by_zone(records: List[dict]) -> Dict[str, dict]:
    idx: Dict[str, dict] = {}
    for r in records:
        zid = r.get("zone_id") or r.get("zone") or r.get("ZoneId")
        if zid:
            idx[str(zid)] = r
    return idx


# -----------------------------
# Rendering logic (taxonomy-aware)
# -----------------------------


def render_metrics_for_zone(
    zone_record: dict,
    metrics: List[MetricDef],
    baseline_snapshot: dict,
) -> Tuple[List[RenderedMetric], List[str]]:
    """
    Returns:
      - rendered metrics list (reported + scorecarded)
      - warnings list (missing baseline, missing fields, etc.)
    """
    rendered: List[RenderedMetric] = []
    warnings: List[str] = []

    for m in metrics:
        if m.taxonomy == "incentive_linked_deferred":
            continue

        if m.output_field:
            val = zone_record.get(m.output_field)
            if val is None:
                continue
            val_str = format_value(m, val)
            rm = RenderedMetric(m.id, m.name, m.taxonomy, m.domain, val, val_str)

            if m.taxonomy == "scorecarded":
                if baseline_snapshot.get("missing"):
                    rm.taxonomy = "reported"
                    warnings.append(
                        f"Baseline missing for metric {m.id}; rendered as reported."
                    )
                elif m.baseline_required:
                    rm.baseline_context = f"Baseline: {baseline_snapshot.get('id')} (context pending)"
                else:
                    warnings.append(
                        f"{m.id} is scorecarded but baseline not marked required in catalog."
                    )
            rendered.append(rm)

        elif m.output_fields:
            vals = {f: zone_record.get(f) for f in m.output_fields}
            if all(v is None for v in vals.values()):
                continue
            val_str = ", ".join(
                [f"{k}={format_value(m, v)}" for k, v in vals.items() if v is not None]
            )
            rm = RenderedMetric(m.id, m.name, m.taxonomy, m.domain, vals, val_str)
            if m.taxonomy == "scorecarded":
                if baseline_snapshot.get("missing"):
                    rm.taxonomy = "reported"
                    warnings.append(
                        f"Baseline missing for metric {m.id}; rendered as reported."
                    )
                elif m.baseline_required:
                    rm.baseline_context = f"Baseline: {baseline_snapshot.get('id')} (context pending)"
            rendered.append(rm)
        else:
            warnings.append(f"Metric {m.id} has no output_field(s); cannot render.")
            continue

    return rendered, warnings


def format_value(metric: MetricDef, val: Any) -> str:
    if val is None:
        return "--"
    if isinstance(val, (int, float)):
        if metric.domain in ("peak", "load") and abs(float(val)) >= 100:
            return f"{float(val):,.0f}"
        if metric.domain == "emissions":
            return f"{float(val):.2f}"
        if metric.domain == "fuel":
            if 0.0 <= float(val) <= 1.0:
                return _pct(float(val))
        if metric.domain == "affordability":
            return f"{float(val):.1f}"
        return f"{float(val):.3g}"
    return str(val)


# -----------------------------
# Signals -> Questions (safe mode)
# -----------------------------


@dataclass
class SignalQuestion:
    signal_type: str  # outcome/program
    signal: str
    question: str


def generate_signals_to_questions(
    zone_id: str,
    rendered_metrics: List[RenderedMetric],
) -> List[SignalQuestion]:
    """
    Minimal safe mode:
    - Only considers scorecarded metrics.
    - No thresholds yet (baseline percentiles not implemented).
    - Emits conservative, clarifying questions based on presence of scorecarded metrics.
    """
    out: List[SignalQuestion] = []
    for rm in rendered_metrics:
        if rm.taxonomy != "scorecarded":
            continue

        sig = f"{zone_id}: {rm.name} = {rm.value_str}"
        q = (
            "What observable public factors (weather, constraints, or load-shape shifts) "
            "could explain movement in this metric relative to its baseline distribution?"
        )
        out.append(SignalQuestion(signal_type="outcome", signal=sig, question=q))

    return out[:5]


# -----------------------------
# EO1 rendering helpers
# -----------------------------


def load_eo1_milestones(path: str) -> dict:
    return _load_yaml(path)


def load_eo1_artifacts_index(path: str) -> dict:
    return _load_yaml(path)


# -----------------------------
# Weekly brief render
# -----------------------------


def render_weekly_brief_markdown(
    template_path: str,
    context: dict,
) -> str:
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path) or "."))
    env.filters["pct"] = _pct
    tpl = env.get_template(os.path.basename(template_path))
    return tpl.render(**context)


# -----------------------------
# CLI
# -----------------------------


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", required=True, help="Quarter period label (e.g., 2026Q1)")
    ap.add_argument("--week-ending", default=_iso_today(), help="YYYY-MM-DD")
    ap.add_argument("--baseline-id", default="BASELINE-2025Q4", help="Baseline snapshot id")
    ap.add_argument("--metric-catalog", default="metrics/metric-catalog.yml")
    ap.add_argument("--baseline-registry", default="baseline/data-snapshots.yml")
    ap.add_argument("--scorecard-all", default=None, help="Path to out/<PERIOD>/scorecard_all.json")
    ap.add_argument("--eo1-milestones", default="eo/EO1/eo1-milestones.yml")
    ap.add_argument("--eo1-artifacts", default="eo/EO1/eo1-public-artifacts-index.yml")
    ap.add_argument("--template", default="reports/weekly/weekly-brief-template.md")
    ap.add_argument(
        "--out",
        default=None,
        help="Output markdown path (default reports/weekly/YYYY-MM-DD.md)",
    )
    args = ap.parse_args()

    scorecard_all_path = args.scorecard_all or f"out/{args.period}/scorecard_all.json"
    out_path = args.out or f"reports/weekly/{args.week_ending}.md"

    metrics = load_metric_catalog(args.metric_catalog)
    baseline_snapshot = load_baseline_registry(args.baseline_registry, args.baseline_id)

    records = load_scorecard_all(scorecard_all_path)
    by_zone = index_scorecard_by_zone(records)

    zone_order = ["AECO", "JCPL", "PSEG", "RECO", "NJ_STATEWIDE"]
    zone_views = []
    all_questions: List[SignalQuestion] = []
    warnings_all: List[str] = []
    if not records:
        warnings_all.append("No scorecard records found; output placeholders only.")

    for zid in zone_order:
        zr = by_zone.get(zid)
        if not zr:
            continue
        rendered, warnings = render_metrics_for_zone(zr, metrics, baseline_snapshot)
        warnings_all.extend([f"{zid}: {w}" for w in warnings])
        questions = generate_signals_to_questions(zid, rendered)
        all_questions.extend(questions)

        zone_views.append(
            {
                "zone_id": zid,
                "metrics": rendered,
            }
        )

    eo1 = load_eo1_milestones(args.eo1_milestones)
    eo1_index = load_eo1_artifacts_index(args.eo1_artifacts)

    reliability_posture = (by_zone.get("NJ_STATEWIDE") or {}).get(
        "reliability_posture", "unknown"
    )
    peak_pressure_trend = (by_zone.get("NJ_STATEWIDE") or {}).get(
        "peak_pressure_trend", "unknown"
    )
    gas_marginal_share_top_n = _to_float(
        (by_zone.get("NJ_STATEWIDE") or {}).get("gas_marginal_share_top_n_hours")
    )

    capacity_exposure_point = (by_zone.get("NJ_STATEWIDE") or {}).get(
        "capacity_exposure_usd_per_customer_month_point"
    )
    capacity_exposure_low = (by_zone.get("NJ_STATEWIDE") or {}).get(
        "capacity_exposure_usd_per_customer_month_low"
    )
    capacity_exposure_high = (by_zone.get("NJ_STATEWIDE") or {}).get(
        "capacity_exposure_usd_per_customer_month_high"
    )

    capacity_exposure_summary = "--"
    if capacity_exposure_point is not None:
        capacity_exposure_summary = f"${float(capacity_exposure_point):.1f}/cust-mo"
        if capacity_exposure_low is not None and capacity_exposure_high is not None:
            capacity_exposure_summary += (
                f" (band ${float(capacity_exposure_low):.1f}–"
                f"${float(capacity_exposure_high):.1f})"
            )

    context = {
        "week_ending_date": args.week_ending,
        "definition_version": os.getenv("DEFINITION_VERSION", "v1.0"),
        "baseline_id": args.baseline_id,
        "reliability_posture": reliability_posture,
        "peak_pressure_trend": peak_pressure_trend,
        "capacity_exposure_summary": capacity_exposure_summary,
        "gas_marginal_share_top_n": gas_marginal_share_top_n,
        "pct": _pct,
        "eo1_rubc_status": "pending",
        "eo1_rubc_link": None,
        "eo1_sbc_status": "pending",
        "eo1_sbc_link": None,
        "eo1_njcep_status": "pending",
        "eo1_njcep_link": None,
        "eo1_rggi_status": "pending",
        "eo1_rggi_link": None,
        "eo1_study_status": "pending",
        "eo1_study_link": None,
        "zones_peak_outliers": "--",
        "peak_coincidence_summary": "--",
        "emissions_summary": "--",
        "emissions_dispersion_summary": "--",
        "capacity_price_anchor": "--",
        "capacity_exposure_band": "--",
        "affordability_volatility_context": "--",
        "signal_1": all_questions[0].signal if len(all_questions) > 0 else "--",
        "question_1": all_questions[0].question if len(all_questions) > 0 else "--",
        "signal_2": all_questions[1].signal if len(all_questions) > 1 else "--",
        "question_2": all_questions[1].question if len(all_questions) > 1 else "--",
        "signal_3": all_questions[2].signal if len(all_questions) > 2 else "--",
        "question_3": all_questions[2].question if len(all_questions) > 2 else "--",
        "pjm_updates": "--",
        "ferc_updates": "--",
        "bpu_updates": "--",
        "_zone_views": zone_views,
        "_warnings": warnings_all,
        "_eo1": eo1,
        "_eo1_index": eo1_index,
        "period": args.period,
    }

    md = render_weekly_brief_markdown(args.template, context)

    _ensure_dir(os.path.dirname(out_path))
    with open(out_path, "w") as f:
        f.write(md)

    print(f"Wrote weekly brief: {out_path}")
    if warnings_all:
        print("Warnings (non-fatal):")
        for w in warnings_all[:20]:
            print(f" - {w}")


if __name__ == "__main__":
    main()
