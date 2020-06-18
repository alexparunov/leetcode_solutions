"""
https://leetcode.com/problems/max-consecutive-ones/

"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c, c = 0, 0

        for n in nums:
            if n == 1:
                c += 1
                max_c = max(max_c, c)
            else:
                c = 0
        return max_c
