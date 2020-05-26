"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/

"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        tot_num_strs = 0
        r, l = 0, 0

        for char in s:
            if char == 'R':
                r += 1
            else:
                l += 1

            if r == l:
                tot_num_strs += 1
                r, l = 0, 0

        return tot_num_strs
