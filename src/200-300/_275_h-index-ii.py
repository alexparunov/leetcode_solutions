"""
https://leetcode.com/problems/h-index-ii/

"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        H = len(citations)

        for i in range(H):
            if citations[i] >= H - i:
                return H - i

        return 0

