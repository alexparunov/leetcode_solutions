"""
https://leetcode.com/problems/min-cost-climbing-stairs/

"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1, f2 = cost[:2]
        for i in range(2, len(cost)):
            f_c = cost[i] + min(f1, f2)
            f1, f2 = f2, f_c

        return min(f1, f2)
