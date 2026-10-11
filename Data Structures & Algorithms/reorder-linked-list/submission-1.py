# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, prev = None):
        if not head: return prev

        head_next = head.next
        head.next = prev
        return self.reverse(head_next, head)

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half = self.reverse(slow.next)
        slow.next = None
        first_half = head
        merge = merged_list = ListNode()
        flip = True
        while first_half and second_half:
            if flip:
                merge.next = first_half
                first_half = first_half.next
            else:
                merge.next = second_half
                second_half = second_half.next
            merge = merge.next
            flip = not flip
        if first_half: merge.next = first_half
        if second_half: merge.next = second_half
        