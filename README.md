LINK --: [Go live](https://diabetes-app-ptcp.onrender.com/)


# GlucoGuard: Diabetes Risk Assessment Web App

GlucoGuard is a web application that predicts the risk of diabetes based on user-provided health and lifestyle information. It uses a machine learning model trained on medical data to provide a probability-based assessment.

## Features
- User-friendly web interface for inputting health metrics
- Predicts diabetes risk (Positive/Negative) with probability
- Medical defaults for all input fields
- Modern, responsive UI

## How It Works
1. User enters health and lifestyle data in the form.
2. Data is preprocessed and scaled using a saved scaler.
3. The trained model predicts diabetes risk and probability.
4. Results are displayed with recommendations.

## Input Features
- Age
- Pregnancies
- BMI
- Glucose
- Blood Pressure
- HbA1c
- LDL
- HDL
- Triglycerides
- Waist Circumference
- Hip Circumference
- Waist-Hip Ratio
- Family History of Diabetes
- Diet Type
- Hypertension
- Medication Use

## Setup Instructions

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `model.pkl` and `scaler.pkl` are present in the root directory.
4. Run the app:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000/`

## File Structure
- `app.py` - Main Flask application
- `templates/index.html` - Web UI template
- `static/style.css` - Stylesheet
- `model.pkl` - Trained ML model
- `scaler.pkl` - Feature scaler
- `requirements.txt` - Python dependencies
- `diabetes_dataset.csv` - (Optional) Dataset used for training

## Notes
- The app uses Flask for the backend and HTML/CSS for the frontend.
- The model and scaler must match the features and order used in the form.
- For best results, consult a healthcare professional for interpretation.

## License
This project is for educational purposes only.
