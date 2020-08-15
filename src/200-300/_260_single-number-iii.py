"""
https://leetcode.com/problems/single-number-iii/

"""
from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums = collections.Counter(nums)
        return [k for k, v in nums.items() if v == 1]
