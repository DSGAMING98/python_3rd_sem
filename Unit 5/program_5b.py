"""Program 5b: Library management system."""


class Library:
    """Track available and borrowed copies of each book."""

    def __init__(self):
        self.stock = {"Python": 3, "Java": 2, "DBMS": 2}
        self.borrowed = {}

    def display(self):
        for name, copies in self.stock.items():
            print(f"{name}: {copies} copies")

    def borrow(self, name):
        if self.stock.get(name, 0) <= 0:
            print("Book unavailable")
        else:
            self.stock[name] -= 1
            self.borrowed[name] = self.borrowed.get(name, 0) + 1
            print(name, "borrowed")

    def return_book(self, name):
        if self.borrowed.get(name, 0) <= 0:
            print("No borrowed copy to return")
        else:
            self.borrowed[name] -= 1
            self.stock[name] += 1
            print(name, "returned")


library = Library()

while True:
    print("\nLIBRARY | 1 Display | 2 Borrow | 3 Return | 4 Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
        library.display()
    elif choice == "2":
        library.borrow(input("Book name: ").strip().title())
    elif choice == "3":
        library.return_book(input("Book name: ").strip().title())
    elif choice == "4":
        print("Library closed")
        break
    else:
        print("Invalid choice")
