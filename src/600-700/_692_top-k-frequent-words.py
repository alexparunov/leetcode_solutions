"""
https://leetcode.com/problems/top-k-frequent-words/

"""
from typing import List
import collections


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        ans_words = list(counts.keys())
        ans_words.sort(key = lambda w: (-counts[w], w))
        return ans_words[:k]
