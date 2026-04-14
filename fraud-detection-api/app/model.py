import pickle

model = pickle.load(open("model/fraud_model.pkl", "rb"))

def predict(tx):
    features = [[
        tx.amount,
        tx.frequency,
        tx.account_age_days
    ]]
    
    return model.predict_proba(features)[0][1]