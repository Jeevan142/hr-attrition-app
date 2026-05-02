import streamlit as st
import numpy as np
import joblib

model = joblib.load("hr_model.pkl")

st.set_page_config(page_title="Prediction", layout="wide")

st.title("🔮 Employee Attrition Prediction")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧾 Employee Details")

    age = st.slider("Age", 18, 60, 30)
    income = st.number_input("Monthly Income", 1000, 20000, 5000)
    job_satisfaction = st.slider("Job Satisfaction", 1, 4, 3)
    overtime = st.selectbox("OverTime", ["Yes", "No"])

    overtime = 1 if overtime == "Yes" else 0

with col2:
    st.subheader("📊 Result")

    if st.button("Predict"):
        input_data = np.array([[age, income, job_satisfaction, overtime, 0,0,0,0,0,0]])

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ Employee likely to leave")
        else:
            st.success("✅ Employee likely to stay")