import streamlit as st
import pandas as pd

st.title("📂 2. Load and Understand Data")

uploaded_file = st.file_uploader(
    "Upload the International Study CSV file",
    type="csv"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/international_study_data.csv")
    st.info("Using the sample international_study_data.csv file.")

st.subheader("First 10 Records")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.subheader("Number of Rows and Columns")

col1, col2 = st.columns(2)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])

st.subheader("Column Names")

st.write(list(df.columns))

st.subheader("Data Types")

st.dataframe(
    df.dtypes.to_frame("Data Type"),
    use_container_width=True
)

st.subheader("Missing Values")

st.dataframe(
    df.isnull().sum().to_frame("Missing Values"),
    use_container_width=True
)

st.subheader("Basic Statistics")

st.dataframe(
    df.describe(include="all").transpose(),
    use_container_width=True
)

st.subheader("Number of Duplicate Rows")

st.write(df.duplicated().sum())

st.subheader("Study Status Distribution")

st.dataframe(
    df["Study_Status"].value_counts().to_frame("Number of Students")
)

st.success("Now go to Page 3 to clean the data.")
