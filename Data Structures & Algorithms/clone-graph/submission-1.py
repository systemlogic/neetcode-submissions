"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node'], cloned = {}) -> Optional['Node']:
        if not node: return
        if node in cloned:
            return cloned[node]
        lst = []
        new_node = Node(node.val, lst)
        cloned[node] = new_node
        for neighbor in node.neighbors:
            lst.append(self.cloneGraph(neighbor, cloned))
        return new_node

        