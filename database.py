import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    subscribed INTEGER
)
""")
conn.commit()

def is_subscribed(user_id):
    cursor.execute("SELECT subscribed FROM users WHERE user_id=?", (user_id,))
    row = cursor.fetchone()
    return row and row[0] == 1

def set_subscribed(user_id):
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?, 1)", (user_id,))
    conn.commit()
