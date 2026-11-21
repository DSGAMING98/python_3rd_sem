"""Program 4c: CSV-based payroll management."""

import csv
from pathlib import Path

path = Path(__file__).with_name("payroll.csv")

print("CSV PAYROLL MANAGEMENT")
emp_id = input("Employee ID: ").strip()
name = input("Employee name: ").strip()

try:
    basic = float(input("Basic salary: "))
    allowance = float(input("Allowance: "))
    deduction = float(input("Deduction: "))
    if not emp_id or not name or min(basic, allowance, deduction) < 0:
        raise ValueError("Invalid employee information")

    net_salary = basic + allowance - deduction
    if net_salary < 0:
        raise ValueError("Net salary cannot be negative")

    new_file = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if new_file:
            writer.writerow(
                ["ID", "Name", "Basic", "Allowance", "Deduction", "Net"]
            )
        writer.writerow(
            [emp_id, name, basic, allowance, deduction, net_salary]
        )

    print(f"Net salary: Rs {net_salary:.2f}")
    print("PAYROLL RECORDS")
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle):
            print(" | ".join(row))
except (ValueError, OSError) as error:
    print("Payroll error:", error)
