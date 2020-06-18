"""
https://leetcode.com/problems/two-city-scheduling/

"""
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        city_a = [a for a, b in costs]
        refunds = [b - a for a, b in costs]
        refunds.sort()

        return sum(city_a) + sum(refunds[:N])
