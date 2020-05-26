"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

"""


from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_1 = collections.Counter(nums1)
        counter_2 = collections.Counter(nums2)

        intersection = []

        for num, counter in counter_1.items():
            intersection += [num] * min(counter, counter_2[num])

        return intersection
