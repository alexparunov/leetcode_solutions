"""
https://leetcode.com/problems/minimum-window-substring/

"""
import collections


class Solution:
    def check_ge(self, occ_counter, target_counter):
        return [a >= b for a, b in zip(occ_counter.values(), target_counter.values())]

    def minWindow(self, s: str, t: str) -> str:
        smallest_w_len = float('inf')
        smallest_w = (0, 0)

        left, right = 0, 0

        str_len = len(s)

        target_counter = collections.Counter(t)
        occ_counter = {k: 0 for k in target_counter.keys()}

        while right < str_len:
            char = s[right]

            if char in target_counter:
                occ_counter[char] += 1

            while all(self.check_ge(occ_counter, target_counter)) and left < len(s):
                first_c = s[left]
                if first_c in t:
                    occ_counter[first_c] -= 1

                if right - left + 1 < smallest_w_len:
                    smallest_w = (left, right)
                    smallest_w_len = right - left + 1

                left += 1

            right += 1

        if smallest_w_len == float('inf'):
            return ""

        l, r = smallest_w
        return s[l:r + 1]
