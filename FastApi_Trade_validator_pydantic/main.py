from fastapi import FastAPI
from database import engine, Base
from routers import trade_router as TradeRouter
import mysql.connector
from services.create_trade import create_trade_table

# Создание подключения к базе данных
connection = mysql.connector.connect(
    host="database-1.cd42w2ayogur.eu-west-3.rds.amazonaws.com",
    user="admin",
    password="Romanko1488",
    database="db_trade"
)

# Вызов функции создания таблицы
create_trade_table(connection)

# Закрытие подключения
connection.close()

# Створення таблиць у базі даних з використанням метаданих моделей
Base.metadata.create_all(bind=engine)

# Ініціалізація основного об'єкту додатку
app = FastAPI()

# Включення роутера для користувачів із префіксом '/trade'
app.include_router(TradeRouter.router, prefix="/trade")

# Умова для запуску додатку через командний рядок
if __name__ == "__main__":
    import uvicorn
    # Запуск сервера на localhost з портом
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=3)




#     FastAPI - Імпорт класу FastAPI для створення основного додатку.
# SessionLocal, engine, Base - Імпорт компонентів бази даних, що включають двигун бази даних та базовий клас для моделей.
# UserRouter - Імпорт роутера для користувачів, що містить маршрути, пов'язані з користувачами.
# Створення та налаштування таблиць:

# Виклик Base.metadata.create_all(bind=engine) створює всі таблиці, визначені у моделях, у базі даних. Це важливо робити перед запуском додатку.
# Настройка FastAPI додатку:

# Ініціалізується об'єкт FastAPI.
# Включається роутер для користувачів з префіксом /user, що означає, що всі маршрути в цьому роутері будуть під цим префіксом.
# Запуск сервера:

# Перевірка, чи файл був запущений як основний скрипт, і якщо так, імпортується uvicorn, сервер ASGI, що використовується для запуску FastAPI.
# uvicorn.run запускає сервер з вказаними параметрами:
# "main:app" вказує на модуль та об'єкт додатку.
# host="0.0.0.0" вказує, що сервер доступний з усіх IP адрес.
# port=8080 встановлює порт для сервера.
# reload=True вмикає автоматичне перезавантаження сервера при зміні коду.
# workers=3 встановлює кількість робітників для обробки запитів.
