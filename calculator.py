# Basic Calculator Program (Loop + Save + History Preview + History Command)

import datetime
import os

HISTORY_FILE = "results.txt"

print(" Simple Calculator")
print("Type your expression (e.g., 10+5, 8-3, 4*2, 9/3)")
print("Type 'history' to view all saved results")
print("Type 'exit' to quit.\n")

# Show last 5 results if history exists
if os.path.exists(HISTORY_FILE):
    print(" Last 5 Results:")
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()[-5:]  # get last 5 lines
        for line in lines:
            print(line.strip())
    print("\n")

while True:
    # Ask user for input
    expression = input("Enter expression: ")

    # Exit condition
    if expression.lower() == "exit":
        print(" Goodbye!")
        break

    # History command
    if expression.lower() == "history":
        if os.path.exists(HISTORY_FILE):
            print("\n Full History:")
            with open(HISTORY_FILE, "r") as file:
                for line in file:
                    print(line.strip())
            print()
        else:
            print(" No history found.\n")
        continue

    try:
        # Evaluate expression
        result = eval(expression)
        output = f"{expression} = {result}"

        # Print result
        print(output)

        # Add timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {output}"

        # Save to results.txt
        with open(HISTORY_FILE, "a") as file:
            file.write(log_entry + "\n")

        print(" Result saved to results.txt\n")

    except ZeroDivisionError:
        print(" Error: Division by zero is not allowed.\n")
    except Exception:
        print(" Invalid input. Please enter in the format: number operator number\n")
