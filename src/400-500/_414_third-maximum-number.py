"""
https://leetcode.com/problems/third-maximum-number/

"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = float('-inf'), float('-inf'), float('-inf')

        for n in set(nums):
            if n > a:
                c = b
                b = a
                a = n
            elif n > b:
                c = b
                b = n
            elif n > c:
                c = n

        return c if c != float('-inf') else max(a, b, c)
