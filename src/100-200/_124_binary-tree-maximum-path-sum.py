"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_sum(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.max_sum(root.left)
        right = self.max_sum(root.right)

        # adding any negative to total sum, will not improve the answer
        left = max(left, 0)
        right = max(right, 0)

        self.max_sum_answ = max(self.max_sum_answ, left + right + root.val)
        return root.val + max(left, right)

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum_answ = -2 ** 31 + 1
        self.max_sum(root)

        return self.max_sum_answ
