import sqlite3

def create_connection():
    conn = sqlite3.connect("contacts.db")
    return conn

def create_table():
    conn = create_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()