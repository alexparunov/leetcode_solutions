"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

"""
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = collections.deque()
        prev_level, prev_number, max_w = 1, 1, 0
        q.append((root, prev_level, prev_number))

        while q:
            node, level, number = q.popleft()
            if level > prev_level:
                prev_level, prev_number = level, number

            max_w = max(max_w, number - prev_number + 1)

            if node.left:
                q.append((node.left, level + 1, number * 2))

            if node.right:
                q.append((node.right, level + 1, number * 2 + 1))

        return max_w

