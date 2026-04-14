import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# بيانات وهمية (تستطيع تحسينها لاحقًا)
data = pd.DataFrame({
    "amount": [100, 2000, 5000, 10000, 15000],
    "frequency": [1, 5, 10, 20, 30],
    "account_age_days": [100, 50, 30, 10, 5],
    "label": [0, 0, 0, 1, 1]
})

X = data[["amount", "frequency", "account_age_days"]]
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

# حفظ الموديل
with open("model/fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved!")