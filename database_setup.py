import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    amount REAL NOT NULL
)
""")

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
