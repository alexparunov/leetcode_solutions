"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/

"""
import collections
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, c in flights:
            graph[u].append((v, c))

        queue = collections.deque([(src, 0, 0)])
        min_cost = float('inf')

        while queue:
            node, n_stops, cost_so_far = queue.popleft()

            if node == dst:
                min_cost = min(min_cost, cost_so_far)
                continue

            if n_stops > K or cost_so_far > min_cost:
                continue

            for nbh, nbh_cost in graph[node]:
                queue.append((nbh, n_stops + 1, cost_so_far + nbh_cost))

        return min_cost if min_cost != float('inf') else -1


