import pytest

from first_week.homework1.anagram import main

@pytest.mark.parametrize(("word", "expected"), [
    ("ppyha", "happy"),
    ("agolthmri", "algorithm"),
    ("a", "a"),
    (" ", 'your word is not an anagram!'),
    ("ghnit", "thing"), # TODO: 複数のanagramがある場合に対応してなかった！
])
def test_main(word, expected):
    assert main(word) == expected

