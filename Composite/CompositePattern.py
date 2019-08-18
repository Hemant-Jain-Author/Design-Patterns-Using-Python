from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Composite(Component):
    def __init__(self):
        self._children = set()

    def operation(self):
        print("Composite Operation")
        for child in self._children:
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
# composite.operation()

composite2 = Composite()
composite2.add(Leaf())

composite.add(composite2)
composite.operation()
