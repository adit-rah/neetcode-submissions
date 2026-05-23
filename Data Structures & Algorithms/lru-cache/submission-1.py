class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        self.cache.pop(node.key)
    
    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(Node(key,value))

        if len(self.cache) > self.cap:
            self.remove(self.left.next)
        
        
