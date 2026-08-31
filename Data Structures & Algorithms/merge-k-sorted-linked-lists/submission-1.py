# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, list1, list2):
        merged = merged_head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                    merged.next = list1
                    list1 = list1.next
            else:
                    merged.next = list2
                    list2 = list2.next
            merged = merged.next
        if list1: merged.next = list1
        elif list2: merged.next = list2
        return merged_head.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        while len(lists) != 1:
            list_1 = lists.pop(0)
            list_2 = lists.pop(0)
            merged = self.merge(list_1, list_2)
            lists.append(merged)

        return lists[0]