"""Program 1c: Simple calculator and area calculations."""

import math

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {a + b:.2f}")
    print(f"Subtraction: {a - b:.2f}")
    print(f"Multiplication: {a * b:.2f}")
    print("Division:", f"{a / b:.2f}" if b else "Undefined (divisor is zero)")

    length = float(input("Rectangle length: "))
    breadth = float(input("Rectangle breadth: "))
    radius = float(input("Circle radius: "))

    if min(length, breadth, radius) < 0:
        print("Dimensions cannot be negative.")
    else:
        print(f"Rectangle area: {length * breadth:.2f}")
        print(f"Circle area: {math.pi * radius ** 2:.2f}")
except ValueError:
    print("Invalid number entered.")
