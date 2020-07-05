"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def tree_s(node, s):
            if not node:
                return 0

            s = s * 10 + node.val

            if not node.right and not node.left:
                return s

            left = tree_s(node.left, s)
            right = tree_s(node.right, s)

            return left + right

        return tree_s(root, 0)
