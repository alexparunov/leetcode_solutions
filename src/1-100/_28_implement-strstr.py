"""
https://leetcode.com/problems/implement-strstr/

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        N = len(haystack)
        K = len(needle)

        if K > N:
            return -1

        for i in range(N - K + 1):
            k = 0

            while k < K and haystack[i + k] == needle[k]:
                k += 1

            if k == K:
                return i

        return -1
