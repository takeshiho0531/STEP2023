import pytest

from first_week.homework1.anagram import get_anagram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("ppyha", ["happy"]),
        ("agolthmri", ["algorithm", "logarithm"]),
        ("a", ["a"]),
        (" ", "your word is not an anagram!"),
        ("ghnit", ["thing", "night"]),
    ],
)
def test_main(word, expected):
    assert set(get_anagram(word)) == set(expected)
