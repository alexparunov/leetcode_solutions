"""
https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

"""
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        tot_sum = sum(nums)

        cur_sum = 0
        ans = []
        for n in nums:
            if tot_sum < 2 * cur_sum:
                break

            ans.append(n)
            cur_sum += n

        return ans
