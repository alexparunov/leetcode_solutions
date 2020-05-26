"""
https://leetcode.com/problems/search-insert-position/

"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mi = (lo + hi) // 2

            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                hi = mi - 1
            else:
                lo = mi + 1

        return lo
