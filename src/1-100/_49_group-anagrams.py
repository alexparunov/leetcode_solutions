"""
https://leetcode.com/problems/group-anagrams/

"""

from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)

        answer = list()
        for v in groups.values():
            answer.append(v)

        return answer
