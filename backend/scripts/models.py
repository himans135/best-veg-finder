import sqlite3

conn = sqlite3.connect("db.sqlite3")
conn.execute("""
CREATE TABLE stalls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    category TEXT,
    rating INTEGER
)
""")
conn.commit()
conn.close()
