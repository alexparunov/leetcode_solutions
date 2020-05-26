"""
https://leetcode.com/problems/arranging-coins/

"""
from math import sqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # solution to quadratic equation x^2 + x - 2*n = 0
        return int((-1 + sqrt(1 + 4 * 2 * n)) // 2)
