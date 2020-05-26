"""
https://leetcode.com/problems/decompress-run-length-encoded-list/

"""
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []

        for i in range(len(nums) // 2):
            freq, val = nums[2 * i], nums[2 * i + 1]
            decompressed += [val] * freq

        return decompressed
