#Q11. Library system. Write Book (title, author, is_issued) and Library (a list of books). Add add_book(), show_available(), issue_book(title) and return_book(title). Handle a book that does not exist or is already issued.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_available(self):
        available_books = [book for book in self.books if not book.is_issued]
        for book in available_books:
            print(f"- {book.title} by {book.author}")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book issued: {book.title}")
                else:
                    print(f"Book is already issued: {book.title}")
                return
        print(f"Book not found: {title}")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book returned: {book.title}")
                else:
                    print(f"Book is not issued: {book.title}")
                return
        print(f"Book not found: {title}")
library = Library()
while True:
    action = input("Choose an action (add, show, issue, return, exit): ").lower()
    if action == "add":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book = Book(title, author)
        library.add_book(book)
        print(f"Book added: {title} by {author}")
    elif action == "show":
        print("Available books:")
        library.show_available()
    elif action == "issue":
        title = input("Enter book title to issue: ")
        library.issue_book(title)
    elif action == "return":
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif action == "exit":
        break
    else:
        print("Invalid action. Please try again.")
print("Exiting the library system. Goodbye!")