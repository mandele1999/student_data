# This script is used to create a Streamlit web application for predicting student GPA and risk status.
# It uses the joblib library to load the pre-trained model and preprocessing pipeline.
# The application allows users to input student data and get predictions on GPA and risk status.

from custom_transformers import ColumnNameTransformer
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load pipeline and model
pipeline = joblib.load('../models/preprocessor_pipeline.pkl')
model = joblib.load('../models/lr_student_grade_model.pkl')

# Page config
st.set_page_config(page_title="Student GPA Predictor", layout="centered")

st.title("🎓 Student GPA Predictor")
st.markdown("Enter student information to predict GPA and identify at-risk status.")

# Input form
with st.form("student_form"):
    gender = st.selectbox("Gender", ['0', '1'])  # Assume 0 = Female, 1 = Male
    tutoring = st.selectbox("Tutoring Support", ['0', '1'])
    extracurricular = st.selectbox("Extracurricular Activities", ['0', '1'])
    sports = st.selectbox("Sports Participation", ['0', '1'])
    music = st.selectbox("Music Involvement", ['0', '1'])
    volunteering = st.selectbox("Volunteering", ['0', '1'])
    parentalsupport = st.selectbox("Parental Support", ['0', '1', '2'])  # Ordinal
    parentaleducation = st.selectbox("Parental Education Level", ['0', '1', '2'])  # Ordinal
    ethnicity = st.selectbox("Ethnicity", ['0', '1', '2', '3'])  # Nominal (to be one-hot encoded)
    studytimeweekly = st.slider("Study Time (hours per week)", 0, 30, 10)
    absences = st.slider("Number of Absences", 0, 50, 3)
    age = st.slider("Age", 13, 22, 16)

    submitted = st.form_submit_button("Predict GPA")

if submitted:
    input_data = pd.DataFrame({
        'gender': [int(gender)],
        'tutoring': [int(tutoring)],
        'extracurricular': [int(extracurricular)],
        'sports': [int(sports)],
        'music': [int(music)],
        'volunteering': [int(volunteering)],
        'parentalsupport': [int(parentalsupport)],
        'parentaleducation': [int(parentaleducation)],
        'ethnicity': [int(ethnicity)],
        'studytimeweekly': [studytimeweekly],
        'absences': [absences],
        'age': [age]
    })

    try:
        # Transform input
        input_transformed = pipeline.transform(input_data)

        # Predict GPA
        predicted_gpa = model.predict(input_transformed)[0]
        risk_status = "At Risk" if predicted_gpa < 2.0 else "Not At Risk"

        st.success(f"🎯 Predicted GPA: **{predicted_gpa:.2f}**")
        st.info(f"📌 Risk Status: **{risk_status}**")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
