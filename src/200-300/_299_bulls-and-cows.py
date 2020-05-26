"""
https://leetcode.com/problems/bulls-and-cows/

"""

import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A, B, n, counts = 0, 0, len(secret), collections.defaultdict(int)

        for i in range(n):
            counts[secret[i]] += 1

        for i in range(n):
            if guess[i] == secret[i]:
                A += 1
                counts[secret[i]] -= 1

        for i in range(n):
            if guess[i] != secret[i] and counts[guess[i]] > 0:
                B += 1
                counts[guess[i]] -= 1

        return str(A) + 'A' + str(B) + 'B'
