def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def parse_products(line: str):
    return line.split(",")


def parse_product_id(ids: list):
    return [i.split("-") for i in ids]


def check_validity_task1(p: list):
    result = 0
    first = int(p[0])
    second = int(p[1])
    for i in range(first, second + 1):
        value = str(i)
        if len(value) % 2 != 0:
            continue
        else:
            length = len(value)
            half = length // 2
            first_part = value[:half]
            second_part = value[half:]
            if first_part != second_part:
                continue
            elif first_part.startswith("0"):
                continue
            else:
                result += i
    return result


def check_validity_task2(p: list):
    first = int(p[0])
    second = int(p[1])
    total = 0
    for i in range(first, second + 1):
        value = str(i)
        length = len(value)
        invalid = False
        for u in range(1, length // 2 + 1):
            if length % u != 0:
                continue
            repeats = length // u
            if repeats < 2:
                continue
            unit = value[:u]
            if unit.startswith("0"):
                continue
            if unit * repeats == value:
                invalid = True
                break
        if invalid:
            total += i

    return total


def main():
    result = 0
    file_content = read_file("./2025/Day2/input.txt")
    parsed_products = parse_products(file_content)
    parsed_id = parse_product_id(parsed_products)
    for p in parsed_id:
        result += check_validity_task2(p)
    print(result)


if __name__ == "__main__":
    main()
