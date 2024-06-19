def is_part_number(char):
    return char.isdigit()

def get_full_number(schematic, i, j):
    cols = len(schematic[0])
    if not schematic[i][j].isdigit():
        return None, j
    
    start = j
    while j < cols and schematic[i][j].isdigit():
        j += 1
    number = int(schematic[i][start:j])
    return number, j

def find_sum_of_gear_ratios(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    gear_char = '*'
    
    def get_adjacent_numbers(i, j):
        numbers = []
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                num, nj = get_full_number(schematic, ni, nj)
                if num is not None:
                    numbers.append(num)
        return numbers
    
    gear_ratios_sum = 0
    
    for i in range(rows):
        for j in range(cols):
            if schematic[i][j] == gear_char:
                adjacent_numbers = get_adjacent_numbers(i, j)
                if len(adjacent_numbers) == 2:
                    gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    gear_ratios_sum += gear_ratio
    
    return gear_ratios_sum

# Read the schematic from the file
with open('Day3/data.txt') as f:
    schematic = f.read().splitlines()

# Calculate the sum of gear ratios
gear_ratios_sum = find_sum_of_gear_ratios(schematic)
print(gear_ratios_sum)
