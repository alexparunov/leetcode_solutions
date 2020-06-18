"""
https://leetcode.com/problems/top-k-frequent-elements/

"""
import collections
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        counts = [(-v, k) for k, v in c.items()]
        heapq.heapify(counts)

        return [heapq.heappop(counts)[1] for _ in range(k)]
