"""
https://leetcode.com/problems/invert-binary-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert_tree(node: TreeNode):
            if not node:
                return

            right = node.right
            left = node.left

            node.left = right
            node.right = left

            invert_tree(node.left)
            invert_tree(node.right)

        invert_tree(root)

        return root
