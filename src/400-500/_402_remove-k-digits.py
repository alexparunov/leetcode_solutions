"""
https://leetcode.com/problems/remove-k-digits/

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        if n == k:
            return "0"

        stack = []

        for ch in num:
            while k > 0 and len(stack) > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1

            stack.append(ch)

        while k > 0:
            stack.pop()
            k -= 1

        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1

        return ''.join(stack[i:]) or '0'
