import streamlit as st
import requests
import json

# Set the FastAPI URL
API_URL = "https://credit_scoring-s010.onrender.com/predict"

# Streamlit UI
st.title("📊 Credit Scoring Predictor")
st.markdown("Enter applicant details and predict the likelihood of loan default.")

# User Inputs
st.sidebar.header("Enter Applicant Details")
revolving_utilization = st.sidebar.slider("Revolving Utilization of Unsecured Lines", 0.0, 2.0, 0.5)
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=35)
num_30_59_days_past_due = st.sidebar.slider("Number of Time 30-59 Days Past Due", 0, 10, 1)
debt_ratio = st.sidebar.slider("Debt Ratio", 0.0, 2.0, 0.3)
monthly_income = st.sidebar.number_input("Monthly Income", min_value=0, max_value=50000, value=5000)
num_open_credit_lines = st.sidebar.slider("Number of Open Credit Lines & Loans", 0, 20, 4)
num_90_days_late = st.sidebar.slider("Number of Times 90 Days Late", 0, 10, 0)
num_real_estate_loans = st.sidebar.slider("Number of Real Estate Loans or Lines", 0, 10, 2)
num_60_89_days_past_due = st.sidebar.slider("Number of Time 60-89 Days Past Due", 0, 10, 0)
num_dependents = st.sidebar.slider("Number of Dependents", 0, 10, 1)

# Submit Button
if st.sidebar.button("Predict"):
    input_data = {
        "RevolvingUtilizationOfUnsecuredLines": revolving_utilization,
        "age": age,
        "NumberOfTime30-59DaysPastDueNotWorse": num_30_59_days_past_due,
        "DebtRatio": debt_ratio,
        "MonthlyIncome": monthly_income,
        "NumberOfOpenCreditLinesAndLoans": num_open_credit_lines,
        "NumberOfTimes90DaysLate": num_90_days_late,
        "NumberRealEstateLoansOrLines": num_real_estate_loans,
        "NumberOfTime60-89DaysPastDueNotWorse": num_60_89_days_past_due,
        "NumberOfDependents": num_dependents
    }

    # Send request to FastAPI
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        prediction = response.json()
        st.success(f"📌 Prediction: {'Default' if prediction['prediction'] == 1 else 'No Default'}")
        st.info(f"💰 Probability of Default: {prediction['probability_of_default']:.2%}")
    else:
        st.error("⚠️ Error: Could not connect to the API. Please try again later.")
