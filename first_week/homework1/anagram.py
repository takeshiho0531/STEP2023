import sys
import ast


def judge_anagram(target, sorted_words_list):
    low = 0
    high = len(sorted_words_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_words_list[mid] == target:
            return mid
        elif sorted_words_list[mid] < target:
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

    sorted_words_list = []
    for sorted_words_set in sorted_words_set_list:
        sorted_words_list.append(ast.literal_eval(sorted_words_set)[0])
    sorted_words_list= [sorted(s) for s in sorted_words_list]
    print(sorted_words_list)

    anagram_judgment = judge_anagram(target, sorted_words_list)
    if anagram_judgment == -1:
        return "your word is not an anagram!"
    else:
        answer = find_value_by_key(target, sorted_words_set_list)
        return answer
