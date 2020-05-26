"""
https://leetcode.com/problems/last-stone-weight/

"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            diff = y - x
            if x != y: heapq.heappush(stones, diff)

        return -stones[0] if stones else 0
