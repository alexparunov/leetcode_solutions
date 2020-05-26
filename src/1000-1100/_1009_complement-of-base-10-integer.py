"""
https://leetcode.com/problems/complement-of-base-10-integer/

"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if not N:
            return 1

        ans = 0
        i = 0
        while N:
            N, dig = divmod(N, 2)
            dig = (dig + 1) % 2
            ans += dig * 2 ** i
            i += 1

        return ans
