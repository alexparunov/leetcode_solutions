"""
https://leetcode.com/problems/maximum-sum-circular-subarray/

"""
from typing import List


class Solution:
    def maxSubarraySum(self, A: List[int]) -> int:
        cur_sum, max_total = 0, -float('inf')
        for n in A:
            cur_sum = max(n, cur_sum + n)
            max_total = max(max_total, cur_sum)

        return max_total

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_kadane = self.maxSubarraySum(A)

        total_sum = sum(A)
        A = [-1 * a for a in A]
        max_wrap_kadane = total_sum + self.maxSubarraySum(A)

        if max_wrap_kadane != 0 and max_wrap_kadane > max_kadane:
            return max_wrap_kadane
        else:
            return max_kadane
