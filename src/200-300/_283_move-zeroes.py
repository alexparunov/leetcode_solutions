"""
https://leetcode.com/problems/move-zeroes/

"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        j = 0

        for i in range(N):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in range(j, N):
            nums[i] = 0
