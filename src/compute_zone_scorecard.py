import argparse
import json
import os
import pandas as pd
from .utils import load_env, env, ensure_dir, read_json, norm_row_keys

def parse_metered_load_json(path: str) -> pd.DataFrame:
    with open(path, "r") as f:
        items = json.load(f)

    rows = []
    for raw in items:
        r = norm_row_keys(raw)
        if "datetime_beginning_ept" not in r or "transmission_zone" not in r or "mw" not in r:
            continue

        rows.append({
            "ts_et": r.get("datetime_beginning_ept"),
            "ts_utc": r.get("datetime_beginning_utc"),
            "zone_id": r.get("transmission_zone"),
            "load_area": r.get("load_area"),
            "load_mw": r.get("mw"),
            "company_verified": r.get("company_verified"),
            "nerc_region": r.get("nerc_region"),
            "market_region": r.get("market_region"),
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        df["ts_et"] = pd.to_datetime(df["ts_et"])
        df["ts_utc"] = pd.to_datetime(df["ts_utc"], errors="coerce")
        df["load_mw"] = pd.to_numeric(df["load_mw"], errors="coerce")
    return df

def parse_marginal_emissions_json(path: str) -> pd.DataFrame:
    with open(path, "r") as f:
        items = json.load(f)

    rows = []
    for raw in items:
        r = norm_row_keys(raw)
        if "datetime_beginning_ept" not in r or "pnode_name" not in r or "marginal_co2_rate" not in r:
            continue

        co2_lbs = r.get("marginal_co2_rate")
        rows.append({
            "ts_et": r.get("datetime_beginning_ept"),
            "ts_utc": r.get("datetime_beginning_utc"),
            "pnode_name": r.get("pnode_name"),
            "pnode_id": r.get("pnode_id"),
            "marginal_co2_lbs_per_mwh": co2_lbs,
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        df["ts_et"] = pd.to_datetime(df["ts_et"])
        df["ts_utc"] = pd.to_datetime(df["ts_utc"], errors="coerce")
        df["marginal_co2_lbs_per_mwh"] = pd.to_numeric(df["marginal_co2_lbs_per_mwh"], errors="coerce")
        df["marginal_co2_tons_per_mwh"] = df["marginal_co2_lbs_per_mwh"] / 2000.0
    return df

def _num_or_dash(value):
    return value if value is not None and pd.notna(value) else "—"

def _quantiles(series: pd.Series):
    if series.empty:
        return None, None, None
    return series.quantile(0.25), series.median(), series.quantile(0.75)

def main():
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", required=True)
    args = ap.parse_args()

    zones_cfg = read_json("config/zones.json")
    cap_cfg = read_json("config/capacity_price.json")
    cust_cfg = read_json("config/customers.json")

    zones = zones_cfg["nj_zones"]
    top_n = int(zones_cfg["top_hours_n"])

    raw_dir = env("RAW_DIR", "./raw")
    stage_dir = env("STAGE_DIR", "./stage")
    out_dir = env("OUT_DIR", "./out")
    stage_period = f"{stage_dir}/{args.period}"
    out_period = f"{out_dir}/{args.period}"
    ensure_dir(stage_period)
    ensure_dir(out_period)

    load_path = f"{raw_dir}/dataminer/{args.period}/hrl_load_metered_ALL.json"
    em_path = f"{raw_dir}/dataminer/{args.period}/hourly_marginal_emissions_ALL.json"

    load_df = parse_metered_load_json(load_path) if os.path.exists(load_path) else pd.DataFrame()
    em_df = parse_marginal_emissions_json(em_path) if os.path.exists(em_path) else pd.DataFrame()

    if not load_df.empty:
        load_df = load_df[load_df["zone_id"].isin(zones)].copy()
    load_df.to_parquet(f"{stage_period}/load_hourly.parquet", index=False)

    pn_cfg = read_json("config/pnodes.json")
    wanted_pnodes = set(pn_cfg["zone_to_pnode_name"].values())
    if not em_df.empty:
        em_df = em_df[em_df["pnode_name"].isin(wanted_pnodes)].copy()
    em_df.to_parquet(f"{stage_period}/emissions_hourly.parquet", index=False)

    rows = []
    for z in zones:
        zdf = load_df[load_df["zone_id"] == z] if not load_df.empty else pd.DataFrame()
        total_load_mwh = _num_or_dash(zdf["load_mw"].sum()) if not zdf.empty else "—"
        peak_load_mw = _num_or_dash(zdf["load_mw"].max()) if not zdf.empty else "—"

        top_hours = []
        if not zdf.empty:
            top_hours = zdf.sort_values("load_mw", ascending=False).head(top_n)["ts_et"].tolist()

        pnode = pn_cfg["zone_to_pnode_name"].get(z) or pn_cfg.get("fallback_pnode_name")
        em_vals = pd.Series(dtype=float)
        if pnode and not em_df.empty and top_hours:
            edf = em_df[em_df["pnode_name"] == pnode].set_index("ts_et")
            em_vals = edf.loc[edf.index.isin(top_hours), "marginal_co2_tons_per_mwh"].dropna()

        p25, p50, p75 = _quantiles(em_vals)
        emissions_note = ""
        if em_vals.empty:
            emissions_note = "No marginal emissions data for top hours."

        rows.append({
            "period": args.period,
            "zone_id": z,
            "zone_rollup_level": "zone",
            "definition_version": env("DEFINITION_VERSION", "v1.0"),
            "top_hours_n": top_n,
            "capacity_price_usd_per_mw_day": cap_cfg["capacity_price_usd_per_mw_day"],
            "capacity_price_source": cap_cfg["capacity_price_source"],
            "capacity_price_effective_date": cap_cfg["capacity_price_effective_date"],
            "customers_count": cust_cfg.get("customers_statewide"),
            "total_load_mwh": total_load_mwh,
            "peak_load_mw": peak_load_mw,
            "coincidence_corr_with_pjm_rto": "—",
            "coincident_top_n_share": None,
            "gas_marginal_share_top_n_hours": None,
            "marginal_co2_tons_per_mwh_top_n_hours_p25": _num_or_dash(p25),
            "marginal_co2_tons_per_mwh_top_n_hours_p50": _num_or_dash(p50),
            "marginal_co2_tons_per_mwh_top_n_hours_p75": _num_or_dash(p75),
            "capacity_exposure_usd_per_customer_month_point": "—",
            "capacity_exposure_confidence": "low",
            "notes": emissions_note
        })

    pd.DataFrame(rows).to_csv(f"{out_period}/scorecard_zone.csv", index=False)
    print(f"Wrote {out_period}/scorecard_zone.csv")

if __name__ == "__main__":
    main()
