"""
https://leetcode.com/problems/fibonacci-number/

"""


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0

        f0, f1 = 1, 1

        for i in range(2, N):
            f2 = f0 + f1
            f0 = f1
            f1 = f2

        return f1
