import pytest

# from third_week.calculate import calculate
from calculation.calculate import calculate


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("1+2", eval("1+2")),
        ("1.0+2.1-3", eval("1.0+2.1-3")),
    ],
)
def test_main(line, expected):
    abs(calculate(line) - expected) < 1e-8
