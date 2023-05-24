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


def make_dict():
    """単語並び替え後の文字列をkeyとして、valueをlistとして並び替え前の文字を格納していく辞書を作り、それをjsonで保存する"""
    with open("first_week/homework1/words.txt", "r") as f:
        words_list = f.read().splitlines()

    sorted_words_set_list = sort_words_mapping(words_list)

    word_dict = {}

    for item in sorted_words_set_list:
        default_value = []
        key, value = item
        word_dict.setdefault(key, default_value)
        word_dict[key].append(value)

    sorted_word_dict = dict(sorted(word_dict.items(), key=lambda x: x[0]))

    with open("first_week/homework1/words.json", "w") as file:
        json.dump(sorted_word_dict, file, indent=4)


if __name__ == "__main__":
    # main()
    make_dict()
