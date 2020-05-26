"""
https://leetcode.com/problems/permutation-in-string/

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1, S2 = len(s1), len(s2)
        if S1 > S2:
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26

        for i in range(S1):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1

        for i in range(S2 - S1):
            if tuple(s1_map) == tuple(s2_map):
                return True

            s2_map[ord(s2[i + S1]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] -= 1

        return tuple(s1_map) == tuple(s2_map)
