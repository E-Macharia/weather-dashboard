# Weather Dashboard

A real-time weather analytics dashboard built with Streamlit and the AccuWeather API.

## Overview

This project lets users search by city and view live weather conditions including temperature, weather status, and day/night information.

The app converts city names into AccuWeather location keys automatically, fetches current weather, and logs historical records to `weather_data.csv` for analytics.

## Key Features

- 🌍 City name search with automatic AccuWeather location lookup
- 🌤️ Real-time weather data from the AccuWeather API
- 📈 Temperature history visualization and charts
- 💾 Automatic CSV logging for historical analytics
- 🔄 Optional live refresh for real-time updates
- 📊 Multi-city temperature comparison charts
- 🧠 Interactive Streamlit dashboard interface

## Tech Stack

- Python
- Streamlit
- Pandas
- Requests
- AccuWeather API

## Setup

1. Clone the repository or copy the project files into a local folder.
2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create an AccuWeather API key by signing up at [AccuWeather Developer](https://developer.accuweather.com/).

## Configure the API Key

The app hides the API key from the user interface and uses a secure configuration instead.

### Option 1: Streamlit secrets (recommended)

1. Open your app on Streamlit Community Cloud.
2. Click **App settings** → **Secrets**.
3. Paste your key in TOML format:

```toml
ACCUWEATHER_API_KEY = "your_real_api_key_here"
```

4. Save the secrets.
5. Wait about one minute for propagation.

When deployed, users will only see the city input. The API key is kept hidden and secure.

### Option 2: Local environment variable

For local development, set the key in your terminal first:

```bash
set ACCUWEATHER_API_KEY=your_real_api_key_here
```

Then run the app normally:

```bash
streamlit run app.py
```

### Option 3: Local secrets file

If you prefer a local config file, create `.streamlit/secrets.toml` from the example:

```bash
copy .streamlit\secrets.toml.example .streamlit\secrets.toml
```

Then update the file with your key:

```toml
ACCUWEATHER_API_KEY = "your_real_api_key_here"
```

> Important: do not commit your real API key to GitHub.

The repository already ignores `.streamlit/secrets.toml`, so your local key file stays private.

## User experience

With this setup, visitors only need to:

1. Enter a city name.
2. Click `Get Live Weather`.

The app will use the configured AccuWeather API key behind the scenes and keep the dashboard user-friendly.

## Running Locally

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Usage

- Enter a city name such as `Nairobi`.
- Click `Get Live Weather` to fetch current weather.
- View temperature history and multi-city comparison charts.

## Deployment

If you deploy to Streamlit Community Cloud, the app will automatically use the secret from your app settings, so visitors only enter a city name.

## Notes

- The app stores historical weather records in `weather_data.csv`.
- The dashboard handles missing or malformed CSV files gracefully.

## License

This project is provided as-is for learning and demo purposes.
