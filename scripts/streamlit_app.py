# This script is used to create a Streamlit web application for predicting student GPA and risk status.
# It uses the joblib library to load the pre-trained model and preprocessing pipeline.
# The application allows users to input student data and get predictions on GPA and risk status.

import streamlit as st
import pandas as pd
import joblib
from sklearn.base import BaseEstimator, TransformerMixin

st.set_page_config(page_title="Student GPA & Risk Predictor", layout="centered")
st.title("🎓 Student GPA & Risk Predictor")
st.markdown("Provide student details below to predict GPA and assess risk status.")

# Custom transformer to retain feature names
class ColumnNameTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, transformer, feature_names):
        self.transformer = transformer
        self.feature_names = feature_names

    def fit(self, X, y=None):
        self.transformer.fit(X, y)
        return self

    def transform(self, X):
        X_t = self.transformer.transform(X)
        return pd.DataFrame(X_t, columns=self.feature_names, index=X.index)

# Load models and preprocessing pipeline
@st.cache_resource
def load_components():
    pipeline = joblib.load("models/preprocessor_pipeline.pkl")
    reg_model = joblib.load("models/lr_student_grade_model.pkl")
    cls_model = joblib.load("models/logreg_risk_classifier_model.pkl")
    return pipeline, reg_model, cls_model

pipeline, reg_model, cls_model = load_components()

# st.write("Pipeline type:", type(pipeline))
# st.set_page_config(page_title="Student GPA & Risk Predictor", layout="centered")
# st.title("🎓 Student GPA & Risk Predictor")
# st.markdown("Provide student details below to predict GPA and assess risk status.")

# --- User Input Form ---
with st.form("student_form"):
    st.header("📋 Student Information")

    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", options=[None, 0, 1], format_func=lambda x: "Select Gender" if x is None else ("Female" if x == 0 else "Male"))
        age = st.number_input("Age", min_value=10, max_value=25, value=None, placeholder="Enter age (e.g., 17)")

    with col2:
        tutoring = st.selectbox("Receiving Tutoring?", options=[None, 0, 1], format_func=lambda x: "Select Option" if x is None else ("No" if x == 0 else "Yes"))
        extracurricular = st.selectbox("In Extracurriculars?", options=[None, 0, 1], format_func=lambda x: "Select Option" if x is None else ("No" if x == 0 else "Yes"))
        volunteering = st.selectbox("Volunteering?", options=[None, 0, 1], format_func=lambda x: "Select Option" if x is None else ("No" if x == 0 else "Yes"))

    with col3:
        sports = st.selectbox("Plays Sports?", options=[None, 0, 1], format_func=lambda x: "Select Option" if x is None else ("No" if x == 0 else "Yes"))
        music = st.selectbox("Plays Music?", options=[None, 0, 1], format_func=lambda x: "Select Option" if x is None else ("No" if x == 0 else "Yes"))

    parentalsupport = st.selectbox("Parental Support", options=[None, 1, 2, 3], format_func=lambda x: "Select Support Level" if x is None else {1: "Low", 2: "Medium", 3: "High"}[x])
    parentaleducation = st.selectbox("Parental Education", options=[None, 1, 2, 3], format_func=lambda x: "Select Education Level" if x is None else {1: "High School", 2: "Undergraduate", 3: "Postgraduate"}[x])
    ethnicity = st.selectbox("Ethnicity", options=[None, 0, 1, 2, 3], format_func=lambda x: "Select Ethnicity" if x is None else {0: "Caucasian", 1: "African American", 2: "Asian", 3: "Other"}[x])
    studytimeweekly = st.number_input("Study Time Weekly (hrs)", min_value=0, max_value=100, value=None, placeholder="e.g. 10")
    absences = st.number_input("Absences", min_value=0, max_value=100, value=None, placeholder="e.g. 3")

    submitted = st.form_submit_button("🔍 Predict")

# --- Prediction Logic ---
if submitted:
    if None in (gender, age, tutoring, extracurricular, volunteering, sports, music,
                parentalsupport, parentaleducation, ethnicity, studytimeweekly, absences):
        st.warning("Please fill in all required fields before submitting.")
    else:
        st.success("Form submitted successfully! Generating Insights...")
        # proceed with prediction
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
        # Preprocess input
        transformed_input = pipeline.transform(input_data)

        # GPA prediction
        predicted_gpa = reg_model.predict(transformed_input)[0]
        gpa_based_risk = "⚠️ At Risk" if predicted_gpa < 2.0 else "✅ Not At Risk"

        # Risk classification
        predicted_risk = cls_model.predict(transformed_input)[0]
        classifier_based_risk = "⚠️ At Risk" if predicted_risk == 1 else "✅ Not At Risk"

        # Display Results
        st.subheader("📈 Prediction Results")

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="🎯 Predicted GPA", value=f"{predicted_gpa:.2f}")
            st.markdown(f"**GPA-Based Risk Status**: {gpa_based_risk}")
        with col2:
            st.metric(label="📊 Classifier-Based Risk", value=classifier_based_risk)
            st.markdown("**(Logistic Regression)**")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
