# AQI (Air Quality Index) Prediction System

A **Machine Learning–based Flask web application** that predicts the **Air Quality Index (AQI)** for Indian cities using historical air-quality data. The system uses **Random Forest Regression** and provides a clean UI for city-wise AQI prediction.

---

## Project Overview

Air pollution is a serious concern across many Indian cities. This project allows users to:

* Select a city
* Predict AQI values
* View results through a simple, responsive web interface

The backend is built with **Flask**, and the ML pipeline includes preprocessing, feature scaling, and model persistence using `joblib`.

---

## Features

* **City-wise AQI prediction**
* **Random Forest Regression model**
* Preprocessing with imputer & scaler
* Flask backend
* Clean UI with HTML, CSS, JavaScript
* Easy retraining of model
* Organized and scalable project structure

---

## Project Structure

```
AQI (Air Quality Index) Prediction System/
│── app.py
│── train_model_city.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── templates/
│   ├── index.html        
│   ├── predict.html      
│   ├── result.html       
│   └── about.html        
│
├── static/
│   ├── style.css         
│   └── script.js         
│
├── artifacts/
│   ├── aqi_model.joblib
│   ├── city_aqi_model.joblib
│   ├── city_label_encoder.joblib
│   ├── features.joblib
│   ├── imputer.joblib
│   └── scaler.joblib
│
├── data/
│   ├── city_day.csv
│   └── city_hour.csv
```

---

## Installation & Setup
 
### 1️ Clone the Repository

```bash
git clone https://github.com/jainam258/AQI-Prediction.git
cd AQI-Prediction
```

---

### 2️ Create & Activate Virtual Environment

```bash
python -m venv .venv
```

Activate:

* **Windows**

```bash
.venv\\Scripts\\activate
```

* **Linux / macOS**

```bash
source .venv/bin/activate
```

---

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## Model & Pipeline Details

* **Algorithm:** RandomForestRegressor
* **Problem Type:** Regression
* **Datasets:** `city_day.csv`, `city_hour.csv`
* **Preprocessing:**

  * Missing value handling using **Imputer**
  * Feature scaling using **StandardScaler**
  * City encoding using **LabelEncoder**
* **Artifacts Stored Using:** `joblib`

### 📊 Performance (Approx.)

* **R² Score:** ~0.85 – 0.90
* **RMSE:** ~25 – 35 AQI units

> AQI prediction is a **regression task**, so accuracy (%) is not applicable.

---

## Model Training

To retrain the model and regenerate artifacts:

```bash
python train_model_city.py
```

This will update files inside:

```
artifacts/
```

---

## UI Preview

* Dark theme
* Responsive design
* City selection dropdown
* Clear AQI prediction output

* home page
  <img width="1898" height="926" alt="image" src="https://github.com/user-attachments/assets/ab0c9ed4-e73c-4f39-8ce8-b88d8bacc87a" />

* about page
  <img width="1893" height="921" alt="image" src="https://github.com/user-attachments/assets/0337faa6-a01e-4ce7-9b14-7a6175c9b17b" />

* predict page
  <img width="1906" height="922" alt="image" src="https://github.com/user-attachments/assets/4b23c181-e900-4dc7-9859-65adbfc25d6f" />
  <img width="1884" height="914" alt="image" src="https://github.com/user-attachments/assets/5b18edd7-6e38-4cb9-96ad-ced1b0642936" />
  <img width="1900" height="790" alt="image" src="https://github.com/user-attachments/assets/fe9cdb68-888b-4ab4-a8bd-5c93ed997ea9" />


---

## Ignored Files (.gitignore)

The following are typically ignored to keep the repo clean:

```
.venv/
__pycache__/
*.joblib
*.csv
```

> If you want to keep `artifacts/` or `data/` in GitHub for demo purposes, remove them from `.gitignore`.

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a pull request

For major changes, please open an issue first.

---
If you found this project helpful, please give it a star on GitHub!
