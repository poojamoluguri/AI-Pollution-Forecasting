import requests
import pandas as pd
from datetime import datetime
import os

def get_air_quality(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        components = data['list'][0]['components']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        row = {
            'timestamp': timestamp,
            'latitude': lat,
            'longitude': lon,
            'pm2_5': components['pm2_5'],
            'pm10': components['pm10'],
            'co': components['co'],
            'no2': components['no2'],
            'o3': components['o3']
        }

        print("✅ Real-time data collected:")
        for k, v in row.items():
            print(f"{k}: {v}")

        # Save to CSV file
        log_file = '../data/realtime_pollution_log.csv'
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        if not os.path.exists(log_file):
            pd.DataFrame([row]).to_csv(log_file, index=False)
        else:
            pd.DataFrame([row]).to_csv(log_file, mode='a', header=False, index=False)

        return row
    else:
        print(f"❌ Failed to fetch data: {response.status_code}")
        return None

if __name__ == "__main__":
    # Replace these with your location
    latitude = 28.7041   # Example: Delhi
    longitude = 77.1025

    # Your API key (in quotes!)
    api_key = '8a785f4b0c8aa4698c30b5e8f6831ca8'

    get_air_quality(latitude, longitude, api_key)
