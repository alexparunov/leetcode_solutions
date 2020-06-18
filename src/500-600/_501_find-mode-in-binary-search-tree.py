"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/

"""
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = [root]
        counters = collections.defaultdict(int)
        max_count = 0

        while stack:
            node = stack.pop()
            if not node:
                continue

            counters[node.val] += 1
            max_count = max(max_count, counters[node.val])

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        modes = []
        for k, v in counters.items():
            if v == max_count:
                modes.append(k)

        return modes
