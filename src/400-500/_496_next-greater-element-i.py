"""
https://leetcode.com/problems/next-greater-element-i/

"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

        for num in nums1:
            idx = nums2.index(num) + 1
            while idx < len(nums2) and num > nums2[idx]:
                idx += 1

            if idx < len(nums2):
                answer.append(nums2[idx])
            else:
                answer.append(-1)

        return answer
