from app.database import engine, Base
from app.models import TransactionDB

Base.metadata.create_all(bind=engine)
print("✅ Tables created!")