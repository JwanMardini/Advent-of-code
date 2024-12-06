import re

REGEX = r"mul[(]\d+,\d+[)]"


def read_input():
    with open("Day3/input.txt") as f:
        data = f.read().splitlines()
    return data


def multiply(data):
    data_split = data.split(",")
    left_side = data_split[0].split("(")[1]
    right_side = data_split[1].split(")")[0]
    return int(left_side) * int(right_side)


def main():
    data = read_input()
    sum = 0
    for line in data:
        list_of_mul = re.findall(REGEX, line)
        for mul in list_of_mul:
            sum += multiply(mul)
    print(sum)


if __name__ == "__main__":
    main()
