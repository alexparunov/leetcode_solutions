"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for ch in S:
            if not stack:
                stack.append(ch)
            elif stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)
