from hw.task02 import check_fibonacci


def test_positive_case():
    """Testing that correcr list gives True"""
    data_to_process = [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
    ]
    assert check_fibonacci(data_to_process)


def test_negative_case():
    """Testing that wrong list gives False"""
    data_to_process = [0, 1, 1, 5]
    assert not check_fibonacci(data_to_process)


def test_case_len_less_3():
    """Testing that list with length less than 3 gives False"""
    data_to_process = [0, 1]
    try:
        check_fibonacci(data_to_process)
    except AssertionError as e:
        pass
    else:
        assert False


def test_wrong_value_type():
    """Testing that wrong value type give False"""
    data_to_process = "abc"
    assert not check_fibonacci(data_to_process)
