Mini Project Report

International Student Study Data Wrangling using Python and Streamlit

1. Introduction

Data wrangling is the process of collecting, cleaning, transforming and preparing raw data for analysis.

In this project, an international student dataset is processed using Python and Pandas and presented through a Streamlit application.

The dataset contains demographic, financial, academic and lifestyle-related information about students studying internationally.

2. Objectives

- Load the international student dataset.
- Understand the structure and characteristics of the data.
- Identify missing values.
- Detect and remove duplicate records.
- Handle missing numerical and categorical values.
- Examine the distribution of student study status.
- Handle class imbalance using random oversampling.
- Create meaningful data visualizations.
- Build an interactive Streamlit application.

3. Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit

4. Dataset Description

The dataset contains the following variables:

Variable| Description
Student_ID| Unique student identification number
Country| Country where the student is studying
Study_Level| Undergraduate or Postgraduate
University_Type| Public or Private university
Age| Student age
Tuition_Fee_USD| Annual tuition fee in US dollars
Monthly_Living_Cost_USD| Estimated monthly living cost
Scholarship_Status| Scholarship availability
English_Proficiency| English proficiency level
Accommodation_Type| Type of accommodation
Part_Time_Work_Hours| Part-time working hours per week
Academic_GPA| Academic GPA on a 4.0 scale
Student_Satisfaction| Satisfaction rating from 1 to 5
Study_Status| Current study status

5. Data Cleaning

The following operations are performed:

1. Duplicate records are identified and removed using "drop_duplicates()".

2. Missing numerical values such as tuition-related, GPA and satisfaction values are filled using the mean of the respective column.

3. Missing categorical values are filled using the mode of the respective column.

4. The dataset is checked again after cleaning to confirm that missing values have been handled.

6. Data Balancing

The "Study_Status" column contains multiple categories representing the student's current status.

The distribution of the categories is first checked using "value_counts()".

If one category contains fewer records than another, Random Oversampling is used. Records from smaller categories are randomly selected with replacement until all categories have the same number of observations.

This demonstrates the concept of handling class imbalance.

7. Visualization

The project creates the following visualizations:

- Study Status distribution bar chart
- Students by Country bar chart
- Tuition Fee distribution histogram
- Tuition Fee vs Academic GPA scatter plot
- Monthly Living Cost vs Student Satisfaction scatter plot
- Academic GPA box plot

These visualizations provide a basic understanding of the demographic, financial and academic characteristics of international students.

8. Streamlit Application

The application contains five pages:

Page 1 — Home

Introduces the project, objectives and dataset variables.

Page 2 — Load and Understand Data

Displays records, dimensions, column names, data types, missing values, statistics, duplicates and Study Status distribution.

Page 3 — Clean Data

Removes duplicate records and handles missing numerical and categorical values.

Page 4 — Balance Data

Examines Study Status imbalance and performs random oversampling.

Page 5 — Data Visualization

Creates charts to explore country distribution, tuition fees, academic GPA, living costs and student satisfaction.

9. Learning Outcomes

After completing this project, students can:

- Load CSV files using Pandas.
- Inspect a dataset.
- Identify missing values.
- Remove duplicate records.
- Handle numerical missing values using the mean.
- Handle categorical missing values using the mode.
- Understand class imbalance.
- Perform random oversampling.
- Create basic charts using Matplotlib.
- Build a multi-page Streamlit application.
- Download processed datasets from Streamlit.

10. Conclusion

This project provides a beginner-friendly introduction to data wrangling using Python, Pandas and Streamlit.

It demonstrates how international student data can be loaded, inspected, cleaned, balanced and visualized.

The project also shows how data-wrangling techniques can be combined with an interactive Streamlit interface to make data analysis easier to understand.