import sqlite3
from datetime import datetime


def openDB():
    conn = sqlite3.connect('blog.db')
    curs = conn.cursor()
    return conn, curs


def closeDB(conn):
    conn.commit()
    conn.close()


def create_table():
    conn, curs = openDB()
    curs.execute('''CREATE TABLE articles (
                 id INTEGER PRIMARY KEY,
                 title VARCHAR(100),
                 intro VARCHAR(300),
                 text TEXT,
                 date VARCAHR(50)
    )''')
    closeDB(conn)


def insert_article(title, intro, text):
    date = datetime.now()
    conn, curs = openDB()
    curs.execute('''INSERT INTO articles (title, intro, text, date)
                 VALUES (?, ?, ?, ?)''', [title, intro, text, date])
    closeDB(conn)


def show_articles():
    conn, curs = openDB()
    curs.execute('''SELECT * FROM articles ORDER BY date DESC''')
    data = curs.fetchall()
    closeDB(conn)
    return data


def show_one_article(id):
    conn, curs = openDB()
    curs.execute('''SELECT * FROM articles WHERE id=(?) LIMIT 1''', [id])
    data = curs.fetchone()
    closeDB(conn)
    return data

