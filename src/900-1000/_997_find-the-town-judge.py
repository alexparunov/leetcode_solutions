"""
https://leetcode.com/problems/find-the-town-judge/

"""
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1

        trusts = [0] * (N + 1)

        for a, b in trust:
            trusts[a] -= 1
            trusts[b] += 1

        for a, b in trust:
            if trusts[b] == N - 1:
                return b

        return -1
