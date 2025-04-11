# Student Performance Prediction

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Model: Linear Regression](https://img.shields.io/badge/Model-Linear%20Regression-blue)](notebooks/03_modeling.ipynb)
[![RMSE: 0.20](https://img.shields.io/badge/RMSE-0.20-brightgreen)](notebooks/03_modeling.ipynb)


---

## 📘 Overview

This project focuses on predicting academic performance among secondary school students using machine learning. The goal is to:

- Predict students' **Grade Point Average (GPA)**
- Classify students as **at-risk** based on predicted GPA (below a threshold)
- Uncover key factors that influence student success

This project empowers educators with early warnings and data-driven insights by combining academic, behavioral, and demographic features.

---

## 📊 Dataset

The dataset contains a range of features such as:

- Demographics (e.g., gender, ethnicity, age)
- Academic indicators (e.g., study time, absences, parental education)
- Behavioral traits (e.g., extracurriculars, volunteering, tutoring)

📄 A full breakdown of features, data types, and example values can be found in the [Data Catalog](docs/data_catalog.md) under the `docs/` folder.

---

## 🎯 Features / Objectives

- ✅ **GPA Prediction**: Estimate students' GPA using regression techniques
- ✅ **At-Risk Classification**: Flag students as "At Risk" when the predicted GPA is below 2.0
- ✅ **Feature Importance**: Analyze key factors driving academic performance
- ✅ **Streamlit App**: Provide a simple user interface for live predictions
- ✅ **Insights for Educators**: Offer actionable data to improve student outcomes

---

## Installation & Setup

### 1. Clone the Repository

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

## 📁 Project Structure

```plaintext
student_performance_project/
│
├── data/
│   ├── raw/                          
│   ├── processed/                   
│   └── feature_engineered_student_data.csv
├── docs/                                                 
│   └── data_catalog.md
|
├── models/
│   ├── lr_student_grade_model.pkl
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

## Usage (Streamlit App)

Once the app is running:

- Enter student details (age, study time, absences, etc.)
- Predict GPA using a trained Linear Regression model
- See a flag if the student is At Risk (GPA < 2.0)
- Get instant feedback on potential student performance

## Results/Insights

✅ Best Model: Linear Regression for GPA prediction

✅ Risk Classification: GPA threshold-based approach using predicted values

✅ Top Influencers: Parental education, study time, absences, and support systems emerged as significant predictors

✅ App Feedback: Real-time, easy-to-understand results to assist decision-makers in schools

## 🤝 Contributing

Contributions are welcome! If you'd like to add improvements, raise issues, or contribute new ideas (e.g., dashboard features, model tuning, or alternative algorithms):

1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Make your changes and commit (`git commit -am 'Add new feature'`)
4. Push the branch (`git push origin feature-xyz`)
5. Create a Pull Request


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Open-source Python tools and libraries
- Contributors and mentors from the data science community
- [Student Performance Dataset on Kaggle](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)
