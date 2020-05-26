"""
https://leetcode.com/problems/projection-area-of-3d-shapes/

"""

from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            max_xz = 0
            max_yz = 0
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans += 1

                max_xz = max(grid[i][j], max_xz)
                max_yz = max(grid[j][i], max_yz)

            ans += max_xz + max_yz

        return ans
