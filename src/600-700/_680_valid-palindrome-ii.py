"""
https://leetcode.com/problems/valid-palindrome-ii/

"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                left_remove = s[:l] + s[l + 1:]
                right_remove = s[:r] + s[r + 1:]

                is_left_pldr = left_remove == left_remove[::-1]
                is_right_pldr = right_remove == right_remove[::-1]

                return is_left_pldr or is_right_pldr

        return True
