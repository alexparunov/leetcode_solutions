"""
https://leetcode.com/problems/reverse-string/

"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        m = n // 2
        for i in range(m):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]

        return s
