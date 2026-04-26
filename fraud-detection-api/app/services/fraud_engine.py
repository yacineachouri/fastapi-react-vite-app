from app.services.rule_engine import rule_based_score
from app.services.ml_model import predict
from app.services.alert_service import create_alert

def analyze_transaction(tx, db=None):

    rule_score, reasons = rule_based_score(tx)

    ml_score = float(predict([
        tx.amount,
        tx.frequency,
        tx.account_age_days
    ]))

    final_score = (rule_score + ml_score) / 2

    risk_level = "HIGH" if final_score > 0.7 else "MEDIUM" if final_score > 0.4 else "LOW"

    result = {
        "score": final_score,
        "risk_level": risk_level,
        "is_suspicious": final_score > 0.7,
        "reasons": reasons
    }

    # 🔥 إذا العملية خطيرة → Alert + Case
    if final_score > 0.7 and db:
        create_alert(
            db=db,
            transaction_id="AUTO-TX",
            risk_score=final_score,
            risk_level=risk_level
        )

    return result