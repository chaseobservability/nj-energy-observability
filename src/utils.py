import os, json, datetime, re
from dotenv import load_dotenv

def load_env():
    load_dotenv()

def read_json(path: str):
    with open(path, "r") as f:
        return json.load(f)

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def now_stamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S")

def pct(x):
    if x is None:
        return "—"
    val = round(float(x) * 100.0, 1)
    if val.is_integer():
        return f"{int(val)}%"
    return f"{val}%"

def env(name: str, default=None):
    return os.getenv(name, default)

def norm_key(k: str) -> str:
    """Normalize PJM Data Miner keys: lowercase, strip, spaces->underscore."""
    k = k.strip().lower()
    k = re.sub(r"\s+", "_", k)
    k = re.sub(r"[^a-z0-9_]", "", k)
    k = re.sub(r"_+", "_", k)
    return k

def norm_row_keys(row: dict) -> dict:
    """Return a dict with normalized keys while preserving values."""
    return {norm_key(k): v for k, v in row.items()}
