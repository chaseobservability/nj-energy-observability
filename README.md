# NJ Capacity Exposure Scorecard (Zone-first + Statewide)

Public-data-based quarterly scorecard for NJ PJM zones:
`AECO`, `JCPL`, `PSEG`, `RECO` plus an `NJ_STATEWIDE` rollup.

This produces an **exposure + risk-hours diagnostic**, not an auction forecast and not a policy recommendation.

## Outputs
For a given quarter (PERIOD):
- `out/<PERIOD>/scorecard_zone.csv`
- `out/<PERIOD>/scorecard_statewide.csv`
- `out/<PERIOD>/scorecard_all.json`
- `out/<PERIOD>/scorecard_onepager.md`
- `out/<PERIOD>/public_onepager_v0.md`
- `out/<PERIOD>/run_manifest.json`

## Setup
1) Copy `.env.example` to `.env` and fill `PJM_API_KEY`.
2) `make install`

## Run
Example quarter:
```bash
make run PERIOD=2026Q1 START=2026-01-01T00:00:00 END=2026-04-01T00:00:00
```
Raw Data Miner pulls are saved as:
- `raw/dataminer/<PERIOD>/hrl_load_metered_ALL.json`
- `raw/dataminer/<PERIOD>/hourly_marginal_emissions_ALL.json`

Staged tables are written to:
- `stage/<PERIOD>/load_hourly.parquet`
- `stage/<PERIOD>/emissions_hourly.parquet`

## Data Miner pulls (what you need)
The prototype pulls these feeds per NJ zone + RTO:
- `hrl_load_metered`
- `hourly_marginal_emissions`

See `scripts/pull_period.sh` for a simple wrapper.

## Status
This repo includes a working scaffold (pull -> compute -> render) and templates.
The compute steps currently include conservative placeholder logic; they are designed to be filled in once you validate the exact field names returned by PJM Data Miner in your environment.

**TODO (near-term)**
- Add `PJM_API_KEY` to `.env` and run sample pulls.
- Confirm PNODE names in `hourly_marginal_emissions` and set `config/pnodes.json` fallback if needed.
- Validate staged outputs in `stage/<PERIOD>/load_hourly.parquet` and `stage/<PERIOD>/emissions_hourly.parquet`.

## Contributing
See `CONTRIBUTING.md` for commit message conventions and release versioning.
