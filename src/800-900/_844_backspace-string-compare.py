"""
https://leetcode.com/problems/backspace-string-compare/

"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        clean_s, clean_t = list(), list()

        for i, c in enumerate(S):
            if c != '#':
                clean_s.append(c)
            elif c == '#' and clean_s:
                clean_s.pop()

        for i, c in enumerate(T):
            if c != '#':
                clean_t.append(c)
            elif c == '#' and clean_t:
                clean_t.pop()

        return ''.join(clean_s) == ''.join(clean_t)
