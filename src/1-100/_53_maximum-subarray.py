"""
https://leetcode.com/problems/maximum-subarray/

"""

from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, current_sum = -math.inf, 0

        for x in nums:
            current_sum = max(x, current_sum + x)
            max_sum = max(max_sum, current_sum)

        return max_sum
