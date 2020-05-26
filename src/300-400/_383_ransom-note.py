"""
https://leetcode.com/problems/ransom-note/

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_counts = [0] * 26
        for l in magazine:
            letter_counts[ord(l) - 97] += 1

        for r in ransomNote:
            letter_counts[ord(r) - 97] -= 1
            if letter_counts[ord(r) - 97] < 0:
                return False

        return True
