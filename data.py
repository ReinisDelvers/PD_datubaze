import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)

def user_creation():
    cur = conn.cursor()
    cur.execute(
        # "DROP TABLE user"
        """
        CREATE TABLE user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE
        )
        """
    )
    conn.commit()
# user_creation()

def message_creation():
    cur = conn.cursor()
    cur.execute(
        # "DROP TABLE message"
        """
        CREATE TABLE message(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEX NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(id)
        )
        """
    )
    conn.commit()
# message_creation()

def add_user(name, lastname, username):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO user(name, lastname, username) VALUES("{name}","{lastname}", "{username}")
        """
    )
    conn.commit()

def add_message(text, user_id):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO message(text, user_id) VALUES("{text}","{user_id}")
        """
    )
    conn.commit()

def get_user():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT id, name, lastname, username FROM user
        """
    )
    conn.commit()
    data = cur.fetchall()
    return data

def get_message():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT id, text, user_id FROM message
        """
    )
    conn.commit()
    data = cur.fetchall()
    return data