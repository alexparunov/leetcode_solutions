"""
https://leetcode.com/problems/reverse-vowels-of-a-string/

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})

        n = len(s)
        st = list(s)
        l, h = 0, n - 1
        while l < h:
            if st[l] in vowels and st[h] in vowels:
                st[l], st[h] = st[h], st[l]
                l += 1
                h -= 1
            elif s[l] not in vowels:
                l += 1
            elif s[h] not in vowels:
                h -= 1

        return ''.join(st)
