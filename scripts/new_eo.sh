#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   scripts/new_eo.sh EO2 "Executive Order No. 2" "https://example.com/EO-2.pdf" "2026-02-01"
#
# Notes:
# - Title/URL/Effective date can be left blank and filled later.
# - This script scaffolds:
#   eo/<EO>/eoN-milestones.yml
#   eo/<EO>/eoN-public-artifacts-index.yml
#   eo/<EO>/README.md
#   docs/eo/<EO>.md (generated placeholder; renderer will overwrite later)

EO_CODE="${1:-}"
EO_TITLE="${2:-}"
EO_URL="${3:-}"
EO_EFFECTIVE="${4:-}"

if [[ -z "${EO_CODE}" ]]; then
  echo "ERROR: Missing EO code. Example: scripts/new_eo.sh EO2"
  exit 1
fi

EO_LOWER="$(echo "${EO_CODE}" | tr '[:upper:]' '[:lower:]')"  # EO2 -> eo2
EO_DIR="eo/${EO_CODE}"
DOCS_DIR="docs/eo"

MILESTONES="${EO_DIR}/${EO_LOWER}-milestones.yml"
ARTIFACTS="${EO_DIR}/${EO_LOWER}-public-artifacts-index.yml"
RUNBOOK="${EO_DIR}/README.md"
DOCS_PAGE="${DOCS_DIR}/${EO_CODE}.md"

mkdir -p "${EO_DIR}"
mkdir -p "${DOCS_DIR}"

# Milestones YAML (skeleton)
cat > "${MILESTONES}" <<EOF
# ${EO_CODE} Milestones Tracker (Public-Artifact-First)
# NJ Energy Observability -- Independent, public-data-based, not official.
#
# Purpose:
# - Track ${EO_CODE} implementation as observable, verifiable public artifacts.
# - No internal deliberations, no confidential data, no forecasts, no recommendations.

meta:
  eo_id: "${EO_CODE}"
  title: "${EO_TITLE:-${EO_CODE}}"
  jurisdiction: "New Jersey"
  effective_date: "${EO_EFFECTIVE:-YYYY-MM-DD}"
  tracking_version: "v1.0"
  last_updated: "YYYY-MM-DD"
  source_url: "${EO_URL:-REPLACE_WITH_OFFICIAL_PDF_URL}"
  sources_policy:
    - "Public sources only"
    - "Links required for status=published"
    - "No internal deliberations"
    - "No forecasts / no recommendations"
  status_values: ["not_started", "in_progress", "published", "superseded"]

milestones:
  # Add milestones here. Keep them public-artifact-first.
  - id: "${EO_CODE}-M1-PLACEHOLDER"
    phase: "TBD"
    title: "Placeholder milestone (replace)"
    target_date: null
    owner_orgs: []
    public_artifact_expected: []
    status: "not_started"
    public_artifact_url: null
    verification_notes:
      - "Replace this placeholder with real milestones from the EO text."
    notes: null
EOF

# Public artifacts index YAML (skeleton)
cat > "${ARTIFACTS}" <<EOF
# ${EO_CODE} Public Artifacts Index
# NJ Energy Observability -- Independent, public-data-based, not official.
#
# Purpose:
# - Maintain a canonical, dated index of publicly posted ${EO_CODE}-related artifacts.
# - Public URLs only. Append entries; do not overwrite history.

meta:
  eo_id: "${EO_CODE}"
  title: "${EO_TITLE:-${EO_CODE}}"
  jurisdiction: "New Jersey"
  source_url: "${EO_URL:-REPLACE_WITH_OFFICIAL_PDF_URL}"
  index_version: "v1.0"
  last_updated: "YYYY-MM-DD"
  maintenance_policy:
    - "Append entries; do not overwrite history."
    - "If a document is superseded, retain the prior link and mark status."

artifacts:
  - id: "${EO_CODE}-ARTIFACT-PLACEHOLDER"
    milestone_id: "${EO_CODE}-M1-PLACEHOLDER"
    title: "Placeholder artifact (replace)"
    owner_org: null
    document_type: "Order / Notice / Report"
    url: null
    posted_date: null
    retrieved_date: null
    status: "pending"
    notes: null
EOF

# Runbook
cat > "${RUNBOOK}" <<EOF
# ${EO_CODE} Update Runbook (Public Artifacts Only)

This directory tracks ${EO_CODE} implementation using:
- \`${EO_LOWER}-milestones.yml\` (canonical milestone logic)
- \`${EO_LOWER}-public-artifacts-index.yml\` (append-only links + dates)

## When a public artifact appears
1) Add the artifact link to \`${EO_LOWER}-public-artifacts-index.yml\`
   - fill \`url\`, \`posted_date\` (if known), \`retrieved_date\` (today), \`status: published\`

2) Update the matching milestone in \`${EO_LOWER}-milestones.yml\`
   - set \`status: published\`
   - set \`public_artifact_url\` to the same URL

3) Regenerate the human-readable docs page
   - \`make render_eo EO=${EO_CODE}\`

4) Open a PR
   - Title: \`${EO_CODE}: add <artifact> (published)\`
   - Body: "Public artifact only; no interpretation."

## Rules
- Public sources only
- No summaries inside YAML
- Append-only in the artifacts index
- No evaluation or recommendations
EOF

# Docs placeholder (renderer will overwrite later)
cat > "${DOCS_PAGE}" <<EOF
# ${EO_TITLE:-${EO_CODE}} -- Implementation Tracker

This page is generated from:
- \`eo/${EO_CODE}/${EO_LOWER}-milestones.yml\`
- \`eo/${EO_CODE}/${EO_LOWER}-public-artifacts-index.yml\`

Run:
\`\`\`bash
make render_eo EO=${EO_CODE}
\`\`\`

to generate the table.
EOF

echo "Scaffolded ${EO_CODE}:"
echo "  - ${MILESTONES}"
echo "  - ${ARTIFACTS}"
echo "  - ${RUNBOOK}"
echo "  - ${DOCS_PAGE}"
