import math

number = float(input("Enter a number: "))

print("\n----- Mathematical Operations -----")
print(f"Number : {number}")
print(f"Square : {number ** 2}")
print(f"Cube : {number ** 3}")
print(f"Square Root : {math.sqrt(number)}")
print(f"Ceiling Value : {math.ceil(number)}")
print(f"Floor Value : {math.floor(number)}")
print(f"Absolute Value : {abs(number)}")
print(f"Type : {type(number)}")
print(f"Memory Address : {id(number)}")