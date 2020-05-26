"""
https://leetcode.com/problems/subarray-sum-equals-k/

"""
from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_sums, t_sum = 0, 0
        sums = collections.defaultdict(int)

        for num in nums:
            t_sum += num
            diff_key = t_sum - k
            if t_sum == k:
                num_sums += 1

            if diff_key in sums:
                num_sums += sums[diff_key]

            sums[t_sum] += 1

        return num_sums
