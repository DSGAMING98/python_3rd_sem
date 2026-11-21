filename = input("Enter file type (txt/csv): ").lower()

if filename == "csv":
    filename = "students.csv"
else:
    filename = "students.txt"

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        with open(filename, "a") as file:
            file.write(f"{roll},{name},{marks}\n")

        print("Student added successfully!")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                print("\nRoll No, Name, Marks")
                print(file.read())
        except FileNotFoundError:
            print("No records found!")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
