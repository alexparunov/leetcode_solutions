"""
https://leetcode.com/problems/number-complement/

"""


class Solution:
    def findComplement(self, num: int) -> int:
        if not num:
            return 1

        ans = 0
        i = 0
        while num:
            num, dig = divmod(num, 2)
            dig = (dig + 1) % 2
            ans += dig * 2 ** i
            i += 1

        return ans
