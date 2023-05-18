import sys
from typing import Optional


def get_anagram(
    target: str, sorted_ori_set_list: list[tuple[str, str]]
) -> Optional[str]:
    """並び替えてできるvalid wordを返す関数

    Args:
        target (str): anagramかどうか判定したい文字列
        sorted_ori_set_list (list[tuple[str, str]]): sorted_words.txtの中身をそのままlistにしたもの。
                                                     tuple内の1つ目の要素は2つ目の要素の文字列をアルファベット順に並べたもの

    Returns:
        Optional[str]: valid word(anagramでなければNone)
    """
    sorted_list = [item[0] for item in sorted_ori_set_list]
    ori_list = [item[1] for item in sorted_ori_set_list]

    low = 0
    high = len(sorted_list) - 1
    sorted_target = "".join(sorted(target))

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == sorted_target:
            return ori_list[mid]

        elif sorted_list[mid] < sorted_target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def main(given_word: str) -> str:
    target = "".join(sorted(given_word))

    with open(
        "first_week/homework1/sorted_words.txt",
        "r",
    ) as f:
        sorted_words_set_list = f.read().splitlines()
    result_list = [eval(item) for item in sorted_words_set_list]

    answer = get_anagram(target, result_list)
    if answer is None:
        return "your word is not an anagram!"
    else:
        return answer


if __name__ == "__main__":
    main(sys.argv[1])
