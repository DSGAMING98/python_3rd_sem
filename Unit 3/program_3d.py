"""Program 3D: Mini attendance tracker."""

students = ["Prajwal", "Nandan", "Ronakk", "Namgay"]
attendance = {}

print("ATTENDANCE TRACKER")
for student in students:
    answer = input(f"{student} present? (P/A): ").strip().upper()
    attendance[student] = answer == "P"

print("ATTENDANCE SUMMARY")
for student, present in attendance.items():
    print(f"{student}: {'Present' if present else 'Absent'}")

present_count = sum(attendance.values())
percentage = present_count / len(students) * 100
print(f"Present: {present_count}/{len(students)}")
print(f"Attendance percentage: {percentage:.2f}%")
