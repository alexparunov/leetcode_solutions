"""
https://leetcode.com/problems/remove-element/

"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n_vals = 0
        n = len(nums)

        i = 0
        while i < n - n_vals:
            if nums[i] == val:
                n_vals += 1
                nums[i], nums[n - n_vals] = nums[n - n_vals], nums[i]
            else:
                i += 1

        nums = nums[:n - n_vals]
        return len(nums)
