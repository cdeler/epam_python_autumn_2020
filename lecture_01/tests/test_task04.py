from hw.task04 import check_sum_of_four


def test_positive_case_1():
    """Testing that with correct arrays"""
    a = [1, 2, 3, 4, 5]
    b = [-1, -2, -3, -4, -5]
    c = [1, 2, 3, 4, 5]
    d = [-1, -2, -3, -4, -5]
    result = 85
    assert check_sum_of_four(a, b, c, d) == result


def test_positive_case_2():
    """Testing with correct arrays"""
    a = [1, 2]
    b = [-1, -2]
    c = [1, 2]
    d = [-1, 111]
    result = 3
    assert check_sum_of_four(a, b, c, d) == result


def test_negative_case():
    """Testing that 2 gives True"""
    a = [1, 2]
    b = [-1, -2]
    c = [1, 2]
    d = [-1, 111]
    result = 3
    assert check_sum_of_four(a, b, c, d) == result


def test_size_arrays_negative_case():
    """Testing that all arrays have only integers"""
    a = [1, "4"]
    b = [-1, 2.3]
    c = [1, {}]
    d = [-1, []]
    assert not all(isinstance(x, int) for x in a + b + c + d)
