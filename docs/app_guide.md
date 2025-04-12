This guide provides an overview of using the interactive Streamlit application built for the Student Performance Prediction project. The app allows users (e.g., teachers, school administrators, researchers) to input student information and receive real-time predictions about their academic performance and risk level.

## 🛠 How the App Works
The app is powered by a trained Linear Regression model for GPA prediction and a rule-based classifier that flags students as At Risk if their predicted GPA is below a set threshold (2.0).

### 🔄 Behind the Scenes:
1. The user fills in a form with relevant student details.
2. Inputs are preprocessed using the saved data pipeline.
3. The regression model predicts the student’s GPA.
4. A classification step checks if the GPA < 2.0.
5. Results are displayed instantly on the screen.

### 🧾 Input Instructions
To get a prediction, the user must provide the following details:

_(To insert table of expected inputs)_

_ℹ️ All fields must be filled correctly for the prediction to work. Use dropdowns and sliders where provided._

## Outputs Explained
After clicking the "Predict" button, two results are displayed:
Predicted GPA - A numeric value representing the expected academic performance of the student.
Example: _Predicted GPA: 3.42_

Risk Flag - A classification label showing whether the student is at risk.
Based on the rule:
_At Risk → GPA < 2.0_
_Not At Risk → GPA ≥ 2.0_

Example: This student is **Not At Risk** ✅
---
_To attach screenshots:_

A screenshot of the full input form
The predicted GPA output
At-risk warning banner
