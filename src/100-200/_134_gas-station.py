"""
https://leetcode.com/problems/gas-station/

"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        curr_gas, total_gas, start = 0, 0, 0
        for i in range(N):
            curr_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]

            if curr_gas < 0:
                curr_gas = 0
                start = i + 1

        return start if total_gas >= 0 else -1
