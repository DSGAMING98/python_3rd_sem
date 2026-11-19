
import csv
import os

filename = "payroll.csv"

while True:
    print("\n--- Payroll Management System ---")
    print("1. Add Employee")
    print("2. Display Payroll")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))
        allowance = float(input("Enter Allowance: "))
        deduction = float(input("Enter Deduction: "))

        net_salary = basic + allowance - deduction

        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize(filename) == 0:
                writer.writerow([
                    "Employee ID", "Name", "Basic Salary",
                    "Allowance", "Deduction", "Net Salary"
                ])

            writer.writerow([
                emp_id, name, basic,
                allowance, deduction, net_salary
            ])

        print("Employee added successfully!")
        print("Net Salary:", net_salary)

    elif choice == "2":
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)

                print("\n--- Employee Payroll Records ---")
                for row in reader:
                    print(" | ".join(row))

        except FileNotFoundError:
            print("No payroll records found!")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
