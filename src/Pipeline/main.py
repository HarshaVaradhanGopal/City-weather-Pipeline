from __future__ import annotations
import yaml
import pandas as pd
from src.pipeline.extract import fetch_hourly_weather
from src.pipeline.transform import tidy
from src.pipeline.load import write_csv

def run(config_path: str = "config.yaml") -> str:
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    frames = []
    base_url = cfg["api"]["base_url"]
    hourly = cfg["api"]["params"]["hourly"]

    for c in cfg["cities"]:
        raw = fetch_hourly_weather(c["lat"], c["lon"], base_url, hourly)
        frames.append(tidy(raw, c["name"]))

    all_rows = pd.concat(frames, ignore_index=True)
    return write_csv(all_rows, cfg["output_path"])

if __name__ == "__main__":
    out = run()
    print(f"Wrote: {out}")
