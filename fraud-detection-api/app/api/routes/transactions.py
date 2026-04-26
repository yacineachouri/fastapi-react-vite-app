from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid

from app.schemas.transaction import TransactionCreate
from app.database import SessionLocal
from app.models.transaction import TransactionDB
from app.services.fraud_engine import analyze_transaction

router = APIRouter(prefix="/transactions")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/detect")
def detect_fraud(tx: TransactionCreate, db: Session = Depends(get_db)):

    result = analyze_transaction(tx)

    db_tx = TransactionDB(
        transaction_id=str(uuid.uuid4()),
        amount=tx.amount,
        country=tx.country,
        transaction_type=tx.transaction_type,
        frequency=tx.frequency,
        account_age_days=tx.account_age_days,
        risk_score=result["score"],
        risk_level=result["risk_level"],
        alert_status=result["alert_status"],
        is_suspicious=int(result["is_suspicious"]),
        reasons=",".join(result["reasons"])
    )

    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)

    return result


@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(TransactionDB).all()


@router.get("/alerts")
def get_alerts(db: Session = Depends(get_db)):
    return db.query(TransactionDB).filter_by(alert_status="OPEN").all()


@router.get("/report")
def report(db: Session = Depends(get_db)):
    return {
        "total": db.query(TransactionDB).count(),
        "high": db.query(TransactionDB).filter_by(risk_level="HIGH").count(),
        "medium": db.query(TransactionDB).filter_by(risk_level="MEDIUM").count(),
        "low": db.query(TransactionDB).filter_by(risk_level="LOW").count()
    }