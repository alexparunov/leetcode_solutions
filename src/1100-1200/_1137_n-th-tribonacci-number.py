"""
https://leetcode.com/problems/n-th-tribonacci-number/

"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        f0, f1, f2 = 0, 1, 1

        for i in range(3, n + 1):
            f3 = f0 + f1 + f2
            f0 = f1
            f1 = f2
            f2 = f3

        return f2
