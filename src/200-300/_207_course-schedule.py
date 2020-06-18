"""
https://leetcode.com/problems/course-schedule/

"""

from typing import List
import collections


class Solution:
    def dfs(self, vertex, visited, rec_stack, graph):
        visited[vertex] = True
        rec_stack[vertex] = True

        for adj_v in graph[vertex]:
            if not visited[adj_v]:
                if self.dfs(adj_v, visited, rec_stack, graph):
                    return True
            elif rec_stack[adj_v]:
                return True

        rec_stack[vertex] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for c1, c2 in prerequisites:
            graph[c2].append(c1)

        rec_stack = [False] * numCourses
        visited = [False] * numCourses

        for vertex in range(numCourses):
            if not visited[vertex]:
                is_cyclic = self.dfs(vertex, visited, rec_stack, graph)
                if is_cyclic:
                    return False

        return True
