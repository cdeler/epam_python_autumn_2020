"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
import pytest
from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    d = list(data)
    for i in d:
        if d[i + 2] == d[i] + d[i + 1]:
            return True
        return False


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1, 1, 2, 3], True),
        ([55, 89, 144], True),
        ([5], True),
        ([1, 8, 34], False),
        ([3, 4, 5], False),
    ],
)
def test_check_fibonacci(value, expected_result: bool):
    result = check_fibonacci(value)
    assert result == expected_result


def test_check_fibonacci_raises():
    with pytest.raises(TypeError, match="Не тот тип данных"):
        check_fibonacci(True)


