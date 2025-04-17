# 📘 Project Overview: Student Performance Prediction

## Objective

This project focuses on predicting academic performance among secondary school students by leveraging machine learning techniques. It aims to:

- **Predict Grade Point Average (GPA)** using regression models.
- **Classify students as at-risk or not-at-risk** using both a GPA threshold and a dedicated classification model.
- **Identify key features** influencing student performance.
- **Empower educators** with insights for timely, data-driven interventions.

---

## Motivation

Identifying students at academic risk early allows educators to intervene with support programs, improving outcomes. This project provides a predictive tool to help schools flag students needing attention and allocate resources effectively.

---

## 🔄 Workflow Summary

The project follows a structured data science workflow from raw data to deployment:

`Raw Data → Preprocessing → Feature Engineering → Modeling → Evaluation → Deployment`

📌 _A visual workflow diagram is planned to be included here._

---

## 📓 Notebook Descriptions

| Notebook | Description |
|----------|-------------|
| **01_data_preprocessing.ipynb** | Loads and cleans raw student data, performs EDA, handles missing values, and prepares the dataset for transformation. |
| **02_feature_engineering.ipynb** | Applies transformations via `ColumnTransformer`, generates final features, and creates both GPA and classification targets (risk flag). |
| **03_modeling.ipynb** | Trains and evaluates regression and classification models, compares performance, and selects the best models for deployment. |

---

## Modeling Steps

### Regression (GPA Prediction)

- Models tested:
  - Linear Regression ✅
  - Ridge Regression
  - Gradient Boosting Regressor
  - Random Forest Regressor
- **Final choice**: Linear Regression (best trade-off between simplicity and performance)

### Classification (At-Risk Detection)

Two approaches were used to flag students as at risk:

1. **Rule-Based Threshold**:  
   - GPA < 2.0 → At Risk  
   - GPA ≥ 2.0 → Not At Risk

2. **Classifier-Based Prediction**:
   - Models tested:
     - Logistic Regression ✅
     - Random Forest Classifier
     - Decision Tree Classifier
   - **Final choice**: Logistic Regression (best balance of accuracy and interpretability)

---

## Key Decisions

- **Risk Threshold**: A GPA of **2.0** was chosen based on academic standards and used for both rule-based logic and labeling training data for classification.
- **Feature Engineering**:
  - Numerical features were scaled.
  - Categorical features were one-hot encoded.
  - Ordinal and binary features were passed through or label encoded.
- **Deployment Strategy**:
  - A **Streamlit** web app was developed to deliver real-time predictions and risk classification based on user inputs.
  - Both the **GPA prediction** and **classification output** are displayed to aid educators in their decisions.

---

## Deployment

The final solution is hosted as an interactive **Streamlit application** where users can:

- Input student profile data via a form
- Receive an instant **GPA prediction**
- View a **risk flag** from both the rule-based and classifier-based methods
- Use the results for early academic interventions

📌 _Screenshots of the deployed interface and prediction output are included in the App Guide._

## Made with 💡 by Frank

This project was developed with a focus on explainability and real-world application in the education sector.  
Feel free to fork, star ⭐, or contribute!

_🔗 Check out the app: [Streamlit App Link Here([streamlit_app.py](https://student-performance-predict-app.streamlit.app/))]_  
_🗂️ Explore the repo: [[GitHub Repo Link Here](https://github.com/mandele1999/student_performance_project)]_

