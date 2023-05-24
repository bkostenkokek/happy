import sqlite3 as sq

db = sq.connect('database.db')
cur = db.cursor()


async def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    username TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS birthdays(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    name TEXT,
    date DATE)""")
    db.commit()


async def init_user(user_id, username):
    user = cur.execute(f"SELECT * FROM users WHERE telegram_id == {user_id}").fetchone()
    if not user:
        cur.execute(f"INSERT INTO users (telegram_id, username) VALUES (?, ?)", (user_id, username))
        db.commit()


# async def add_birthday(telegram_id, name, date):
#     cur.execute("""INSERT INTO birthdays(user_id, name, date)
#                    SELECT id, ?, ?
#                    FROM users
#                    WHERE telegram_id = ?""", (name, date, telegram_id))
#     db.commit()


async def insert_data(telegram_id, username, name, date):
    # Записываем данные в таблицу "users"
    cur.execute("INSERT INTO users (telegram_id, username) VALUES (?, ?)", (telegram_id, username))
    user_id = cur.lastrowid  # Получаем ID новой записи в таблице "users"

    # Записываем данные в таблицу "birthdays"
    cur.execute("INSERT INTO birthdays (user_id, name, date) VALUES (?, ?, ?)", (user_id, name, date))

    db.commit()
