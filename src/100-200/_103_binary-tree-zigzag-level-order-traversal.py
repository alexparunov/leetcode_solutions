"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

"""
from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque([root])

        flag = 0
        traces = []
        while q:
            next_level = collections.deque()
            current_level = []
            while q:
                node = q.popleft()
                if node:
                    current_level.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)

            if flag:
                current_level = current_level[::-1]

            q = next_level
            flag = (flag + 1) % 2
            if current_level:
                traces.append(current_level)

        return traces
