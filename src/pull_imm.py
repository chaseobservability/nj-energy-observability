import argparse
from .utils import load_env, env, ensure_dir

def main():
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", required=True)
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    args = ap.parse_args()

    # MVP: manual download of IMM marginal fuel CSVs into raw/imm/<period>/
    raw_dir = env("RAW_DIR", "./raw")
    out_dir = f"{raw_dir}/imm/{args.period}"
    ensure_dir(out_dir)

    print(f"Place IMM marginal fuel CSVs for {args.period} into: {out_dir}")
    print("This placeholder keeps the workflow consistent; automation can be added later.")

if __name__ == "__main__":
    main()
