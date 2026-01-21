import argparse, json, requests
from .utils import load_env, env, ensure_dir

def fetch_feed(feed: str, params: dict) -> list[dict]:
    api_key = env("PJM_API_KEY")
    base = env("PJM_API_BASE")
    if not api_key:
        raise RuntimeError("PJM_API_KEY not set. Copy .env.example to .env and fill it.")

    headers = {"Ocp-Apim-Subscription-Key": api_key}
    url = f"{base}/{feed}"

    out = []
    start_row = 1
    row_count = 50000

    while True:
        p = dict(params)
        p["startRow"] = start_row
        p["rowCount"] = row_count
        r = requests.get(url, headers=headers, params=p, timeout=60)
        r.raise_for_status()
        data = r.json()

        items = data.get("items") if isinstance(data, dict) else None
        if items is None:
            items = data.get("data") if isinstance(data, dict) else None
        if items is None:
            items = data

        if not items:
            break
        if isinstance(items, dict):
            items = [items]

        out.extend(items)
        if len(items) < row_count:
            break
        start_row += row_count

    return out

def main():
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", required=True)
    ap.add_argument("--start", required=True)  # ISO-ish
    ap.add_argument("--end", required=True)
    args = ap.parse_args()

    raw_dir = env("RAW_DIR", "./raw")
    out_dir = f"{raw_dir}/dataminer/{args.period}"
    ensure_dir(out_dir)

    # NOTE: Data Miner feed parameter names can vary; avoid zone filters until confirmed.
    # Pull once per feed for the time window, then filter locally by zone/pnode.
    load_params = {
        "datetime_beginning": args.start,
        "datetime_ending": args.end
    }
    load_items = fetch_feed("hrl_load_metered", load_params)
    with open(f"{out_dir}/hrl_load_metered_ALL.json", "w") as f:
        json.dump(load_items, f)

    em_params = {
        "datetime_beginning": args.start,
        "datetime_ending": args.end
    }
    em_items = fetch_feed("hourly_marginal_emissions", em_params)
    with open(f"{out_dir}/hourly_marginal_emissions_ALL.json", "w") as f:
        json.dump(em_items, f)

    print(f"Wrote raw Data Miner pulls to {out_dir}")

if __name__ == "__main__":
    main()
