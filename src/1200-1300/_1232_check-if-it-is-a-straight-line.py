"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/

"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x2 - x1 == 0:
            slope = 0
        else:
            slope = (y2 - y1) / (x2 - x1)

        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i - 1]
            x2, y2 = coordinates[i]

            if x2 - x1 == 0:
                new_slope = 0
            else:
                new_slope = (y2 - y1) / (x2 - x1)

            if new_slope != slope:
                return False

        return True

