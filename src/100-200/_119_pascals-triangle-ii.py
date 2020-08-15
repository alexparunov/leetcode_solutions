"""
https://leetcode.com/problems/pascals-triangle-ii/

"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row_above = []
        for r in range(rowIndex + 1):
            new_row = [1]
            if row_above:
                for i in range(len(row_above) - 1):
                    new_row.append(row_above[i] + row_above[i + 1])

                new_row.append(1)
            row_above = new_row

        return new_row
