"""Program 1a: Basic Python Program."""

name = input("Enter your name: ").strip()

if not name:
    print("Name cannot be empty.")
else:
    print("Welcome,", name)
    print("Subject: Python Programming")
    print("Result: Basic Python program executed successfully.")
