# Student Performance Predictor

## Objectives

The primary objective of this project is to leverage data science techniques to `analyze` and `predict` student performance in secondary school. The project aims to assist educators and administrators in identifying at-risk students and understanding key factors influencing academic success. Below are the specific goals of the project:

- **Predict Student Grades**: Develop a predictive model to estimate student grades based on various demographic, academic, and personal features.

- **Identify At-Risk Students**: Classify students who may be at risk of underperforming, enabling targeted interventions to support them.

- **Feature Analysis**: Analyze and identify the most influential factors contributing to student performance, such as parental education, family background, health, and study habits.

- **Provide Actionable Insights**: Offer insights and recommendations to educators for improving student outcomes, based on data-driven analysis.

- **Build a User-Friendly Tool (Optional)**: Create an interactive dashboard or application to allow users to input data and receive predictions or insights in real-time.

### Student Information
**Student ID**
StudentID: A unique identifier assigned to each student (1001 to 3392).

### Demographic Details

- Age: The age of the students ranges from 15 to 18 years.
- Gender: Gender of the students, where 0 represents Male and 1 represents Female.
- Ethnicity: The ethnicity of the students, coded as follows:
  
0: Caucasian
1: African American
2: Asian
3: Other

- ParentalEducation: The education level of the parents, coded as follows:
0: None
1: High School
2: Some College
3: Bachelor's
4: Higher

### Study Habits

- StudyTimeWeekly: Weekly study time in hours, ranging from 0 to 20.
- Absences: Number of absences during the school year, ranging from 0 to 30.
- Tutoring: Tutoring status, where 0 indicates No and 1 indicates Yes.
  
### Parental Involvement

- ParentalSupport: The level of parental support, coded as follows:
0: None
1: Low
2: Moderate
3: High
4: Very High

### Extracurricular Activities

Extracurricular: Participation in extracurricular activities, where 0 indicates No and 1 indicates Yes.
- Sports: Participation in sports, where 0 indicates No and 1 indicates Yes.
- Music: Participation in music activities, where 0 indicates No and 1 indicates Yes.
- Volunteering: Participation in volunteering, where 0 indicates No and 1 indicates Yes.

### Academic Performance

**GPA**: Grade Point Average on a scale from 2.0 to 4.0, influenced by study habits, parental involvement, and extracurricular activities.
**Target Variable**: Grade Class
**GradeClass**: Classification of students' grades based on GPA:
0: 'A' (GPA >= 3.5)
1: 'B' (3.0 <= GPA < 3.5)
2: 'C' (2.5 <= GPA < 3.0)
3: 'D' (2.0 <= GPA < 2.5)
4: 'F' (GPA < 2.0)
