# Input grid as a multiline string
with open("Day4/input.txt", "r") as file:
    grid = file.read()

# Convert the grid into a 2D matrix
matrix = [list(row.strip()) for row in grid.strip().split("\n")]

# Dimensions of the grid
rows = len(matrix)
cols = len(matrix[0])

# Valid patterns for MAS
mas_patterns = ["MAS", "SAM"]

# Function to check for X-MAS centered at (r, c)
def is_xmas(r, c):
    count = 0
    
    # Check top-left to bottom-right and bottom-left to top-right diagonals
    for mas1 in mas_patterns:
        for mas2 in mas_patterns:
            # Top-left to bottom-right diagonal
            if (
                0 <= r - 1 < rows and 0 <= c - 1 < cols and matrix[r - 1][c - 1] == mas1[0] and
                0 <= r + 1 < rows and 0 <= c + 1 < cols and matrix[r + 1][c + 1] == mas1[2] and
                matrix[r][c] == mas1[1]
            ):
                # Bottom-left to top-right diagonal
                if (
                    0 <= r - 1 < rows and 0 <= c + 1 < cols and matrix[r - 1][c + 1] == mas2[0] and
                    0 <= r + 1 < rows and 0 <= c - 1 < cols and matrix[r + 1][c - 1] == mas2[2] and
                    matrix[r][c] == mas2[1]
                ):
                    count += 1

    return count

# Count total X-MAS patterns
total_count = 0
for r in range(rows):
    for c in range(cols):
        total_count += is_xmas(r, c)

print(f"Total X-MAS patterns: {total_count}")
