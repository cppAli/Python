import mysql.connector
from typing import Optional

# Создание таблицы
def create_trade_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            currency VARCHAR(3) NOT NULL,
            side ENUM('buy', 'sell') NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL
        )
    """)
    connection.commit()

# Вставка данных
def insert_trade(connection, user_id: int, currency: str, side: str, price: float, amount: float):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO trades (user_id, currency, side, price, amount)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, currency, side, price, amount))
    connection.commit()
    return cursor.lastrowid

# Обновление данных
def update_trade(connection, trade_id: int, user_id: Optional[int] = None, currency: Optional[str] = None, side: Optional[str] = None, price: Optional[float] = None, amount: Optional[float] = None):
    cursor = connection.cursor()
    query = "UPDATE trades SET "
    params = []

    if user_id is not None:
        query += "user_id = %s, "
        params.append(user_id)
    if currency is not None:
        query += "currency = %s, "
        params.append(currency)
    if side is not None:
        query += "side = %s, "
        params.append(side)
    if price is not None:
        query += "price = %s, "
        params.append(price)
    if amount is not None:
        query += "amount = %s, "
        params.append(amount)

    query = query.rstrip(", ")  # Удаление лишней запятой
    query += " WHERE id = %s"
    params.append(trade_id)

    cursor.execute(query, tuple(params))
    connection.commit()
    return cursor.rowcount

# Выбор данных
def select_trades(connection, skip: int = 0, limit: int = 100):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM trades LIMIT %s OFFSET %s", (limit, skip))
    result = cursor.fetchall()
    trades = []
    for row in result:
        trades.append({
            "id": row[0],
            "user_id": row[1],
            "currency": row[2],
            "side": row[3],
            "price": row[4],
            "amount": row[5]
        })
    return trades

# Удаление данных
def delete_trade(connection, trade_id: int):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM trades WHERE id = %s", (trade_id,))
    connection.commit()
    return cursor.rowcount

