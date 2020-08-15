"""
https://leetcode.com/problems/course-schedule-ii/

"""
from typing import List
import collections


class Solution:
    def dfs(self, graph, vertex, visited, rec_stack, ordered_courses):
        visited[vertex] = True
        rec_stack[vertex] = True

        for adj_v in graph[vertex]:
            if not visited[adj_v]:
                cycle_exists = self.dfs(graph, adj_v, visited, rec_stack, ordered_courses)
                if cycle_exists:
                    return True
            elif rec_stack[adj_v]:
                return True

        ordered_courses.append(vertex)
        rec_stack[vertex] = False
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for c1, c2 in prerequisites:
            graph[c2].append(c1)

        visited = [False] * numCourses
        rec_stack = [False] * numCourses
        ordered_courses = []

        for vertex in range(numCourses):
            if not visited[vertex]:
                cycle_exists = self.dfs(graph, vertex, visited, rec_stack, ordered_courses)
                if cycle_exists:
                    return []

        return ordered_courses[::-1]
