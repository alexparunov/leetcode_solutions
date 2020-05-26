"""
https://leetcode.com/problems/palindrome-linked-list/

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow_p = fast_p = head
        # reversed first half of a list
        prev_node = None

        # iterate over list and determine where is the middle
        # also reverse first half of the array meanwhile
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next

            slow_p_next = slow_p.next
            slow_p.next = prev_node
            prev_node = slow_p
            slow_p = slow_p_next

        odd_nodes = bool(fast_p and slow_p)

        if odd_nodes:
            while slow_p.next and slow_p != fast_p:
                if slow_p.next.val != prev_node.val:
                    return False
                slow_p = slow_p.next
                prev_node = prev_node.next
        else:
            while slow_p:
                if slow_p.val != prev_node.val:
                    return False
                slow_p = slow_p.next
                prev_node = prev_node.next

        return True
