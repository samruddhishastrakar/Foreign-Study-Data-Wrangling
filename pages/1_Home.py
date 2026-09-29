import streamlit as st

st.title("🌍 1. Home")

st.header("International Student Study Data Wrangling")

st.write("""
Data wrangling is the process of collecting, cleaning, transforming and
preparing raw data for analysis.

In this project, we use an international student dataset containing
demographic, financial, academic and lifestyle-related information.
""")

st.subheader("Project Objectives")

st.write("1. Load a CSV file using Pandas.")
st.write("2. Check the number of rows and columns.")
st.write("3. Identify missing values.")
st.write("4. Find and remove duplicate records.")
st.write("5. Fill missing numerical and categorical values.")
st.write("6. Understand class imbalance in Study Status.")
st.write("7. Balance the data using random oversampling.")
st.write("8. Create basic charts.")

st.subheader("Dataset Columns")

st.table({
    "Column": [
        "Student_ID",
        "Country",
        "Study_Level",
        "University_Type",
        "Age",
        "Tuition_Fee_USD",
        "Monthly_Living_Cost_USD",
        "Scholarship_Status",
        "English_Proficiency",
        "Accommodation_Type",
        "Part_Time_Work_Hours",
        "Academic_GPA",
        "Student_Satisfaction",
        "Study_Status"
    ],
    "Meaning": [
        "Unique student identification number",
        "Country where the student is studying",
        "Undergraduate or Postgraduate",
        "Public or Private university",
        "Student age",
        "Annual tuition fee in USD",
        "Monthly living cost in USD",
        "Scholarship status",
        "English proficiency level",
        "Type of accommodation",
        "Part-time work hours per week",
        "Academic GPA",
        "Student satisfaction rating",
        "Current study status"
    ]
})

st.subheader("Dataset Context")

st.write("""
The dataset represents students pursuing education abroad. It can be
used to explore financial, academic and lifestyle factors associated
with international student experiences.
""")

st.success("Go to Page 2 to load and inspect the data.")
