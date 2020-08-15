"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        stack, f_nodes = [head], []

        while stack:
            node = stack.pop()
            f_nodes.append(node)
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)

        for i in range(len(f_nodes) - 1):
            f_nodes[i + 1].prev = f_nodes[i]
            f_nodes[i].next = f_nodes[i + 1]
            f_nodes[i].child = None

        return f_nodes[0]
