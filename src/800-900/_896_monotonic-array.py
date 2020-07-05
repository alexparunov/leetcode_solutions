"""
https://leetcode.com/problems/monotonic-array/

"""
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = all(A[i - 1] <= A[i] for i in range(1, len(A)))
        decreasing = all(A[i - 1] >= A[i] for i in range(1, len(A)))

        return increasing or decreasing
