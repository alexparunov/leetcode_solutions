"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

"""
from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque([(root, 0, 0)])

        nodes = collections.defaultdict(list)
        while q:
            while q:
                node, x, y = q.popleft()
                nodes[(x, y)].append(node)
                if node.left:
                    q.append((node.left, x - 1, y - 1))

                if node.right:
                    q.append((node.right, x + 1, y - 1))

        sorted_keys = sorted(nodes.keys(), key=lambda k: (k[0], -k[1]))

        x_vals = collections.defaultdict(list)
        for key in sorted_keys:
            vals = sorted([node.val for node in nodes[key]])
            x_vals[key[0]].extend(vals)

        return [list(val) for val in x_vals.values()]
