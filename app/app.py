from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

# ------------------------------
# 1️⃣ Initialize FastAPI
# ------------------------------
app = FastAPI(title="Credit Scoring API", description="Predict loan default risk using XGBoost.")

# ------------------------------
# 2️⃣ Load Trained Model, Scaler, and Threshold
# ------------------------------
model = joblib.load("models/credit_scoring_xgb_best.pkl")
scaler = joblib.load("models/scaler.pkl")
best_threshold = joblib.load("models/threshold.pkl")

# ------------------------------
# 3️⃣ Define the Prediction Endpoint
# ------------------------------

@app.get("/")
def home():
    return {"message": "Credit Scoring API is running! Use /predict to make predictions."}


@app.post("/predict")
def predict_credit_risk(features: dict):
    """
    Receives input features and returns a credit risk prediction (0 = No Default, 1 = Default).
    """
    # Convert input dictionary to DataFrame
    df = pd.DataFrame([features])

    # Apply scaling
    df_scaled = scaler.transform(df)

    # Get predicted probability
    proba = model.predict_proba(df_scaled)[:, 1]

    # Apply decision threshold
    prediction = int(proba > best_threshold)

    return {
        "prediction": prediction,
        "probability_of_default": round(float(proba[0]), 4),
        "decision_threshold": round(float(best_threshold), 4)
    }
