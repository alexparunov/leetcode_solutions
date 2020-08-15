"""
https://leetcode.com/problems/reverse-bits/

"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res, p = 0, 31

        while n:
            res += (n & 1) << p
            n >>= 1
            p -= 1

        return res
