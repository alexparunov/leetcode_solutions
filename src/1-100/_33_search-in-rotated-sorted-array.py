"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            m = (low + high) // 2

            if target == nums[m]:
                return m

            # rotation version when middle is right part of original array
            if nums[m] > nums[high]:
                if nums[low] <= target < nums[m]:
                    high = m - 1
                else:
                    low = m + 1
            elif nums[m] < nums[low]:  # rotation version when middle is left part of original array
                if nums[m] < target <= nums[high]:
                    low = m + 1
                else:
                    high = m - 1
            else:  # normal binary search. no rotation
                if target < nums[m]:
                    high = m - 1
                else:
                    low = m + 1

        return -1
