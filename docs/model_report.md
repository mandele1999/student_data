# Model Documentation

This document outlines the modeling approach, performance, and decisions made for the Student Performance Prediction project.

---

## Model Comparison Summary

This project involved both regression and classification tasks:

- **Regression**: Predict student GPA
- **Classification**: Identify students at risk of academic underperformance

### Models Tested

**Regression Models (for GPA prediction):**
- Linear Regression (_Best-performing model_)
- Random Forest Regressor
- Gradient Boosting Regressor
- Ridge Regression

**Classification Models (for Risk Flag):**
- Logistic Regression (_Selected model for classification_)
- Decision Tree Classifier
- Random Forest Classifier

---

## 📈 Performance Metrics

### Regression (GPA Prediction)

| Model                   | R² Score | MAE  |
|------------------------|----------|------|
| Linear Regression       | 0.95     | 0.16 |
| Random Forest Regressor| 0.92     | 0.19 |
| Gradient Boosting       | 0.93     | 0.24 |
| Ridge Regression        | --     | -- |

> **Final Model for GPA Prediction:** Linear Regression

---

### Classification (At-Risk Detection)

| Model                  | Accuracy | Precision | Recall | F1 Score |
|-----------------------|----------|-----------|--------|----------|
| Logistic Regression ✅ | 0.94     | 0.94      | 0.94   | 0.94     |
| Gradient Boosting      | 0.92     | 0.93      | 0.92   | 0.92     |
| Random Forest          | 0.92     | 0.92      | 0.92   | 0.93     |

> **Final Model for Risk Classification:** Logistic Regression

---

## Final Models Summary

### Linear Regression (GPA)

Chosen due to:
- **Simplicity & Interpretability** – Transparent to explain to educators.
- **Strong Performance** – Competitive R² and low MAE.
- **Deployment-Ready** – No need for complex tuning or dependencies.

---

### Logistic Regression (Risk Classification)

Chosen due to:
- **Generalization** – Performs well without overfitting.
- **Explainability** – Coefficients can inform which factors contribute to risk.
- **Complementary** – Enhances the rule-based method with data-driven logic.

---

## 🛠 Hyperparameter Tuning

- **Regression**: Minimal tuning for Ridge and ensemble models. Linear Regression performed best without tuning.
- **Classification**: Basic grid search was used to tune Logistic Regression and Decision Tree parameters.

---

## Risk Classification Approaches

Two approaches were used to identify students at academic risk:

### 1. **Rule-Based Approach**
- Based on **predicted GPA**
- Rule:  
  - GPA < 2.0 → At Risk  
  - GPA ≥ 2.0 → Not At Risk

### 2. **Classifier-Based Approach**
- A separate classification model trained to directly predict "At Risk" label using selected features.
- Benefits:
  - Handles nonlinear patterns in risk
  - Adds an extra validation layer to the rule-based method

Both results are shown in the app to give educators flexibility in decision-making.

---

## Limitations

- **Rule-Based Simplicity**: The 2.0 GPA threshold may not suit all institutions.
- **Classification Model Bias**: Trained on a labeled dataset that may inherit historical bias.
- **Limited Data**: Some important factors like household income or learning challenges were not included.
- **Explainability in Classifier Models**: Slightly lower transparency than rule-based thresholds.

---

## Conclusion

The combined use of a regression model and classification model provides a **robust, interpretable, and practical** system for early academic risk detection. This multi-model setup improves confidence and allows education stakeholders to act proactively.
