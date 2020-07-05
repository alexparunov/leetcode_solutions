"""
https://leetcode.com/problems/hamming-distance/

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(b == '1' for b in bin(x ^ y))
