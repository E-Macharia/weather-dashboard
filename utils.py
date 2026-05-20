import requests
import pandas as pd
import os
from datetime import datetime

# =========================
# GET LOCATION KEY FROM CITY
# =========================
def get_location_key(api_key, city_name):
    url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city_name}"
    
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if not data:
        return None

    return {
        "location_key": data[0]["Key"],
        "city": data[0]["LocalizedName"]
    }


# =========================
# GET CURRENT WEATHER
# =========================
def get_weather(api_key, location_key):
    url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if not data:
        return None

    w = data[0]

    return {
        "condition": w.get("WeatherText"),
        "temperature": w.get("Temperature", {}).get("Metric", {}).get("Value"),
        "is_day": w.get("IsDayTime"),
        "precipitation": w.get("HasPrecipitation"),
        "time": w.get("LocalObservationDateTime")
    }


# =========================
# SAVE TO CSV
# =========================
def save_to_csv(record, filename="weather_data.csv"):
    df = pd.DataFrame([record])

    if not os.path.exists(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode="a", header=False, index=False)


# =========================
# LOAD HISTORY
# =========================
def load_history(filename="weather_data.csv"):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return None