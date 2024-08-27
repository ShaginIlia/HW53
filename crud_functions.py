import sqlite3

import text_to_HW52

connection = sqlite3.connect('db_zoj.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEST,
    price INT NOT NULL
    );
    ''')

    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   ('Апельсин', text_to_HW52.orange, text_to_HW52.orange_price))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   ('Брокколи', text_to_HW52.broccoli, text_to_HW52.broccoli_price))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   ('Марковка', text_to_HW52.carrot, text_to_HW52.carrot_price))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   ('Яблоко', text_to_HW52.apple, text_to_HW52.apple_price))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
        );
        ''')
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    return products


def add_user(username, email, age):
    user = cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                          (username, email, age, 1000))
    connection.commit()
    return user


def is_included(username):
    cursor.execute("SELECT id FROM Users WHERE username=?", (username,))
    connection.commit()
    return cursor.fetchone() is not None
