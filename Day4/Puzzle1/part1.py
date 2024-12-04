def count_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    # Directions: (row_increment, col_increment)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1), # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0), # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    # Helper function to check word in a specific direction
    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return False
        return True

    # Iterate over every cell in the grid
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count

# Input the word search grid line by line
print("Enter the word search grid line by line (press Enter on an empty line to finish):")
grid = []
while True:
    line = input()
    if not line.strip():  # Stop when an empty line is entered
        break
    grid.append(line)

# Convert the grid into a list of lists (optional)
grid = [list(row) for row in grid]

# Find and print the number of XMAS occurrences
result = count_xmas(grid)
print(f"XMAS occurs {result} times in the grid.")
