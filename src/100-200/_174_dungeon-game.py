"""
https://leetcode.com/problems/dungeon-game/

"""
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        N, M = len(dungeon), len(dungeon[0])

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        dp[N - 1][M], dp[N][M - 1] = 1, 1

        for i in range(N - 1):
            dp[i][M] = float('inf')

        for j in range(M - 1):
            dp[N][j] = float('inf')

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                up, left = dp[i + 1][j], dp[i][j + 1]
                hp = dungeon[i][j]

                dp[i][j] = max(min(up, left) - hp, 1)

        return dp[0][0]
