# 📘 Project Overview: Student Performance Prediction

## 🎯 Objective

This project focuses on predicting academic performance among secondary school students by leveraging machine learning techniques. It aims to:

- **Predict Grade Point Average (GPA)** using regression models.
- **Classify students as at-risk or not-at-risk** based on their predicted GPA.
- **Identify key features** influencing student performance.
- **Empower educators** with insights for timely, data-driven interventions.

---

## 🧠 Motivation

Identifying students at academic risk early allows educators to intervene with support programs, improving outcomes. This project provides a predictive tool to help schools flag students needing attention and allocate resources effectively.

---

## 🔄 Workflow Summary

The project follows a structured data science workflow from raw data to deployment:

Raw Data → Preprocessing → Feature Engineering → Modeling → Evaluation → Deployment

📌 _A detailed workflow diagram will be included here._

---

## 📓 Notebook Descriptions

| Notebook | Description |
|----------|-------------|
| **01_data_preprocessing.ipynb** | Handles raw data loading, cleaning, and preparation (missing value handling, encoding binary/ordinal features, etc.). |
| **02_feature_engineering.ipynb** | Applies transformations using `ColumnTransformer`, engineers the final features, adds the target label `risk_flag`, and exports the final processed dataset. |
| **03_modeling.ipynb** | Loads processed data, trains multiple regression and classification models, evaluates them, and selects the best-performing models. |

---

## 🧪 Modeling Steps

- **Regression Models**:
  - Linear Regression (best-performing)
  - Ridge Regression
  - XGBoost Regressor
- **Classification**:
  - After predicting GPA, a classification label (`risk_flag`) is derived by applying a threshold:
    - **Threshold decision**: Students with predicted **GPA < 2.0** are classified as **"At Risk"**.
  - Classification models (e.g., Logistic Regression, Random Forest) were explored but not used in deployment since regression + threshold performed better.

---

## ⚙️ Key Decisions

- **Risk Threshold**: A GPA of **2.0** was selected as the cutoff for flagging students as at risk, based on educational standards.
- **Feature Engineering**: One-hot encoding for nominal features, scaling for numerical features, and passthrough for binary/ordinal.
- **Deployment Strategy**: A **Streamlit** application was developed to make predictions in real time from user input.

---

## 🚀 Deployment

The final model and preprocessing pipeline are deployed in a Streamlit app that allows users to:

- Enter student information
- Predict GPA
- Flag whether the student is “At Risk”
- Gain instant, actionable feedback
"""
