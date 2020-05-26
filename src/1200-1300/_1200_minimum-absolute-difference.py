"""
https://leetcode.com/problems/minimum-absolute-difference/

"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[1] - arr[0]

        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        answer = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff == min_diff:
                answer.append([arr[i - 1], arr[i]])

        return answer
