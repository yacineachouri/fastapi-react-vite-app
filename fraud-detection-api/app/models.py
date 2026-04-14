from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    country = Column(String)
    transaction_type = Column(String)
    frequency = Column(Integer)
    account_age_days = Column(Integer)
    risk_score = Column(Float)
    is_suspicious = Column(Integer)