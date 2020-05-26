"""
https://leetcode.com/problems/remove-outermost-parentheses/

"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        lr, st, decomps = 0, 0, ""
        for idx, p in enumerate(S):
            if p == '(':
                lr += 1
            else:
                lr -= 1

            if lr == 0:
                decomps += S[st + 1:idx]
                st = idx + 1

        return decomps
