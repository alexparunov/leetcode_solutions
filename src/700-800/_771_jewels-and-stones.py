"""
https://leetcode.com/problems/jewels-and-stones/

"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        n_jewels = 0
        for stone in S:
            if stone in jewels: n_jewels += 1

        return n_jewels
