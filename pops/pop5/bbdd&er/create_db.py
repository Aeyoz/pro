import sqlite3
from pathlib import Path


def create(db_path: str):
    db = Path(db_path)
    db.unlink(missing_ok=True)

    con = sqlite3.connect(db)
    cur = con.cursor()

    sql = """CREATE TABLE login (
        username TEXT PRIMARY KEY,
        password TEXT,
        domain TEXT
    )"""
    cur.execute(sql)

    sql = """CREATE TABLE activity (
        id INTEGER PRIMARY KEY,
        sender TEXT,
        recipient TEXT,
        subject TEXT,
        body TEXT
    )"""
    cur.execute(sql)

    sql = 'INSERT INTO login VALUES("anna", "python", "gmail.com")'
    cur.execute(sql)
    sql = 'INSERT INTO login VALUES("evva", "rust", "icloud.com")'
    cur.execute(sql)

    con.commit()
    con.close()


if __name__ == "__main__":
    create("mail.db")
