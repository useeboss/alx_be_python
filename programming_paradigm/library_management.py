# library_management.py
# Defines Book and Library classes for basic library management

class Book:
    """Represents a book with title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books and their availability."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' is not currently checked out.")

    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
