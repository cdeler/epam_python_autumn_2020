"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def last_fib(num: int) -> int:
    """Return first 2 numbers of Fibonacci sequnce before number num"""
    if num == 0:
        return 0
    fib = [0, 1]
    i = 2
    while fib[-1] < num:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1

    return fib[-1]


def check_fibonacci(data: Sequence[int]) -> bool:

    assert len(data) >= 3, "The sequence length should be more than 3"

    if data[0] != last_fib(data[0]):
        return False

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
