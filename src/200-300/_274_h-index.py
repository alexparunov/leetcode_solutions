"""
https://leetcode.com/problems/h-index/

"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        H = len(citations)

        for i in range(H):
            if citations[i] >= H - i:
                return H - i

        return 0
