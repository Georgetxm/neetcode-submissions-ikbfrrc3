class DoublyListNode:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {} # key to node
        
        self.head = DoublyListNode(-1, -1)
        self.tail = DoublyListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node):
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.remove_node(self.cacheMap[key])
            self.add_to_tail(self.cacheMap[key])
            return self.cacheMap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove_node(self.cacheMap[key])

        new_node = DoublyListNode(key, value)
        self.cacheMap[key] = new_node

        if len(self.cacheMap) > self.capacity:
            del self.cacheMap[self.head.next.key]
            self.remove_node(self.head.next)
        
        self.add_to_tail(new_node)
        
