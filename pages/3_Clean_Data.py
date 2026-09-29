import streamlit as st
import pandas as pd

st.title("🧹 3. Clean Data")

df = pd.read_csv("data/international_study_data.csv")

st.subheader("Before Cleaning")

st.write("Missing values:")
st.dataframe(
    df.isnull().sum().to_frame("Missing Values")
)

st.write(
    "Duplicate rows:",
    df.duplicated().sum()
)

st.subheader("Step 1: Remove Duplicate Rows")

df = df.drop_duplicates()

st.write(
    "Rows after removing duplicates:",
    len(df)
)

st.subheader("Step 2: Fill Missing Numerical Values")

numeric_columns = [
    "Age",
    "Tuition_Fee_USD",
    "Monthly_Living_Cost_USD",
    "Part_Time_Work_Hours",
    "Academic_GPA",
    "Student_Satisfaction"
]

for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].mean()
    )

st.write("Missing numerical values have been filled using the mean.")

st.subheader("Step 3: Fill Missing Categorical Values")

categorical_columns = [
    "Country",
    "Study_Level",
    "University_Type",
    "Scholarship_Status",
    "English_Proficiency",
    "Accommodation_Type",
    "Study_Status"
]

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(
            df[column].mode()[0]
        )

st.write("Missing categorical values have been filled using the mode.")

st.subheader("Missing Values After Cleaning")

st.dataframe(
    df.isnull().sum().to_frame("Missing Values")
)

st.subheader("Cleaned Data")

st.dataframe(
    df,
    use_container_width=True
)

st.success("Cleaning completed!")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Cleaned Data",
    csv,
    "cleaned_international_study_data.csv",
    "text/csv"
)

st.info("""
### What did we do?

* Removed duplicate rows using drop_duplicates()

* Filled missing numerical values using the mean

* Filled missing categorical values using the mode

* Checked the dataset again after cleaning
""")
