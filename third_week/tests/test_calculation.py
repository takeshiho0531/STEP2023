import pytest
from calculation.calculate import calculate, make_plus_minus_only
from calculation.tokenize import tokenize, tokenize_number


@pytest.mark.parametrize(
    ("line", "expected", "expected_increment"),
    [
        ("27", 27, 2),
        ("356", 356, 3),
        ("36.5", 36.5, 4),
        ("27.0", 27, 4),
        ("27.00", 27.00, 5),
    ],
)
def test_tokenize_number(line, expected, expected_increment):
    number_token, increment = tokenize_number(line, 0)
    assert number_token["type"] == "NUMBER"
    assert number_token["value"] == expected
    assert expected_increment == increment


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("27", [{"type": "NUMBER", "value": 27}]),
        ("27+", [{"type": "NUMBER", "value": 27}, {"type": "PLUS"}]),
        ("27-", [{"type": "NUMBER", "value": 27}, {"type": "MINUS"}]),
        ("27*", [{"type": "NUMBER", "value": 27}, {"type": "MULTIPLY"}]),
        ("27/", [{"type": "NUMBER", "value": 27}, {"type": "DEVIDE"}]),
        (
            "27+36.5*47.0/35",
            [
                {"type": "NUMBER", "value": 27},
                {"type": "PLUS"},
                {"type": "NUMBER", "value": 36.5},
                {"type": "MULTIPLY"},
                {"type": "NUMBER", "value": 47.0},
                {"type": "DEVIDE"},
                {"type": "NUMBER", "value": 35},
            ],
        ),
    ],
)
def test_tokenize(line, expected):
    token_list = tokenize(line)
    assert token_list == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("1", [{"type": "NUMBER", "value": 1}]),
        (
            "1+2*8",
            [
                {"type": "NUMBER", "value": 1},
                {"type": "PLUS"},
                {"type": "NUMBER", "value": 16},
            ],
        ),
        (
            "1+2*8*4/8",
            [
                {"type": "NUMBER", "value": 1},
                {"type": "PLUS"},
                {"type": "NUMBER", "value": 8},
            ],
        ),
        (
            "1+2*8*4+5",
            [
                {"type": "NUMBER", "value": 1},
                {"type": "PLUS"},
                {"type": "NUMBER", "value": 64},
                {"type": "PLUS"},
                {"type": "NUMBER", "value": 5},
            ],
        ),
        (
            "1+2*8*4-5",
            [
                {"type": "NUMBER", "value": 1},
                {"type": "PLUS"},
                {"type": "NUMBER", "value": 64},
                {"type": "MINUS"},
                {"type": "NUMBER", "value": 5},
            ],
        ),
    ],
)
def test_make_plus_minus_only(line, expected):
    token_list = tokenize(line)
    flat_list = make_plus_minus_only(token_list)
    assert expected == flat_list


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("1", 1),
        ("1+2*8", 17),
        ("1+2*8*4/8", 1 + 2 * 8 * 4 / 8),
        ("1+2*8*4+5", 1 + 2 * 8 * 4 + 5),
        ("1+2*8*4-5", 1 + 2 * 8 * 4 - 5),
    ],
)
def test_calculate(line, expected):
    token_list = tokenize(line)
    flat_list = make_plus_minus_only(token_list)
    answer = calculate(flat_list)
    assert answer == expected
