"""Program 3b: Student grading system."""

try:
    name = input("Student name: ").strip()
    marks = {}

    for subject in ("Python", "Mathematics", "Operating Systems"):
        value = float(input(f"Marks in {subject} (0-100): "))
        if not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100")
        marks[subject] = value

    total = sum(marks.values())
    percentage = total / len(marks)
    grade = (
        "A" if percentage >= 90 else
        "B" if percentage >= 75 else
        "C" if percentage >= 60 else
        "D" if percentage >= 40 else
        "F"
    )

    print("STUDENT GRADE REPORT")
    print("Name:", name)
    for subject, mark in marks.items():
        print(f"{subject}: {mark:.1f}")
    print(
        f"Total: {total:.1f}/300 | "
        f"Percentage: {percentage:.2f}% | Grade: {grade}"
    )
except ValueError as error:
    print("Invalid marks:", error)
