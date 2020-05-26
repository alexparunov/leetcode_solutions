"""
https://leetcode.com/problems/linked-list-cycle/

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow_node = head
        fast_node = head.next

        while slow_node != fast_node:
            if not fast_node or not fast_node.next:
                return False

            slow_node = slow_node.next
            fast_node = fast_node.next.next

        return True
