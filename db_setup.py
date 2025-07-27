import sqlite3

connecti=sqlite3.connect("library.db")
cursor=connecti.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT PRIMARY KEY,
    is_borrowed INTEGER DEFAULT 0         
)
''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS patrons(
    name TEXT NOT NULL,
    patron_id INTEGER PRIMARY KEY,
    joining_date TEXT
)
''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS borrowed_log(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patron_id INTEGER,
    isbn TEXT,
    borrow_date TEXT,
    return_date TEXT,
    FOREIGN KEY(patron_id) REFERENCES patrons(patron_id),
    FOREIGN KEY(isbn) REFERENCES books(isbn)       
)
''')

connecti.commit()
connecti.close()