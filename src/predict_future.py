import pandas as pd
import joblib
import os

def load_latest_realtime(log_path):
    df = pd.read_csv(log_path, parse_dates=['timestamp'])
    return df.sort_values('timestamp').iloc[-1]

if __name__ == "__main__":
    model = joblib.load('pollution_forecast_model.pkl')
    latest = load_latest_realtime("../data/realtime_pollution_log.csv")

    features = [[latest['pm2_5']]]
    predicted = model.predict(features)[0]

    print(f"Latest PM2.5: {latest['pm2_5']:.2f}")
    print(f"Predicted next hour PM2.5: {predicted:.2f}")

