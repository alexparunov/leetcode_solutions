"""
https://leetcode.com/problems/baseball-game/

"""
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for op in ops:
            if op == 'C' and stack:
                n = stack.pop()
            elif op == 'D' and stack:
                stack.append(stack[-1] * 2)
            elif op == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)
