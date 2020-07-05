"""
https://leetcode.com/problems/isomorphic-strings/

"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = dict()

        if len(s) != len(t):
            return False

        for c1, c2 in zip(s, t):
            if c1 not in maps:
                if c2 in maps.values():
                    return False
                maps[c1] = c2
            else:
                if maps[c1] != c2:
                    return False

        return True
