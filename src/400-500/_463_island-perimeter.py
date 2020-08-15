"""
https://leetcode.com/problems/island-perimeter/

"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        N, M = len(grid), len(grid[0])
        perimeter = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if ni < 0 or nj < 0 or ni >= N or nj >= M:
                            perimeter += 1
                            continue
                        if grid[ni][nj] == 0:
                            perimeter += 1
        return perimeter

