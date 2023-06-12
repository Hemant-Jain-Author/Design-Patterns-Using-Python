import collections.abc

class LinkedList(collections.abc.Iterable):
    # Node class representing elements of linked list.
    class Node:
        def __init__(self, v, n=None):
            self.value = v
            self.next = n
            
    # Constructor of linked list.
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_tail(self, value):
        new_node = self.Node(value, None)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def add_head(self, value):
        new_node = self.Node(value, self.head)
        if self.head == None:
            self.tail = new_node
        self.head = new_node

    def __iter__(self):
        return LinkedListIterator(self)


class LinkedListIterator(collections.abc.Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = aggregate.head

    def __next__(self):
        if self.curr == None:  # if no_elements_to_traverse:
            raise StopIteration
        val = self.curr.value
        self.curr = self.curr.next
        return val

# Client code.
aggregate = LinkedList()
for i in range(5):
    aggregate.add_head(i)

for val in aggregate:
    print(val, end=" ")

"""
4 3 2 1 0 
"""