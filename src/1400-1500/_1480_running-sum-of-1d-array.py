"""
https://leetcode.com/problems/running-sum-of-1d-array/

"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            nums[i] = cur_sum

        return nums
