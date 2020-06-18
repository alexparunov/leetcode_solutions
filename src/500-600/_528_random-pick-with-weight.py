"""
https://leetcode.com/problems/random-pick-with-weight/

"""
from typing import List
import itertools
import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.cum_weights = list(itertools.accumulate(w))
        self.indices = list(range(len(w)))

    def pickIndex(self) -> int:
        return random.choices(self.indices, cum_weights=self.cum_weights)[0]
