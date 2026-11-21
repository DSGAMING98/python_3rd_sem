"""Program 1D: Menu-driven unit converter."""

print("UNIT CONVERTER")
print("1. Kilometres to miles")
print("2. Celsius to Fahrenheit")
choice = input("Choose conversion (1/2): ").strip()

try:
    if choice == "1":
        km = float(input("Enter distance in km: "))
        print(f"{km:.2f} km = {km * 0.621371:.2f} miles")
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius:.2f} C = {celsius * 9 / 5 + 32:.2f} F")
    else:
        print("Invalid menu choice.")
except ValueError:
    print("Invalid numeric input.")
