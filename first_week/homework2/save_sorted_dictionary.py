# from first_week.homework2.score_checker import read_words
from score_checker import read_words  # TODO: なぜ上のでうまく行かないのか

SCORES = [
    1,
    3,
    2,
    2,
    1,
    3,
    3,
    1,
    1,
    4,
    4,
    2,
    2,
    1,
    1,
    3,
    4,
    1,
    1,
    1,
    2,
    3,
    3,
    4,
    3,
    4,
]  # TODO: score_checker.pyにもある
WORDS_FILE_PATH = "first_week/homework2/words.txt"  # TODO: 同じく


def calculate_valid_word_score(valid_word):
    data_table = [0] * 26
    score = 0
    for character in valid_word:
        alpha_index = ord(character) - ord("a")
        data_table[alpha_index] += 1
        score += SCORES[alpha_index] * 1
    # ex. data="happy" -> data_table=[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    return score


def save_sorted_dictionary():
    words_list = read_words(WORDS_FILE_PATH)

    score_word_set_list = []

    for word in words_list:
        score = calculate_valid_word_score(word)
        score_word_set_list.append((score, word))

    sorted_by_score_word_ist = sorted(
        score_word_set_list, key=lambda x: x[0], reverse=True
    )

    with open(
        "first_week/homework2/sorted_by_score_words.txt",
        "w",
    ) as file:
        for score_word_set in sorted_by_score_word_ist:
            file.write(str(score_word_set) + "\n")


if __name__ == "__main__":
    save_sorted_dictionary()
