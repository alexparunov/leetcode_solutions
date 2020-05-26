"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        answer = 0
        for row in range(m):
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2

                if grid[row][mid] >= 0:
                    low = mid + 1
                else:
                    high = mid - 1

            answer += n - low

        return answer
