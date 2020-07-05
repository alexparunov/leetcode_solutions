"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        traversals = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            cur_level = []
            next_level = collections.deque()

            while q:
                node = q.popleft()
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
                    cur_level.append(node.val)

            if cur_level:
                traversals.append(cur_level)

            q = next_level

        return traversals

