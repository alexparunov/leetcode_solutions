"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(node):
            if not node:
                return []

            return helper(node.left) + [node.val] + helper(node.right)

        return helper(root)[k - 1]
