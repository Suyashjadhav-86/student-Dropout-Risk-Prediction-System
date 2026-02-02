# 🎓 Student Dropout Risk Prediction System

A **Machine Learning–based web application** that predicts whether a student is at **risk of dropping out** based on academic, personal, and socio-economic factors.  
Built using **Python, Scikit-learn, and Streamlit**.

---

## 📌 Overview

Student dropout is a critical issue in education systems.  
This project helps educational institutions **identify at-risk students early** so that proper guidance, mentoring, and support can be provided.

The system classifies students into:
- ⚠️ High Dropout Risk  
- ✅ Low Dropout Risk  

---

## 🚀 Features

- 🎯 Machine Learning–based prediction
- 📊 Interactive web interface using Streamlit
- 🧠 Pre-trained ML model
- ⚖️ Feature scaling with saved scaler
- 📝 Actionable suggestions for high-risk students
- ⚡ Real-time prediction

---

## 🧾 Input Parameters

| Feature | Description |
|------|-------------|
| Attendance | Attendance percentage |
| Study_Hours | Study hours per day |
| Previous_Score | Previous exam score |
| Family_Income | Monthly family income |
| Internet_Access | Yes / No |
| Stress_Level | Stress level (1–10) |

---

## 🛠️ Tech Stack

- Python
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- Pickle

---

## 📂 Project Structure

📁 Student-Dropout-Risk-Prediction
│
├── app.py                          # Streamlit application
├── model.pkl                       # Trained ML model
├── scaler.pkl                      # Feature scaler
├── requirements.txt                # Dependencies
├── student Dropout Risk Prediction System.ipynb
└── README.md

## ⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/student-dropout-risk-prediction.git
cd student-dropout-risk-prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

## 🧪 How It Works

User enters student details via UI

Input data is scaled using saved scaler

Scaled data is passed to trained ML model

Model predicts dropout risk

Result and suggestions are displayed instantly

## 📊 Prediction Output

✅ Low Dropout Risk

Student is performing well

Encourage consistency

⚠️ High Dropout Risk

Improve attendance

Reduce stress

Increase study hours

Provide mentoring support

## 📦 Dependencies

All required libraries are listed in requirements.txt 

requirements

## 📜 Source Code

Main application logic is implemented using Streamlit and Pickle-loaded ML models 

app (1)

## 🔮 Future Enhancements

Add more student features

Use advanced ML models

Store prediction history

Deploy on cloud (AWS / Heroku)

Add authentication for institutions

## 👨‍💻 Author

Suyash Jadhav
Computer Engineering | Data Science & ML Enthusiast

## ❤️ Acknowledgment

Built with ❤️ using Python, Machine Learning, and Streamlit
