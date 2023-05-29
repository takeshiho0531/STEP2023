def get_digits(line: str, start_idx: int) ->dict:
    """_summary_

    Args:
        line (str): _description_
        start_idx (int): NUMERICAL(数字部分)が始まるindex

    Returns:
        dict: _description_
    """

    digits = ['0','1','2', '3', '4', '5', '6', '7', '8', '9', '.']
    idx=start_idx
    digit_list=[]
    while idx in digits:
        digit_list.append(line[idx])
        idx+=1
    next_idx =idx
    return next_idx, digit_list

def digits_to_number(digit_list):
    idx=0
    number =0
    while digit_list[idx]!=".":
        number=number*10+digit_list[idx]
        idx+=1
    if digit_list[idx]==".":
        decimal_point_idx=idx
        idx+=1
        while idx<len(digit_list):
            number+=digit_list[idx]*(10**(idx-decimal_point_idx))
            idx+=1
    return number


def read_digits(line: str, start_idx: int):
    # assert line[start_idx]
    next_idx, digit_list = get_digits(line, start_idx)
    number = digits_to_number[digit_list]
    return {"type": "NUMBER", "value": number, "next_idx": next_idx}

def read_plus(line: str, start_idx: int):
    assert line[start_idx]=="+"
    return {"type": "PLUS", "next_idx": start_idx+1}

def read_minus(line: str, start_idx: int):
    assert line[start_idx]=="-"
    return {"type": "MINUS", "next_idx": start_idx+1}

def read_multiply(line: str, start_idx: int):
    assert line[start_idx]=="*"
    return {"type": "MULTIPLY", "next_idx": start_idx+1}

def read_divide(line: str, start_idx: int):
    assert line[start_idx]=="/"
    return {"type": "DIVIDE", "next_idx": start_idx+1}

def get_brackets_idx(line):
    brackets_idx_list=[]
    tmp_list = []
    idx=0
    for i in range(len(line)):
        if line[idx]=='(':
            tmp_list.append(idx)
        elif line[idx]==')':
            start_bracket_idx = tmp_list[-1]
            tmp_list=tmp_list.pop(-1)
            brackets_idx_list.append((start_bracket_idx, idx))
    return brackets_idx_list





