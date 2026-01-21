# EO1 Update Runbook (Public Artifacts Only)

This directory tracks EO1 implementation using:
- `eo1-milestones.yml` (canonical milestone logic)
- `eo1-public-artifacts-index.yml` (append-only links + dates)

## When a public EO1 artifact appears

1) Add the artifact link to `eo1-public-artifacts-index.yml`
   - fill `url`, `posted_date` (if known), `retrieved_date` (today), `status: published`

2) Update the matching milestone in `eo1-milestones.yml`
   - set `status: published`
   - set `public_artifact_url` to the same URL

3) Regenerate the human-readable page
   - `make render_eo`

4) Open a PR
   - Title: `EO1: add <artifact> (published)`
   - Body: "Public artifact only; no interpretation."

## Rules
- Public sources only
- No summaries inside YAML
- Append-only in the artifacts index
- No policy evaluation or recommendations
