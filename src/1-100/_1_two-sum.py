"""
https://leetcode.com/problems/two-sum/

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()

        for i, num in enumerate(nums):
            comp = target - num
            if comp in complements:
                return [complements[comp], i]

            complements[num] = i

        return []
