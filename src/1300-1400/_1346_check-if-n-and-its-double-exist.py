"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/

"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        vals = set()

        for a in arr:
            if 2 * a in vals or (a % 2 == 0 and a // 2 in vals):
                return True
            vals.add(a)

        return False
