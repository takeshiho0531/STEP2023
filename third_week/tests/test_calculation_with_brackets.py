import pytest
from calculation.tokenize import tokenize_with_brackets

@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("27)", [{"type": "NUMBER", "value": 27}, {"type": "RIGHT_BRACKET"}]),
        ("27+(", [{"type": "NUMBER", "value": 27}, {"type": "PLUS"}, {"type": "LEFT_BRACKET"}]),
        ("27+(12-", [{"type": "NUMBER", "value": 27}, {"type": "PLUS"}, {"type": "LEFT_BRACKET"}, {"type": "NUMBER", "value": 12},{"type": "MINUS"}]),
        ("27*)2", [{"type": "NUMBER", "value": 27}, {"type": "MULTIPLY"}, {"type": "RIGHT_BRACKET"}, {"type": "NUMBER", "value": 2}]),
        ("27()", [{"type": "NUMBER", "value": 27}, {"type": "LEFT_BRACKET"},{"type": "RIGHT_BRACKET"},]),
    ],
)
def test_tokenize_with_brackets(line, expected):
    print("line", line)
    token_list = tokenize_with_brackets(line)
    assert token_list == expected