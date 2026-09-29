import streamlit as st

st.set_page_config(
    page_title="International Student Study Analysis",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 International Student Study Data Wrangling")

st.write("""
A beginner-friendly Data Wrangling project using Python, Pandas,
Matplotlib and Streamlit to analyze international student study data.
""")

st.subheader("What will we learn?")

st.write("""
This project demonstrates the basic data-wrangling workflow:

1. Load and understand data
2. Inspect the dataset
3. Identify missing values and duplicates
4. Clean the dataset
5. Handle class imbalance
6. Create visualizations
""")

st.info(
    "Use the pages in the left sidebar to go through the project step by step."
)

st.subheader("Tools Used")

st.write("• Python")
st.write("• Pandas")
st.write("• Matplotlib")
st.write("• Streamlit")

st.subheader("Project Dataset")

st.write("""
The dataset represents students studying internationally. It contains
information about their destination country, study level, university
type, tuition fees, living costs, scholarships, English proficiency,
accommodation, part-time work, GPA, satisfaction and study status.
""")

st.subheader("Dataset Variables")

st.write("""
* Student_ID – Unique student identification number

* Country – Country where the student is studying

* Study_Level – Undergraduate or Postgraduate

* University_Type – Public or Private university

* Age – Student age

* Tuition_Fee_USD – Annual tuition fee in US dollars

* Monthly_Living_Cost_USD – Estimated monthly living cost

* Scholarship_Status – Whether the student receives a scholarship

* English_Proficiency – Student's English proficiency level

* Accommodation_Type – Type of accommodation

* Part_Time_Work_Hours – Part-time working hours per week

* Academic_GPA – Academic GPA on a 4.0 scale

* Student_Satisfaction – Satisfaction rating from 1 to 5

* Study_Status – Current study status
""")

st.success("Start with Page 1 to begin the project.")
