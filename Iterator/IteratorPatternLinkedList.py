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

    def addTail(self, value):
        newNode = self.Node(value, None)
        if self.head == None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    def addHead(self, value):
        newNode = self.Node(value, self.head)
        if self.head == None:
            self.tail = newNode
        self.head = newNode

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

aggregate = LinkedList()

for i in range(10):
    aggregate.addTail(i)
    aggregate.addHead(i)

for val in aggregate:
    print(val, end=" ")