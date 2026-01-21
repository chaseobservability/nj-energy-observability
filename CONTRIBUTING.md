# Contributing

Thanks for your interest in improving this project. Please follow these guidelines to keep contributions consistent.

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
