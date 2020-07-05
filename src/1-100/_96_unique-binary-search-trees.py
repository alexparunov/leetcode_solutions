"""
https://leetcode.com/problems/unique-binary-search-trees/

"""


class Solution:
    def numTrees(self, n: int) -> int:
        # Calculate N-th Catalan Number
        cat = [0] * (n + 1)
        cat[0] = 1
        cat[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                cat[i] += cat[j] * cat[i - j - 1]

        return cat[n]

