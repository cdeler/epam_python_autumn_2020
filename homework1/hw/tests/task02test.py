import os
import sys

import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from task02 import check_fibonacci




def test_positive_case():
    """Testing correct seq"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8])


def test_negative_case():
    """Testing wrong seq"""
    assert not check_fibonacci([0, 1, 1, 2, 4, 5, 8])
