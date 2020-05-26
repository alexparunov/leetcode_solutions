"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashp = sum(hash(ch) for ch in p)
        hashi = sum(hash(ch) for ch in s[:len(p) - 1])

        ret = []
        for idx, (ch_out, ch_in) in enumerate(zip([""] + list(s), s[len(p) - 1:])):
            hashi += hash(ch_in) - hash(ch_out)
            if hashi == hashp:
                ret.append(idx)

        return ret
