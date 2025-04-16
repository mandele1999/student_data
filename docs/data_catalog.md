# 📘 Data Dictionary – Student Performance Dataset

| Feature              | Description                                                                 | Type       | Values / Range                                     |
|----------------------|-----------------------------------------------------------------------------|------------|----------------------------------------------------|
| `StudentID`          | Unique identifier for each student                                          | Numeric    | 1001 – 3392                                        |
| `Age`                | Age of the student                                                          | Numeric    | 15 – 18                                            |
| `Gender`             | Gender of the student                                                       | Categorical| 0 = Male, 1 = Female                               |
| `Ethnicity`          | Ethnicity category                                                          | Categorical| 0 = Caucasian, 1 = African American, 2 = Asian, 3 = Other |
| `ParentalEducation`  | Education level of parents                                                  | Categorical| 0 = None, 1 = High School, 2 = Some College, 3 = Bachelor's, 4 = Higher |
| `StudyTimeWeekly`    | Weekly study time in hours                                                  | Numeric    | 0 – 20                                             |
| `Absences`           | Number of school absences                                                   | Numeric    | 0 – 30                                             |
| `Tutoring`           | Whether the student receives tutoring support                               | Binary     | 0 = No, 1 = Yes                                    |
| `ParentalSupport`    | Level of parental support                                                   | Categorical| 0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High |
| `Extracurricular`    | Participation in any extracurricular activity                               | Binary     | 0 = No, 1 = Yes                                    |
| `Sports`             | Participation in sports                                                     | Binary     | 0 = No, 1 = Yes                                    |
| `Music`              | Participation in music-related activities                                   | Binary     | 0 = No, 1 = Yes                                    |
| `Volunteering`       | Participation in volunteering/community service                             | Binary     | 0 = No, 1 = Yes                                    |
| `GPA`                | Grade Point Average                                                         | Numeric    | 2.0 – 4.0                                          |
| `GradeClass`         | Classification of student based on GPA (target for classification)          | Categorical| e.g. A, B, C, D, F (based on thresholds)       |


0. 'A' (GPA >= 3.5)
1. 'B' (3.0 <= GPA < 3.5)
2. 'C' (2.5 <= GPA < 3.0)
3. 'D' (2.0 <= GPA < 2.5)
4. 'F' (GPA < 2.0)
