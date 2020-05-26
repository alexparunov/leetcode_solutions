"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        if N == 1:
            return [-1]

        i = N - 1

        max_so_far = -1

        while i >= 0:
            max_so_far = max(max_so_far, arr[i])
            arr[i] = max_so_far
            i -= 1

        arr.append(-1)

        return arr[1:]
