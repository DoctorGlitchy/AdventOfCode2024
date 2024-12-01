# Function to calculate the total distance
def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Initialize total distance
    total_distance = 0
    
    # Calculate the sum of absolute differences
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

# Function to read the multi-line input and convert it to a list of integers
def read_input():
    print("Enter the left list of numbers (multi-line, press Enter twice to end):")
    left_list = []
    while True:
        line = input()
        if line == "":
            break
        left_list.append(int(line))
    
    print("Enter the right list of numbers (multi-line, press Enter twice to end):")
    right_list = []
    while True:
        line = input()
        if line == "":
            break
        right_list.append(int(line))

    return left_list, right_list

# Get the input from the user
left_list, right_list = read_input()

# Calculate the total distance
result = calculate_total_distance(left_list, right_list)

# Output the result
print(f"The total distance is: {result}")
