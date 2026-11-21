"""Program 4b: Store and display student records in a CSV file."""

import csv
from pathlib import Path

path = Path(__file__).with_name("student_records.csv")

print("STUDENT DATA MANAGER")
usn = input("USN: ").strip().upper()
name = input("Student name: ").strip()

try:
    marks = float(input("Marks (0-100): "))
    if not usn or not name or not 0 <= marks <= 100:
        raise ValueError("Invalid student record")

    new_file = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if new_file:
            writer.writerow(["USN", "Name", "Marks"])
        writer.writerow([usn, name, marks])

    print("Record saved.")
    print("STORED STUDENTS")
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle):
            print(" | ".join(row))
except (ValueError, OSError) as error:
    print("Unable to save:", error)
