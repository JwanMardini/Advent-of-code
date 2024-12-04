def read_input():
    with open("2024/Day2/test_input.txt") as f:
        data = f.read().splitlines()
    return data


def is_safe(data):
    differences = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    increasing = True
    decreasing = True

    for diff in differences:
        if not (1 <= diff <= 3):
            increasing = False
        if not (-3 <= diff <= -1):
            decreasing = False

    return increasing or decreasing


def is_safe_with_dampener(data):
    # Check if already safe
    if is_safe(data):
        return True

    # Try removing one level
    for i in range(len(data)):
        modified_report = data[:i] + data[i+1:]
        if is_safe(modified_report):
            return True

    return False


def read_reports(data):
    number_of_safe_reports_task1 = 0
    number_of_safe_reports_task2 = 0
    for line in data:
        levels = list(map(int, line.split()))
        print(f"report: {levels}")
        if is_safe(levels):
            number_of_safe_reports_task1 += 1
        if is_safe_with_dampener(levels):
            number_of_safe_reports_task2 += 1
    return number_of_safe_reports_task1, number_of_safe_reports_task2


def main():
    data = read_input()
    task1, task2 = read_reports(data)
    print(f"Number of safe reports: {task1}")
    print(f"Number of safe reports with dampener: {task2}")


if __name__ == "__main__":
    main()
