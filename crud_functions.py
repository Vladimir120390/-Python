import sqlite3


# crud_functions.py
#
# cart = []  # Глобальная переменная для хранения товаров в корзине
#
# def add_to_cart(product_title):
#     cart.append(product_title)
#
# def get_cart_items():
#     return cart
#
# def clear_cart():
#     cart.clear()




def initiate_db():
    conn1 = sqlite3.connect('products.db')
    cursor1 = conn1.cursor()

    cursor1.execute('DROP TABLE IF EXISTS Products')
    cursor1.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            description TEXT,
            price INTEGER NOT NULL,
            image_path TEXT NOT NULL
        )
        ''')

    conn1.commit()
    conn1.close()

    conn2 = sqlite3.connect('users.db')
    cursor2 = conn2.cursor()
    cursor2.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    conn2.commit()
    conn2.close()


def add_user(username, email, age):
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (username, email, age))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    conn.close()
    return user is not None



def get_all_products():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        products = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
        products = []
    finally:
        conn.close()
    return products


def is_db_populated():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]

    conn.close()
    return count > 0



def populate_db():
    if is_db_populated():
        return

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    products = [
        ("Продукт 1", "Кисель 'Очищающий'", 252, 'files_update/Продукт1.png'),
        ("Продукт 2", "Кофе для похудения", 333, 'files_update/Продукт2.png'),
        ("Продукт 3", "Магний B6 таблетки 200мг", 1555, 'files_update/Продукт3.png'),
        ("Продукт 4", "Мультивитамины универсальные", 795, 'files_update/Продукт4.png'),
    ]

    for product in products:
        try:
            cursor.execute('INSERT INTO Products (title, description, price, image_path) VALUES (?, ?, ?, ?)', product)
        except sqlite3.IntegrityError:
            continue

    conn.commit()
    conn.close()



