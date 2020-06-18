"""
https://leetcode.com/problems/counting-bits/

"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = []
        for i in range(num + 1):
            n_bits = len([b for b in bin(i) if b == '1'])
            bits.append(n_bits)

        return bits
