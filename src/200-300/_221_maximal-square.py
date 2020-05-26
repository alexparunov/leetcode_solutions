"""
https://leetcode.com/problems/maximal-square/

"""

from typing import List


class Solution:
    def n_ones(self, matrix, i, j, sq):
        max_area = 0
        for ni in range(i, i + sq):
            for nj in range(j, j + sq):
                if matrix[ni][nj] == "1":
                    max_area += 1
                else:
                    return 0

        return max_area

    def squareArea(self, matrix, i, j) -> int:
        N, M = len(matrix), len(matrix[0])

        sqs = [k + 1 for k in range(min(N, M)) if k + i < N and k + j < M]

        for sq in reversed(sqs):
            max_area = self.n_ones(matrix, i, j, sq)
            if max_area == sq ** 2:
                return max_area

        return 0

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        N, M = len(matrix), len(matrix[0])
        max_area = 0
        max_possible_area = min(N, M) * min(N, M)

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "1":
                    area = self.squareArea(matrix, i, j)
                    max_area = max(max_area, area)
                    if max_area == max_possible_area:
                        return max_area

        return max_area
