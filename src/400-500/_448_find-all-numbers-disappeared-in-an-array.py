"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for val in nums:
            v = abs(val) - 1
            nums[v] = abs(nums[v]) * -1

        return [i + 1 for i in range(0, len(nums)) if nums[i] > 0]
