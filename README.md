# 🌫️ AQI (Air Quality Index) Prediction System

A machine learning–powered web application that predicts the **Air Quality Index (AQI)** for Indian cities.  
The project uses **Random Forest Regression**, trained on real-world data (`city_day.csv`), and provides a clean UI for users to check AQI by selecting a city.

---

##  Features

- **AQI Prediction** based on the city and current date  
- **Random Forest Model** trained on real AQI dataset   
- Flask backend  
- Real-time prediction  
- Clean file structure for easy deployment

---

##  Project Structure
AQI Prediction System/
│── app.py
│── train_model_city.py
│── requirements.txt
│── .gitignore
│
├── templates/
│ ├── index.html
│ └── result.html
│
├── static/
│ ├── style.css
│ └── script.js
│
├── artifacts/ # (NOT uploaded to GitHub)
│ ├── city_aqi_model.joblib
│ └── city_label_encoder.joblib
│
└── data/ # (NOT uploaded to GitHub)
├── city_day.csv


---

##  Installation & Setup

###  Clone the repository
git clone https://github.com/YOUR_USERNAME/AQI-Prediction.git
cd AQI-Prediction

python -m venv venv
venv/Scripts/activate

###  Install dependencies

pip install -r requirements.txt


###  Run the Flask app



python app.py


Now open your browser at:

 **http://127.0.0.1:5000**

---

##  Model Information

- Algorithm: **RandomForestRegressor**
- Dataset: `city_day.csv`
- Categorical Encoding: `LabelEncoder` on city names
- Date Features: **Day, Month, Year**
- Metrics:
  - **R² Score:** ~0.85–0.90  
  - **RMSE:** ~25–35 AQI units  

 Since AQI is a **regression problem**, accuracy (%) is **not used**.

---

##  Training the Model

To retrain:



python train_model_city.py


It will generate:



/artifacts/city_aqi_model.joblib
/artifacts/city_label_encoder.joblib


---

## UI Preview

- Dark theme  
- Responsive  
- Dropdown city selection  
- Clean prediction output  

(Add screenshots if you want)

---

## Files Not Included in Repo

The following large files are intentionally ignored:



data/
artifacts/
*.joblib
*.csv



---

## Contributing

Pull requests are welcome.  
For major changes, open an issue first to discuss what you want to update.
