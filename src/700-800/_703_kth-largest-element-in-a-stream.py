"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

"""
from typing import List
import bisect


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]
