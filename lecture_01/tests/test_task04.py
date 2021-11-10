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


def test_positive_case_3():
    """Testing with correct arrays"""
    a = [2, 1]
    b = [2, 5]
    c = [1, -2]
    d = [-4, 5]
    result = 2
    assert check_sum_of_four(a, b, c, d) == result


def test_positive_case_4():
    """Testing with correct arrays"""
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [-7, -8, -9]
    d = [0, -1, -2]
    result = 10
    assert check_sum_of_four(a, b, c, d) == result


def test_positive_case_5():
    """Testing with correct arrays"""
    a = []
    b = []
    c = []
    d = []
    result = 0
    assert check_sum_of_four(a, b, c, d) == result


def test_positive_case_6():
    """Testing with correct arrays"""
    a = [i for i in range(1000)]
    b = [i for i in range(1000)]
    c = [i for i in range(1000)]
    d = [i for i in range(1000)]
    result = 1
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
