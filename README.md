# 🌍 AI-Pollution-Forecasting

An AI-powered pollution forecasting system that predicts next-hour PM2.5 levels using **real-time data** from the OpenWeatherMap API and a **Random Forest model**.  

This project was developed as part of the **Edunet Foundation’s Green Skills with AI** internship program in collaboration with **AICTE** and **Shell**.

---

## 📌 Overview

- Collects **live air pollution data** (PM2.5, PM10, CO, NO2, O3) from OpenWeatherMap.  
- Logs the real-time readings into a CSV file (`realtime_pollution_log.csv`).  
- Trains a **Random Forest Regressor** on historical PM2.5 data (`historical_pm25_2024.csv`).  
- Uses the trained model to **predict the next hour’s PM2.5 level**.  
- Categorizes air quality into **Good, Moderate, Unhealthy, or Very Unhealthy**.  

---

## 📁 Project Structure

```

AI-Pollution-Forecasting/
├── data/
│   ├── realtime\_pollution\_log.csv       # Live collected data
│   └── historical\_pm25\_2024.csv         # Training dataset
│
├── src/
│   ├── fetch\_real\_time\_data.py          # Fetch & log live data
│   ├── train\_model.py                   # Train ML model
│   └── predict\_future.py                # Predict next-hour PM2.5
│
├── models/ (optional, if you save models here)
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. ✅ Install Dependencies
Install required Python libraries:

```bash
pip install -r requirements.txt
````

Or manually:

```bash
pip install pandas scikit-learn joblib requests
```

---

### 2. 🔑 Get an API Key

* Sign up at [OpenWeatherMap](https://openweathermap.org/api)
* Copy your **API key**.
* Replace the placeholder in `fetch_real_time_data.py`:

```python
api_key = "YOUR_API_KEY"
```

---

### 3. 📥 Prepare Data

* Place your historical dataset in the `data/` folder:

```
data/historical_pm25_2024.csv
```

This file must contain:

* `timestamp` column
* `pm25_one_hourly` column

---

### 4. 🌐 Fetch Live Data

Run:

```bash
python src/fetch_real_time_data.py
```

✅ This will:

* Fetch real-time pollution data from OpenWeatherMap.
* Print the collected values.
* Append them into `data/realtime_pollution_log.csv`.

---

### 5. 🧠 Train the Model

Run:

```bash
python src/train_model.py
```

✅ This will:

* Train a **Random Forest model** using historical data.
* Save the trained model as:

```
src/pollution_forecast_model.pkl
```

---

### 6. 🔮 Predict Future Air Quality

Run:

```bash
python src/predict_future.py
```

✅ This will:

* Load the trained model.
* Read the **latest PM2.5 value** from `data/realtime_pollution_log.csv`.
* Predict the **next hour’s PM2.5**.

Example output:

```
Latest PM2.5: 26.51
Predicted next hour PM2.5: 19.49
```

---

## 🏷️ Air Quality Levels (PM2.5)

<img width="766" height="221" alt="image" src="https://github.com/user-attachments/assets/61e28563-66c3-479c-95c5-c23cd25cd6b7" />


---

## 🚀 Future Improvements

* Integrate **weather data** (temperature, humidity, wind speed) as features.
* Build a **Streamlit dashboard** for visualization.
* Add **SMS/Email alerts** for unhealthy levels.
* Automate logging & prediction with a **cron job**.
* Experiment with **LSTM / ARIMA** for advanced time-series forecasting.

---

## 🧪 Tech Stack

* **Python** 🐍
* **Pandas** 🐼
* **Scikit-learn** 🤖
* **Joblib** (model saving/loading)
* **Requests** (API calls)
* **OpenWeatherMap API** 🌐

---

## 👩‍💻 Author

Internship Project under **Edunet Foundation** in collaboration with **AICTE** & **Shell**.

**Contributor:** Moluguri Pooja

---

## 📜 License

This project is **open-source** and for **educational purposes only**. Attribution appreciated.

 
