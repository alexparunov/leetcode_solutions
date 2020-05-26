"""
https://leetcode.com/problems/play-with-chips/

"""
from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        n_odd = sum([c % 2 for c in chips])

        return min(n_odd, len(chips) - n_odd)
