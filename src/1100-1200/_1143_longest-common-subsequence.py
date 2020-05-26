"""
https://leetcode.com/problems/longest-common-subsequence/

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            for j in range(M + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    next_num = 1 if text1[i - 1] == text2[j - 1] else 0
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + next_num)

        return dp[-1][-1]
