"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

"""
from typing import List


class Solution:
    def num_digits(self, num: int) -> int:
        n_digits = 0

        while num:
            n_digits += 1
            num //= 10

        return n_digits

    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans += (1 if self.num_digits(num) % 2 == 0 else 0)
        return ans
