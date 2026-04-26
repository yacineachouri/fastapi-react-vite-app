from pydantic import BaseModel

class TransactionCreate(BaseModel):
    transaction_id: str
    amount: float
    country: str
    transaction_type: str
    frequency: int
    account_age_days: int

    class Config:
        from_attributes = True

class TransactionResponse(BaseModel):
    id: int
    transaction_id: str
    amount: float
    country: str
    risk_score: float
    risk_level: str
    
    class Config:
        from_attributtes = True