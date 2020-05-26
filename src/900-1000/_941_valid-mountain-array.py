"""
https://leetcode.com/problems/valid-mountain-array/

"""
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        if N < 3:
            return False

        i = 1

        while i < N and A[i - 1] < A[i]:
            i += 1

        if i == N or i == 1:
            return False

        while i < N and A[i - 1] > A[i]:
            i += 1

        return i == N
