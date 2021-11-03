"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:

    assert len(data) >= 3, "The sequence length should be more than 3"

    a, b, c = data[0], data[1], data[2]

    while data:
        if not (a + b == c):
            return False

        if len(data) != 3:
            a, b, c = b, c, data[3]
            data = data[1:]
        else:
            data = []

    return True
