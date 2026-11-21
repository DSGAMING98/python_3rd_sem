"""Program 2c: Recursive Fibonacci series."""

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(number):
    """Return the Fibonacci value at the supplied zero-based position."""
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


try:
    terms = int(input("Enter number of terms (1-25): "))

    if not 1 <= terms <= 25:
        print("Number of terms must be between 1 and 25.")
    else:
        values = [fibonacci(index) for index in range(terms)]
        print("Fibonacci series:", *values)
except ValueError:
    print("Invalid integer input.")
