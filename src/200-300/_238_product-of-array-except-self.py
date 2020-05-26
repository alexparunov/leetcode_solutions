"""
https://leetcode.com/problems/product-of-array-except-self/

"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        p_1 = [0] * N
        p_2 = [0] * N

        p_1[0] = 1
        for i in range(1, len(nums)):
            p_1[i] = p_1[i - 1] * nums[i - 1]

        p_2[N - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            p_2[i] = nums[i + 1] * p_2[i + 1]

        answer = list()
        for p1, p2 in zip(p_1, p_2):
            answer.append(p1 * p2)

        return answer
