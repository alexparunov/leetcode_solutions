"""
https://leetcode.com/problems/validate-binary-search-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True

            val = root.val
            if val <= lower or val >= upper:
                return False

            if not is_valid(root.left, lower, val):
                return False

            if not is_valid(root.right, val, upper):
                return False

            return True

        return is_valid(root)
