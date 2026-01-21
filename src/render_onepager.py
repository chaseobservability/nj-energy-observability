import argparse, json
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from .utils import load_env, env, ensure_dir, read_json, pct

def main():
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", required=True)
    args = ap.parse_args()

    out_dir = env("OUT_DIR", "./out")
    out_period = f"{out_dir}/{args.period}"
    ensure_dir(out_period)

    # Load outputs (may be placeholders in early iterations)
    zone_df = pd.read_csv(f"{out_period}/scorecard_zone.csv")
    state_df = pd.read_csv(f"{out_period}/scorecard_statewide.csv")

    def row_to_dict(df: pd.DataFrame, zid: str) -> dict:
        return df[df["zone_id"] == zid].iloc[0].to_dict()

    # Build context for render
    ctx = {
        "period": args.period,
        "definition_version": env("DEFINITION_VERSION", "v1.0"),
        "data_vintage": f"pulled_{env('DATA_VINTAGE', 'TODO')}",
        "code_version": env("CODE_VERSION", "git:manual"),
        "top_hours_n": read_json("config/zones.json")["top_hours_n"],
        "pct": pct,

        # Capacity price anchors
        "capacity_price_usd_per_mw_day": zone_df.get("capacity_price_usd_per_mw_day", pd.Series([None])).iloc[0],
        "capacity_price_source": zone_df.get("capacity_price_source", pd.Series([""])).iloc[0],
        "capacity_price_effective_date": zone_df.get("capacity_price_effective_date", pd.Series([""])).iloc[0],

        "aeco": row_to_dict(zone_df, "AECO"),
        "jcpl": row_to_dict(zone_df, "JCPL"),
        "pseg": row_to_dict(zone_df, "PSEG"),
        "reco": row_to_dict(zone_df, "RECO"),
        "nj_statewide": state_df.iloc[0].to_dict(),

        # What changed placeholders
        "what_changed_1": "—",
        "what_changed_2": "—",
        "what_changed_3": "—",
        "watch_list": "—",
        "data_quality_notes": "—",
        "candidate_followups": "—"
    }

    jenv = Environment(loader=FileSystemLoader("templates"))
    internal_tpl = jenv.get_template("scorecard_onepager.md")
    public_tpl = jenv.get_template("public_onepager_v0.md")

    with open(f"{out_period}/scorecard_onepager.md", "w") as f:
        f.write(internal_tpl.render(**ctx))

    with open(f"{out_period}/public_onepager_v0.md", "w") as f:
        f.write(public_tpl.render(**ctx))

    
    # Write a simple run manifest + combined JSON for audit
    manifest = {
        "period": args.period,
        "definition_version": ctx["definition_version"],
        "data_vintage": ctx["data_vintage"],
        "code_version": ctx["code_version"],
        "inputs": {
            "capacity_price": "config/capacity_price.json",
            "customers": "config/customers.json",
            "zones": "config/zones.json"
        },
        "warnings": []
    }
    with open(f"{out_period}/run_manifest.json", "w") as mf:
        json.dump(manifest, mf, indent=2)

    # Combine zone + statewide outputs into one JSON list (best-effort)
    combined = []
    try:
        combined.extend(zone_df.to_dict(orient="records"))
        combined.extend(state_df.to_dict(orient="records"))
    except Exception as _e:
        pass
    with open(f"{out_period}/scorecard_all.json", "w") as jf:
        json.dump(combined, jf, indent=2)

    print(f"Wrote onepagers to {out_period}/" )

if __name__ == "__main__":
    main()
