# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, prev = None):
        if not head: return prev
        next_node = head.next
        head.next = prev
        return self.reverse(next_node, head)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev_node = self.reverse(head)
        _head = rev_node
        if n == 1:
            return self.reverse(rev_node.next)
        for _ in range(n - 2):
            _head = _head.next
        if _head.next:    
            _head.next = _head.next.next
            return self.reverse(rev_node)
        return None