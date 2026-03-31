# DiaPredict AI - Diabetes Risk Assessment

A modern web application for predicting diabetes risk using machine learning. Built with Flask and featuring a sleek, cyber-themed UI.

## 🚀 Features

- **AI-Powered Prediction**: Uses a trained machine learning model to assess diabetes risk
- **User-Friendly Interface**: Clean, responsive web interface with dark/light theme toggle
- **Real-time Analysis**: Instant prediction results based on user input
- **Medical Parameters**: Analyzes key health indicators including glucose levels, BMI, age, and more

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠 Installation

1. **Clone or download the project files**

2. **Navigate to the project directory**
   ```bash
   cd diabetics
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the model file is present**
   - The `best_model_DIABETICS.pkl` file should be in the root directory
   - This file contains the trained machine learning model

## 🎯 Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   - Navigate to `http://127.0.0.1:5000/`

3. **Enter patient information**
   - Fill in the form with the following parameters:
     - Pregnancies: Number of times pregnant
     - Glucose: Plasma glucose concentration
     - Blood Pressure: Diastolic blood pressure (mm Hg)
     - Insulin: 2-Hour serum insulin (mu U/ml)
     - BMI: Body mass index
     - DPF: Diabetes pedigree function
     - Age: Age in years

4. **Get prediction**
   - Click "Analyze Risk" to receive the diabetes risk assessment

## 🏗 Project Structure

```
diabetics/
├── app.py                 # Main Flask application
├── best_model_DIABETICS.pkl  # Trained ML model
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Web interface
└── README.md             # This file
```

## 🧪 Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn (via joblib for model loading)
- **Frontend**: HTML5, CSS3 (with custom animations)
- **Styling**: Custom CSS with theme support

## 🔧 Development

The application runs in debug mode by default. For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Configure proper environment variables

## 📊 Model Information

The prediction model was trained on the Pima Indians Diabetes Dataset and uses the following features:
- Pregnancies
- Glucose
- Blood Pressure
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Please check the license file for details.

## ⚠️ Disclaimer

This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.