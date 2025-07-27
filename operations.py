import sqlite3
from datetime import date

DB_NAME = "library.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def add_book(title, author, isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO books (title, author, isbn) VALUES (?, ?, ?)",
                   (title, author, isbn))
    conn.commit()
    conn.close()

def register_patron(name, patron_id, joining_date=None):
    if joining_date is None:
        joining_date = str(date.today())
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO patrons (name, patron_id, joining_date) VALUES (?, ?, ?)",
                   (name, patron_id, joining_date))
    conn.commit()
    conn.close()

def borrow_book(patron_id, isbn):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT is_borrowed FROM books WHERE isbn = ?", (isbn,))
    row = cursor.fetchone()
    if not row:
        print("Book not found.")
    elif row[0] == 1:
        print("Book already borrowed.")
    else:
        cursor.execute("UPDATE books SET is_borrowed = 1 WHERE isbn = ?", (isbn,))
        cursor.execute("INSERT INTO borrowed_log (patron_id, isbn, borrow_date) VALUES (?, ?, ?)",
                       (patron_id, isbn, str(date.today())))
        conn.commit()
        print(f"Book {isbn} borrowed.")
    
    conn.close()
