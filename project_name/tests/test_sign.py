import pytest
import numpy as np

from ..feature_sign import sign_func


def test_simple_sign_func():
    assert sign_func(-100000.346) == -1


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 1),
        (10000.0, 1),
        (-345236.78, -1)
    ]
)

def test_sign_func(value: float, expected: float):
    sign_val = sign_func(value)
    expected = np.sign(value)
    assert expected==sign_val
