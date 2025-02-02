import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Load the model
model_path = "xgboost_student_risk_model.pkl"

# Ensure the file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

try:
    model = joblib.load(model_path)
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Streamlit UI
st.title("🎓 Student At-Risk Prediction")

# User input fields
absences = st.number_input("📌 Number of Absences", min_value=0, step=1)
parentalsupport = st.slider("👨‍👩‍👧‍👦 Parental Support (1-4)", min_value=1, max_value=4, step=1)
studytimeweekly = st.number_input("📖 Study Time Weekly (hours)", min_value=0.0, step=0.5)
gpa = st.number_input("📊 GPA", min_value=0.0, step=0.1)

# Ensure we get the correct feature order from the model
if hasattr(model, "get_booster"):  # XGBClassifier stores feature names differently
    booster = model.get_booster()
    model_features = booster.feature_names  # Extract feature names from the trained model
else:
    model_features = ['absences', 'parentalsupport', 'studytimeweekly', 'gpa']  # Fallback

# Prediction
if st.button("🚀 Predict"):
    # Convert input to DataFrame and reorder columns to match the model
    input_df = pd.DataFrame([[absences, parentalsupport, studytimeweekly, gpa]], columns=['absences', 'parentalsupport', 'studytimeweekly', 'gpa'])
    input_df = input_df[model_features]  # Reorder columns to match model training data

    # Make prediction
    try:
        prediction = model.predict(input_df)[0]
        result = "⚠️ At Risk" if prediction == 1 else "✅ Not At Risk"
        st.subheader(f"🎯 Prediction: **{result}**")
    except Exception as e:
        st.error(f"❌ Error making prediction: {e}")