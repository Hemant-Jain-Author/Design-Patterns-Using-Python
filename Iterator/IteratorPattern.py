from abc import ABC, abstractmethod

class Aggregate(ABC):
    @abstractmethod
    def get_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._data = []

    def addData(self, val):
        self._data.append(val)

    def get_iterator(self):
        return ConcreteIterator(self)

class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass
    
    @abstractmethod
    def has_next(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self._aggregate = aggregate
        self._index = 0

    def next(self):
        if self._index >= len(self._aggregate._data):
            raise StopIteration
        val = self._aggregate._data[self._index]
        self._index += 1
        return val
    
    def has_next(self):
        if self._index >= len(self._aggregate._data):
            return False
        return True

# Client code.
aggregate = ConcreteAggregate()
for i in range(5):
    aggregate.addData(i)

iterator =ConcreteIterator(aggregate)
while iterator.has_next():
    print(iterator.next())