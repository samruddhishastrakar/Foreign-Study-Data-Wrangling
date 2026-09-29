import streamlit as st
import pandas as pd

st.title("⚖️ 4. Balance Data")

df = pd.read_csv("data/international_study_data.csv")

# Clean the data first
df = df.drop_duplicates()

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

st.subheader("Step 1: Check Study Status Distribution")

status_count = df["Study_Status"].value_counts()

st.dataframe(
    status_count.to_frame("Number of Students")
)

st.bar_chart(status_count)

st.write("""
If some Study Status categories contain many more records than others,
the dataset is considered imbalanced.
""")

st.subheader("Step 2: Balance the Data")

st.write("Original distribution:")

st.dataframe(
    df["Study_Status"].value_counts().to_frame("Students")
)

max_count = df["Study_Status"].value_counts().max()

balanced_groups = []

for status in df["Study_Status"].unique():

    group = df[df["Study_Status"] == status]

    balanced_group = group.sample(
        n=max_count,
        replace=True,
        random_state=42
    )

    balanced_groups.append(balanced_group)

balanced_df = pd.concat(
    balanced_groups,
    ignore_index=True
)

balanced_df = balanced_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

st.subheader("After Balancing")

balanced_count = balanced_df["Study_Status"].value_counts()

st.dataframe(
    balanced_count.to_frame("Students")
)

st.bar_chart(balanced_count)

st.dataframe(
    balanced_df.head(20),
    use_container_width=True
)

csv = balanced_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Balanced Data",
    csv,
    "balanced_international_study_data.csv",
    "text/csv"
)

st.success(
    "The minority Study Status categories were increased using "
    "Random Oversampling."
)

st.info("""
### Simple idea behind balancing

Suppose the dataset contains:

Currently Enrolled = 160 students  
Graduated = 60 students  
Withdrawn = 20 students

Random oversampling selects records from the smaller categories again
with replacement until each category has the same number of records.

This technique is called *Random Oversampling*.
""")
