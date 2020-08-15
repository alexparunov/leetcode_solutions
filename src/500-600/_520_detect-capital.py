"""
https://leetcode.com/problems/detect-capital/

"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n_uppers = sum(int(w.isupper()) for w in word)

        return n_uppers == len(word) or n_uppers == 0 or (n_uppers == 1 and word[0].isupper())
