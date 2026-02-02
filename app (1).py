import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Page config
st.set_page_config(
    page_title="Student Dropout Predictor",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Dropout Risk Prediction")
st.markdown("Predict whether a student is at **risk of dropping out** using Machine Learning")

st.divider()

# Input fields
attendance = st.slider("📊 Attendance (%)", 40, 100, 75)
study_hours = st.slider("📚 Study Hours per Day", 1, 10, 4)
previous_score = st.slider("📝 Previous Exam Score", 30, 100, 60)
family_income = st.number_input("💰 Family Monthly Income", 5000, 100000, 25000)
internet_access = st.selectbox("🌐 Internet Access", ["Yes", "No"])
stress_level = st.slider("😟 Stress Level (1–10)", 1, 10, 5)

# Convert categorical
internet_access = 1 if internet_access == "Yes" else 0

# Predict button
if st.button("🔍 Predict Dropout Risk"):

    input_data = pd.DataFrame({
        "Attendance": [attendance],
        "Study_Hours": [study_hours],
        "Previous_Score": [previous_score],
        "Family_Income": [family_income],
        "Internet_Access": [internet_access],
        "Stress_Level": [stress_level]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    st.divider()

    if prediction[0] == 1:
        st.error("⚠️ High Dropout Risk")
        st.markdown("""
        **Suggestions:**
        - Improve attendance  
        - Reduce stress  
        - Increase daily study hours  
        - Provide mentoring support
        """)
    else:
        st.success("✅ Low Dropout Risk")
        st.markdown("""
        **Student is performing well.**
        - Keep monitoring progress  
        - Encourage consistency  
        """)

# Footer
st.divider()
st.caption("Built with ❤️ using Python, ML & Streamlit")
