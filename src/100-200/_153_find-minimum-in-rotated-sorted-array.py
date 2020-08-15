"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        low, high = 0, len(nums) - 1

        while low < high:
            m = (low + high) // 2

            if nums[m] < nums[high]:
                high = m
            else:
                low = m + 1

        return nums[low]

