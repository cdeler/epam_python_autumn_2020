"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    maxsum=None
    list1=list(range(0, len(nums)))
    for i in list1:
        try:
            listv=list1.copy()
            listv.remove(i)
            for j in listv:
                try:
                    listv.remove(j)
                    for k in listv:
                        if maxsum == None:

                            maxsum = nums[i] + nums[j] + nums[k]
                            #print('test',maxsum)
                        if  maxsum<nums[i]+nums[j]+nums[k]:
                            maxsum=nums[i]+nums[j]+nums[k]
                            #print('test2n', maxsum)
                except TypeError:
                    pass
        except TypeError:
            pass
    return maxsum

print(find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k = 3))