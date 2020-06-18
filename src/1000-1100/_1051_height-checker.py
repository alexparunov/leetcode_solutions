"""
https://leetcode.com/problems/height-checker/

"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(int(a != b) for a, b in zip(heights, sorted(heights)))
