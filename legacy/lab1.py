
try:
    error_count = 0

    with open("log.txt", "r") as file:
        print("Log File Contents:\n")

        for line in file:
            print(line, end="")

            if "ERROR" in line:
                error_count += 1

    print("\n\nTotal number of errors:", error_count)

except FileNotFoundError:
    print("Error: log.txt file does not exist.")
