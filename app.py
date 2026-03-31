from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# 1. Load the trained model
# Ensure 'best_model_DIABETICS.pkl' is in the same directory as this file
model = joblib.load('best_model_DIABETICS.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # 2. Extract data from form fields
            # The names here must match the 'name' attribute in your HTML input tags
            features = [
                float(request.form['pregnancies']),
                float(request.form['glucose']),
                float(request.form['blood_pressure']),
                float(request.form['insulin']),
                float(request.form['bmi']),
                float(request.form['dpf']),
                float(request.form['age'])
            ]
            
            # 3. Convert to 2D array for prediction
            final_features = [np.array(features)]
            prediction = model.predict(final_features)
            
            # 4. Determine result text
            if prediction[0] == 1:
                result = "The analysis suggests a High Risk of Diabetes."
            else:
                result = "The analysis suggests a Low Risk of Diabetes."
                
            return render_template('index.html', prediction_text=result)
        
        except Exception as e:
            return render_template('index.html', prediction_text=f"Error in prediction: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)