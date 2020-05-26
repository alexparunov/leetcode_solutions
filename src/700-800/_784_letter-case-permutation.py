"""
https://leetcode.com/problems/letter-case-permutation/

"""
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.answer = []

        def backtrack(temp, st, idx):
            if idx == len(st):
                self.answer.append(temp)
                return

            if st[idx].isalpha():
                backtrack(temp + st[idx].upper(), st, idx + 1)
                backtrack(temp + st[idx].lower(), st, idx + 1)
            else:
                backtrack(temp + st[idx], st, idx + 1)

        backtrack('', S, 0)

        return self.answer
