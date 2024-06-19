# Redefine the necessary function and data, and recalculate the result

# Function to find and sum all part numbers adjacent to symbols
def find_sum_of_part_numbers(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    symbols = set('*#%+=-&/@$')
    part_numbers_sum = 0

    def is_symbol_adjacent(i, j):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and schematic[ni][nj] in symbols:
                    return True
        return False

    #visited = set()
    
    for i in range(rows):
        j = 0
        while j < cols:
            if schematic[i][j].isdigit():
                # Find the full number
                start = j
                while j < cols and schematic[i][j].isdigit():
                    j += 1
                number = int("".join(schematic[i][start:j]))
                
                # Check adjacency for the whole number
                if any(is_symbol_adjacent(i, k) for k in range(start, j)):
                    part_numbers_sum += number
            j += 1
    
    return part_numbers_sum

# Read the schematic from the file
with open('Day3/data.txt') as f:
    schematic = f.read().splitlines()


# Calculate the sum of part numbers
part_numbers_sum = find_sum_of_part_numbers(schematic)
print(part_numbers_sum)
