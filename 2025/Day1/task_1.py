def read_file(file_path: str):
    with open(file_path, "r") as file:
        return file.read()


def extract_rotations(rotation: str):
    direction = ""
    number_of_rotations = ""
    chars = list(rotation)
    direction = chars[0]
    for i in range(1, len(chars)):
        number_of_rotations += chars[i]
    return direction, int(number_of_rotations)


def new_state(current, direction, number_of_rot):
    if direction == "R":
        current = (current + number_of_rot) % 100
    elif direction == "L":
        current = (current - number_of_rot) % 100
    return current


def count_hits_at_zero(start_pos, direction, number_of_rot):
    hits = 0
    if direction == "R":
        if number_of_rot > 0:
            hits = (start_pos + number_of_rot - 1) // 100
    elif direction == "L":
        if start_pos == 0:
            hits = (number_of_rot - 1) // 100 if number_of_rot > 0 else 0
        elif number_of_rot > start_pos:
            remaining = number_of_rot - start_pos
            hits = 1 + (remaining - 1) // 100
    return hits


def main():
    current = 50
    result = 0
    file_content = read_file("2025/Day1/input.txt")
    rotations = file_content.split("\n")
    for rotation in rotations:
        r, n = extract_rotations(rotation)
        start_pos = current
        zero_hits = count_hits_at_zero(start_pos, r, n)
        result += zero_hits
        current = new_state(current, r, n)
        if current == 0:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
