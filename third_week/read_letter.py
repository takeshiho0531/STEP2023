# def read_number(letters, index):
def read_number(letters, index):
    number = 0
    # if letters[index] == ".":
        # decimal_point_index = index
    #decimal_point_index = len(letters)
    #print("decimal_point_index_0", decimal_point_index)

    decimal_point_index = None
    # print("decimal_point_index_0", decimal_point_index)
    # index=0
    while index < len(letters) and (letters[index].isdigit() or letters[index] == "."):
        if letters[index] == ".":
            # continue
            decimal_point_index = index
        else:
            number = number * 10 + int(letters[index])
        index += 1
    if decimal_point_index==None:
        decimal_point_index = index-1
    print("decimal_point_index", decimal_point_index)
    print("nubmer_1", number)
    number = number / 10 ** (index - decimal_point_index-1)
    token = {"type": "Number", "number": number}
    return token, index


def read_plus(letters, index):
    token = {"type": "PLUS"}
    return token, index + 1


def read_minus(letters, index):
    token = {"type": "MINUS"}
    return token, index + 1


def read_multiply(letters, index):
    token = {"type": "MULTIPLY"}
    return token, index + 1


def read_divide(letters, index):
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
    print("parentheses_index_list", parentheses_index_list)
    return parentheses_index_list
