from calculation.tokenize import tokenize


def multiply_devide(token_list):
    token_list.insert(0, {"type": "MULTIPLY"})
    value = 1
    index = 0
    while index < len(token_list):
        if token_list[index]["type"] == "MULTIPLY":
            value *= token_list[index + 1]["value"]
            index += 2
            continue
        if token_list[index]["type"] == "DEVIDE":
            value /= token_list[index + 1]["value"]
            index += 2
            continue
        else:
            break
    else:
        return {"type": "NUMBER", "value": value}


def make_plus_minus_only(line):
    token_list = tokenize(line)
    token_list.append({"type": "PLUS"})
    flat_list = []
    index = 0
    tmp_token_list = []
    while index < len(token_list):
        token = token_list[index]
        if token["type"] == "NUMBER":
            tmp_token_list.append(token)
            index += 1
            token = token_list[index]
            continue
        if (token["type"] == "MULTIPLY") or (token["type"] == "DEVIDE"):
            tmp_token_list.append(token)
            index += 1
            token = token_list[index]
            continue

        if (token["type"] == "PLUS") or (token["type"] == "MINUS"):
            tmp_token = multiply_devide(tmp_token_list)
            flat_list.append(tmp_token)
            flat_list.append(token)
            index += 1
            tmp_token_list = []
            continue

    flat_list = flat_list[:-1]
    return flat_list


def calculate(line):
    #token_list=tokenize(line)
    flat_token_list=make_plus_minus_only(line)
    index=0
    answer=0
    flat_token_list.insert(0, {"type":"PLUS"})
    while index<len(flat_token_list):
        if flat_token_list[index]["type"]=="PLUS":
            answer+=flat_token_list[index+1]["value"]
            index+=2
            continue
        if flat_token_list[index]["type"]=="MINUS":
            answer-=flat_token_list[index+1]["value"]
            index+=2
            continue
    else:
        return answer
