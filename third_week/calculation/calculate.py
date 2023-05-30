
from calculation.read_letter import (
    read_digits,
    read_divide,
    read_minus,
    read_multiply,
    read_plus,
)

"""
from read_letter import (
    read_digits,
    read_divide,
    read_minus,
    read_multiply,
    read_plus,
)
"""

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]


def tokenize(line):
    print("line", line)
    idx = 0
    token_list = []
    # if idx>= len(line):
        # print("token_list", token_list)
        # return token_list
    while idx < len(line):
        print("idx", idx)
        if line[idx] in digits:
            token = read_digits(line, start_idx=idx)
        elif line[idx] == "+":
            token = read_plus(line, start_idx=idx)
        elif line[idx] == "-":
            token = read_minus(line, start_idx=idx)
        elif line[idx] == "*":
            token = read_multiply(line, start_idx=idx)
        elif line[idx] == "/":
            token = read_divide(line, start_idx=idx)
        else:
            #print('Invalid character found: ' + line[idx])
            print('Invalid character found: ')
            print(line[idx])
            exit(1)

        token_list.append(token)
        print("nex_idx", token["next_idx"])
        idx = token["next_idx"]
        print("idx_2", idx)
        print("line2", line)
    else:
        print("token_list!", token_list)
        print("抜けた")
        return token_list


def calculate(line):
    # 括弧ある場合はまず除く。
    token_list = tokenize(line)
    print("token_list_calculate", token_list)
    #idx = 0

    #while idx < len(token_list):
        #token = token_list[idx]
        #if token["type"] == "MULTIPLY":
            #assert idx != 0
            #previous = token_list[idx - 1]
            #subsequent = token_list[idx + 1]
            #assert (previous["type"] == "NUMBER") and (subsequent["type"] == "NUMBER")
            #token[idx - 1] = {
                #"type": "NUMBER",
                #"value": previous["value"] * subsequent["value"],
                #"next_idx": None,
            #}
        #elif token["type"] == "DIVIDE":
            #assert idx != 0
            #previous = token_list[idx - 1]
            #subsequent = token_list[idx + 1]
            #assert (previous["type"] == "NUMBER") and (subsequent["type"] == "NUMBER")
            #token[idx - 1] = {
                #"type": "NUMBER",
                #"value": previous["value"] / subsequent["value"],
                #"next_idx": None,
            #}

        #token_list[idx] = None
        #token_list[idx + 1] = None
        #idx = idx + 2

    #for i in range(len(token_list)):
        #if token_list[i] is None:
            #token_list = token_list.pop(i)


    idx = 0
    answer = 0
    print("len(token_list)", len(token_list))
    while idx < len(token_list):
        token = token_list[idx]
        print("token", token)

        if token["type"] == "NUMBER":
            if idx == 0:
                previous = {"type": "PLUS", "next_idx": 1}
            else:
                previous = token_list[idx - 1]

            if previous["type"] == "PLUS":
                answer += token["value"]
            elif previous["type"] == "MINUS":
                answer -= token["value"]
        
        idx+=1

    return answer

def test(line):
    #tokens = tokenize(line)
    actual_answer = calculate(line)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    print("==== Test finished! ====\n")

run_test()
