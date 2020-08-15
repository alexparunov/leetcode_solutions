"""
https://leetcode.com/problems/subsets/

"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        indices = [bin(i)[2:] for i in range(2 ** n)]
        indices = ['0' * (n - len(idx)) + idx for idx in indices]

        super_set = [[]] * 2 ** n
        for i, idx in enumerate(indices):
            super_set[i] = [nums[i] for i in range(n) if idx[i] == '1']

        return super_set
