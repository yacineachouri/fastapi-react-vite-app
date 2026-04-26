from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from app.database import Base

class CaseDB(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)

    alert_id = Column(Integer, ForeignKey("alerts.id"))

    assigned_to = Column(String, nullable=True)

    status = Column(String, default="OPEN")
    decision = Column(String, nullable=True)  # FRAUD / LEGIT

    risk_score = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)