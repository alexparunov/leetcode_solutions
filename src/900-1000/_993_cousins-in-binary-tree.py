"""
https://leetcode.com/problems/cousins-in-binary-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getParentDepth(self, root, parent, depth, val):
        if not root:
            return None, -1

        if root.val == val:
            return parent, depth

        left_parent, left_depth = self.getParentDepth(root.left, root, depth + 1, val)
        right_parent, right_depth = self.getParentDepth(root.right, root, depth + 1, val)

        if left_parent:
            return left_parent, left_depth
        else:
            return right_parent, right_depth

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent_1, depth_1 = self.getParentDepth(root, None, 0, x)
        parent_2, depth_2 = self.getParentDepth(root, None, 0, y)

        if not (parent_1 and parent_2):
            return False

        return parent_1 != parent_2 and depth_1 == depth_2
