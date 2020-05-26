"""
https://leetcode.com/problems/valid-anagram/

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet = [0] * 26
        for i in range(len(s)):
            alphabet[ord(s[i]) - ord('a')] += 1
            alphabet[ord(t[i]) - ord('a')] -= 1

        return all([a == 0 for a in alphabet])
