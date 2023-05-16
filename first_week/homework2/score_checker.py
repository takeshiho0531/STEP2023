#! /usr/bin/python3

import ast
import sys

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

SORTED_WORDS_FILE_PATH = "first_week/homework2/sorted_by_score_words.txt"


class TxtFileRreader:
    @classmethod
    def words(cls, word_file_path):
        words_list = []
        with open(word_file_path) as f:
            for line in f:
                line = line.rstrip("\n")
                words_list.append(line)
        return words_list

    @classmethod
    def tuples(cls, tuple_file_path):
        tuples_list = []
        with open(tuple_file_path) as f:
            for line in f:
                line = line.rstrip("\n")
                tuples_list.append(ast.literal_eval(line))
        return tuples_list


def is_valid(valid_word: str, data: str) -> bool:
    """dataに意味のある単語を含むか判定してスコアを返す関数

    Args:
        valid_word (str): (並び替えた際に)意味のある単語となる文字列
        data (str): その中にanagramが含まれるかを判定してスコアをカウントしたい文字列

    Returns:
        int : スコア
    """
    data_table = [0] * 26
    for character in data:
        data_table[ord(character) - ord("a")] += 1
    # ex. data="happy" -> data_table=[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]

    for character in valid_word:
        if (
            data_table[ord(character) - ord("a")] == 0
        ):  # そもそもvalid_wordにその文字が含まれてなかったらだめ
            return False
        data_table[ord(character) - ord("a")] -= 1
    return True


def get_score(sorted_score_and_valid_words_list: list[tuple[int, str]], data: str) -> int:
    """各データのスコアを計算する関数

    Args:
        sorted_score_valid_words_list (list[tuple[int, str]]): (valid_wordのスコア, valid_word)が集まってlistになったもの
        data (str): スコアを計算したい文字列

    Returns:
        int : スコア
    """

    score = 0
    for score_valid_word_set in sorted_score_and_valid_words_list:
        if is_valid(score_valid_word_set[1], data):
            score = score_valid_word_set[0]
            return score
    return score


def main(data_file_path):
    sorted_score_and_valid_words_list = TxtFileRreader.tuples(SORTED_WORDS_FILE_PATH)
    data_words_list = TxtFileRreader.words(data_file_path)
    total_score = 0
    for data in data_words_list:
        total_score += get_score(sorted_score_and_valid_words_list, data)

    print("You answer is correct! Your score is %d." % total_score)


if __name__ == "__main__":
    main(sys.argv[1])
