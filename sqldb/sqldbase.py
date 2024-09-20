import sqlite3 as sq

async def db_connect()->None:
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY , Film TEXT)")
    db.commit()