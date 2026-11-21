"""Program 2b: Prime-number test and factorial calculation."""

import math

try:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Negative numbers are not accepted.")
    else:
        is_prime = number > 1 and all(
            number % divisor for divisor in range(2, math.isqrt(number) + 1)
        )
        print(f"{number} is {'prime' if is_prime else 'not prime'}.")

        factorial = 1
        for value in range(2, number + 1):
            factorial *= value
        print(f"Factorial of {number} = {factorial}")
except ValueError:
    print("Invalid integer input.")
