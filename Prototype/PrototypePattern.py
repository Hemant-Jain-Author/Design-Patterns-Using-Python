
from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def clone(self):
        print("clone")

class ConcretePrototype1(Prototype):
    def clone(self):
        print("ConcretePrototype1 clone")
        return copy.deepcopy(self)

class ConcretePrototype2(Prototype):
    def clone(self):
        print("ConcretePrototype2 clone")
        return copy.deepcopy(self)

class ObjectFactory:
    _objects = {}

    @staticmethod
    def addObject(key, value):
        if key not in ObjectFactory._objects:
            ObjectFactory._objects[key] = value
    
    @staticmethod
    def getObject(key):
        if key  in ObjectFactory._objects:
            return ObjectFactory._objects[key].clone()
        return None

    @staticmethod
    def load():
        ObjectFactory.addObject("1", ConcretePrototype1())
        ObjectFactory.addObject("2", ConcretePrototype2())

ObjectFactory.load()
c1 = ObjectFactory.getObject("1")
c2 = ObjectFactory.getObject("1")
print(c1, c2)
c3 = ObjectFactory.getObject("2")
c4 = ObjectFactory.getObject("2")
print(c3, c4)