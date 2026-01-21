# Contributing

Thanks for your interest in improving this project. Please follow these guidelines to keep contributions consistent.

Repository: https://github.com/chaseobservability/nj-energy-observability

## Commit messages

Use Conventional Commits format:

```
<type>(optional scope): <short summary>
```

Types (use the most appropriate):
- feat: new feature or capability
- fix: bug fix
- docs: documentation-only change
- refactor: code change that neither fixes a bug nor adds a feature
- perf: performance improvement
- test: adding or updating tests
- chore: tooling, build, or maintenance tasks
- ci: CI-related changes
- build: build system or dependencies

Examples:
- feat: add statewide rollup output
- docs: document data sources
- fix(parser): handle empty zone list

## PR Checklist (Required)

Before requesting review, confirm:

- [ ] No `raw/`, `stage/`, `.env*`, API keys, or parquet files are committed
- [ ] If EO YAML changed, run `make render_all_eos` and commit updated `docs/eo/*.md`
- [ ] If docs changed, confirm GitHub Pages build is expected to pass
- [ ] If metrics changed, update `metrics/metric-catalog.yml` (taxonomy + allowed/disallowed claims)
- [ ] No forecasts, recommendations, or nonpublic content added

## Versioning, tags, and releases

Use Semantic Versioning (SemVer): `MAJOR.MINOR.PATCH`.

- MAJOR: incompatible changes
- MINOR: backward-compatible features
- PATCH: backward-compatible fixes

Tag releases with a `v` prefix (e.g., `v1.2.3`).

## Pull requests

- Keep changes focused and well-scoped.
- Update or add documentation and tests when needed.
- Ensure scripts or tooling changes are documented.
