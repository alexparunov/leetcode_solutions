"""
https://leetcode.com/problems/increasing-decreasing-string/

"""


class Solution:
    def sortString(self, word: str) -> str:
        A = 26
        letters = [0] * A
        for s in word:
            letters[ord(s) - 97] += 1

        first_letter_pos = 0
        for pos in range(A):
            if letters[pos] > 0:
                first_letter_pos = pos
                break

        last_letter_pos = A - 1
        for pos in range(A - 1, -1, -1):
            if letters[pos] > 0:
                last_letter_pos = pos
                break

        result = ""
        while len(result) != len(word):
            i = first_letter_pos
            while i <= last_letter_pos:
                if letters[i] > 0:
                    result += chr(i + 97)
                    letters[i] -= 1
                i += 1

            j = last_letter_pos
            while j >= first_letter_pos:
                if letters[j] > 0:
                    result += chr(j + 97)
                    letters[j] -= 1
                j -= 1

        return result
