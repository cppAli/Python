import mysql.connector
from users_api import select_data

# Подключение к базе данных
def create_db_connection():
    connection = mysql.connector.connect(
        host="db-fastapi-aws.cd42w2ayogur.eu-west-3.rds.amazonaws.com",        # Адрес сервера базы данных
        user="admin",    # Имя пользователя
        password="Romanko1488",# Пароль
        database="db_demo"       # Имя базы данных
    )
    return connection

connection = create_db_connection()
connection

select_data(connection)

connection.close()