"""
https://leetcode.com/problems/build-an-array-with-stack-operations/

"""
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        num = 1

        i = 0
        while i < len(target):
            if target[i] == num:
                operations.append('Push')
                i += 1
                num += 1
            elif target[i] > num:
                operations.extend(['Push', 'Pop'])
                num += 1

        return operations
