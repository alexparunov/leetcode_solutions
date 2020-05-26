"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/

"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        pad = 0
        while m != n:
            m >>= 1
            n >>= 1
            pad += 1

        return n << pad
