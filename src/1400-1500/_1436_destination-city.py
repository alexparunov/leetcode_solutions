"""
https://leetcode.com/problems/destination-city/

"""
from typing import List
import collections


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoings = collections.defaultdict(int)

        for src, dst in paths:
            outgoings[src] += 1

        for src, dst in paths:
            if dst not in outgoings:
                return dst

        return ""
