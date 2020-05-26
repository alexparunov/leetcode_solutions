"""
https://leetcode.com/problems/sqrtx/

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        lo, hi = 1, x

        while lo <= hi:
            m = (lo + hi) // 2

            if m ** 2 <= x < (m + 1) ** 2:
                return m
            elif m ** 2 > x:
                hi = m - 1
            else:
                lo = m + 1

        return lo
