from __future__ import annotations
import pandas as pd
from pathlib import Path

def write_csv(df: pd.DataFrame, path: str, mode: str = "w") -> str:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False, mode=mode, header=(mode == "w"))
    return str(p)
