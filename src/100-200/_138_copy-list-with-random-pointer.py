"""
https://leetcode.com/problems/copy-list-with-random-pointer/

"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        root = Node(0, None, None)
        nodes = {}

        current = head
        while current:
            nodes[id(current)] = Node(current.val, None, None)
            current = current.next

        current = root
        while head:
            new_node = nodes[id(head)]
            rand_node = nodes[id(head.random)] if head.random else None

            new_node.random = rand_node

            current.next = new_node

            current = current.next
            head = head.next

        return root.next
