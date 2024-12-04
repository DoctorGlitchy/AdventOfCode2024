def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Helper function to check MAS on a diagonal
    def check_mas(r1, c1, r2, c2, r3, c3):
        if (0 <= r1 < rows and 0 <= c1 < cols and
            0 <= r2 < rows and 0 <= c2 < cols and
            0 <= r3 < rows and 0 <= c3 < cols):
            # Check for "MAS" or "SAM" pattern
            if (grid[r1][c1] == 'M' and grid[r2][c2] == 'A' and grid[r3][c3] == 'S'):
                return True
            if (grid[r1][c1] == 'S' and grid[r2][c2] == 'A' and grid[r3][c3] == 'M'):
                return True
        return False

    # Iterate over the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'A':  # Potential center of an X-MAS
                # Check top-left to bottom-right diagonal
                diagonal1 = check_mas(r - 1, c - 1, r, c, r + 1, c + 1)
                # Check top-right to bottom-left diagonal
                diagonal2 = check_mas(r - 1, c + 1, r, c, r + 1, c - 1)
                if diagonal1 and diagonal2:
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

# Convert the grid into a list of lists
grid = [list(row) for row in grid]

# Find and print the number of X-MAS occurrences
result = count_xmas(grid)
print(f"X-MAS occurs {result} times in the grid.")
