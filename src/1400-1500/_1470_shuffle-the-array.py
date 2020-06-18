"""
https://leetcode.com/problems/shuffle-the-array/

"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = [-1] * (2 * n)

        p1, p2 = 0, n
        i = 0
        while p1 < n and p2 < 2 * n:
            answer[i] = nums[p1]
            answer[i + 1] = nums[p2]
            i += 2

            p1 += 1
            p2 += 1

        return answer
