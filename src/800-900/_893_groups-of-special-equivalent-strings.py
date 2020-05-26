"""
https://leetcode.com/problems/groups-of-special-equivalent-strings/

"""
from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        special_words = set()

        for word in A:
            alphabet = [0] * 52
            for i, letter in enumerate(word):
                alphabet[ord(letter) - 97 + 26 * (i % 2)] += 1

            special_words.add(tuple(alphabet))

        return len(special_words)
