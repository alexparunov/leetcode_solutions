"""
https://leetcode.com/problems/guess-number-higher-or-lower/

"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n

        while lo <= hi:
            m = (lo + hi) // 2
            guessed = guess(m)
            if guessed == 0:
                return m
            elif guessed == -1:
                hi = m - 1
            else:
                lo = m + 1

        return -1
