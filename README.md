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
student_performance_project/
│
├── data/
│   ├── raw/                          
│   ├── processed/                   
│   └── feature_engineered_student_data.csv
│
├── models/
│   ├── student_gpa_regression_model.pkl
│   └── student_data_preprocessing_pipeline.pkl
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb  
│   ├── 02_feature_engineering.ipynb 
│   └── 03_modeling.ipynb            
│
├── scripts/
│   └── streamlit_app.py             
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## How to Run This Project

### 1.Clone the Repository

```plaintext
git `clone` https://github.com/mandele1999/student_performance_project.git
cd student_performance_project
```

### 2. Install Required Packages

```plaintext
pip install -r requiremnts.txt
```

### 3. Launch the Streamlit App

```plaintext
cd scripts
streamlit run streamlit_app.py
```

## Models and Performance

- Best-performing model: **Linear Regression**
- Target: **GPA prediction**
- Threshold for risk classification: **GPA < 2.0**

## Features in the Streamlit App

- Enter student details (age, gender, absences, etc.)
- Predict GPA using a trained regression model
- Flag students as "At Risk" or "Not At Risk"
- Real-time feedback for proactive decision-making

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Thanks to the open-source Python community, Kaggle-style student datasets, and all mentors who support data science learning and development.

[Data Source](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)
