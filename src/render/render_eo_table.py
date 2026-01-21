"""
Render EO tracker markdown from YAML (Multi-EO scaffold)
NJ Energy Observability

Public-only, descriptive-only renderer:
- Reads eo/<EO>/eoN-milestones.yml
- Reads eo/<EO>/eoN-public-artifacts-index.yml
- Writes docs/eo/<EO>.md

Guardrails:
- No interpretations
- No internal deliberations
- Links only
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from typing import Any, List, Optional, Tuple

import yaml


def load_yaml(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def iso_today() -> str:
    return dt.date.today().isoformat()


def _safe(value: Any) -> str:
    if value is None or value == "":
        return "--"
    return str(value)


def _status_label(status: Optional[str]) -> str:
    if not status:
        return "--"
    mapping = {
        "not_started": "Pending",
        "in_progress": "In progress",
        "published": "Published",
        "superseded": "Superseded",
    }
    return mapping.get(status, status)


def find_best_artifact_link(artifacts: List[dict], milestone_id: str) -> Optional[str]:
    matches = [a for a in artifacts if a.get("milestone_id") == milestone_id and a.get("url")]
    if not matches:
        return None

    def key(a: dict) -> Tuple[int, str, str]:
        status = a.get("status", "")
        posted = a.get("posted_date") or ""
        retrieved = a.get("retrieved_date") or ""
        return (1 if status == "published" else 0, posted, retrieved)

    matches.sort(key=key, reverse=True)
    return matches[0].get("url")


def render_table_rows(milestones: List[dict], artifacts: List[dict]) -> List[str]:
    rows: List[str] = []
    for m in milestones:
        section = _safe(m.get("eo_section"))
        title = _safe(m.get("title"))
        target_date = _safe(m.get("target_date"))
        owners = m.get("owner_orgs") or []
        owners_str = " / ".join([str(o) for o in owners]) if owners else "--"

        status = _status_label(m.get("status"))
        url = m.get("public_artifact_url") or find_best_artifact_link(artifacts, m.get("id"))
        ref = url if url else "--"

        rows.append(f"| {section} | {title} | {target_date} | {owners_str} | {status} | {ref} |")
    return rows


def render_markdown(eo_code: str, milestones_doc: dict, artifacts_doc: dict) -> str:
    meta = milestones_doc.get("meta", {})
    milestones = milestones_doc.get("milestones", [])
    artifacts = artifacts_doc.get("artifacts", [])

    title = meta.get("title") or f"Executive Order {eo_code}"
    source_url = meta.get("source_url") or "--"
    effective_date = meta.get("effective_date") or "--"
    generated_on = iso_today()

    table_header = [
        "| Section | Milestone | Target Date | Owner(s) | Status | Public Reference |",
        "|--------|----------|-------------|----------|--------|------------------|",
    ]
    table_rows = render_table_rows(milestones, artifacts)

    md: List[str] = []
    md.append(f"# {title} -- Implementation Tracker")
    md.append("")
    md.append(
        "This page presents a **human-readable view** of implementation milestones, "
        "derived entirely from **public artifacts** and maintained in version control."
    )
    md.append("")
    md.append("**Canonical sources:**")
    md.append(f"- Milestones YAML: `eo/{eo_code}/{eo_code.lower()}-milestones.yml`")
    md.append(f"- Public artifacts index: `eo/{eo_code}/{eo_code.lower()}-public-artifacts-index.yml`")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Official Source")
    md.append(f"- Effective date: **{effective_date}**")
    md.append(f"- Official PDF: {source_url}")
    md.append("")
    md.append(f"*This page was generated on {generated_on}.*")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Milestones (Public-Artifact-Based)")
    md.append("")
    md.extend(table_header)
    md.extend(table_rows)
    md.append("")
    md.append("**Status definitions**")
    md.append("- `Pending` -- no public artifact posted yet")
    md.append("- `In progress` -- partial public artifacts exist")
    md.append("- `Published` -- required public artifact posted and linked")
    md.append("- `Superseded` -- replaced by a later public artifact")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Update discipline")
    md.append("- Status is updated **only** when a public document exists and is linked.")
    md.append("- Links should include `posted_date` (if known) and `retrieved_date` in the artifacts index.")
    md.append("- This tracker does not assess effectiveness or recommend actions.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Related")
    md.append("- EO overview: `/docs/eo/`")
    md.append("- Weekly briefs: `/docs/weekly/`")
    md.append("")
    return "\n".join(md)


def default_paths(eo_code: str) -> Tuple[str, str, str]:
    eo_lower = eo_code.lower()
    milestones = f"eo/{eo_code}/{eo_lower}-milestones.yml"
    artifacts = f"eo/{eo_code}/{eo_lower}-public-artifacts-index.yml"
    out = f"docs/eo/{eo_code}.md"
    return milestones, artifacts, out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--eo", required=True, help="EO code like EO1, EO2, EO3")
    ap.add_argument("--milestones", default=None)
    ap.add_argument("--artifacts", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    milestones_path, artifacts_path, out_path = default_paths(args.eo)

    milestones_path = args.milestones or milestones_path
    artifacts_path = args.artifacts or artifacts_path
    out_path = args.out or out_path

    milestones_doc = load_yaml(milestones_path)
    artifacts_doc = load_yaml(artifacts_path)

    md = render_markdown(args.eo, milestones_doc, artifacts_doc)

    ensure_dir(os.path.dirname(out_path))
    with open(out_path, "w") as f:
        f.write(md)

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
