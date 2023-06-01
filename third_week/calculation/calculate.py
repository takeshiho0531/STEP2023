"""
from calculation.read_letter import (
    read_digits,
    read_divide,
    read_minus,
    read_multiply,
    read_plus,
    get_brackets_idx
)

"""
from read_letter import (
    read_digits,
    read_divide,
    read_minus,
    read_multiply,
    read_plus,
    get_brackets_idx
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

def solve_multiply_divide(multiply_divide_token_list):
    value=multiply_divide_token_list[0]["value"]
    idx=1
    while idx<len(multiply_divide_token_list):
        if multiply_divide_token_list[idx]=="MULTIPLY":
            value*=multiply_divide_token_list[idx+1]["value"]
            idx+=2
        elif multiply_divide_token_list[idx]=="DEVIDE":
            value/=multiply_divide_token_list[idx+1]["value"]
            idx+=2
    else:
        return {"type": "NUMBER", "value": value}


def make_plus_minus_only(token_list):
    idx=0
    print("token_list!!!", token_list)
    token_list.append({"type": "PLUS"})

    new_token_list=[]


    tmp_token_list=[]
    print("tkoen_list", token_list)
    # while token in token_list:
    while idx in range(len(token_list)):
        token=token_list[idx]
        print("token", token)
        if token["type"]=="NUMBER":
            tmp_token_list.append(token)
            print("tmp_token_list", tmp_token_list)
            idx+=1
            continue
        elif token["type"]=="MULTIPLY":
            tmp_token_list.append(token)
            idx+=1
            continue
        elif token["type"]=="DIVIDE":
            tmp_token_list.append(token)
            idx+=1
            continue
        else:
            print("tmp_token_list",  tmp_token_list)
            value=solve_multiply_divide(tmp_token_list)
            print("value", value)
            term_token={"type": "NUMBER", "value": value["value"]}
            print("term_token", term_token)
            # print("new_token_list", new_token_list)
            new_token_list.append(term_token)
            new_token_list.append(token)
            tmp_token_list=[]
            idx+=1
            continue
    else:
        print("new_token_list...",new_token_list)
        new_token_list=new_token_list[:-1]
        print("new_token_list.....",new_token_list)
        return new_token_list


def solve_brackets(line):
    brackets_idx_list=get_brackets_idx(line)
    print("brackets_idx_list",brackets_idx_list)
    if len(brackets_idx_list)==0:
        return calculate(line)
    else:
        brackets_pair_num=len(brackets_idx_list)/2
        print("brackets_pair_num",brackets_pair_num)
        new_line=""
        for i in range(int(brackets_pair_num)):
            line_in_brackets=line[brackets_idx_list[0]+1:brackets_idx_list[1]]
            tmp_answer=calculate(line_in_brackets)
            new_line+=line[:brackets_idx_list[0]]
            new_line+=str(tmp_answer)
            new_line+=line[brackets_idx_list[1]+1:]
            line=new_line
            print("line_koshin", line)
            brackets_idx_list=get_brackets_idx(line)
            new_line=""
        # 最初と最後が括弧で括られてることはないと考えて。
        answer=calculate(line)
        return answer


def calculate(plain_token_list):
    #plain_token_list = make_plain(line)
    plain_token_list.insert(0, {'type': 'PLUS'})
    print("token_list_calculate_plain", plain_token_list)

    answer=0
    idx=0

    while idx<len(plain_token_list):
        if plain_token_list[idx]["type"]=="NUMBER":
            idx+=1
            continue
        elif plain_token_list[idx]["type"]=="PLUS":
            answer+=plain_token_list[idx+1]["value"]
            idx+=2
            continue
        elif plain_token_list[idx]["type"]=="MINUS":
            answer-=plain_token_list[idx+1]["value"]
            idx+=2
            continue
    else:
        return answer




def test(line):
    tokens = tokenize(line)
    print("tokens!!", tokens)
    new_token_list=make_plus_minus_only(tokens)
    print("new_token_list!", new_token_list)
    actual_answer=calculate(new_token_list)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("******PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("******FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("1*2-2")
    test("1+2*3-7")
    test("1+2+3+4*5*6")
    test("1+2+3*4/5")
    test("(1+2)+3")
    test("3/3")
    #test("3/(1+2)")
    #test("(3.0+4*(2-1))/5")
    print("==== Test finished! ====\n")

run_test()

