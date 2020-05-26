"""
https://leetcode.com/problems/first-unique-character-in-a-string/

"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.Counter(s)

        for i, c in enumerate(s):
            if counts[c] == 1:
                return i

        return -1
