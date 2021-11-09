import os
import sys

import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from task04 import check_sum_of_four




def test_positive_case():
    """Testing correct tuple"""
    assert check_sum_of_four([],[],[],[])==0


def test_negative_case():
    """Testing wrong tuple"""
    assert not check_sum_of_four([3],[-3],[10],[-10])==0
