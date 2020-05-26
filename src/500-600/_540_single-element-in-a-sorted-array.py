"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            return nums[0]

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            m = (lo + hi) // 2

            if lo == hi:
                return nums[lo]

            if nums[m] == nums[m - 1]:
                if (m - lo - 1) % 2 == 1:
                    hi = m - 2
                else:
                    lo = m + 1
            elif nums[m] == nums[m + 1]:
                if (hi - m - 1) % 2 == 1:
                    lo = m + 2
                else:
                    hi = m - 1
            else:
                return nums[m]

        return -1
