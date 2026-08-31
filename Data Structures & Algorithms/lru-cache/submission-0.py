class Node:
    def __init__(self,key = None, value = None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.first = Node()
        self.last = Node()
        self.first.next = self.last
        self.last.prev = self.first
        

    def __add_to_head(self, node):
        first_node = self.first.next
        self.first.next = node
        node.next = first_node
        first_node.prev = node
        node.prev = self.first

    def __remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        node = self.map.get(key, None)
        if node:
            self.__remove(node)
            self.__add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key, None)
        if node:
            self.__remove(node)
        node = Node(key, value)
        self.__add_to_head(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            node = self.last.prev
            self.__remove(node)
            del self.map[node.key]


