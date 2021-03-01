"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
import pytest
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open("some_file.txt") as fi:
        line = fi.readline().strip().split(", ")
        maxline = int(max(line))
        minline = int(min(line))
        for line in fi:
            line = line.strip().split(", ")
            if maxline < int(max(line)):
                maxline = int(max(line))
            if minline > int(min(line)):
                minline = int(min(line))
        return minline, maxline


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("test1_find_max_min.txt", (-5, 34)),
        ("test2_find_max_min.txt", (1, 1)),
    ],
)
def test_maximum_and_minimum(file_name: str, expected_result: Tuple[int, int]):
    result = find_maximum_and_minimum(file_name)
    assert result == expected_result
