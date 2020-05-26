"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen_letters = set()
        i, j, answer = 0, 0, 0

        while i < n and j < n:
            right_letter = s[j]
            left_letter = s[i]

            if right_letter not in seen_letters:
                seen_letters.add(right_letter)
                j += 1
                answer = max(answer, j - i)
            else:
                seen_letters.remove(left_letter)
                i += 1

        return answer
