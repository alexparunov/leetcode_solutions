"""
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

"""
from typing import List
import operator


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def n_bits(num):
            bits = 0
            while num:
                num, d = divmod(num, 2)
                bits += d
            return bits

        num_bits = [(num, n_bits(num)) for num in arr]

        num_bits.sort(key=operator.itemgetter(1, 0))
        return [n for n, bit in num_bits]
