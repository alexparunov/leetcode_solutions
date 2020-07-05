"""
https://leetcode.com/problems/permutation-sequence/

"""
import itertools


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        final_p = []
        for p in itertools.permutations(range(1, n + 1)):
            if not k:
                break
            final_p = p
            k -= 1

        return ''.join([str(c) for c in final_p])
