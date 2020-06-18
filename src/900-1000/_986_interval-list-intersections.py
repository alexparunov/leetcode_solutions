"""
https://leetcode.com/problems/interval-list-intersections/

"""
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        N, M = len(A), len(B)

        if N == 0 or M == 0:
            return []

        i, j = 0, 0

        intersections = []

        while i < N and j < M:
            beg = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])

            if beg <= end:
                intersections.append([beg, end])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return intersections
