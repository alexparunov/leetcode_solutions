"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

"""

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        total_squares = 0
        N, M = len(matrix), len(matrix[0])

        for i in range(N):
            for j in range(M):
                if not matrix[i][j]:
                    continue

                if i == 0 or j == 0:
                    total_squares += 1
                else:
                    cell_val = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + matrix[i][j]
                    total_squares += cell_val
                    matrix[i][j] = cell_val

        return total_squares
