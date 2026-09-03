name = input("Enter Student Name: ")
usn = input("Enter USN (25BTRCLXXX): ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

mark1 = float(input("Enter Marks of Subject 1: "))
mark2 = float(input("Enter Marks of Subject 2: "))
mark3 = float(input("Enter Marks of Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n----- STUDENT DETAILS -----")
print("Student Name :", name)
print("USN          :", usn)
print("Branch       :", branch)
print("Semester     :", semester)
print("Subject 1    :", mark1)
print("Subject 2    :", mark2)
print("Subject 3    :", mark3)
print("Total Marks  :", total)
print("Average Marks:", average)