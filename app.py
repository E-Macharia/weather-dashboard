import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Live Weather Dashboard", layout="wide")

st.title("🌍 Real-Time Weather Data Dashboard")

# =========================
# AUTO REFRESH OPTION (SAFE)
# =========================
auto_refresh = st.checkbox("🔄 Enable Auto Refresh (10s)")

if auto_refresh:
    st.info("Auto-refresh enabled... updating every 10 seconds")
    st.rerun()

# =========================
# API KEY INPUT
# =========================
API_KEY = st.text_input("🔑 Enter your AccuWeather API Key", type="password")

# =========================
# CITY SEARCH
# =========================
city = st.text_input("🌍 Search City Name (e.g. Nairobi, Kerugoya)")

# =========================
# GET LOCATION KEY
# =========================
def get_location_key(city_name):
    url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={city_name}"
    response = requests.get(url)

    if response.status_code != 200:
        st.error("Error fetching location")
        return None

    data = response.json()

    if not data:
        st.error("City not found")
        return None

    return data[0]["Key"], data[0]["LocalizedName"]

# =========================
# GET WEATHER DATA
# =========================
def get_weather(location_key):
    url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        st.error("Error fetching weather")
        return None

    return response.json()

# =========================
# SAVE TO CSV
# =========================
def save_data(record):
    file = "weather_data.csv"
    df = pd.DataFrame([record])

    if not os.path.exists(file):
        df.to_csv(file, index=False)
    else:
        df.to_csv(file, mode="a", header=False, index=False)

# =========================
# MAIN LOGIC
# =========================
if API_KEY and city:

    if st.button("🔍 Get Live Weather"):

        loc = get_location_key(city)

        if loc:
            location_key, city_name = loc

            weather = get_weather(location_key)

            if weather and len(weather) > 0:
                w = weather[0]

                condition = w.get("WeatherText")
                temp = w.get("Temperature", {}).get("Metric", {}).get("Value")
                is_day = w.get("IsDayTime")

                # DISPLAY
                st.subheader(f"📍 {city_name}")
                st.metric("🌡 Temperature (°C)", temp)
                st.write("🌤 Condition:", condition)
                st.write("☀️ Daytime:", is_day)

                # SAVE RECORD
                record = {
                    "time": datetime.now(),
                    "city": city_name,
                    "temp": temp,
                    "condition": condition
                }

                save_data(record)

                st.success("Data saved to CSV ✔")

# =========================
# HISTORY + CHARTS
# =========================
st.divider()
st.subheader("📊 Temperature History")

file = "weather_data.csv"
if os.path.exists(file) and os.path.getsize(file) > 0:
    try:
        df = pd.read_csv(file)

        # If file was written without a header, retry parsing assuming known columns
        if "temp" not in df.columns:
            df = pd.read_csv(file, header=None, names=["time", "city", "temp", "condition"])

        if "temp" in df.columns and not df["temp"].dropna().empty:
            st.line_chart(df["temp"])
        else:
            st.info("No temperature data to chart")

        st.dataframe(df)

        # =========================
        # MULTI-CITY COMPARISON
        # =========================
        cities = df["city"].dropna().unique().tolist() if "city" in df.columns else []
        if cities:
            selected_cities = st.multiselect("Compare cities", options=cities, default=cities[:2])

            if selected_cities:
                if "time" in df.columns:
                    try:
                        df["time"] = pd.to_datetime(df["time"])
                    except Exception:
                        pass

                pivot = None
                try:
                    pivot = df.pivot_table(index="time", columns="city", values="temp")
                    pivot = pivot.sort_index()
                except Exception:
                    pivot = None

                if pivot is not None and any(c in pivot.columns for c in selected_cities):
                    st.subheader("📈 Multi-city Temperature Comparison")
                    st.line_chart(pivot[selected_cities])
                else:
                    st.info("Not enough data to build a comparison chart")
    except pd.errors.EmptyDataError:
        st.info("CSV file is empty or malformed. No historical data to show.")
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
else:
    st.info("No historical data yet")