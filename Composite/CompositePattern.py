from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Composite(Component):
    def __init__(self):
        self._children = set()

    def operation(self):
        for child in self._children:
            print("Composite Operation")
            child.operation()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)


class Leaf(Component):
    def operation(self):
        print("Leaf Operation")

composite = Composite()
composite.add(Leaf())
composite.operation()