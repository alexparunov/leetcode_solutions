"""
https://leetcode.com/problems/powx-n/

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if abs(x) < 1e-40:
            return 0

        if n < 0:
            return self.myPow(1 / x, -n)

        low = self.myPow(x, n // 2)

        if n % 2 == 0:
            return low * low
        else:
            return low * low * x
