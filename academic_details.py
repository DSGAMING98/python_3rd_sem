# Student Information and Academic Summary

name = input("Enter Student Name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

mark1 = float(input("Enter Marks in Subject 1: "))
mark2 = float(input("Enter Marks in Subject 2: "))
mark3 = float(input("Enter Marks in Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\nSTUDENT REPORT")
print(f"Name : {name}")
print(f"USN : {usn}")
print(f"Branch : {branch}")
print(f"Semester : {semester}")
print(f"Total Marks : {total}")
print(f"Average : {average:.2f}")