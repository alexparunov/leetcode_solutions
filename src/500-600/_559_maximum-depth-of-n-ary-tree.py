"""
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
import collections


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        q = collections.deque([root])

        level = 0
        while q:
            next_level = collections.deque()
            while q:
                node = q.popleft()
                if node:
                    next_level.extend(node.children)

            q = next_level
            level += 1

        return level


