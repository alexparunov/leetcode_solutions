"""
https://leetcode.com/problems/squares-of-a-sorted-array/

"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x**2, A)))
