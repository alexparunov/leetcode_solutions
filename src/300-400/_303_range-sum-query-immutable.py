"""
https://leetcode.com/problems/range-sum-query-immutable/

"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        N = len(nums)
        sums = [0] * (N + 1)

        for i in range(N):
            sums[i + 1] = sums[i] + nums[i]

        self.sums = sums

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]
