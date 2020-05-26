"""
https://leetcode.com/problems/sort-colors/

"""

from typing import List


class Solution:
    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos, two_pos = 0, len(nums) - 1

        i = 0
        while i <= two_pos:
            if nums[i] == 0:
                self.swap(nums, i, zero_pos)
                zero_pos += 1
                i += 1
            elif nums[i] == 2:
                self.swap(nums, i, two_pos)
                two_pos -= 1
            else:
                i += 1

        return nums
