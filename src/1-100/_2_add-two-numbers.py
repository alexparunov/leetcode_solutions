"""
https://leetcode.com/problems/add-two-numbers/

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode(0)
        answer_tail = answer
        carry_over = 0
        while l1 or l2 or carry_over:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            carry_over, new_value = divmod(x + y + carry_over, 10)

            answer_tail.next = ListNode(new_value)
            answer_tail = answer_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return answer.next
