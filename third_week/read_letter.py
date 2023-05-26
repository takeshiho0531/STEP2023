def read_number(letters, index):
    number = 0
    if letters[index] == ".":
        decimal_point_index = index

    while index < len(letters) and (letters[index].isdigit() or letters[index] == "."):
        if letters[index] == ".":
            continue
        number = number * 10 + int(letters[index])
        index += 1

    number = number / 10 ** (len(letters) - decimal_point_index - 1)
    token = {"type": "Number", "number": number}
    return token, index


def read_plus(index):
    token = {"type": "PLUS"}
    return token, index + 1


def read_minus(index):
    token = {"type": "MINUS"}
    return token, index + 1


def read_multiply(index):
    token = {"type": "MULTIPLY"}
    return token, index + 1


def read_divide(index):
    token = {"type": "DEVIDE"}
    return token, index + 1


def parse_by_parentheses(letters):
    letter_list = []
    starting_parenthese_index_list = []
    parentheses_index_list = []
    for i in range(len(letters)):
        letter_list.append(letters[i])
        if letters[i] == "(":
            starting_parenthese_index_list.append(i)
        if letters[i] == ")":
            starting_parenthese_index = starting_parenthese_index_list[-1]
            parentheses_index_list.append((starting_parenthese_index, i))
            starting_parenthese_index_list = starting_parenthese_index_list[:-1]
    return parentheses_index_list
