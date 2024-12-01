def calculate_difference(input_str):
    # Split the input string by spaces
    parts = input_str.split()
    
    # Ensure exactly two numbers are entered
    if len(parts) != 2:
        return "Invalid input. Please enter exactly two numbers separated by 3 spaces."
    
    try:
        # Convert both numbers to integers
        num1 = int(parts[0])
        num2 = int(parts[1])
        
        # Calculate the difference, always positive
        diff = abs(num2 - num1)
        return diff
    except ValueError:
        return "Invalid input. Please enter valid numbers."

def main():
    differences = []  # List to store differences
    
    while True:
        # Ask for user input
        user_input = input("Enter two numbers separated by 3 spaces (or type 'done' to finish): ")
        
        # If the user is done, break the loop
        if user_input.lower() == 'done':
            break
        
        # Call the function and store the result
        result = calculate_difference(user_input)
        
        # If the result is valid (not an error message), store it
        if isinstance(result, int):
            differences.append(result)
        else:
            print(result)  # Print the error message if input is invalid
    
    # After all inputs, print all differences
    if differences:
        print("\nDifferences for all inputs:")
        for diff in differences:
            print(diff)
    else:
        print("No valid input was entered.")

# Run the main function
main()
