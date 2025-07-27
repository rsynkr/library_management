from operations import add_book, register_patron, borrow_book

# Add books
add_book("Harry Potter", "J.K. Rowling", "ISBN001")
add_book("RD Sharma", "R.D. Sharma", "ISBN002")

# Register patrons
register_patron("Rishi", 9898)

# Borrow a book
borrow_book(9898, "ISBN002")
