from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class AlertDB(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(String, index=True)
    risk_score = Column(Float)
    risk_level = Column(String)

    status = Column(String, default="OPEN")  # OPEN / UNDER_REVIEW / CLOSED

    created_at = Column(DateTime, default=datetime.utcnow)