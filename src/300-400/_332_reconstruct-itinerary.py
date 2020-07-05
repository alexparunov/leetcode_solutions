"""
https://leetcode.com/problems/reconstruct-itinerary/

"""
from typing import List
import collections


class Solution:
    def dfs(self, graph, node, stack):
        while graph[node]:
            next_flight = graph[node].pop()
            self.dfs(graph, next_flight, stack)

        stack.append(node)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        stack = list()

        for fr, to in tickets:
            graph[fr].append(to)

        for airport in graph:
            graph[airport] = sorted(graph[airport], reverse=True)

        self.dfs(graph, 'JFK', stack)

        return stack[::-1]
