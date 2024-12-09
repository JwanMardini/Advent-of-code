import re

REGEX_TASK1 = r"mul[(]\d+,\d+[)]"
REGEX_TASK2 = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"


def read_input():
    with open("Day3/input.txt") as f:
        data = f.read().splitlines()
    return data


def multiply(data):
    data_split = data.split(",")
    left_side = data_split[0].split("(")[1]
    right_side = data_split[1].split(")")[0]
    return int(left_side) * int(right_side)


def task1(data):
    sum = 0
    for line in data:
        list_of_mul = re.findall(REGEX_TASK1, line)
        for mul in list_of_mul:
            sum += multiply(mul)
    return sum


def task2(data):
    total = 0
    enable_mul = True
    for line in data:
        list_of_matches = re.findall(REGEX_TASK2, line)
        for match in list_of_matches:
            if match == "don't()":
                enable_mul = False
            elif match == "do()":
                enable_mul = True
            elif enable_mul:
                total += multiply(match)
    return total


def main():
    data = read_input()
    # task_1 = task1(data)
    # print(task_1)
    task_2 = task2(data)
    print(task_2)


if __name__ == "__main__":
    main()
