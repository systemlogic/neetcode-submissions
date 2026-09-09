"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copy_map = {None: None}

        _head = head
        while _head:
            node = Node(_head.val)
            copy_map[_head] = node
            _head = _head.next
        _head = head
        while _head:
            copied_node = copy_map[_head]
            copied_node.next = copy_map[_head.next]
            copied_node.random = copy_map[_head.random]
            _head = _head.next
            
        return copy_map[head]
        