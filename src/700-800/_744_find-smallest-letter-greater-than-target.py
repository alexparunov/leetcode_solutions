"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, h = 0, len(letters)

        while l < h:
            m = (l + h) // 2

            if letters[m] > target:
                h = m
            else:
                l = m + 1

        return letters[l % len(letters)]
