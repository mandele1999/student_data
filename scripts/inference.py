# This script is used to load the pre-trained model and make predictions on new data.
# It uses the joblib library to load the model and preprocess the input data before making predictions.
# The script also includes a function to load the preprocessing pipeline and the model from disk.

import joblib

def load_components():
    preprocessor = joblib.load('../models/student_data_preprocessing_pipeline.pkl')
    model = joblib.load('../models/lr_student_grade_model.pkl')
    return preprocessor, model

def predict_student_gpa_risk(input_df):
    preprocessor, model = load_components()
    processed = preprocessor.transform(input_df)
    predicted_gpa = model.predict(processed)[0]
    risk_flag = int(predicted_gpa < 2.0)
    return predicted_gpa, risk_flag
