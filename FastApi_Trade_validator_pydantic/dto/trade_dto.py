from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class Side(str, Enum):
    buy = 'buy'
    sell = 'sell'

class TradeBase(BaseModel):
    user_id: int = Field(ge=100)
    currency: str = Field(max_length=5)
    side: Side
    price: float = Field(ge=0)
    amount: float = Field(ge=10)

class TradeCreate(TradeBase):
    pass

class TradeUpdate(BaseModel):
    currency: Optional[str] = Field(max_length=5)
    side: Optional[Side]
    price: Optional[float] = Field(ge=0)
    amount: Optional[float] = Field(ge=10)

class TradeResponse(TradeBase):
    id: int

    class Config:
        from_attributes = True
