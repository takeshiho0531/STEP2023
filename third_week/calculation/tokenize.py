def tokenize_number():
    pass

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

def tokenize(line):
    index=0
    token_list=[]
    while index<len(line):
        if line[index]=="+":
            token, increment = tokenize_plus()
            token_list.append(token)
            index+=increment
            continue
        if line[index]=="-":
            token, increment = tokenize_minus()
            token_list.append(token)
            index+=increment
            continue
        if line[index]=="*":
            token, increment = tokenize_multiply()
            token_list.append(token)
            index+=increment
            continue
        if line[index]=="/":
            token, increment = tokenize_devide()
            token_list.append(token)
            index+=increment
            continue
