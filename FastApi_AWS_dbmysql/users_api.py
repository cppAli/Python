import mysql.connector

# Подключение к базе данных
def create_db_connection():
    connection = mysql.connector.connect(
        host="db-fastapi-aws.cd42w2ayogur.eu-west-3.rds.amazonaws.com",        # Адрес сервера базы данных
        user="admin",    # Имя пользователя
        password="Romanko1488",# Пароль
        database="db_demo"       # Имя базы данных
    )
    return connection

# Создание таблицы
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            position VARCHAR(255)
        )
    """)
    connection.commit()

# Вставка данных
def insert_data(connection, name, age, position):
    cursor = connection.cursor()
    insert_query = "INSERT INTO employees (name, age, position) VALUES (%s, %s, %s)"
    values = (name, age, position)
    cursor.execute(insert_query, values)
    connection.commit()

# Вставка данных (нескольких записей)
def insert_multiple_data(connection, data_list):
    cursor = connection.cursor()
    insert_query = "INSERT INTO employees (name, age, position) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, data_list)
    connection.commit()

# Обновление данных
def update_data(connection, new_age, name):
    cursor = connection.cursor()
    update_query = "UPDATE employees SET age = %s WHERE name = %s"
    cursor.execute(update_query, (new_age, name))
    connection.commit()

# Выбор данных
def select_data(connection):
    cursor = connection.cursor()
    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Удаление данных
def delete_data(connection, name):
    cursor = connection.cursor()
    delete_query = "DELETE FROM employees WHERE name = %s"
    cursor.execute(delete_query, (name,))
    connection.commit()

# Основной блок кода
if __name__ == "__main__":
    connection = create_db_connection()
    
    create_table(connection)
    
    insert_data(connection, "John Doe", 30, "Software Engineer")

    # Вставка нескольких записей
    employees = [
        ("John Doe_1", 30, "Software Engineer"),
        ("Jane Smith_1", 28, "Data Scientist"),
        ("Michael Brown_1", 35, "Project Manager"),
        ("Emily Davis_1", 22, "Intern"),
        ("Robert Johnson_1", 40, "Senior Developer")
    ]
    insert_multiple_data(connection, employees)


    update_data(connection, 31, "John Doe")
    select_data(connection)
    delete_data(connection, "John Doe")
    
    connection.close()
