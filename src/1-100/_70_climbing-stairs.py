"""
https://leetcode.com/problems/climbing-stairs/

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        f1, f2 = 1, 1
        for i in range(2, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3

        return f2

