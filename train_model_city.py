import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/city_day.csv")

df.columns = [c.strip() for c in df.columns]

# Remove missing AQI rows
df = df.dropna(subset=["AQI"])

# Convert Date to features
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Year"] = df["Date"].dt.year

# Encode City
le = LabelEncoder()
df["City_encoded"] = le.fit_transform(df["City"])
    
# Features for training
features = ["City_encoded", "Month", "Day", "Year"]
target = "AQI"

X = df[features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Training complete.")
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2:", r2_score(y_test, y_pred))

# Save artifacts
os.makedirs("artifacts", exist_ok=True)

joblib.dump(model, "artifacts/city_aqi_model.joblib")
joblib.dump(le, "artifacts/city_label_encoder.joblib")

print("Model saved.")
