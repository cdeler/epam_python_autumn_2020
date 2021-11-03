from hw.task03 import find_maximum_and_minimum


def test_positive_case_1():
    """Testing that actual powers of 2 give True"""
    if not find_maximum_and_minimum("files_for_task03/sample_1.txt"):
        assert False
