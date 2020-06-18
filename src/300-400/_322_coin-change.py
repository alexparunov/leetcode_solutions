"""
https://leetcode.com/problems/coin-change/

"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for a in range(amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] <= amount else -1
