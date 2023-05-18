import sys
import ast



def judge_anagram(target: str, sorted_ori_set_list): # TODO: sorted_ori_set_listの型定義 # sorted_ori_set_list: list[tuple(str, str)

    print(sorted_ori_set_list, "sorted_ori_set_list", )
    sorted_list= [item[0] for item in sorted_ori_set_list]
    ori_list = [item[1] for item in sorted_ori_set_list]
    print(sorted_list, "sorted_list")

    low = 0
    high = len(sorted_list) - 1
    print(high)
    sorted_target="".join(sorted(target))
    print(sorted_target, "sorted_target")

    while low <= high:
        mid = (low + high) // 2
        print(mid, "mid")
        if sorted_list[mid] == sorted_target:
            return ori_list[mid]

        elif sorted_list[mid] < sorted_target:
            print(sorted_list[mid])
            low = mid + 1
        else:
            high = mid - 1
    return -1


def find_value_by_key(key, data_list):
    for data in data_list:
        if data[0] == key:
            return data[1]
    return False


def main(given_word: str) -> str:
    target = "".join(sorted(given_word))

    with open(
        "first_week/homework1/sorted_words.txt",
        "r",
    ) as f:
        sorted_words_set_list = f.read().splitlines()
    print(sorted_words_set_list)
    # print(ast.literal_eval(sorted_words_set_list))
    result_list = [eval(item) for item in sorted_words_set_list]


    # for sorted_words_set in sorted_words_set_list:
        # print(ast.literal_eval(sorted_words_set))
    anagram_judgment = judge_anagram(target, result_list)
    if anagram_judgment == -1:
        return "your word is not an anagram!"
    else:
            # answer = find_value_by_key(target, sorted_words_set_list)
        # answer = anagram_judgment(target, sorted_words_set_list)
        return anagram_judgment
