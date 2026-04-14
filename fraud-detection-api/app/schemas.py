from pydantic import BaseModel

class Transaction(BaseModel):
    amount: float
    country: str
    transaction_type: str
    frequency: int
    account_age_days: int