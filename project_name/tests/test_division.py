import pytest

from ..feature import divide_by_two


def test_simple_divide_by_two():
    assert divide_by_two(10) == 5


@pytest.mark.parametrize(
    "value, expected",
    [
        (10, 5),
        (12, 6),
        (13, 6.5),
    ]
)
def test_divide_by_two(value: float, expected: float):
    divided = divide_by_two(value)
    assert (divided - expected) < 1e-6
