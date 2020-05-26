"""
https://leetcode.com/problems/array-partition-i/

"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total_sum = sum(nums[::2])

        return total_sum
