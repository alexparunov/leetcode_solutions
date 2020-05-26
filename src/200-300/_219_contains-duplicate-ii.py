"""
https://leetcode.com/problems/contains-duplicate-ii/

"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        answer = False
        digits = dict()

        for i, num in enumerate(nums):
            if num in digits:
                if i - digits[num] <= k:
                    answer = True

            digits[num] = i

        return answer
