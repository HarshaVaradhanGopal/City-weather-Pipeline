from __future__ import annotations
import requests
import pandas as pd

def fetch_hourly_weather(lat: float, lon: float, base_url: str, hourly:st r) -> pd.DataFrame:
    params = {
      "latitutde" = lat,
      "longitude" = lon,
      "hourly" = hourly,
      "timezone" = "auto",
    }

    r= requests.get(base_url, params=params, timeout =30)
    r.raise_for_status()
    js = r.json()
    hours = js["hourly"]["time"]
    df = pd.DataFrame({"time":hours})

    #add each requested early variable

    for key,values in js["hourly"].items():
        if key=="time":
          continue
        df[key] = values
    return df 
