"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Return how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero."""

    # I thougt this solution was smart but then I'd realised it isn't
    # the same O(n^4) algorithm speed
    amount = 0
    sublist_ab = []  # the list with combination of sum of numbers in list a and b
    sublist_cd = []  # ... in list c and d

    for i in a:
        for j in b:
            sublist_ab.append(i+j)
    for i in c:
        for j in d:
            sublist_cd.append(i+j)

    for i in sublist_ab:
        for j in sublist_cd:
            if i + j == 0:
                amount += 1

    return amount
