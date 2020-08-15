"""
https://leetcode.com/problems/longest-palindrome/

"""
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)

        max_len = 0
        has_any_odd = 0
        for char, count in counts.items():
            if count % 2 == 0:
                max_len += count
            else:
                max_len += count - 1
                has_any_odd = 1

        return max_len + has_any_odd
