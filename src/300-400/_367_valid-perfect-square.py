"""
https://leetcode.com/problems/valid-perfect-square/

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num

        while low <= high:
            m = (low + high) // 2
            if m ** 2 == num:
                return True
            elif m ** 2 < num:
                low = m + 1
            else:
                high = m - 1

        return False
