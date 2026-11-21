"""Program 1b: Variables, operators, and input/output."""

try:
    price1 = float(input("Enter price of item 1: "))
    qty1 = int(input("Enter quantity of item 1: "))
    price2 = float(input("Enter price of item 2: "))
    qty2 = int(input("Enter quantity of item 2: "))

    if min(price1, price2, qty1, qty2) < 0:
        print("Price and quantity must not be negative.")
    else:
        subtotal = price1 * qty1 + price2 * qty2
        discount = subtotal * 0.10
        print(f"Subtotal: Rs {subtotal:.2f}")
        print(f"Discount (10%): Rs {discount:.2f}")
        print(f"Amount payable: Rs {subtotal - discount:.2f}")
except ValueError:
    print("Invalid input. Enter numeric values.")
