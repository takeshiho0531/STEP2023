#! /usr/bin/python3

import sys
from typing import Optional

# How to use:
#
# $ python3 score_checker.py your_answer_file
#

# SCORES of the characters:
# ----------------------------------------
# | 1 point  | a, e, h, i, n, o, r, s, t |
# | 2 points | c, d, l, m, u             |
# | 3 points | b, f, g, p, v, w, y       |
# | 4 points | j, k, q, x, z             |
# ----------------------------------------
SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]

WORDS_FILE_PATH = "first_week/homework2/words.txt"


def read_words(word_file_path):
    words_list = []
    with open(word_file_path) as f:
        for line in f:
            line = line.rstrip("\n")
            words_list.append(line)
    return words_list


def calculate_score(valid_word: str, data: str) -> Optional[int]:
    """dataを並び替えた時に意味のある単語を含むか判定するして、その時のスコアを返す関数

    Args:
        valid_word (str): (並び替えた際に)意味のある単語となる文字列
        data (str): その中にanagramが含まれるかを判定してスコアをカウントしたい文字列

    Returns:
        int : スコア
    """
    score = 0
    data_table = [0] * 26
    for character in data:
        data_table[ord(character) - ord("a")] += 1
    # ex. data="happy" -> data_table=[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    for character in valid_word:
        if (
            data_table[ord(character) - ord("a")] == 0
        ):  # そもそもvalid_wordにその文字が含まれてなかったらだめ
            score = 0
            break
        data_table[ord(character) - ord("a")] -= 1
        score += SCORES[ord(character) - ord("a")]
    return score


def get_highest_scores(valid_words_list, data_list):
    sum_score = 0
    for data in data_list:
        highest_score = 0
        for valid_word in valid_words_list:
            score = calculate_score(valid_word, data)
            if highest_score < score:
                highest_score = score
        sum_score += highest_score
    return sum_score


def main(data_file_path):
    valid_words_list = read_words(WORDS_FILE_PATH)
    data_words_list = read_words(data_file_path)
    highest_score = get_highest_scores(valid_words_list, data_words_list)
    print("You answer is correct! Your score is %d." % highest_score)


if __name__ == "__main__":
    main(sys.argv[1])
