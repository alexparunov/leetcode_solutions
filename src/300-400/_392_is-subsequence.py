"""
https://leetcode.com/problems/is-subsequence/

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        for target in t:
            if j < len(s) and s[j] == target:
                j += 1

        return j == len(s)
