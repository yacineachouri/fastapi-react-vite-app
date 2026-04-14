from fastapi import FastAPI
from app.schemas import Transaction
from app.rules import rule_based_score
from app.model import predict
from app.database import SessionLocal
from app.models import TransactionDB

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/detect")
def detect_fraud(tx: Transaction):
    print("🔥 REQUEST RECEIVED")

    db = SessionLocal()

    rule_score = rule_based_score(tx)
    ml_score = float (predict(tx))
    final_score = (rule_score + ml_score) / 2
    final_score = float(final_score)

    is_suspicious = final_score > 0.7

    db_tx = TransactionDB(
        amount=tx.amount,
        country=tx.country,
        transaction_type=tx.transaction_type,
        frequency=tx.frequency,
        account_age_days=tx.account_age_days,
        risk_score=final_score,
        is_suspicious=int(is_suspicious)
    )

    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)

    db.close()

    return {
        "risk_score": float (final_score),
        "is_suspicious": is_suspicious
    }