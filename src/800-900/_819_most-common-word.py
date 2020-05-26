"""
https://leetcode.com/problems/most-common-word/

"""
from typing import List
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = ''.join([p if p.isalpha() else ' ' for p in paragraph])

        all_words = [word for word in paragraph.split(' ') if word not in banned and len(word) > 0]

        counter = collections.Counter(all_words)

        return max(counter.keys(), key=counter.get)
