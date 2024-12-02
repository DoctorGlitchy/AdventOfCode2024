def is_safe(report):
    # Check if the report is consistently increasing or decreasing
    is_increasing = all(0 < report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    is_decreasing = all(0 < report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return is_increasing or is_decreasing

def count_safe_reports():
    print("Enter the reports line by line (press Enter on an empty line to finish):")
    data = []
    while True:
        line = input()
        if not line.strip():  # Stop input on empty line
            break
        data.append([int(level) for level in line.split()])

    # Count the number of safe reports
    return sum(1 for report in data if is_safe(report))

# Main logic
safe_count = count_safe_reports()
print(f"Number of safe reports: {safe_count}")
