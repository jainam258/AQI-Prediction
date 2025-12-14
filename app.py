from flask import Flask, render_template, request
import joblib
from datetime import datetime

app = Flask(__name__)

# Load your trained model
model = joblib.load('artifacts/city_aqi_model.joblib')
label_encoder = joblib.load('artifacts/city_label_encoder.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            city = request.form.get('city')
            
            # Encode city
            city_encoded = label_encoder.transform([city])[0]
            
            # Get current date
            now = datetime.now()
            day = now.day
            month = now.month
            year = now.year
            
            # Make prediction
            features = [[city_encoded, day, month, year]]
            prediction = model.predict(features)[0]
            
            return render_template('result.html', 
                                 city=city, 
                                 prediction=round(prediction, 2))
        except Exception as e:
            return render_template('result.html', 
                                 error=f"Error: {str(e)}")
    
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
