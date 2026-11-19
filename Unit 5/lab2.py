
class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C++", "HTML"]
        self.borrowed = []

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.borrowed.append(book)
            print("Book borrowed:", book)
        else:
            print("Book not available")

    def return_book(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)
            self.books.append(book)
            print("Book returned:", book)
        else:
            print("This book was not borrowed")


library = Library()

while True:
    print("\n1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        book = input("Enter book name: ")
        library.borrow_book(book)
    elif choice == "3":
        book = input("Enter book name: ")
        library.return_book(book)
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
