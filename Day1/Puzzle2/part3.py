# Function to calculate the similarity score
def calculate_similarity_score(left_list, right_list):
    similarity_score = 0
    
    # For each number in the left list
    for num in left_list:
        # Count how many times it appears in the right list
        count_in_right = right_list.count(num)
        # Add the result of num * count_in_right to the similarity score
        similarity_score += num * count_in_right
    
    return similarity_score

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

# Calculate the similarity score
result = calculate_similarity_score(left_list, right_list)

# Output the result
print(f"The similarity score is: {result}")
