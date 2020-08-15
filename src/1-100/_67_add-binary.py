"""
https://leetcode.com/problems/add-binary/

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, 0
        res = ''
        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0
            carry, digit = divmod(d1 + d2 + carry, 2)
            res = str(digit) + res
            i -= 1
            j -= 1

        return res
