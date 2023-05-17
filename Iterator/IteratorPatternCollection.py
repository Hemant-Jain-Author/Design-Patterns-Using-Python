import collections.abc

class ConcreteAggregate(collections.abc.Iterable):
    def __init__(self):
        self._data = []

    def addData(self, val):
        self._data.append(val)

    def __iter__(self):
        return ConcreteIterator(self)


class ConcreteIterator(collections.abc.Iterator):
    def __init__(self, aggregate):
        self._aggregate = aggregate
        self._index = 0

    def __next__(self):
        if self._index >= len(self._aggregate._data):  # if no_elements_to_traverse:
            raise StopIteration
        val = self._aggregate._data[self._index]
        self._index += 1
        return val

# Client code
aggregate = ConcreteAggregate()
for i in range(10):
    aggregate.addData(i)

for val in aggregate:
    print(val)