# Model Documentation
This document outlines the modeling approach, performance, and decisions made for the Student Performance Prediction project.

## Model Comparison Summary
In this project, we focused on regression models to predict the GPA of secondary school students. Classification was not performed using traditional classification algorithms; instead, we applied a rule-based risk flag after predicting GPA.

### Models Tested:
- Linear Regression ✅ (Best-performing model)
- Random Forest Regressor
- Gradient Boosting Regressor
- _Ridge Regression_

## Performance Metrics
The models were evaluated using the following regression metrics:

Model          R2 Score        MAE
- 
-
-
-
 ## Final Model: Linear Regression
 
Linear Regression was chosen for the following reasons:
- **Simplicity & Interpretability** – Easy to understand and explain predictions to stakeholders.
- **Strong Baseline** – Performed competitively across key metrics.
- **Generalization** – Low overfitting compared to more complex models.

## Hyperparameter Tuning
Only minimal tuning was done, mainly for regularized models like Ridge and ensemble models. Since Linear Regression had no hyperparameters and performed best, no further tuning was needed.

## Risk Classification
Rather than using a classification model, we derived a binary risk flag from the predicted GPA using a business-rule threshold:

- Threshold: GPA < 2.0 → At Risk

- Otherwise → Not At Risk

This rule simplifies deployment and makes interpretation easier for end-users such as educators.

## Limitations
- **Rule-Based Risk Classification**: The 2.0 threshold is static and may not generalize across all school systems.

- **Limited Feature Set**: The dataset doesn’t include some potentially influential features (e.g., socioeconomic status, learning disabilities).

- **Bias Risk**: Predictions depend on historical data, which may encode bias.


