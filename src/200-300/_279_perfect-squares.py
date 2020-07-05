"""
https://leetcode.com/problems/perfect-squares/

"""


class Solution:
    def numSquares(self, n: int) -> int:
        amounts = [n] * (n + 1)
        amounts[0], amounts[1] = 0, 1

        for am in range(1, n + 1):
            c = 1
            while c * c <= am:
                amounts[am] = min(amounts[am], amounts[am - c * c] + 1)
                c += 1

        return amounts[n]
