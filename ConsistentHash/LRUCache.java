class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {} # map a key to a Nodes
        self.head = None # Node with the least recently used key
        self.tail = None # Node with the most recently used key

    def update(self, node):
        # Already most recent key.
        if node is self.tail: 
            return

        # Remove node.
        node.next.prev = node.prev
        if node.prev: 
            node.prev.next = node.next
        
        # Head adjestment
        if self.head == node:
            self.head = node.next 

        # Insert node at tail.
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node


    def read(self, key):
        if key in self.map:
            self.update(self.map[key])
            return self.map[key].value
        else:
            return -1

    def print(self):
        curr = self.head
        while curr != None:
            print("<", curr.key, curr.value, end = "> ")
            curr = curr.next
        print()


    def write(self, key, value):
        if key in self.map:
            self.update(self.map[key])
            self.map[key].value = value
            return
        
        node = Node(key, value)
        self.map[key] = node

        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1

        if self.size > self.capacity:
            key = self.head.key
            self.head = self.head.next 
            self.size -= 1
            del self.map[key]


lru = LRUCache(5)
lru.write(1, "One")
lru.write(2, "Two")
lru.print()
lru.write(3, "Three")
lru.write(1, "ONE")
lru.print()
lru.write(4, "Four")
lru.print()
lru.write(5, "Five")
lru.print()
lru.write(6, "Six")
lru.print()
print("Data read with key 4 : ", lru.read(4))
lru.print()
print("Data read with key 1 : ", lru.read(1))
lru.print()