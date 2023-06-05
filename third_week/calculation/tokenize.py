def tokenize_number(line, index):
    idx = index
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    number = 0
    decimal_point_idx = None
    while idx < len(line):
        if line[idx] in digits:
            if line[idx] == ".":
                decimal_point_idx = idx
                idx += 1
                continue
            else:
                number = number * 10 + int(line[idx])
                idx += 1
                continue
        else:
            break
    if decimal_point_idx is None:
        number = number
    else:
        number /= 10 ** (idx - decimal_point_idx - 1)
    increment = idx - index
    return {"type": "NUMBER", "value": number}, increment


def tokenize_plus():
    increment = 1
    return {"type": "PLUS"}, increment


def tokenize_minus():
    increment = 1
    return {"type": "MINUS"}, increment


def tokenize_multiply():
    increment = 1
    return {"type": "MULTIPLY"}, increment


def tokenize_devide():
    increment = 1
    return {"type": "DEVIDE"}, increment

def tokenize_left_bracket():
    increment = 1
    return {"type": "LEFT_BRACKET"}, increment

def tokenize_right_bracket():
    increment = 1
    return {"type": "RIGHT_BRACKET"}, increment


def tokenize(line):
    index = 0
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    token_list = []
    while index < len(line):
        if line[index] in digits:
            token, increment = tokenize_number(line, index)
            token_list.append(token)
            index += increment
            continue
        if line[index] == "+":
            token, increment = tokenize_plus()
            token_list.append(token)
            index += increment
            continue
        if line[index] == "-":
            token, increment = tokenize_minus()
            token_list.append(token)
            index += increment
            continue
        if line[index] == "*":
            token, increment = tokenize_multiply()
            token_list.append(token)
            index += increment
            continue
        if line[index] == "/":
            token, increment = tokenize_devide()
            token_list.append(token)
            index += increment
            continue
    return token_list


def tokenize_with_brackets(line):
    index = 0
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    token_list = []
    while index < len(line):
        if line[index] in digits:
            token, increment = tokenize_number(line, index)
            token_list.append(token)
            index += increment
            continue
        if line[index] == "+":
            token, increment = tokenize_plus()
            token_list.append(token)
            index += increment
            continue
        if line[index] == "-":
            token, increment = tokenize_minus()
            token_list.append(token)
            index += increment
            continue
        if line[index] == "*":
            token, increment = tokenize_multiply()
            token_list.append(token)
            index += increment
            continue
        if line[index] == "/":
            token, increment = tokenize_devide()
            token_list.append(token)
            index += increment
            continue
        if line[index] == "(":
            token, increment = tokenize_left_bracket()
            token_list.append(token)
            index += increment
            continue
        if line[index] == ")":
            token, increment = tokenize_right_bracket()
            token_list.append(token)
            index += increment
            continue
    return token_list
