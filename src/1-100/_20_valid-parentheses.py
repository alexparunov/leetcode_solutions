"""
https://leetcode.com/problems/valid-parentheses/

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        reverses = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ch in s:
            if ch in reverses:
                top_bracket = stack.pop() if stack else '-'

                if reverses[ch] != top_bracket:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
