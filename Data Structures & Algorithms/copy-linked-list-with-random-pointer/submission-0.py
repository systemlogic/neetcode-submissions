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
        _head = head
        _map = {None : None}
        while _head:
            copy = Node(_head.val)
            _map[_head] = copy
            _head = _head.next

        _head = head

        while _head:
            copy = _map[_head]
            copy.next = _map[_head.next]
            copy.random = _map[_head.random]
            _head = _head.next
        return _map[head]
        
                