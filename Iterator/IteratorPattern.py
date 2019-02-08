from abc import ABC, abstractmethod

class Aggregate(ABC):
    @abstractmethod
    def getIterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._data = []

    def addData(self, val):
        self._data.append(val)

    def getIterator(self):
        return ConcreteIterator(self)

class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass
    
    @abstractmethod
    def hasNext(self):
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
    
    def hasNext(self):
        if self._index >= len(self._aggregate._data):
            return False
        return True


aggregate = ConcreteAggregate()
for i in range(5):
    aggregate.addData(i)

iterator =ConcreteIterator(aggregate)
while iterator.hasNext():
    print(iterator.next())