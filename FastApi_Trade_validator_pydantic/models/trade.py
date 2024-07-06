from sqlalchemy import Column, Integer, String, Float
from database import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    currency = Column(String(3), index=True)
    side = Column(String(4), index=True)
    price = Column(Float)
    amount = Column(Float)
