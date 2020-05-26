"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        _sum = 0

        while n:
            n, d = divmod(n, 10)
            prod *= d
            _sum += d

        return prod - _sum
