# Weather Dashboard

A real-time weather analytics dashboard built with Streamlit and the AccuWeather API.

## Overview

This project allows users to search for any city and view live weather conditions including temperature, weather status, and day/night information. The app automatically converts city names into AccuWeather location keys, fetches current weather data, and logs historical records to a CSV file for analytics and comparison.

## Key Features

- 🌍 City name search with automatic AccuWeather location lookup
- 🌤️ Real-time weather data from the AccuWeather API
- 📈 Temperature history visualization and charts
- 💾 Automatic CSV logging for historical analytics
- 🔄 Optional live refresh for real-time updates
- 📊 Multi-city temperature comparison charts
- 🧠 Interactive and easy-to-use Streamlit dashboard interface

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

## Running Locally

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Usage

- Enter your AccuWeather API key in the app.
- Search for a city name such as `Nairobi`.
- Click `Get Live Weather` to fetch current weather.
- View the temperature history and multi-city comparison charts.

## Deployment

Live demo: [https://weather-dashboard-etkw2apywytwvh8n3cjnqw.streamlit.app/](https://weather-dashboard-etkw2apywytwvh8n3cjnqw.streamlit.app/)

To deploy on Streamlit Community Cloud:

1. Push this repository to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub account and select this repository.
4. Deploy the current branch.

> Make sure this repo includes `app.py`, `requirements.txt`, and optionally `weather_data.csv`.

## Notes

- The app stores historical weather records to `weather_data.csv` in the project folder.
- If the CSV file is missing or malformed, the app includes error handling to gracefully recover.

## License

This project is provided as-is for learning and demo purposes.
