#  read from file and split by new line char into list


def read_file():
    with open("Day1/data.txt") as f:
        lines = f.read().splitlines()
    return lines


# make a function to find and return tne num as text (one,two,...) in string
def find_num_as_text(string):
    num_of_tre_char = {"one": 1, "two": 2, "six": 6}
    num_of_four_char = {"four": 4, "five": 5, "nine": 9}
    num_of_five_char = {"three": 3, "seven": 7, "eight": 8}
    num_as_text = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    return_list = []
    #  go throw the string and find the num as text and add the num befor the first char of the num
    #  and the num after the last char of the num
    for i in range(len(string)):
        char = string[i]
        if char.isdigit():
            # add the num as text to return list
            return_list.append(int(char))
        #  check if the num is one of the num of one char
        if string[i] in num_as_text:
            # add the num to the first chat in the string
            #  add the num to the list
            return_list.append(num_as_text[string[i]])
        #  check if the num is one of the num of three char
        elif string[i : i + 3] in num_of_tre_char:
            # add the num to the first chat in the string
            #  add the num to the list
            return_list.append(num_of_tre_char[string[i : i + 3]])
        #  check if the num is one of the num of four char
        elif string[i : i + 4] in num_of_four_char:
            #  add the num to the list
            return_list.append(num_of_four_char[string[i : i + 4]])
        #  check if the num is one of the num of five char
        elif string[i : i + 5] in num_of_five_char:
            #  add the num to the list
            return_list.append(num_of_five_char[string[i : i + 5]])
    return return_list


def main():
    lines = read_file()
    #  go throw the listt
    total = 0
    for line in lines:
        # check if the line is num as text
        num_as_text = find_num_as_text(line)
        #  if the num as text is not empty
        first_num = num_as_text[0] * 10
        last_num = num_as_text[-1]
        total += first_num + last_num

    print(total)


def main1():
    lines = read_file()
    #  go throw the listt
    total = 0
    for line in lines:
        first_char = 0
        last_char = 0

        #  go throw the each char and find the sava the cahr if number only the first and the last char
        for char in line:
            if char.isdigit():
                if first_char == 0:
                    first_char = char
                last_char = char
                # print the first and the last char
        # print("first char is: " + first_char)
        # print("last char is: " + last_char)
        # now combine the first and the last char and make it one number of two digits the first is tens and the last is units
        #  convert to int
        first_char = int(first_char)
        last_char = int(last_char)
        #  combine the first and the last char
        result = first_char * 10 + last_char

        #  print the result
        print("the result is: " + str(result))
        #  now calculate the result of all  the result
        #  now add the result to the total
        total = total + result
        #  print the total
        print("the total is: " + str(total))


if __name__ == "__main__":
    main()
