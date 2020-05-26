"""
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = {str(i): chr(97 + i - 1) for i in range(1, 10)}
        numbers = {str(i) + '#': chr(97 + i - 1) for i in range(10, 27)}

        alphabet.update(numbers)

        i = len(s) - 1
        ans = ''

        while i >= 0:
            if s[i] == '#':
                next_letter = alphabet[s[i - 2:i + 1]]
                i -= 3
            else:
                next_letter = alphabet[s[i]]
                i -= 1

            ans = next_letter + ans

        return ans
