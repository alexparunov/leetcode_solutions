"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

"""


class Solution:
    def reverse(self, word, st, end):
        while st < end:
            word[st], word[end] = word[end], word[st]
            st += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        word = list(s)
        i, j = 0, 0
        n = len(s)

        while i < n and j < n:
            while i < n and word[i] == ' ':
                i += 1

            j = i
            while j < n and word[j] != ' ':
                j += 1

            self.reverse(word, i, j - 1)
            i = j

        return ''.join(word)


