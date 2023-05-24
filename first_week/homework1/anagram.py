import json
import sys
from typing import Optional


def binary_search(sorted_target, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == sorted_target:
            return sorted_list[mid]

        elif sorted_list[mid] < sorted_target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def get_anagram(target):
    with open("first_week/homework1/words.json") as file:
        sorted_dict = json.load(file)

    sorted_target = "".join(sorted(target))
    sorted_key_list = list(sorted_dict.keys())
    anagram = binary_search(sorted_target, sorted_key_list)
    if anagram is None:
        return "your word is not an anagram!"
    else:
        return sorted_dict[anagram]


if __name__ == "__main__":
    get_anagram(sys.argv[1])
