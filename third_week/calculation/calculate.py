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
    
def make_plain(line):
    token_list = tokenize(line)
    plain_token_list=[]

    idx=0
    while idx<len(token_list):
        if ((token_list[idx]["type"]=="MULTIPLY") or (token_list[idx]["type"]=="DIVIDE")):
            value=token_list[idx-1]["value"]
            while (idx<len(token_list)) and ((token_list[idx]["type"]=="MULTIPLY") or (token_list[idx]["type"]=="DIVIDE")):
                if token_list[idx]["type"]=="MULTIPLY":
                    value*=token_list[idx+1]["value"]
                    idx+=2
                elif token_list[idx]["type"]=="DIVIDE":
                    value/=token_list[idx+1]["value"]
                    idx+=2
            else:
                new_token={"type": "NUMBER", "value": value}
                plain_token_list.append(new_token)
        elif (token_list[idx]["type"]=="PLUS"):
            plain_token_list.append(token_list[idx])
            idx+=1
        elif (token_list[idx]["type"]=="MINUS"):
            plain_token_list.append(token_list[idx])
            idx+=1
        elif (token_list[idx]["type"]=="NUMBER"):
            if (idx+1<len(token_list)) and ((token_list[idx+1]["type"]=="MULTIPLY") or (token_list[idx+1]["type"]=="DEVIDE")):
                idx+=1
            else:
                plain_token_list.append(token_list[idx])
                idx+=1
    else:
        return plain_token_list



def calculate(line):
    # 括弧ある場合はまず除く。
    plain_token_list = make_plain(line)
    plain_token_list.insert(0, {'type': 'PLUS'})
    print("token_list_calculate_plain", plain_token_list)

    answer=0
    idx=0

    while idx<len(plain_token_list):
        if plain_token_list[idx]["type"]=="NUMBER":
            idx+=1
        elif plain_token_list[idx]["type"]=="PLUS":
            answer+=plain_token_list[idx+1]["value"]
            idx+=2
        elif plain_token_list[idx]["type"]=="MINUS":
            answer-=plain_token_list[idx+1]["value"]
            idx+=2
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
    test("1+2+3*4/5")
    print("==== Test finished! ====\n")

run_test()

