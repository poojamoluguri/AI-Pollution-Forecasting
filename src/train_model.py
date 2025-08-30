import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data_path):
    df = pd.read_csv(data_path, parse_dates=['timestamp'])
    df = df.sort_values('timestamp')
    
    # Use past PM2.5 values as lag features
    df['pm2_5_lag1'] = df['pm25_one_hourly'].shift(1)
    df = df.dropna()

    features = ['pm2_5_lag1']
    X = df[features]
    y = df['pm25_one_hourly']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Model trained. R^2 score:", model.score(X_test, y_test))

    joblib.dump(model, '../src/pollution_forecast_model.pkl')
    print("Model saved as pollution_forecast_model.pkl")

if __name__ == "__main__":
    train_model("../data/historical_pm25_2024.csv")
