"""
https://leetcode.com/problems/coin-change-2/

"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.insert(0, 0)

        dp = [[0] * (amount + 1) for _ in range(len(coins))]

        for am in range(amount + 1):
            for c_idx, coin in enumerate(coins):
                if am == 0:
                    dp[c_idx][am] = 1
                elif coin == 0:
                    dp[c_idx][am] = 0
                else:
                    if coin <= am:
                        dp[c_idx][am] = dp[c_idx - 1][am] + dp[c_idx][am - coin]
                    else:
                        dp[c_idx][am] = dp[c_idx - 1][am]

        return dp[-1][-1]
