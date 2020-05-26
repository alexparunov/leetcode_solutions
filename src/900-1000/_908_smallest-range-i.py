"""
https://leetcode.com/problems/smallest-range-i/

"""
from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_max = max(A) - K
        max_min = min(A) + K

        return max(0, min_max - max_min)
