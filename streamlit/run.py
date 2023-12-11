import streamlit as st
import pandas as pd
from PIL import Image


if __name__ == "__main__":
    data = pd.read_csv("salaries.csv")
    st.title("Example of DataFrame on Streamlit")
    st.header("Example of DataFrame on Streamlit")
    st.subheader("Describe")
    st.write("""The dataset contains one table structured as follow:\n

work_year: The year the salary was paid.\n
experience_level: The experience level in the job during the year with the following possible values:\n
EN: Entry-level / Junior\n
MI: Mid-level / Intermediate\n
SE: Senior-level / Expert\n
EX: Executive-level / Director\n
employment_type: The type of employement for the role:\n
PT: Part-time\n
FT: Full-time\n
CT: Contract\n
FL: Freelance\n
job_title: The role worked in during the year.\n
salary: The total gross salary amount paid.\n
salary_currency: The currency of the salary paid as an ISO 4217 currency code.\n
salary_in_usd: The salary in USD (FX rate divided by avg. USD rate for the respective year via fxdata.foorilla.com).\n
employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.\n
remote_ratio: The overall amount of work done remotely, possible values are as follows:\n
0: No remote work (less than 20%)\n
50: Partially remote\n
100: Fully remote (more than 80%)\n
company_location: The country of the employer's main office or contracting branch as an ISO 3166 country code.\n
company_size: The average number of people that worked for the company during the year:\n
S: less than 50 employees (small)\n
M: 50 to 250 employees (medium)\n
L: more than 250 employees (large)""")
    st.dataframe(data.head())
    st.subheader("Some Graphics")
    choose = st.selectbox("Graphics: ", ['Map', 'Salary in dollars depends on the position', 'Comparison of EU and USA', 'Count of jobs per year'])
    if choose == 'Map':
        img = Image.open("hse_final_project/static/map.png")
        st.image(img)
    if choose == 'Salary in dollars depends on the position':
        img = Image.open("hse_final_project/static/comp_salary.png")
        st.image(img)
    if choose == 'Comparison of EU and USA':
        img = Image.open("hse_final_project/static/comparison.png")
        st.image(img)
    if choose == 'Count of jobs per year':
        img = Image.open("hse_final_project/static/count_of_jobs.png")
        st.image(img)
