"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import pytest
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    return len(
        [
            i + j + k + m
            for i in a
            for j in b
            for k in c
            for m in d
            if i + j + k + m == 0
        ]
    )

    @pytest.mark.parametrize(
        ["a", "b", "c", "d", "expected_result"],
        [
            ([1, 2, 3, 4], [2, 3, -3, 2], [-2, -4, -2, -4], [1, -1, 3, -2], 32),
            ([1, 2, 3, 4], [2, 3, 3, 2], [2, 4, 2, 4], [1, 1, 3, 2], 0),
            ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 256),
            ([0], [0], [0], [0], 1),
            ([], [], [], [], 0),
        ],
    )
    def test_check_sum_of_four(
            a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
    ):
        actual_result = check_sum_of_four(a, b, c, d)
        assert actual_result == expected_result

    def test_check_sum_of_four_raises():
        with pytest.raises(ValueError):
            check_sum_of_four([1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3])
