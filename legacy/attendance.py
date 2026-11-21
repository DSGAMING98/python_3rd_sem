import csv
import os
import sys
from datetime import date

FILE_NAME = "attendance.csv"

# Create attendance file

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Attendance"])


# Mark Attendance

def attendance():
    create_file()

    name = input("Enter student name: ").strip()

    status = input("Enter attendance (P = Present / A = Absent): ").upper()

    if status not in ["P", "A"]:
        print("❌ Invalid attendance. Enter only P or A.")
        return

    today = date.today()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, today, status])

    if status == "P":
        print(f"✅ {name} marked PRESENT")
    else:
        print(f"❌ {name} marked ABSENT")


# Display All Attendance

def display():
    create_file()

    print("\n----------- ATTENDANCE -----------")
    print(f"{'NAME':20} {'DATE':15} {'STATUS'}")
    print("-" * 45)

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            name, attendance_date, status = row

            if status == "P":
                status_text = "Present"
            else:
                status_text = "Absent"

            print(f"{name:20} {attendance_date:15} {status_text}")

    print("-" * 45)


# Search Student

def student():
    create_file()

    search_name = input("Enter student name: ").strip().lower()

    found = False

    print("\n------ STUDENT ATTENDANCE ------")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            name, attendance_date, status = row

            if name.lower() == search_name:

                found = True

                if status == "P":
                    status_text = "Present"
                else:
                    status_text = "Absent"

                print(
                    f"Name: {name} | Date: {attendance_date} | Attendance: {status_text}"
                )

    if not found:
        print("Student not found.")


# Terminal Commands

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("""
Attendance Management System

Commands:

python attendance.py attendance
python attendance.py display
python attendance.py student
""")

    else:

        command = sys.argv[1].lower()

        if command == "attendance":
            attendance()

        elif command == "display":
            display()

        elif command == "student":
            student()

        else:
            print("❌ Unknown command")