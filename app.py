from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# List of expected features in correct order (must match training data order)
FEATURE_NAMES = [
    'Age', 'Pregnancies', 'BMI', 'Glucose', 'BloodPressure', 
    'HbA1c', 'LDL', 'HDL', 'Triglycerides', 'WaistCircumference',
    'HipCircumference', 'WHR', 'FamilyHistory', 'DietType', 
    'Hypertension', 'MedicationUse'
]

# Medical reasonable defaults for each feature
FEATURE_DEFAULTS = {
    'Age': 30, 'Pregnancies': 0, 'BMI': 23.5, 'Glucose': 100,
    'BloodPressure': 80, 'HbA1c': 5.5, 'LDL': 100, 'HDL': 50,
    'Triglycerides': 150, 'WaistCircumference': 80, 
    'HipCircumference': 95, 'WHR': 0.85, 'FamilyHistory': 0,
    'DietType': 2, 'Hypertension': 0, 'MedicationUse': 0
}

@app.route('/')
def home():
    return render_template('index.html', features=FEATURE_NAMES, defaults=FEATURE_DEFAULTS)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Create dictionary with default values
        features = FEATURE_DEFAULTS.copy()
        
        # Update with values from form
        for name in FEATURE_NAMES:
            if name in request.form and request.form[name].strip():
                features[name] = float(request.form[name])
        
        # Convert to array in correct order
        final_features = np.array([features[name] for name in FEATURE_NAMES]).reshape(1, -1)
        
        # Scale features
        final_features = scaler.transform(final_features)
        
        # Make prediction
        prediction = model.predict(final_features)
        probability = model.predict_proba(final_features)[0][1]  # Probability of diabetes
        
        output = "Positive (%.1f%%)" % (probability*100) if prediction[0] == 1 else "Negative (%.1f%%)" % ((1-probability)*100)
        
        return render_template('index.html', 
                            prediction_text=f'Diabetes Prediction: {output}',
                            features=FEATURE_NAMES,
                            defaults=features,
                            show_result=True)
    
    except Exception as e:
        return render_template('index.html', 
                            prediction_text=f'Error: {str(e)}',
                            features=FEATURE_NAMES,
                            defaults=FEATURE_DEFAULTS,
                            show_result=True)

if __name__ == "__main__":
    app.run()