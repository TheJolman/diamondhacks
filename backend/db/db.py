import sqlite3
import json
import os

DB_FILE = "stocks.db"

def initialize():
    db_exists = os.path.exists(DB_FILE)

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        if not db_exists:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS stocks (
                ticker TEXT PRIMARY KEY,
                price REAL NOT NULL,
                date NOT NULL
            )
            """)

            print("DB initialized")

        conn.commit()

    return db_exists

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == "__main__":
    initialize()
