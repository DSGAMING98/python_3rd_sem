
import random

while True:
    print("\nDice Simulator")
    print("1. Roll Dice")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        number = random.randint(1, 6)
        print("Dice rolled:", number)
    elif choice == "2":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice")
