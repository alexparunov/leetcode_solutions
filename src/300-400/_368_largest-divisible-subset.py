"""
https://leetcode.com/problems/largest-divisible-subset/

"""
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        sol = [[n] for n in nums]

        for i in range(len(nums)):
            for j in range(i):
                if not nums[i] % nums[j] and len(sol[i]) - 1 < len(sol[j]):
                    sol[i] = sol[j] + [nums[i]]

        return max(sol, key=len)
