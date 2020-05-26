"""
https://leetcode.com/problems/rotting-oranges/

"""
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()

        max_v, max_h = len(grid), len(grid[0])

        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 2:
                    # initial depth of BFS tree is 0
                    starting_pos = (i, j, 0)
                    q.append(starting_pos)

        def neighbors(i, j):
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < max_v and 0 <= nj < max_h:
                    yield ni, nj

        max_depth = 0
        while q:
            i, j, max_depth = q.popleft()

            for ni, nj in neighbors(i, j):
                if grid[ni][nj] == 1:
                    next_pos = (ni, nj, max_depth + 1)
                    q.append(next_pos)
                    grid[ni][nj] = 2

        any_1_left = any(1 in row for row in grid)

        return -1 if any_1_left else max_depth
