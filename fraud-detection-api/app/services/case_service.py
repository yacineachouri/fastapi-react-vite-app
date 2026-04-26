from app.models.case import CaseDB

def create_case(db, alert_id, risk_score):

    case = CaseDB(
        alert_id=alert_id,
        risk_score=risk_score,
        status="OPEN"
    )

    db.add(case)
    db.commit()
    db.refresh(case)

    return case