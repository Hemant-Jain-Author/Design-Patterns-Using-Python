from abc import ABC, abstractmethod

class Flyweight(ABC):
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state  # intrinsic state

    @abstractmethod
    def operation(self, extrinsic_state): # extrinsic state
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print("Operation inside concrete flyweight")

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def getFlyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight()
        return self._flyweights[key]

factory = FlyweightFactory()
flyweight1 = factory.getFlyweight("key")
flyweight2 = factory.getFlyweight("key")
flyweight1.operation(None)
print(flyweight1, flyweight2)