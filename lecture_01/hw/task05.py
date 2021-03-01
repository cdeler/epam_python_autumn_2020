"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
import pytest
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    @pytest.mark.parametrize(
        ["nums", "k", "expected_result"],
        [
            ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
            ([-1, -2, 3, 1, 4], 3, 8),
            ([1, 2, 3, 4], 2, 7),
        ],
    )
    def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):
        result = find_maximal_subarray_sum(nums, k)
        assert result == expected_result

    def test_find_maximal_subarray_sum_raises():
        with pytest.raises(ValueError):
            find_maximal_subarray_sum([1, 3, 6, 7], 7)
