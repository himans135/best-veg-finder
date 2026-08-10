import sqlite3

conn = sqlite3.connect("db.sqlite3")
conn.execute("""
CREATE TABLE stalls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    state TEXT,
    city TEXT,
    location TEXT,
    phone TEXT,
    category TEXT,
    rating INTEGER,
    style TEXT
)
""")
conn.commit()
conn.close()
