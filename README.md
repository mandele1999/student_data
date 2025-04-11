# 🏫 Student Performance Prediction

## Objectives

The primary objective of this project is to leverage data science techniques to `analyze` and `predict` student performance in secondary school. The project aims to assist educators and administrators in identifying at-risk students and understanding key factors influencing academic success. Below are the specific goals of the project:

- **Predict Student Grades**: Develop a predictive model to estimate student grades based on various demographic, academic, and personal features.

- **Identify At-Risk Students**: Classify students who may be at risk of underperforming, enabling targeted interventions to support them.

- **Feature Analysis**: Analyze and identify the most influential factors contributing to student performance, such as parental education, family background, health, and study habits.

- **Provide Actionable Insights**: Offer insights and recommendations to educators for improving student outcomes, based on data-driven analysis.

- **Build a User-Friendly Tool (Optional)**: Create an interactive dashboard or application to allow users to input data and receive predictions or insights in real-time.

## 📁 Project Structure

```plaintext
student-performance-project/
│
├── data/
│   ├── raw/                          # Raw data files (if any)
│   ├── processed/                    # Cleaned data (optional)
│   └── feature_engineered_student_data.csv
│
├── models/
│   ├── student_gpa_regression_model.pkl
│   └── student_data_preprocessing_pipeline.pkl
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb  # Data loading, cleaning, EDA
│   ├── 02_feature_engineering.ipynb # Feature transformation pipeline
│   └── 03_modeling.ipynb            # Regression & risk classification
│
├── scripts/
│   └── streamlit_app.py             # Streamlit web app
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE (optional)
```

## How to Run This Project

### 1.Clone the Repository

```plaintext
git clone https://github.com/mandele1999/student-performance-project.git
cd student-performance-project
```

[Data Source](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)
