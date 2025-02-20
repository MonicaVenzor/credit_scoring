🛡️ Credit Scoring API using Machine Learning

🚀 A FastAPI-powered credit scoring system using XGBoost. This API predicts the likelihood of loan default based on applicant financial data.

📌 Features
✔ FastAPI for real-time credit risk prediction
✔ XGBoost Model trained on financial applicant data
✔ Custom Decision Threshold for improved accuracy
✔ Endpoints for Real-Time Predictions
✔ Streamlit UI for user-friendly interaction

📂 Project Structure

credit_scoring/
   ├── 📂 app/
   │   ├── app.py
   ├── 📂 data/
   │   ├── cs-test.csv
   │   ├── cs-training.csv
   │   ├── Data Dictionary.xls
   │   ├── sampleEntry.csv
   ├── 📂 models/
   │   ├── credit_scoring_xgb_best.pkl
   │   ├── scaler.pkl
   │   ├── threshold.pkl
   ├── 📂 notebooks/
   │   ├── credit_scoring_prediction.ipynb
   ├── 📂 scripts/
   ├── venv_credit/ (excluded from Git)
   ├── .gitignore
   ├── app_streamlit.py
   ├── README.md
   ├── requirements_streamlit.txt
   ├── requirements.txt
   ├── start.sh

🚀 Installation & Usage

1️⃣ Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/credit_scoring.git
cd credit_scoring

2️⃣ Create a Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt

3️⃣ Run the FastAPI Server
uvicorn app.app:app --reload

The API will be available at 👉 http://127.0.0.1:8000/docs

🌐 API Endpoints

Method   Endpoint           Description

GET         /                Home Page

POST        /predict/      Predict Loan Default Risk

📌 Example Request (JSON)

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

📌 Example Response

{
    "prediction": 0,
    "probability_of_default": 0.0886,
    "decision_threshold": 0.1849
}

🛠️ Deployment

📦 Deploy to Render
1️⃣ Link GitHub repo to Render.com
2️⃣ Set root directory as app/
- Build Command: pip install -r requirements.txt
- Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT
3️⃣ Deploy and access API at: https://your-app-name.onrender.com

📦 Deploying Streamlit UI
1️⃣ Install Streamlit dependencies
pip install -r requirements_streamlit.txt

2️⃣ Run Streamlit Locally
streamlit run app_streamlit.py

3️⃣ Deploy on Streamlit Cloud

Go to Streamlit Cloud

Connect your GitHub repository

Select app_streamlit.py as the main entry file

Deploy 🎉
4️⃣ Access your deployed Streamlit dashboard at:
https://your-streamlit-app.streamlit.app

🎯 Next Steps
🔹 Improve Model Performance with better hyperparameter tuning
🔹 Optimize feature selection for better predictive power
🔹 Enhance UI with additional insights and charts

👨‍💻 🏆 Author: Monica Venzor
📌 GitHub Repo: credit_scoring
