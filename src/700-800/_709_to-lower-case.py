"""
https://leetcode.com/problems/to-lower-case/

"""


class Solution:
    def toLowerCase(self, str_: str) -> str:
        N = len(str_)
        n_letters = 26
        extra_chars = 6

        ans = ''
        for i in range(N):
            if ord('A') <= ord(str_[i]) <= ord('Z'):
                ans += chr(ord(str_[i]) + n_letters + extra_chars)
            else:
                ans += str_[i]

        return ans
