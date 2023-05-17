
from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def clone(self):
        pass

class ConcretePrototype1(Prototype):
    def clone(self):
        # ConcretePrototype1 clone
        return copy.deepcopy(self)

class ConcretePrototype2(Prototype):
    def clone(self):
        # ConcretePrototype2 clone
        return copy.deepcopy(self)

# Client code
c1 = ConcretePrototype1()
c2 = ConcretePrototype2()
print(c1, c2)
c3 = c1.clone()
c4 = c2.clone()
print(c3, c4)


class PrototypeRegistry:
    _prototypes = {}

    @staticmethod
    def add_prototype(key, value):
        if key not in PrototypeRegistry._prototypes:
            PrototypeRegistry._prototypes[key] = value
    
    @staticmethod
    def get_prototype(key):
        if key  in PrototypeRegistry._prototypes:
            return PrototypeRegistry._prototypes[key].clone()
        return None

    @staticmethod
    def load():
        PrototypeRegistry.add_prototype("1", ConcretePrototype1())
        PrototypeRegistry.add_prototype("2", ConcretePrototype2())

# Client code
PrototypeRegistry.load()
c1 = PrototypeRegistry.get_prototype("1")
c2 = PrototypeRegistry.get_prototype("2")
print(c1, c2)
