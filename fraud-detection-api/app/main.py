from fastapi import FastAPI
from app.schemas import Transaction
from app.rules import rule_based_score
from app.model import predict
from app.database import SessionLocal
from app.models import TransactionDB
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ function خارج endpoints
def classify_risk(score):
    if score > 0.7:
        return "HIGH"
    elif score > 0.4:
        return "MEDIUM"
    else:
        return "LOW"


@app.get("/")
def home():
    return {"status": "API is running"}


@app.post("/detect")
def detect_fraud(tx: Transaction):
    print("🔥 REQUEST RECEIVED")

    db = SessionLocal()

    # rule-based
    rule_score, reasons = rule_based_score(tx)

    # ML
    ml_score = float(predict(tx))

    # final score
    final_score = (rule_score + ml_score) / 2

    # classification
    risk_level = classify_risk(final_score)
    is_suspicious = final_score > 0.7

    # save to DB
    db_tx = TransactionDB(
        amount=tx.amount,
        country=tx.country,
        transaction_type=tx.transaction_type,
        frequency=tx.frequency,
        account_age_days=tx.account_age_days,
        risk_score=final_score,
        risk_level=risk_level,  # ✅ صحيح
        is_suspicious=int(is_suspicious)
    )

    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    db.close()

    return {
        "risk_score": final_score,
        "risk_level": risk_level,
        "is_suspicious": is_suspicious,
        "reasons": reasons
    }


@app.get("/report")
def generate_report():
    db = SessionLocal()

    total = db.query(TransactionDB).count()
    high = db.query(TransactionDB).filter_by(risk_level="HIGH").count()
    medium = db.query(TransactionDB).filter_by(risk_level="MEDIUM").count()
    low = db.query(TransactionDB).filter_by(risk_level="LOW").count()

    db.close()

    return {
        "total_transactions": total,
        "high_risk": high,
        "medium_risk": medium,
        "low_risk": low
    }