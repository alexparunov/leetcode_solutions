"""
https://leetcode.com/problems/all-paths-from-source-to-target/

"""
from typing import List


class Solution:
    def dfs(self, g, N, node, visited, path, paths):
        if node == N - 1:
            paths.append(path)
            return

        if node < 0 or node >= N:
            return

        visited[node] = True
        for nc in range(N):
            if g[node][nc] == 1 and not visited[nc]:
                self.dfs(g, N, nc, visited, path + [nc], paths)

        visited[node] = False

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        g = [[0] * N for _ in range(N)]
        visited = [False] * N

        for r in range(N):
            for c in graph[r]:
                g[r][c] = 1

        paths = []
        self.dfs(g, N, 0, visited, [0], paths)
        return paths
