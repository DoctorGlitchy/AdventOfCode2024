def is_safe(report):
    """Checks if a report is safe according to the rules."""
    is_increasing = all(0 < report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    is_decreasing = all(0 < report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return is_increasing or is_decreasing

def is_safe_with_dampener(report):
    """Checks if a report can be made safe by removing one level."""
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports():
    print("Enter the reports line by line (press Enter on an empty line to finish):")
    data = []
    while True:
        line = input()
        if not line.strip():  # Stop input on empty line
            break
        data.append([int(level) for level in line.split()])

    # Count the number of safe reports considering the Problem Dampener
    safe_count = 0
    for report in data:
        if is_safe(report) or is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

# Main logic
safe_count = count_safe_reports()
print(f"Number of safe reports (with Problem Dampener): {safe_count}")
