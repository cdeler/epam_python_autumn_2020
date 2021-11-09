"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    counter=0
    for i, itema in enumerate(a):
        for j, itemb in enumerate(b):
            for k, itemc in enumerate(c):
                for l, itemd in enumerate(d):
                    if itema+itemb+itemc+itemd==0:
                        counter += 1
    return counter