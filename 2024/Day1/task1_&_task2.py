def read_input():
    with open("2024/Day1/input.txt") as f:
        data = f.read().splitlines()
    return data


def read_left_and_right(data):
    return data.split("   ")[0], data.split("   ")[1]


def convert_to_int(data):
    for i in range(len(data)):
        data[i] = int(data[i])


def get_left_and_right(data):
    left_list = []
    right_list = []

    for i in data:
        left, right = read_left_and_right(i)
        left_list.append(left)
        right_list.append(right)

    convert_to_int(left_list)
    convert_to_int(right_list)
    return left_list, right_list


def task_1(left, right):
    result = 0

    for i in range(len(left)):
        if min(left) < min(right):
            diff = min(right) - min(left)
        else:
            diff = min(left) - min(right)

        left.remove(min(left))
        right.remove(min(right))
        result += diff

    return result


def task_2(left, right):
    result = 0
    for i in left:
        apperances = 0
        for j in right:
            if i == j:
                apperances += 1
        result += i * apperances
        apperances = 0
    return result


def main():
    data = read_input()
    left, right = get_left_and_right(data)
    # task1 = task_1(left, right)
    # print(task1)
    task2 = task_2(left, right)
    print(task2)


if __name__ == "__main__":
    main()
