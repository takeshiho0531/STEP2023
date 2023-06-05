from calculation.tokenize import tokenize

def make_plus_minus_only(line):
    token_list=tokenize(line)
    token_list.append({"type":"PLUS"})
    print(token_list)
    flat_list=[]
    tmp_value=1
    index=0
    while index<len(token_list):
        token=token_list[index]
        print(token)
        if token["type"]=="NUMBER":
            tmp_value*=token["value"]
            print(tmp_value)
            index+=1
            #while (token["type"]=="NUMBER") or (token["type"]=="MULTIPLY") or (token["type"]=="DEVIDE"):
            while index<len(token_list):
                if token["type"]=="MULTIPLY":
                    value*=token_list[index+1]
                    index+=2
                    token=token_list[index]
                    print(token)
                    continue
                if token["type"]=="DEVIDE":
                    value/=token_list[index+1]
                    index+=2
                    token=token_list[index]
                    print(token)
                    continue
                else:
                    break
            #else:
                #token = token_list[index]
                #print(token)
                #continue

            if index < len(token_list):
                continue

        if (token["type"]=="PLUS") or (token["type"]=="MINUS"):
            flat_list.append({"type": "NUMBER", "value": tmp_value})
            flat_list.append(token)
            print(flat_list)
            index+=1
            continue
        #else:
            #break
        index+=1
    flat_list=flat_list[:-1]
    return flat_list



def calculate():
    pass