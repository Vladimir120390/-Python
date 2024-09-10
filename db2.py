import sqlite3

with sqlite3.connect("not_telegram.db") as connection:
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
    ''')

    # Удаление всех записей из таблицы Users, если они существуют
    cursor.execute("DELETE FROM Users")


    users_data = [
        (f"User{i+1}", f"example{i+1}@gmail.com", (i + 1) * 10, 1000) for i in range(10)
    ]
    cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users_data)

    # Обновление balance у каждой 2-й записи, начиная с 1-й
    for i in range(1, 11, 2):
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))


    connection.commit()

    # Удаление каждой 3-й записи, начиная с 1-й
    for i in range(1, 11, 3):  # Индексы 1, 4, 7, 10 (всего 10 записей)
        cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

    
    connection.commit()

    # Выборка всех записей, где возраст не равен 60
    cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
    rows = cursor.fetchall()

# Вывод результатов в нужном формате
for row in rows:
    username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")
