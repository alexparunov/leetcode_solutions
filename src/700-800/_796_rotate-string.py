"""
https://leetcode.com/problems/rotate-string/

"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True

        for s in A:
            first = A[0]
            A = A[1:] + first
            if A == B:
                return True
        return False
