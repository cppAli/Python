# Імпортування необхідних бібліотек та модулів для роботи з SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL для підключення до бази даних SQLite
SQLALCHEMY_URL = "mysql+mysqlconnector://admin:Romanko1488@database-1.cd42w2ayogur.eu-west-3.rds.amazonaws.com"

# Створення об'єкта двигуна для взаємодії з базою даних
engine = create_engine(SQLALCHEMY_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Створення фабрики сесій, параметр autocommit=False вимикає автоматичне підтвердження транзакцій
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функція для отримання сесії з бази даних
def get_db():
    db = SessionLocal()  # Створення нової сесії
    try:
        yield db  # Повернення сесії для використання
    finally:
        db.close()  # Закриття сесії після завершення використання


# SQLAlchemy: Це бібліотека SQL Toolkit і Object-Relational Mapping (ORM), яка дозволяє розробникам використовувати Python для взаємодії з базами даних у вигляді Python об'єктів замість написання чистого SQL.
# engine: Об'єкт двигуна забезпечує підключення до бази даних. Параметр check_same_thread встановлений у False для SQLite, щоб уникнути помилок, пов'язаних з доступом з різних потоків.
# SessionLocal: Це фабрика, яка буде генерувати сесії для взаємодії з базою даних. Сесії використовуються для збереження "робочих" об'єктів і здійснення бази даних транзакцій.
# Base: Цей об'єкт використовується як базовий клас для класів моделей, де можна визначати структуру таблиць бази даних.
# get_db: Це генератор, який використовується для отримання та автоматичного закриття сесій. Це корисно при використанні з FastAPI або іншими асинхронними фреймворками.

