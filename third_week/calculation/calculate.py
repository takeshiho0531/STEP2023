"""
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
    token_list.insert(0, {'type': 'PLUS'})
    print("token_list_calculate", token_list)

    answer=0
    idx=0

    while idx<len(token_list):
        token=token_list[idx]
        if (token["type"]=="MULTIPLY") or (token["type"]=="DIVIDE"):
            assert idx>=2
            first_idx=idx-1
            tmp=token_list[idx-1]["value"]
            if token_list[idx+1]["type"]=="MULTIPLY":
                tmp*=token_list[idx+1]["value"]
            elif token_list[idx+1]["type"]=="DIVIDE":
                tmp/=token_list[idx+1]["value"]
            idx+=2
            while (idx<len(token_list)) and ((token_list[idx]["type"]=="MULTIPLY") or (token_list[idx]["type"]=="DIVIDE")):
                if token_list[idx+1]["type"]=="MULTIPLY":
                    tmp*=token_list[idx+1]["value"]
                elif token_list[idx+1]["type"]=="DIVIDE":
                    tmp/=token_list[idx+1]["value"]
                idx+=2
            else:
                if token_list[first_idx-1]["type"]=="PLUS":
                    answer+=tmp
                    print("answer_plus", tmp)
                elif token_list[first_idx-1]["type"]=="MINUS":
                    answer-=tmp
                    print("answer_minus", answer)
        elif (token["type"]=="PLUS"):
            if (idx+2<len(token_list)) and ((token_list[idx+2]["type"]=="MULTIPLY") or (token_list[idx+2]["type"]=="DIVIDE")):
                idx+=2
            else:
                answer+=token_list[idx+1]["value"]
                idx+=1
        elif (token["type"]=="MINUS"):
            if (idx+2<len(token_list)) and ((token_list[idx+2]["type"]=="MULTIPLY") or (token_list[idx+2]["type"]=="DIVIDE")):
                idx+=2
            else:
                answer-=token_list[idx+1]["value"]
                idx+=1
        else:
            idx+=1
    else:
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
    test("1*2-2")
    test("1+2*3-7")
    test("1+2+3+4*5*6")
    #test("1+2+3*4/5")
    print("==== Test finished! ====\n")

run_test()

