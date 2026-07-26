import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

gender_encoder = joblib.load("models/gender_encoder.pkl")

education_encoder = joblib.load("models/education_encoder.pkl")

job_encoder = joblib.load("models/job_encoder.pkl")

st.title("Employee Salary Prediction")

st.write("Enter Employee Details")

age = st.number_input("Age", 18, 65, 25)

gender = st.selectbox(
    "Gender",
    gender_encoder.classes_
)

education = st.selectbox(
    "Education Level",
    education_encoder.classes_
)

job = st.selectbox(
    "Job Title",
    job_encoder.classes_
)

experience = st.number_input(
    "Years of Experience",
    0,
    40,
    2
)

if st.button("Predict Salary"):

    gender = gender_encoder.transform([gender])[0]

    education = education_encoder.transform([education])[0]

    job = job_encoder.transform([job])[0]

    data = pd.DataFrame({
        "Age":[age],
        "Gender":[gender],
        "Education Level":[education],
        "Job Title":[job],
        "Years of Experience":[experience]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Salary: ${prediction[0]:,.2f}")