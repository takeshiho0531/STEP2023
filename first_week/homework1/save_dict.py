import json


def sort_words_mapping(words_list: list) -> list[tuple[str, str]]:
    sorted_word_set_list = []
    for word in words_list:
        sorted_word = "".join(sorted(word))
        sorted_word_set_list.append((sorted_word, word))
    return sorted_word_set_list


def main():
    with open("first_week/homework1/words.txt", "r") as f:
        words_list = f.read().splitlines()

    sorted_words_set_list = sort_words_mapping(words_list)
    sorted_set_list = sorted(sorted_words_set_list, key=lambda x: x[0])

    with open(
        "first_week/homework1/sorted_words.txt",
        "w",
    ) as file:
        for mapped_words in sorted_set_list:
            file.write(str(mapped_words) + "\n")


if __name__ == "__main__":
    main()
