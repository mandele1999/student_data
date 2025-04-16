# App Guide

This guide provides an overview of using the interactive Streamlit application built for the Student Performance Prediction project. The app allows users (e.g., teachers, school administrators, researchers) to input student information and receive real-time predictions about their academic performance and risk level.

---

## 🛠 How the App Works

The app is powered by:

- A trained **Linear Regression model** for GPA prediction  
- Two **risk classification approaches**:
  - **Threshold-based**: Flags students as At Risk if predicted GPA < 2.0
  - **Classifier-based**: Uses a trained classification model to determine risk directly

### 🔄 Behind the Scenes

1. The user fills in a form with relevant student details.
2. Inputs are preprocessed using the saved transformation pipeline (includes custom transformers).
3. The regression model predicts the student’s GPA.
4. Two classification steps follow:
   - One checks if predicted GPA < 2.0
   - Another uses a trained classifier to output risk status
5. All results are displayed side by side.

---

## 🧾 Input Instructions

To get a prediction, the user must provide the following details:

| Feature               | Description                                     | Input Type       |
|----------------------|-------------------------------------------------|------------------|
| Age                  | Student's age in years                          | Number input     |
| Gender               | Student's gender                                | Dropdown (M/F)   |
| Study Time           | Weekly study time in hours                      | Slider           |
| Absences             | Number of school absences                       | Number input     |
| Parental Education   | Average education level of parents              | Dropdown         |
| Paid Classes         | Enrolled in extra paid classes                  | Dropdown (Yes/No)|
| Tutoring             | Receiving additional tutoring                   | Dropdown (Yes/No)|
| Internet Access      | Access to internet at home                      | Dropdown (Yes/No)|
| Health               | Current health status (1–5)                     | Slider           |
| Support Systems      | Family/school support participation             | Multiple dropdowns or Yes/No |
| ...                  | _(Additional features depending on your dataset)_| _As applicable_  |

_ℹ️ All fields must be filled correctly for the prediction to work. Use dropdowns and sliders where provided._

---

## Outputs Explained

After clicking the **"Predict"** button, three results are displayed:

1. **🎓 Predicted GPA**  
   A numeric value representing the expected academic performance of the student.  
   _Example: Predicted GPA: **3.42**_

2. **⚠️ Risk Flag (Threshold-Based)**  
   A classification label showing whether the student is At Risk based on GPA:  
   - ✅ Not At Risk → GPA ≥ 2.0  
   - ❌ At Risk → GPA < 2.0  
   _Example: This student is **Not At Risk** ✅_

3. **🧠 Risk Flag (Classifier-Based)**  
   A second label from a trained classification model predicting if a student is likely to be at risk.  
   _Example: Classifier Prediction: **At Risk** ❌_

Both risk flags are displayed to help educators **compare the two methods** and decide on interventions more confidently.

---

## 🖼 Screenshots (To Attach)

- ✅ Full input form interface
- 🎓 Predicted GPA display
- ⚠️ Threshold-based risk banner
- 🧠 Classifier-based risk message

---
