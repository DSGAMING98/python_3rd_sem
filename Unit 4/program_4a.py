"""Program 4a: Read and display a prepared application log file."""

from pathlib import Path

log_path = Path(__file__).with_name("sample_system.log")

try:
    lines = log_path.read_text(encoding="utf-8").splitlines()
    print("APPLICATION LOG READER")
    for line_number, line in enumerate(lines, start=1):
        print(f"{line_number}: {line}")
    print("Total log entries:", len(lines))
except FileNotFoundError:
    print("Error: sample_system.log not found.")
except OSError as error:
    print("Cannot read log:", error)
