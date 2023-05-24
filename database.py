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


async def insert_data(telegram_id, name, date):
    user = cur.execute(f"SELECT * FROM users WHERE telegram_id == {telegram_id}").fetchone()
    cur.execute("INSERT INTO birthdays (user_id, name, date) VALUES (?, ?, ?)", (user[0], name, date))
    db.commit()


def get_birthdays_by_telegram_id(telegram_id):
    cur.execute("""
            SELECT birthdays.id, name, date FROM birthdays
            JOIN users ON birthdays.user_id = users.id
            WHERE users.telegram_id = ?
        """, (telegram_id,))
    birthdays = cur.fetchall()
    birthdays_str = '\n'.join(f'{id}| {name}: {date}' for id, name, date in birthdays)

    return birthdays_str


async def delete_birthday(birthday_id):
    cur.execute("DELETE FROM birthdays WHERE id = ?", (birthday_id,))
    db.commit()
