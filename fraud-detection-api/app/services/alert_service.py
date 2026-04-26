from app.models.alert import AlertDB
from app.services.case_service import create_case

def create_alert(db, transaction_id, risk_score, risk_level):

    alert = AlertDB(
        transaction_id=transaction_id,
        risk_score=risk_score,
        risk_level=risk_level,
        status="OPEN"
    )

    db.add(alert)
    db.commit()
    db.refresh(alert)

    # 🔥 مباشرة ننشئ Case
    case = create_case(
        db=db,
        alert_id=alert.id,
        risk_score=risk_score
    )

    return alert, case