"""Program 3a: Contact book using dictionaries."""

contacts = {}

while True:
    print("\nCONTACT BOOK | 1 Add | 2 Search | 3 Display | 4 Delete | 5 Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
        name = input("Name: ").strip().title()
        phone = input("Phone: ").strip()
        if not name or not phone.isdigit():
            print("Invalid contact details.")
        else:
            contacts[name] = {"phone": phone}
            print("Saved:", name)
    elif choice == "2":
        name = input("Search name: ").strip().title()
        print(name, contacts.get(name, "not found"))
    elif choice == "3":
        for name, data in sorted(contacts.items()):
            print(f"{name}: {data['phone']}")
        if not contacts:
            print("Contact book is empty.")
    elif choice == "4":
        name = input("Delete name: ").strip().title()
        print("Deleted." if contacts.pop(name, None) else "Not found.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
