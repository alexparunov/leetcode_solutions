"""
https://leetcode.com/problems/minimum-path-sum/

"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        N, M = len(grid), len(grid[0])

        dp_m = [[0] * M for _ in range(N)]

        dp_m[0][0] = grid[0][0]

        for i in range(1, N):
            dp_m[i][0] = grid[i][0] + dp_m[i - 1][0]

        for j in range(1, M):
            dp_m[0][j] = grid[0][j] + dp_m[0][j - 1]

        for i in range(1, N):
            for j in range(1, M):
                down = grid[i][j] + dp_m[i - 1][j]
                right = grid[i][j] + dp_m[i][j - 1]

                dp_m[i][j] = min(down, right)

        return dp_m[N - 1][M - 1]
