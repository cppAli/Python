
from typing import List
from fastapi import FastAPI, HTTPException
app = FastAPI(
    title="Trading App"
)
'''
fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

@app.get("/users/")
def get_all_users():
    # Возвращает список всех пользователей
    return fake_users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


@app.post("/users/")
def create_user(user_id: int, role: str, name: str):
    # Проверка, существует ли уже пользователь с таким ID
    if any(u['id'] == user_id for u in fake_users):
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    
    # Добавление нового пользователя в базу данных
    new_user = {"id": user_id, "role": role, "name": name}
    fake_users.append(new_user)
    return {"message": "User created successfully", "user": new_user}
'''


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
    {"id": 3, "user_id": 2, "currency": "ETH", "side": "buy", "price": 2000, "amount": 1.5},
    {"id": 4, "user_id": 2, "currency": "ETH", "side": "sell", "price": 2100, "amount": 1.0},
    {"id": 5, "user_id": 3, "currency": "LTC", "side": "buy", "price": 150, "amount": 10.0},
    {"id": 6, "user_id": 3, "currency": "LTC", "side": "sell", "price": 155, "amount": 5.0},
    {"id": 7, "user_id": 4, "currency": "XRP", "side": "buy", "price": 0.5, "amount": 1000.0},
    {"id": 8, "user_id": 4, "currency": "XRP", "side": "sell", "price": 0.6, "amount": 800.0},
    {"id": 9, "user_id": 5, "currency": "ADA", "side": "buy", "price": 1.2, "amount": 500.0},
    {"id": 10, "user_id": 5, "currency": "ADA", "side": "sell", "price": 1.3, "amount": 300.0},

]

@app.get("/trades/")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:offset+limit]

@app.get("/trades/all")
def get_all_trades():
    return fake_trades

@app.get("/trades/{trade_id}")
def get_trade(trade_id: int):
    trade = next((trade for trade in fake_trades if trade["id"] == trade_id), None)
    if trade is None:
        raise HTTPException(status_code=404, detail="Trade not found")
    return trade

@app.post("/trades/")
def create_trade(trade_id: int, user_id: int, currency: str, side: str, price: float, amount: float):
    if any(t["id"] == trade_id for t in fake_trades):
        raise HTTPException(status_code=400, detail="Trade with this ID already exists")
   
    # Добавление нового trade в базу данных
    new_trade = {"id": trade_id, "user_id": user_id, "currency": currency, "side": side, "price": price, "amount": amount}
    fake_trades.append(new_trade)
    return {"message": "Trade created successfully", "trade": new_trade}



# fake_users2 = [
#     {"id": 1, "role": "admin", "name": "Bob"},
#     {"id": 2, "role": "investor", "name": "John"},
#     {"id": 3, "role": "trader", "name": "Matt"},
# ]


# @app.post("/users/{user_id}")
# def change_user_name(user_id: int, new_name: str):
#     current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
#     current_user["name"] = new_name
#     return {"status": 200, "data": current_user}