# from third_week.read_letter import (
    # parse_by_parentheses,
    # read_divide,
    # read_minus,
    # read_multiply,
    # read_number,
    # read_plus,
# )
from read_letter import (
        parse_by_parentheses,
    read_divide,
    read_minus,
    read_multiply,
    read_number,
    read_plus,
)



def tokenize(letters):
    tokens = []
    index = 0
    while index < len(letters):
        if letters[index].isdigit() or letters[index]==".":
            (token, index) = read_number(letters, index)
        #elif letters[index] == "+":
        elif letters[index] == "+":
            (token, index) = read_plus(letters, index)
        elif letters[index] == "-":
            (token, index) = read_minus(letters, index)
        elif letters[index] == "*":
            (token, index) = read_multiply(letters, index)
        elif letters[index] == "/":
            (token, index) = read_divide(letters, index)
        else:
            print("Invalid character found: " + letters[index])
            exit(1)
        print("token", token)
        tokens.append(token)
    return tokens


def calculate_by_token(tokens):
    answer = 0
    tokens.insert(0, {"type": "PLUS"})  # Insert a dummy "+" token
    index = 1
    while index < len(tokens):
        if tokens[index]["type"] == "Number":
            if tokens[index - 1]["type"] == "Multiply":
                answer *= tokens[index]["number"]
            elif tokens[index - 1]["type"] == "DEVIDE":
                answer /= tokens[index]["number"]
        index += 1
        print("answer1", answer)
    index=1
    while index < len(tokens):
        if tokens[index]["type"] == "Number":
            if tokens[index - 1]["type"] == "PLUS":
                answer += tokens[index]["number"]
                print("index",index)
            elif tokens[index - 1]["type"] == "MINUS":
                answer -= tokens[index]["number"]
        index += 1
    return answer


def calculate(letters):
    print("letters",letters)
    tokens_list = tokenize(letters)
    print(tokens_list)
    answer = calculate_by_token(tokens_list)
    print("answer", answer)
    return answer


def integrate(whole_letters, parentheses_index_list):
    answer = 0
    if parentheses_index_list==[]:
        answer = calculate(whole_letters)
    else:
        for i in range(len(parentheses_index_list)):
            parentheses_index = parentheses_index_list[i]
            answer_by_parse = calculate(
                whole_letters[(parentheses_index[0] + 1) : (parentheses_index[1] - 1)]
            )
            whole_letters[parentheses_index[0] + 2] = "."
            whole_letters[(parentheses_index[0] + 3) : (parentheses_index[1] - 1)] = "0"
            answer += answer_by_parse
    return answer


def main():
    while True:
        whole_letters = input()
        parentheses_index_list = parse_by_parentheses(whole_letters)
        answer = integrate(whole_letters, parentheses_index_list)
    print("answer = %d\n" % answer)

def test(line):
    #tokens = tokenize(line)
    print("line", line)
    parentheses_index_list = parse_by_parentheses(line)
    actual_answer = integrate(line, parentheses_index_list)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))

def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    print("==== Test finished! ====\n")

run_test()
