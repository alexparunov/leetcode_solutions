"""
https://leetcode.com/problems/3sum/

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_set = set()
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    solution_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1

        return [list(s) for s in solution_set]
