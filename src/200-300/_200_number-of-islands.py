"""
https://leetcode.com/problems/number-of-islands/

"""

from typing import List


class Solution:
    def neighbors(self, i, j, N, M):
        for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if ni >= 0 and ni < N and nj >= 0 and nj < M:
                yield (ni, nj)

    def DFS(self, i, j, N, M, grid):
        stack = [(i, j)]
        grid[i][j] == '#'

        while len(stack) > 0:
            i, j = stack.pop()
            for ni, nj in self.neighbors(i, j, N, M):
                if grid[ni][nj] == '1':
                    grid[ni][nj] = '#'
                    stack.append((ni, nj))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        N, M = len(grid), len(grid[0])

        islands = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    self.DFS(i, j, N, M, grid)
                    islands += 1

        return islands
