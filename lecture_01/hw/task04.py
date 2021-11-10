"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Return how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero."""

    amount = 0

    sublist_ab = [
        i + j for i in a for j in b
    ]  # the list with combination of sum of numbers in list a and b
    sublist_ab.sort()
    sublist_cd = [i + j for i in c for j in d]  # ... in list c and d
    sublist_cd.sort()
    print(sublist_ab, "\n", sublist_cd)

    len_arr = len(sublist_ab)  # initiliaze the array's size
    i = 0
    j = len_arr - 1

    while i < len_arr and j >= 0:
        if sublist_ab[i] + sublist_cd[j] == 0:
            ab = 1
            cd = 1
            while (i != len_arr - 1) and sublist_ab[i] == sublist_ab[i + 1]:
                ab += 1
                i += 1
            while j != 0 and sublist_cd[j] == sublist_cd[j - 1]:
                cd += 1
                j -= 1
            amount += ab * cd
            i += 1
            j -= 1
        elif sublist_ab[i] + sublist_cd[j] > 0:
            j -= 1
        else:
            i += 1
    return amount
