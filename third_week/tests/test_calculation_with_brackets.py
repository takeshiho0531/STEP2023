import pytest
from calculation.brackets import solve_outermost_brackets
from calculation.tokenize import tokenize_with_brackets


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("27)", [{"type": "NUMBER", "value": 27}, {"type": "RIGHT_BRACKET"}]),
        (
            "27+(",
            [
                {"type": "NUMBER", "value": 27},
                {"type": "PLUS"},
                {"type": "LEFT_BRACKET"},
            ],
        ),
        (
            "27+(12-",
            [
                {"type": "NUMBER", "value": 27},
                {"type": "PLUS"},
                {"type": "LEFT_BRACKET"},
                {"type": "NUMBER", "value": 12},
                {"type": "MINUS"},
            ],
        ),
        (
            "27*)2",
            [
                {"type": "NUMBER", "value": 27},
                {"type": "MULTIPLY"},
                {"type": "RIGHT_BRACKET"},
                {"type": "NUMBER", "value": 2},
            ],
        ),
        (
            "27()",
            [
                {"type": "NUMBER", "value": 27},
                {"type": "LEFT_BRACKET"},
                {"type": "RIGHT_BRACKET"},
            ],
        ),
    ],
)
def test_tokenize_with_brackets(line, expected):
    token_list = tokenize_with_brackets(line)
    assert token_list == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("1+(2*3)", [{"type": "NUMBER", "value": 7}]),
        ("(1+2)*3", [{"type": "NUMBER", "value": 9}]),
        ("(1+(2*3))", [{"type": "NUMBER", "value": 7}]),
        ("((1+(2*3)))*4", [{"type": "NUMBER", "value": 28}]),
        ("((1+2)*3)*4", [{"type": "NUMBER", "value": 36}]),
        ("((1+2)*3)/4", [{"type": "NUMBER", "value": 2.25}]),
    ],
)
def test_solve_outermost_brackets(line, expected):
    token_list = tokenize_with_brackets(line)
    brackets_solved_token_list = solve_outermost_brackets(token_list)
    assert brackets_solved_token_list == expected
