from read_letter import read_number, read_plus, read_minus, read_multiply, read_divide, get_string_in_parentheses

def tokenize(letters):
    tokens = []
    index = 0
    while index < len(letters):
        if letters[index].isdigit():
            (token, index) = read_number(letters, index)
        elif letters[index] == '+':
            (token, index) = read_plus(letters, index)
        elif letters[index] == '-':
            (token, index) = read_minus(letters, index)
        elif letters[index] == '*':
            (token, index) = read_multiply(letters, index)
        elif letters[index] == '/':
            (token, index) = read_divide(letters, index)
        else:
            print('Invalid character found: ' + letters[index])
            exit(1)
        tokens.append(token)
    return tokens


def calculate(tokens):
    answer = 0
    tokens.insert(0, {'type': "PLUS"}) # Insert a dummy "+" token
    index=1
    while index<len(tokens):
        if tokens[index]["type"]=="NUMBER":
            if tokens[index-1]["type"]=="Multiply":
                answer*=tokens[index]["number"]
            elif tokens[index-1]["type"]=="DEVIDE":
                answer/=tokens[index]["number"]
        index+=1
    while index<len(tokens):
        if tokens[index]["type"]=="NUMBER":
            if tokens[index-1]["type"]=="PLUS":
                answer+=tokens[index]["number"]
            elif tokens[index-1]["type"]=="MINUS":
                answer-=tokens[index]["number"]
        index+=1
    return answer



def main():
    while True:
        letters=input()
        tokens_list=tokenize(letters)
        answer=calculate(tokens_list)
    print("answer = %d\n" % answer)
