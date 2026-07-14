import sqlite3
from datetime import datetime

DB_NAME = "ids_log.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source_ip TEXT,
            dest_ip TEXT,
            protocol TEXT,
            length INTEGER,
            attack_type TEXT,
            severity TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_alert(source_ip, dest_ip, protocol, length, attack_type, severity):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO alerts (timestamp, source_ip, dest_ip, protocol, length, attack_type, severity)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (timestamp, source_ip, dest_ip, protocol, length, attack_type, severity))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")