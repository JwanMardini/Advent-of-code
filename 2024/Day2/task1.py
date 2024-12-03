def read_input():
    with open("Day2/input.txt") as f:
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


def read_reports(data):
    number_of_safe_reports = 0
    for line in data:
        levels = list(map(int, line.split()))
        print(f"report: {levels}")
        if is_safe(levels):
            number_of_safe_reports += 1
    return number_of_safe_reports


def main():
    data = read_input()
    safe_report_count = read_reports(data)
    print(f"Number of safe reports: {safe_report_count}")


if __name__ == "__main__":
    main()
