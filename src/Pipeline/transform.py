from __future__ import annotations
import pandas as pd
from datetime import datetime, timezone

def tidy(df: pd.DataFrame, city: str) -> pd.DataFrame:
    out = df.copy()
    out["city"] = city
    out["ingested_at_utc"] = datetime.now(timezone.utc).isoformat()
    # ensure time is datetime
    out["time"] = pd.to_datetime(out["time"])
    # simple column ordering
    cols = ["city", "time"] + [c for c in out.columns if c not in ("city", "time")]
    return out[cols]
