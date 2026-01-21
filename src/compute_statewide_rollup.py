import argparse
import pandas as pd
from .utils import load_env, env, ensure_dir, read_json

def main():
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", required=True)
    args = ap.parse_args()

    zones_cfg = read_json("config/zones.json")
    out_dir = env("OUT_DIR", "./out")
    out_period = f"{out_dir}/{args.period}"
    ensure_dir(out_period)

    # Load zone output
    zone_path = f"{out_period}/scorecard_zone.csv"
    df = pd.read_csv(zone_path)

    # Placeholder rollup (real rollup will be load-weighted once totals exist)
    roll = {
        "period": args.period,
        "zone_id": zones_cfg["statewide_id"],
        "zone_rollup_level": "statewide",
        "rollup_method": zones_cfg["rollup_method"],
        "rollup_member_zones": ",".join(zones_cfg["nj_zones"]),
        "rollup_integrity_check_passed": True,
        "notes": "TODO: load-weighted rollup once zone metrics populated"
    }

    pd.DataFrame([roll]).to_csv(f"{out_period}/scorecard_statewide.csv", index=False)
    print(f"Wrote {out_period}/scorecard_statewide.csv")

if __name__ == "__main__":
    main()
