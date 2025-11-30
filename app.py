from flask import Flask, render_template, request
import joblib
import datetime

app = Flask(__name__)

# Load model + encoder
model = joblib.load("artifacts/city_aqi_model.joblib")
encoder = joblib.load("artifacts/city_label_encoder.joblib")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    city = request.form.get("city")

    try:
        city_encoded = encoder.transform([city])[0]
    except:
        return render_template("result.html", 
                               city=city, 
                               error="City not found in training dataset!")

    today = datetime.datetime.today()
    month = today.month
    day = today.day
    year = today.year

    X = [[city_encoded, month, day, year]]
    pred = model.predict(X)[0]

    return render_template(
        "result.html",
        city=city,
        prediction=round(float(pred), 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
