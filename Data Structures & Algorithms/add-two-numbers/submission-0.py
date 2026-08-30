# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _sum = head = ListNode()
        carry = 0
        while carry or l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            addition = carry + l1_val + l2_val
            digit = addition % 10
            carry = addition // 10
            head.next = ListNode(digit)
            head = head.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return _sum.next

        