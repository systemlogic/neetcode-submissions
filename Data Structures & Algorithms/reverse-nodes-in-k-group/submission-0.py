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

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        _head = head
        arr = []
        _map = {}
        while _head:
            first = _head
            index = 1
            for _ in range(k-1):
                if _head.next:
                    index += 1
                    _head = _head.next
            if _head:
                head_next = _head.next
                _head.next = None
                _head = head_next
            arr.append(first)
            _map[first] = index

        for index in range(len(arr)):
            if k == _map[arr[index]]:
                arr[index] = self.reverse(arr[index])
                
        for index in range(len(arr) - 1):
            lst = arr[index]
            while lst.next:
                lst = lst.next
            lst.next = arr[index+1]

        return arr[0]