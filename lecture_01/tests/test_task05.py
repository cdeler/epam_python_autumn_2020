from hw.task05 import find_maximal_subarray_sum


def test_positive_case1():
    """Testing that correct list gives right answer"""
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = 16
    assert find_maximal_subarray_sum(nums, k) == result


def test_positive_case2():
    """Testing that correct list gives right answer"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    result = 24
    assert find_maximal_subarray_sum(nums, k) == result


def test_positive_case3():
    """Testing that correct list gives right answer"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 9
    result = 45
    assert find_maximal_subarray_sum(nums, k) == result


def test_positive_case4():
    """Testing that correct list gives right answer"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 100
    result = 45
    assert find_maximal_subarray_sum(nums, k) == result


def test_positive_case5():
    """Testing that correct list gives right answer"""
    nums = [1, 3, -1, -3, 5, -3, 6, 7]
    k = 3
    result = 13
    assert find_maximal_subarray_sum(nums, k) == result


def test_positive_case6():
    """Testing that correct list gives right answer"""
    nums = [1, 3, -1, -3, 5, -3, 6, 7]
    k = 1
    result = 7
    assert find_maximal_subarray_sum(nums, k) == result


def test_all_negative_case():
    """Testing that negative numbers list gives right answer"""
    nums = [-5, -3, -1, -3, -5, -3, -6, -7]
    k = 3
    result = -1
    assert find_maximal_subarray_sum(nums, k) == result


def test_k_lower_one_case():
    """Testing that k < 1 list asserts error"""
    nums = [-5, -3, -1, -3, -5, -3, -6, -7]
    k = 0
    try:
        find_maximal_subarray_sum(nums, k)
    except AssertionError as e:
        pass
    else:
        assert False, "k must be a natural number"
