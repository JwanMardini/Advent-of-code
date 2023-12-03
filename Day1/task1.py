FILE_PATH = "Day1/data.txt"
result = 0
with open(FILE_PATH, "r") as file:
    for line in file:
        digits = ""
        for char in line:
            if char.isdigit():
                digits += char
        if digits:
            print(digits[0]+digits[digits.__len__()-1])
            result += int(digits[0]+digits[digits.__len__()-1])
print(result)
