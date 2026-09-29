International Student Study Data Wrangling

Beginner Mini Project

This is a beginner-level Data Wrangling project created using:

- Python
- Pandas
- Matplotlib
- Streamlit

The project uses an international student dataset containing demographic, financial, academic and lifestyle-related information.

Pages

Page 1 — Home

Introduction, project objectives and dataset information.

Page 2 — Load and Understand Data

Learn:

- "read_csv()"
- "head()"
- "shape"
- "dtypes"
- "isnull()"
- "describe()"
- "duplicated()"
- "value_counts()"

Page 3 — Clean Data

Learn:

- "drop_duplicates()"
- "fillna()"
- "mean()"
- "mode()"

Missing numerical values are handled using the mean, while missing categorical values are handled using the mode.

Page 4 — Balance Data

Learn:

- "value_counts()"
- Class imbalance
- Random oversampling
- "sample()"
- "concat()"

The smaller Study Status categories are increased using random sampling with replacement.

Page 5 — Data Visualization

Learn:

- Bar charts
- Histograms
- Scatter plots
- Box plots

The project visualizes:

- Study Status distribution
- Students by Country
- Tuition Fee distribution
- Tuition Fee vs Academic GPA
- Living Cost vs Student Satisfaction
- Academic GPA distribution

Installation

Install Python 3.10 or newer.

Open Command Prompt or Terminal in the project folder.

Run:

pip install -r requirements.txt

Then run:

streamlit run app.py

Dataset

The dataset contains the following variables:

- Student ID
- Country
- Study Level
- University Type
- Age
- Tuition Fee
- Monthly Living Cost
- Scholarship Status
- English Proficiency
- Accommodation Type
- Part-Time Work Hours
- Academic GPA
- Student Satisfaction
- Study Status

The dataset intentionally contains missing values and duplicate records so that data-cleaning techniques can be demonstrated.

The Study Status variable is also imbalanced so that Random Oversampling can be demonstrated.

Project Structure

international_student_project/
│
├── app.py
│
├── data/
│   └── international_study_data.csv
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_Load_and_Understand_Data.py
│   ├── 3_Clean_Data.py
│   ├── 4_Balance_Data.py
│   └── 5_Data_Visualization.py
│
├── requirements.txt
├── README.md
└── Mini_Project_Report.md

Important

This is an educational project. Random Oversampling is demonstrated to explain the concept of handling class imbalance.

In a real machine-learning project, balancing should normally be performed only on the training data after splitting the dataset to avoid data leakage.

Learning Outcome

After completing this project, students will understand the basic data-wrangling workflow:

Load → Understand → Clean → Balance → Visualize