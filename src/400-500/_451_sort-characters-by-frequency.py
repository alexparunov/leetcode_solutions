"""
https://leetcode.com/problems/sort-characters-by-frequency/

"""
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        t_counts = [(k, v) for k, v in counts.items()]
        t_counts.sort(key=lambda x: x[1], reverse=True)
        substrings = [ch * count for ch, count in t_counts]

        return ''.join(substrings)
