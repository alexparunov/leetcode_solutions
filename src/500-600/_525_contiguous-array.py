"""
https://leetcode.com/problems/contiguous-array/

"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = dict()

        max_len, count = 0, 0
        for i, n in enumerate(nums):
            count += (1 if n == 1 else -1)

            if count == 0:
                max_len = max(max_len, i + 1)
            if count in counts:
                max_len = max(max_len, i - counts[count])
            else:
                counts[count] = i

        return max_len
