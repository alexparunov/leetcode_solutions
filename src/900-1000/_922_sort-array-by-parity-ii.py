"""
https://leetcode.com/problems/sort-array-by-parity-ii/

"""
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        N = len(A)
        ans = [-1] * N

        t = 0
        for i, n in enumerate(A):
            if n % 2 == 0:
                ans[t] = n
                t += 2

        t = 1
        for i, n in enumerate(A):
            if n % 2 == 1:
                ans[t] = n
                t += 2

        return ans
