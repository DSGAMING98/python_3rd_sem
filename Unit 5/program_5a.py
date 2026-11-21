"""Program 5a: Bank account management system."""


class BankAccount:
    """Store an account owner's name and current balance."""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print("Deposit successful")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print("Invalid amount or insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")


owner = input("Account holder: ").strip()

try:
    opening_balance = float(input("Opening balance: "))
    if opening_balance < 0:
        raise ValueError
except ValueError:
    print("Invalid opening balance")
else:
    account = BankAccount(owner, opening_balance)

    while True:
        print("\n1 Deposit | 2 Withdraw | 3 Balance | 4 Exit")
        option = input("Choice: ").strip()

        if option == "4":
            print("Thank you!")
            break
        if option in ("1", "2"):
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount")
                continue

            if option == "1":
                account.deposit(amount)
            else:
                account.withdraw(amount)
        elif option == "3":
            print(f"{account.owner}'s balance: Rs {account.balance:.2f}")
        else:
            print("Invalid choice")
