"""
https://leetcode.com/problems/binary-tree-paths/

"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        if not (root.left or root.right):
            return [str(root.val)]

        left_str = [str(root.val) + '->' + n for n in left]
        right_str = [str(root.val) + '->' + n for n in right]

        return left_str + right_str
