"""
https://leetcode.com/problems/plus-one/

"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            carry, new_num = divmod(digits[i] + carry, 10)
            digits[i] = new_num

        if carry:
            digits.insert(0, carry)

        return digits
