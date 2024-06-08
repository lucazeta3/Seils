import sqlite3
import os

DATABASE = 'search_results.db'

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT NOT NULL,
                summary TEXT NOT NULL,
                outreach_message TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

def save_to_db(website, summary, outreach_message):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO results (website, summary, outreach_message)
        VALUES (?, ?, ?)
    ''', (website, summary, outreach_message))
    conn.commit()
    conn.close()
