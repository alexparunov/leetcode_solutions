"""
https://leetcode.com/problems/majority-element/

"""
from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        return max(counts.keys(), key=counts.get)
