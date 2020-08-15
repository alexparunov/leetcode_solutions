"""
https://leetcode.com/problems/excel-sheet-column-number/

"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        alph = {chr(ord('A') + i): i + 1 for i in range(26)}

        N = len(s)
        tot_sum = 0
        for i, ch in enumerate(s):
            tot_sum += 26 ** (N - i - 1) * alph[ch]

        return tot_sum
