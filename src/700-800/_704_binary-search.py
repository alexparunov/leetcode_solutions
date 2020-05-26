"""
https://leetcode.com/problems/binary-search/

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)

        while l < h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m
            else:
                l = m + 1

        return -1
