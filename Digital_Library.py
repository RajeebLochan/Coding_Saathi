class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' has been removed from the library.")
        else:
            print("Book not found in the library.")

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f"Member '{member.name}' has been removed from the library.")
        else:
            print("Member not found in the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books in the library:")
            for book in self.books:
                if book.is_available:
                    print(f"Title: {book.title}, Author: {book.author}, Category: {book.category}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                print(f"Book found - Title: {book.title}, Author: {book.author}, Category: {book.category}")
                return
        print("Book not found or unavailable in the library.")

    def issue_book(self, title, member):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f"Book '{book.title}' has been issued to {member.name}.")
                return
        print("Book not found or already issued.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                print(f"Book '{book.title}' has been returned.")
                return
        print("Book not found or already returned.")

class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Admin:
    def __init__(self, library):
        self.library = library

    def update_book(self, book, new_title, new_author, new_category):
        book.title = new_title
        book.author = new_author
        book.category = new_category
        print(f"Book '{book.title}' has been updated.")

    def delete_book(self, book):
        self.library.remove_book(book)

    def update_member(self, member, new_name, new_email):
        member.name = new_name
        member.email = new_email
        print(f"Member '{member.name}' has been updated.")

    def delete_member(self, member):
        self.library.remove_member(member)

# Sample usage of the Library, Member, and Admin classes
library = Library()

# Adding books to the library
book1 = Book("Python Crash Course", "Eric Matthes", "Programming")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display available books
library.display_books()

# Creating a member
member1 = Member("John Doe", "johndoe@example.com")
library.add_member(member1)

# Issuing a book to a member
library.issue_book("Python Crash Course", member1)

# Attempting to issue a book that is already issued
library.issue_book("Python Crash Course", member1)

# Returning a book
library.return_book("Python Crash Course")

# Attempting to return a book that is already returned
library.return_book("Python Crash Course")

# Displaying available books
library.display_books()

# Searching for a book
library.search_book("the great gatsby")

# Creating an admin
admin1 = Admin(library)

# Updating a book
admin1.update_book(book1, "Python Crash Course, 2nd Edition", "Eric Matthes", "Programming")
library.display_books()

# Deleting a book
admin1.delete_book(book2)
library.display_books()

# Updating a member
admin1.update_member(member1, "Jane Doe", "janedoe@example.com")

# Deleting a member
# admin1.delete_member(member1)

