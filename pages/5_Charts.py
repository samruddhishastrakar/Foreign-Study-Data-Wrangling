import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 5. Data Visualization")

df = pd.read_csv("data/international_study_data.csv")

# Simple cleaning
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


# ---------------------------------------------------
# 1. STUDY STATUS DISTRIBUTION
# ---------------------------------------------------

st.subheader("1. Study Status Distribution")

status_count = df["Study_Status"].value_counts()

fig, ax = plt.subplots()

status_count.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Study Status")
ax.set_ylabel("Number of Students")
ax.set_title("International Student Study Status")

st.pyplot(fig)


# ---------------------------------------------------
# 2. STUDENTS BY COUNTRY
# ---------------------------------------------------

st.subheader("2. Students by Country")

country_count = df["Country"].value_counts()

fig, ax = plt.subplots()

country_count.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Country")
ax.set_ylabel("Number of Students")
ax.set_title("Students by Study Destination")

plt.xticks(rotation=45)

st.pyplot(fig)


# ---------------------------------------------------
# 3. TUITION FEE DISTRIBUTION
# ---------------------------------------------------

st.subheader("3. Tuition Fee Distribution")

fig, ax = plt.subplots()

ax.hist(
    df["Tuition_Fee_USD"],
    bins=10
)

ax.set_xlabel("Tuition Fee (USD)")
ax.set_ylabel("Number of Students")
ax.set_title("Distribution of Tuition Fees")

st.pyplot(fig)


# ---------------------------------------------------
# 4. TUITION VS GPA
# ---------------------------------------------------

st.subheader("4. Tuition Fee vs Academic GPA")

fig, ax = plt.subplots()

ax.scatter(
    df["Tuition_Fee_USD"],
    df["Academic_GPA"]
)

ax.set_xlabel("Tuition Fee (USD)")
ax.set_ylabel("Academic GPA")
ax.set_title("Tuition Fee vs Academic GPA")

st.pyplot(fig)


# ---------------------------------------------------
# 5. LIVING COST VS SATISFACTION
# ---------------------------------------------------

st.subheader("5. Living Cost vs Student Satisfaction")

fig, ax = plt.subplots()

ax.scatter(
    df["Monthly_Living_Cost_USD"],
    df["Student_Satisfaction"]
)

ax.set_xlabel("Monthly Living Cost (USD)")
ax.set_ylabel("Student Satisfaction")
ax.set_title("Living Cost vs Student Satisfaction")

st.pyplot(fig)


# ---------------------------------------------------
# 6. GPA DISTRIBUTION
# ---------------------------------------------------

st.subheader("6. Academic GPA Distribution")

fig, ax = plt.subplots()

ax.boxplot(
    df["Academic_GPA"]
)

ax.set_ylabel("Academic GPA")
ax.set_title("Academic GPA Box Plot")

st.pyplot(fig)


# ---------------------------------------------------
# OBSERVATIONS
# ---------------------------------------------------

st.subheader("Simple Observations")

st.write(
    "• The Study Status chart shows the distribution of students "
    "across different study-status categories."
)

st.write(
    "• The country chart shows the number of students studying "
    "in different international destinations."
)

st.write(
    "• The tuition histogram shows the distribution of tuition fees "
    "among the students."
)

st.write(
    "• The Tuition Fee vs GPA scatter plot helps explore the "
    "relationship between education cost and academic performance."
)

st.write(
    "• The Living Cost vs Satisfaction scatter plot helps explore "
    "the relationship between living expenses and student satisfaction."
)

st.write(
    "• The GPA box plot shows the spread of academic performance "
    "and can help identify possible outliers."
)

st.success(
    "Project completed! You have now performed a basic international "
    "student data-wrangling and visualization workflow."
)
