"""
https://leetcode.com/problems/merge-two-sorted-lists/

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        merged = root

        while l1 and l2:
            if l1.val < l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next

            merged = merged.next

        if l1:
            merged.next = l1

        if l2:
            merged.next = l2

        return root.next
