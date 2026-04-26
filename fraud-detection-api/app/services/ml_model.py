# app/services/ml_model.py

import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "fraud_model.pkl")

# تحميل الموديل مرة واحدة
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict(tx):
    """
    tx: Transaction object
    """
    features = [[
        tx.amount,
        tx.frequency,
        tx.account_age_days
    ]]

    prediction = model.predict_proba(features)[0][1]
    return prediction