import json
import os
from datetime import datetime

filename = "logs.json"

# Create JSON file if it does not exist
if not os.path.exists(filename):
    with open(filename, "w") as file:
        json.dump([], file, indent=4)

while True:
    print("\n--- JSON Log File Analyzer ---")
    print("1. Add Log")
    print("2. Display All Logs")
    print("3. Analyze Logs")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        with open(filename, "r") as file:
            logs = json.load(file)

        if not isinstance(logs, list):
            raise ValueError("Invalid log data")

        if choice == "1":
            level = input(
                "Enter Log Level (INFO/WARNING/ERROR): "
            ).upper()

            if level not in ["INFO", "WARNING", "ERROR"]:
                print("Invalid log level!")
                continue

            message = input("Enter Message: ")

            log = {
                "timestamp": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "level": level,
                "message": message
            }

            logs.append(log)

            with open(filename, "w") as file:
                json.dump(logs, file, indent=4)

            print("Log created and stored successfully!")

        elif choice == "2":
            print("\n--- All Log Records ---")

            if not logs:
                print("No logs found.")

            for log in logs:
                print(log["timestamp"],
                      log["level"],
                      log["message"])

        elif choice == "3":
            info = 0
            warning = 0
            error = 0

            for log in logs:
                if log["level"] == "INFO":
                    info += 1
                elif log["level"] == "WARNING":
                    warning += 1
                elif log["level"] == "ERROR":
                    error += 1

            print("\n--- Log Analysis ---")
            print("INFO:", info)
            print("WARNING:", warning)
            print("ERROR:", error)
            print("Total Logs:", len(logs))

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

    except FileNotFoundError:
        print("File missing! Creating new file.")
        with open(filename, "w") as file:
            json.dump([], file)

    except (json.JSONDecodeError, ValueError, KeyError, TypeError):
        print("Invalid JSON data or log structure!")
