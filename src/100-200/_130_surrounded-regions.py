"""
https://leetcode.com/problems/surrounded-regions/

"""
from typing import List


class Solution:
    def dfs(self, board: List[List[str]], i, j, N, M):
        if i < 0 or j < 0 or i >= N or j >= M or board[i][j] != 'O':
            return

        board[i][j] = 'T'
        for nr, nc in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            self.dfs(board, nr, nc, N, M)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        if not board[0]:
            return

        N, M = len(board), len(board[0])

        for r in range(N):
            self.dfs(board, r, 0, N, M)
            self.dfs(board, r, M - 1, N, M)

        for c in range(M):
            self.dfs(board, 0, c, N, M)
            self.dfs(board, N - 1, c, N, M)

        for r in range(N):
            for c in range(M):
                board[r][c] = 'O' if board[r][c] == 'T' else 'X'
