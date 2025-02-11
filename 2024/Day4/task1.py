# Input grid as a multiline string
with open("Day4/input.txt", "r") as file:
    grid = file.read()

# Convert the grid into a list of lists (2D matrix)
matrix = [list(row.strip()) for row in grid.strip().split("\n")]

# Dimensions of the grid
rows = len(matrix)
cols = len(matrix[0])

# Define the target word
target = "MAS"
target_length = len(target)

# Define all possible directions to search (row, column deltas)
directions = [
    (0, 1),   # Horizontal (right)
    (0, -1),  # Horizontal (left)
    (1, 0),   # Vertical (down)
    (-1, 0),  # Vertical (up)
    (1, 1),   # Diagonal (bottom-right)
    (-1, -1), # Diagonal (top-left)
    (1, -1),  # Diagonal (bottom-left)
    (-1, 1),  # Diagonal (top-right)
]


# Function to check if the target word exists starting at (r, c) in a specific direction
def search_from_position(r, c, dr, dc):
    for k in range(target_length):
        nr, nc = r + k * dr, c + k * dc
        if not (0 <= nr < rows and 0 <= nc < cols):  # Out of bounds
            return False
        if matrix[nr][nc] != target[k]:  # Character mismatch
            return False
    return True


# Count all occurrences of the target word
count = 0
for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            if search_from_position(r, c, dr, dc):
                count += 1

# Output the result
print(f"Total occurrences of '{target}': {count}")
