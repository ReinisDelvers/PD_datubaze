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


def get_message_message():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT user.name, user.lastname, message.text
        FROM
        message JOIN user ON message.user_id = user.id
        ORDER BY message.id DESC
        """
    )
    conn.commit()
    data = cur.fetchall()
    return data

def get_user_message():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT id, username FROM user
        ORDER BY username ASC
        """
    )
    conn.commit()
    data = cur.fetchall()
    return data

def get_statistics():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT user.name, user.lastname, COUNT(message.user_id)
        FROM
        message JOIN user ON message.user_id = user.id
        GROUP BY user.id
        """
    )
    conn.commit()
    data = cur.fetchall()
    return data
