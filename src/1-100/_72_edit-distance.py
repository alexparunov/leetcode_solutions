"""
https://leetcode.com/problems/edit-distance/

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)

        if N == 0:
            return M
        elif M == 0:
            return N

        word1 = '#' + word1
        word2 = '#' + word2

        lh = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            for j in range(M + 1):
                if i == 0 or j == 0:
                    lh[i][j] = max(i, j)
                else:
                    delete = lh[i - 1][j] + 1
                    insert = lh[i][j - 1] + 1
                    horizontal = lh[i - 1][j - 1] + int(word1[i] != word2[j])
                    lh[i][j] = min(delete, insert, horizontal)

        return lh[-1][-1]
