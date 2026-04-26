from sqlalchemy import Column, Integer, Float, String, DateTime
from app.database import Base
from datetime import datetime 
import uuid

class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    
    transaction_id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()), unique=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    amount = Column(Float)
    country = Column(String)
    transaction_type = Column(String)
    frequency = Column(Integer)
    account_age_days = Column(Integer)

    risk_score = Column(Float)
    risk_level = Column(String)
    alert_status = Column(String)
    is_suspicious = Column(Integer)

    reasons = Column(String)