"""
https://leetcode.com/problems/sort-array-by-parity/

"""
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        write_p = 0

        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i], A[write_p] = A[write_p], A[i]
                write_p += 1

        return A
