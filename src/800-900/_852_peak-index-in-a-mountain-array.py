"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/

"""
from typing import List


class Solution(object):
    def peakIndexInMountainArray(self, A: List[int]):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            m = (lo + hi) // 2
            if A[m] < A[m + 1]:
                lo = m + 1
            else:
                hi = m
        return lo
