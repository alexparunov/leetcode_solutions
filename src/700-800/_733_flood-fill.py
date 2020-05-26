"""
https://leetcode.com/problems/flood-fill/

"""
from typing import List


class Solution:
    def neighbors(self, x, y, N, M):
        for row, col in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= row < N and 0 <= col < M:
                yield row, col

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = [(sr, sc)]
        original_color = image[sr][sc]

        N, M = len(image), len(image[0])

        while stack:
            row, col = stack.pop()
            image[row][col] = newColor
            for n_row, n_col in self.neighbors(row, col, N, M):
                if image[n_row][n_col] == original_color and image[n_row][n_col] != newColor:
                    stack.append((n_row, n_col))

        return image
