import sqlite3
import os

DB_STRING = "app.db"

db_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(db_directory, DB_STRING)


def setup_database():
    users_table = """CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL DEFAULT '',
    last_name VARCHAR(50) NOT NULL DEFAULT '', 
    birth_date DATE NOT NULL DEFAULT (date()),
    phone_number CHAR(9) NOT NULL DEFAULT '',
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    image_file TEXT NOT NULL DEFAULT ''
    );
    """

    chat_messages = """CREATE TABLE IF NOT EXISTS chat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender VARCHAR(50) NOT NULL,
    receiver VARCHAR(50) NOT NULL, 
    date DATE NOT NULL, 
    message TEXT NOT NULL
    );
    """

    with sqlite3.connect(db_path) as conn:
        conn.execute(users_table)
        conn.execute(chat_messages)


def show_database():
    users_table = " SELECT * FROM users; "
    chat_table = " SELECT * FROM chat; "

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(users_table)
        for row in cursor.fetchall():
            print(row)

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(chat_table)
        for row in cursor.fetchall():
            print(row)

def clean_database():
    users_table = " DROP TABLE IF EXISTS users;"
    chat_table = " DROP TABLE IF EXISTS chat; "

    with sqlite3.connect(db_path) as conn:
        conn.execute(users_table)
        conn.execute(chat_table)


def main():
    setup_database()
    # show_database()
    # clean_database()


if __name__ == '__main__':
    main()
