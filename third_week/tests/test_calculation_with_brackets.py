import pytest
from calculation.tokenize import tokenize_with_brackets
from calculation.brackets import solve_outermost_brackets

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

@pytest.mark.parametrize(("line", "expected"),[
    ("1+(2*3)", [{"type": "NUMBER", "value": 1}, {"type": "PLUS"},{"type": "NUMBER", "value": 6}]),
    ("(1+2)*3", [{"type": "NUMBER", "value": 3}, {"type": "MULTIPLY"},{"type": "NUMBER", "value": 3}]),
    #("(1+(2*3))", [{"type": "NUMBER", "value": 7}]),
    ("((1+(2*3)))*4", [{"type": "NUMBER", "value": 7}, {"type": "MULTIPLY"},{"type": "NUMBER", "value": 4}]),
])
def test_solve_outermost_brackets(line, expected):
    token_list=tokenize_with_brackets(line)
    print(token_list)
    brackets_solved_token_list=solve_outermost_brackets(token_list)
    assert brackets_solved_token_list==expected
