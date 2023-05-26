def read_number(letters, index):
    number = 0
    if letters[index]==".":
        decimal_point_index=index

    while index<len(letters) and (letters[index].isdigit() or letters[index]=="."):
        if letters[index]==".":
            continue
        number=number*10+int(letters[index])
        index+=1

    number=number/10**(len(letters)-decimal_point_index-1)
    token = {'type': 'Number', 'number': number}
    return token, index


def read_plus(index):
    token = {'type': 'PLUS'}
    return token, index+1

def read_minus(index):
    token = {'type': 'MINUS'}
    return token, index+1

def read_multiply(index):
    token = {'type': 'MULTIPLY'}
    return token, index+1

def read_divide(index):
    token = {'type': 'DEVIDE'}
    return token, index+1

def get_string_in_parentheses():
    pass

