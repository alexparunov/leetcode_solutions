"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def max_d(root: TreeNode, d=0) -> int:
            if not root:
                return d

            left = max_d(root.left, d + 1)
            right = max_d(root.right, d + 1)

            return max(left, right)

        return max_d(root, 0)
