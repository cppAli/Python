from fastapi import APIRouter, Depends, HTTPException
from typing import List

from database import get_db
from dto.trade_dto import TradeCreate, TradeUpdate, TradeResponse
from services.create_trade import create_trade_table, insert_trade, update_trade, select_trades, delete_trade
import mysql.connector

router = APIRouter()

# Подключение к базе данных
def get_connection():
    connection = mysql.connector.connect(
        host="database-1.cd42w2ayogur.eu-west-3.rds.amazonaws.com",
        user="admin",
        password="Romanko1488",
        database="db_trade"
    )
    return connection

@router.post("/trades/", response_model=TradeResponse)
def create_trade_view(trade: TradeCreate):
    connection = get_connection()
    trade_id = insert_trade(connection, trade.user_id, trade.currency, trade.side, trade.price, trade.amount)
    connection.close()
    return {"id": trade_id, **trade.dict()}

@router.get("/trades/", response_model=List[TradeResponse])
def read_trades(skip: int = 0, limit: int = 100):
    connection = get_connection()
    trades = select_trades(connection, skip=skip, limit=limit)
    connection.close()
    return trades

@router.put("/trades/{trade_id}", response_model=TradeResponse)
def update_trade_view(trade_id: int, trade: TradeUpdate):
    connection = get_connection()
    updated_rows = update_trade(connection, trade_id, trade.user_id, trade.currency, trade.side, trade.price, trade.amount)
    connection.close()
    if updated_rows == 0:
        raise HTTPException(status_code=404, detail="Trade not found")
    return {"id": trade_id, **trade.dict()}

@router.delete("/trades/{trade_id}", response_model=TradeResponse)
def delete_trade_view(trade_id: int):
    connection = get_connection()
    deleted_rows = delete_trade(connection, trade_id)
    connection.close()
    if deleted_rows == 0:
        raise HTTPException(status_code=404, detail="Trade not found")
    return {"id": trade_id}
