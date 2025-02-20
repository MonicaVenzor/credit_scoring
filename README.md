# 📊 Credit Scoring API - Loan Default Prediction

[![Deploy to Render](https://img.shields.io/badge/Live%20API-Online-green)](https://credit_scoring-s010.onrender.com)
[![FastAPI](https://img.shields.io/badge/Made%20With-FastAPI-blue)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🚀 Project Overview
This is a **machine learning API** that predicts whether a loan applicant is likely to **default** on their payments or not.
The model was trained using **XGBoost** and deployed with **FastAPI**.

🔗 **Live API:** [credit_scoring-s010.onrender.com](https://credit_scoring-s010.onrender.com)
📑 **API Docs:** [Swagger UI](https://credit_scoring-s010.onrender.com/docs)

---

## 🛠️ Features
✅ Predicts loan default risk (`0` = No Default, `1` = Default)
✅ Uses **XGBoost** for high-accuracy classification
✅ Fully deployed via **Render**
✅ JSON-based REST API with **FastAPI**

---

## 📦 Installation
To run the API locally:

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/MonicaVenzor/credit_scoring.git
cd credit_scoring

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate     # (Windows)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run FastAPI Locally
uvicorn app.app:app --reload

📌 Local API will be available at:

Swagger Docs: http://127.0.0.1:8000/docs
Prediction Endpoint: http://127.0.0.1:8000/predict

🔥 API Usage
➤ POST /predict
Send a JSON payload to get a loan default prediction.

📤 Request
{
  "RevolvingUtilizationOfUnsecuredLines": 0.5,
  "age": 35,
  "NumberOfTime30-59DaysPastDueNotWorse": 1,
  "DebtRatio": 0.3,
  "MonthlyIncome": 5000,
  "NumberOfOpenCreditLinesAndLoans": 4,
  "NumberOfTimes90DaysLate": 0,
  "NumberRealEstateLoansOrLines": 2,
  "NumberOfTime60-89DaysPastDueNotWorse": 0,
  "NumberOfDependents": 1
}

📥 Response

{
  "prediction": 0,
  "probability_of_default": 0.0886,
  "decision_threshold": 0.1849
}

⚙️ Model & Training
Dataset: Kaggle - Give Me Some Credit
Algorithm: XGBoost (Optimized with Hyperparameter Tuning)
Preprocessing: StandardScaler for feature scaling

🚀 Deployment
This project is deployed on Render.
To deploy a new version:

1️⃣ Push changes to GitHub
git add .
git commit -m "Updated model"
git push origin main

2️⃣ Render will automatically detect the changes & redeploy the API.

👤 Author
Monica Venzor
