"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, N = 0, 0, len(nums)

        if N == 0: return 0

        for j in range(1, N):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
