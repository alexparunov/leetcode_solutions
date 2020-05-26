"""
https://leetcode.com/problems/diameter-of-binary-tree/

"""


# finition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0

        l_h = self.height(root.left)
        r_h = self.height(root.right)

        l_d = self.diameterOfBinaryTree(root.left)
        r_d = self.diameterOfBinaryTree(root.right)

        return max(l_h + r_h, max(l_d, r_d))

