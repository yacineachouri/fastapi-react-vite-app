from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    country = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)