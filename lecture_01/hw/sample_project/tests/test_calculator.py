from calculator.calc import check_power_of_2


def test_positive_case1():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_positive_case2():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(4)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_negative_number_case():
    """Testing that negative number give False"""
    assert not check_power_of_2(-128)


def test_zero_case():
    """Testing that zero number give False"""
    assert not check_power_of_2(0)
